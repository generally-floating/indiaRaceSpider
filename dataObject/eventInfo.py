

class EventInfo:
    def __init__(self, venueId, venueName, eventDate, raceType):
        # venueId=1&event_date=2020-03-04&race_type=RESULTS
        self.venueId = venueId
        self.venueName = venueName
        self.eventDate = eventDate
        self.raceType = raceType