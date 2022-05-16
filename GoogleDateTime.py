from datetime import datetime


class GoogleDateTime():
    date_time: datetime
    time_zone: str

    def __init__(self, date_time: datetime, time_zone: str):
        self.date_time = date_time
        self.time_zone = time_zone