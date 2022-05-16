# Strava to Google Calendar Sync
This utility checks recent activities on Strava and uploads them to your Google Calendar if the ativity is not already present. Checking if the activity exists is based on the Strava activity ID. Using Docker is slightly overkill, but due to local development on Mac and publishing on Raspberry Pi I decided to go for Docker. Python venv would probably work as well.

## Prerequisits
- Strava account
- Google account
- Google Cloud Platform access
- Docker
- A app.ini file in project root directory

## Building and running the script
1. Build using Docker:
```
docker build -t google-cal .
```
2. Run using Docker:
```
docker run google-cal
```
3. Optional: Set up cron job using crontab

## app.ini contents
### `[GOOGLE]` section:
| Property name     | Description                                                      |
| ----------------- | ---------------------------------------------------------------- |
| GoogleCalendarId  | The Calendar ID of the desired Google Calendar                   |
| GoogleClientId    | Found in the Credentials page of the Google API Console          |
| GoogleClientScret | Found in the Credentials page of the Google API Console          |
| GoogleProjectId   | Google Cloud Platform Project ID found in the Google API Console |

### `[Strava]` section:
| Property name      | Description                              |
| ------------------ | ---------------------------------------- |
| StravaClientId     | Found in the Strava developer page       |
| StravaClientScret  | Found in the Strava developer page       |
| StravaRefreshToken | Acquired through OAuth (does not change) |

## Useful links:
- [Youtube Strava API with Python](https://www.youtube.com/watch?v=2FPNb1XECGs)
- [Google Cloud Platform Dashboard](https://console.cloud.google.com/home/dashboard)
- [Setting up Google Cloud Platform access](https://developers.google.com/workspace/guides/create-project)
- [Strava API reference](https://developers.strava.com/docs/reference/)
- [Strava API reference - Events](https://developers.google.com/calendar/api/v3/reference/events)
- [Containerizing Python project](https://www.docker.com/blog/containerized-python-development-part-1/)
- [Python .gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)
- [Creating GitHub repository from existing project](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github)
- [Cron job every hour](https://crontab.guru/every-1-hour)