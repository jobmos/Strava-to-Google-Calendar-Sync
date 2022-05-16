from datetime import timedelta
from GoogleDateTime import GoogleDateTime
from GoogleEvent import GoogleEvent
from dateutil import parser as dateparser


class StravaActivityConverter:
    def to_google_event(activity) -> GoogleEvent:
        act_name = activity["name"]
        act_type = activity["type"]
        act_start_date_str = activity["start_date"]
        act_timezone = activity["timezone"]
        act_start_latlng = activity["start_latlng"]
        act_elapsed_time = activity["elapsed_time"]
        act_id = activity["id"]

        act_start_date = dateparser.parse(act_start_date_str)
        act_end_date = act_start_date.__add__(timedelta(seconds=act_elapsed_time))

        google_start_date = GoogleDateTime(act_start_date, act_timezone)
        google_end_date = GoogleDateTime(act_end_date, act_timezone)
        event_title = "{}: {}".format(act_type, act_name)
        event_description = "https://www.strava.com/activities/{}\nid: {}".format(act_id, act_id)

        lat_lng_str = ""
        if act_start_latlng != None and len(act_start_latlng) > 0:
            lat_lng_str = "{}, {}".format(
                act_start_latlng[0], act_start_latlng[1]
            )

        google_event = GoogleEvent(
            event_title, google_start_date, google_end_date, lat_lng_str, event_description
        )

        return google_event
