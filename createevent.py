import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def create_event(start_datetime, end_datetime, therapist_name):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    print(start_datetime)
    start_datetime_isoformat = start_datetime.isoformat()
    end_datetime_isoformat = end_datetime.isoformat()
    print(start_datetime_isoformat)
    print(end_datetime_isoformat)
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    
    try:
        service = build("calendar", "v3", credentials=creds)
        print(service)

    
        event = {
            'summary': f'Therapy Session with {therapist_name}',
            'location': 'Online',
            'description': f'Therapy session with {therapist_name}',
            'start': {
                'dateTime': start_datetime_isoformat,
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': end_datetime_isoformat,
                'timeZone': 'Asia/Kolkata',
            },
            'conferenceData': {
                'createRequest': {
                    'requestId': f'therapy_{start_datetime.strftime("%Y%m%d%H%M%S")}',
                    'conferenceSolutionKey': {'type': 'hangoutsMeet'}
                }
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        try:
            event = service.events().insert(calendarId='primary', body=event, conferenceDataVersion=1).execute()
            return {
                'status': 'success',
                'meet_link': event.get('hangoutLink'),
                'event_id': event.get('id')
            }
        except HttpError as error:
            print(f"An error occurred while creating the event: {error}")
            return {'status': 'error', 'message': str(error)}
    
    except HttpError as error:
        print(f"An error occurred while building the service: {error}")
        return {'status': 'error', 'message': str(error)}

__all__ = ['create_event']