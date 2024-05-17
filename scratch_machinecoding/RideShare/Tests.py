from Ride import ride

def test_add_user():
    ride.add_user("Rohan", "M", 36)
    ride.add_user("Sanjay", "M", 29)
    ride.add_user("Shweta", "F", 29)
    # for usr in ride.users:
    #     print(usr)

def test_add_vehicle():
    ride.add_vehicle("Rohan", "XUV", "KA-01-12345")
    ride.add_vehicle("Sanjay", "Swift", "KA-01-12346")
    ride.add_vehicle("Shweta", "Swift", "KA-01-12347")
    # for vh in ride.vehicles:
    #     print(vh)

def test_offer_rides():
    ride.offer_rides("Sanjay", "Bangalore", "Hyderabad", "Swift", "KA-01-12346", 1)
    ride.offer_rides("Rohan", "Bangalore", "Hyderabad", "XUV", "KA-01-12345", 2)

def test_select_ride():
    book_id1 = ride.select_ride("Sanjay", "Bangalore", "Hyderabad", 2, "most vacant")
    if book_id1 is not None:
        print(f"Booking Id1: {book_id1}")
    book_id2 = ride.select_ride("Shweta", "Bangalore", "Hyderabad", 1, "Swift")
    if book_id2 is not None:
        print(f"Booking Id2: {book_id2}")
    # book_id3 = ride.select_ride("Sanjay", "Bangalore", "Hyderabad", 1, "XUV")
    # if book_id3:
    #     print(f"Booking Id3: {book_id3}")

def test_end_ride():
    ride.end_ride(1)
    ride.end_ride(0)


if __name__ == "__main__":
    test_add_user()
    test_add_vehicle()
    test_offer_rides()
    test_select_ride()
    test_end_ride()
    ride.print_ride_stats()
