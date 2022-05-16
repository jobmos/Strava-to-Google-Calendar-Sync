from googleapiclient.errors import HttpError
from GoogleService import GoogleService
from StravaService import StravaService
from StravaActivityConverter import StravaActivityConverter


class App:
    def __init__(self, google_service: GoogleService, strava_service: StravaService):
        self._google_service = google_service
        self._strava_service = strava_service

    def run(self):
        try:
            google_events = self._google_service.get_past_events(30)
            strava_activities = self._strava_service.get_activities(5)

            for strava_activity in strava_activities:
                if self._activity_already_exists(strava_activity, google_events):
                    continue

                google_event = StravaActivityConverter.to_google_event(strava_activity)
                self._google_service.insert_event(google_event)

            print("Exiting app...")

        except HttpError as error:
            print("An error occurred: %s" % error)
            raise

    def _activity_already_exists(self, strava_activity, google_events):
        matches = self._find_google_match(strava_activity, google_events)
        return any(matches)

    def _find_google_match(self, strava_activity, google_events):
        activity_id = str(strava_activity["id"])
        matching_google_events = [
            google_event
            for google_event in google_events
            if activity_id in google_event["description"]
        ]
        return matching_google_events
