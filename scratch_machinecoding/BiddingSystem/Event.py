class Event(object):
    def __init__(self, event_id, event_name, prize_name, event_date):
        self.event_id = event_id
        self.event_name = event_name
        self.prize_name = prize_name
        self.event_date = event_date
        self.winner = None
        self.winner_bid = None

    def __str__(self):
        winner = None
        if self.winner is not None:
            winner = self.winner.name
        return f"Event Id: {self.event_id}, Event Name: {self.event_name}, Prize Name: {self.prize_name}, " \
               f"Event Date: {self.event_date}, Winner: {winner}, Lowest Bid: {self.winner_bid}"
