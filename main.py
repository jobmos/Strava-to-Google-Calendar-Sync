import configparser
from datetime import datetime
from App import App
from GoogleService import GoogleService
from StravaService import StravaService


def main():
    print('Current time: {}'.format(datetime.now()))

    config = configparser.ConfigParser()
    config.read('app.ini')

    google_service = GoogleService(config['GOOGLE'])
    strava_service = StravaService(config['STRAVA'])

    app = App(google_service, strava_service)
    app.run()


if __name__ == "__main__":
    main()
