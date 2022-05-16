from GoogleDateTime import GoogleDateTime


class GoogleEvent:
    def __init__(
        self,
        title: str,
        start: GoogleDateTime,
        end: GoogleDateTime,
        location: str,
        description: str
    ):
        self.title = title
        self.start = start
        self.end = end
        self.location = location
        self.description = description
