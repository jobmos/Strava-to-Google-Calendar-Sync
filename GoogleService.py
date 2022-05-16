from configparser import SectionProxy
import datetime
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from GoogleEvent import GoogleEvent

SCOPES = ["https://www.googleapis.com/auth/calendar"]


class GoogleService:
    _service = None
    _calendar_id: str

    def __init__(self, config: SectionProxy):
        credentials = self._get_credentials()
        self._service = build("calendar", "v3", credentials=credentials)
        self._calendar_id = config["GoogleCalendarId"]

    def insert_event(self, google_event: GoogleEvent):
        event_body = {
            "summary": google_event.title,
            "description": google_event.description,
            "start": {
                "dateTime": google_event.start.date_time.isoformat(),
                "timeZone": google_event.start.time_zone,
            },
            "end": {
                "dateTime": google_event.end.date_time.isoformat(),
                "timeZone": google_event.end.time_zone,
            },
            "location": google_event.location,
        }

        event = (
            self._service.events()
            .insert(calendarId=self._calendar_id, body=event_body)
            .execute()
        )

        print("Event created: %s" % (event.get("htmlLink")))

    def get_upcoming_events(self):
        now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
        print("Getting the upcoming 10 events")
        events_result = (
            self._service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])
        return events

    def get_past_events(self, days: int):
        now = datetime.datetime.utcnow()
        now_str = now.isoformat() + "Z"
        x_days_ago = now - datetime.timedelta(days=days)
        x_days_ago_str = x_days_ago.isoformat() + "Z"
        print("Getting events of past {} days".format(days))
        events_result = (
            self._service.events()
            .list(
                calendarId=self._calendar_id,
                timeMin=x_days_ago_str,
                timeMax=now_str,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])
        return events

    def print_events(self, events):
        if not events:
            print("No upcoming events found.")
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])
        return event

    def _get_credentials(self):
        print("Requesting Google Token...")
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists("google-token.json"):
            creds = Credentials.from_authorized_user_file("google-token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "google-credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("google-token.json", "w") as token:
                token.write(creds.to_json())
        print("Google Token acquired succesfully...")
        return creds
