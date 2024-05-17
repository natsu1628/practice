from Bid import Bid


bid = Bid()

def test_add_member():
    bid.add_member("Sanjay", 1, 1000)
    bid.add_member("Shweta", 2, 500)

def test_add_events():
    bid.add_event(1, "BDD", "Iphone-14", "2023-06-01")
    bid.add_event(2, "BDD1", "Iphone-14", "2023-06-03")

def test_register_member():
    bid.register_member(1, 1)
    bid.register_member(2, 2)

def test_submit_bids():
    bid.submit_bid(1, 1, 100, 200, 300, 400, 1000)
    bid.submit_bid(2, 1, 400, 500)
    bid.submit_bid(2, 2, 400, 500)

def test_declare_winner():
    bid.declare_winner(2)
    bid.declare_winner(1)


if __name__ == "__main__":
    test_add_member()
    test_add_events()
    test_register_member()
    test_submit_bids()
    # print(bid.event_bids)
    print("########################################################")
    test_declare_winner()
    print("########################################################")
    bid.see_past_winners()
    print("########################################################")
    bid.see_past_winners(sort_by_id=True)
    print("########################################################")
    bid.see_past_winners(sort_by_date=True)
    print("########################################################")
    # for member in bid.members:
    #     print(bid.members[member])

