from configparser import SectionProxy
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class StravaService:
    _access_token: str
    _config: SectionProxy

    def __init__(self, config):
        self._config = config
        self._access_token = self._get_access_token()

    def _get_access_token(self):
        auth_url = "https://www.strava.com/oauth/token"
        payload = {
            "client_id": self._config["StravaClientId"],
            "client_secret": self._config["StravaClientSecret"],
            "refresh_token": self._config["StravaRefreshToken"],
            "grant_type": "refresh_token",
            "f": "json",
        }

        print("Requesting Strava Access Token...")
        token_response = requests.post(auth_url, data=payload, verify=False)
        access_token = token_response.json()["access_token"]
        print("Strava Access Token = {}".format(access_token))
        return access_token

    def get_activities(self, n_activities):
        activities_url = "https://www.strava.com/api/v3/athlete/activities"
        header = {"Authorization": "Bearer " + self._access_token}
        param = {"per_page": n_activities, "page": 1}
        activities_response = requests.get(activities_url, headers=header, params=param)
        activities = activities_response.json()
        return activities
