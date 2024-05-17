from Member import Member
from Event import Event


class Bid(object):
    def __init__(self):
        self.members = dict()
        self.events = dict()
        self.bids = []
        self.winners = []
        self.event_regd = dict()
        self.event_bids = dict()

    def add_member(self, name, member_id, supercoins):
        try:
            member = Member(name, member_id, supercoins)
            for regd_members in self.members.values():
                if regd_members.name == name:
                    raise Exception(f"{name} is already registered")
                if regd_members.member_id == member_id:
                    raise Exception(f"{member_id} is already registered with user {regd_members.user}")
            self.members[member_id] = member
            print(f"{name} is added successfully")
        except Exception as e:
            print(str(e))

    def add_event(self, event_id, event_name, prize_name, event_date):
        try:
            event = Event(event_id, event_name, prize_name, event_date)
            for regd_events in self.events.values():
                if regd_events.event_id == event_id:
                    raise Exception(f"Event with Event ID {event_id} is already registered")
                if regd_events.event_name == event_name:
                    raise Exception(f"Event with Event Name {event_name} is already registered")
            self.events[event_id] = event
            print(f"{event_name} with {prize_name} is added successfully")
        except Exception as e:
            print(str(e))

    def register_member(self, member_id, event_id):
        try:
            if member_id not in self.members.keys():
                raise Exception(f"Member ID {member_id} is not yet registered")
            if event_id not in self.events.keys():
                raise Exception(f"Event Id {event_id} is not yet registered")
            if event_id not in self.event_regd:
                self.event_regd[event_id] = []
            self.event_regd[event_id].append(member_id)
            print(f"{self.members[member_id].name} registered to the {self.events[event_id].event_name} successfully")
        except Exception as e:
            print(str(e))

    def submit_bid(self, member_id, event_id, bid1=None, bid2=None, bid3=None, bid4=None, bid5=None):
        try:
            if member_id not in self.members.keys():
                raise Exception(f"Member ID {member_id} is not yet registered")
            if event_id not in self.events.keys():
                raise Exception(f"Event Id {event_id} is not yet added")
            if event_id not in self.event_regd or member_id not in self.event_regd[event_id]:
                raise Exception(f"Member ID {member_id} did not register for the event")
            bids = []
            for bid in [bid1, bid2, bid3, bid4, bid5]:
                if bid is not None:
                    if bid <= 0:
                        print("Bid should be greater than 0")
                    else:
                        bids.append(bid)
            if len(bids) == 0:
                raise Exception(f"No bids are placed")
            max_bid = max(bids)
            min_bid = min(bids)
            # print(max_bid, min_bid)
            if self.members[member_id].superCoins >= max_bid:
                self.members[member_id].superCoins -= max_bid
                if event_id not in self.event_bids:
                    self.event_bids[event_id] = []
                self.event_bids[event_id].append([member_id, min_bid])
                print(f"Bids submitted successfully")
        except Exception as e:
            print(str(e))

    def declare_winner(self, event_id):
        try:
            if event_id not in self.events.keys():
                raise Exception(f"Event Id {event_id} is not yet added")
            if event_id not in self.event_bids or len(self.event_bids[event_id]) == 0:
                raise Exception(f"No bids are present for Event ID {event_id}")
            bids = self.event_bids[event_id]
            bids.sort(key=lambda x: x[1])
            winner_member_id = bids[0][0]
            winner_bid = bids[0][1]
            self.events[event_id].winner = self.members[winner_member_id]
            self.events[event_id].winner_bid = winner_bid
            self.winners.append((event_id, self.events[event_id].event_date))
            print(f"{self.members[winner_member_id].name} wins the {self.events[event_id].prize_name} with lowest bid of {winner_bid}")
        except Exception as e:
            print(str(e))

    def see_past_winners(self, sort_by_date=False, sort_by_id=False):
        past_events = self.winners[-5:]
        if sort_by_date:
            past_events.sort(key=lambda x: x[1])
        if sort_by_id:
            past_events.sort(key=lambda x: x[0])
        for event_id, event_date in past_events:
            print(self.events[event_id])

