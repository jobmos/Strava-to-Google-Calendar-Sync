# Strava to Google Calendar Sync
This utility checks recent activities on Strava and uploads them to your Google Calendar if the ativity is not already present. Checking if the activity exists is based on the Strava activity ID.

## Prerequisits
- Strava account
- Google account
- Google Cloud Platform access
- Docker
- A app.ini file in project root directory

## app.ini contents
### `[GOOGLE]` section:
| Property name | Description |
| ------------- | ----------- |
| GoogleCalendarId | The Calendar ID of the desired Google Calendar |
| GoogleClientId | Found in the Credentials page of the Google API Console |
| GoogleClientScret | Found in the Credentials page of the Google API Console |
| GoogleProjectId | Google Cloud Platform Project ID found in the Google API Console |

### `[Strava]` section:
| Property name | Description |
| ------------- | ----------- |
| StravaClientId | Found in the Strava developer page |
| StravaClientScret | Found in the Strava developer page |
| StravaRefreshToken | Acquired through OAuth (does not change) |

## Useful links:
- https://www.youtube.com/watch?v=2FPNb1XECGs
- https://console.cloud.google.com/home/dashboard
- https://developers.google.com/workspace/guides/create-project
- https://developers.google.com/calendar/api/v3/reference/events
- https://developers.strava.com/docs/reference/
- https://www.docker.com/blog/containerized-python-development-part-1/
- https://github.com/github/gitignore/blob/main/Python.gitignore
- https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github