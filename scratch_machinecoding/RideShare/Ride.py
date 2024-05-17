from User import User, UserNotRegistered
from Vehicle import Vehicle, VehicleAlreadyRegistered, VehicleNotRegistered


class Ride(User, Vehicle):
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.offeredRides = []
        self.ridemap = dict()
        self.offer = 1

    def add_user(self, name, sex, age):
        try:
            user = User(name, sex, age)
            self.users.append(user)
            # print("User added successfully")
        except Exception as e:
            print(e)
    
    def check_user_registration(self, username):
        user = None
        for usr in self.users:
            if usr.get_name() == username:
                return usr
        raise UserNotRegistered("User registration is not yet done.")

    def check_vehicle_registration(self, license_plate):
        for curr_vehicle in self.vehicles:
            if curr_vehicle.get_license_plate() == license_plate:
                return curr_vehicle
        return None

    def add_vehicle(self, username, vehicle_type, license_plate):
        try:
            user = self.check_user_registration(username)
            
            if not self.check_vehicle_registration(license_plate):
                vehicle = Vehicle(user, vehicle_type, license_plate)
                self.vehicles.append(vehicle)
                # print("Vehicle added successfully")
            else:
                raise VehicleAlreadyRegistered("Vehicle is already registered")
        except Exception as e:
            print(e)
    
    def offer_rides(self, username, origin, destination, vehicle_type, vehicle_license, available_seats):
        user = self.check_user_registration(username)
        vehicle = self.check_vehicle_registration(vehicle_license)
        if not vehicle:
            raise VehicleNotRegistered("Register the vehicle first")
        user.set_rides_offered()
        vehicle.set_available_seats(available_seats)
        offered = {
            "user": user,
            "origin": origin,
            "destination": destination,
            "vehicle": vehicle
        }
        self.offeredRides.append(offered)
    
    def search_based_on_vacancy(self, origin, destination, seat):
        get_rides = []
        for i, rides in enumerate(self.offeredRides):
            if rides["origin"] == origin and rides["destination"] == destination and rides["vehicle"].available_seats >= seat and not rides["vehicle"].availability:
                get_rides.append([i, rides["vehicle"].available_seats])
        if get_rides:
            get_rides.sort(reverse=True, key=lambda x: x[1])
            return get_rides[0][0]
        print(f"No Rides Found based on vacancy {seat}")
        return None

    def search_based_on_vehicle(self, origin, destination, seat, vehicle_type):
        get_rides = []
        for i, rides in enumerate(self.offeredRides):
            if rides["origin"] == origin and rides["destination"] == destination and rides["vehicle"].available_seats >= seat \
                and rides["vehicle"].vehicle_type == vehicle_type and not rides["vehicle"].availability:
                get_rides.append(i)
        if get_rides:
            return get_rides[0]
        print(f"No Rides Found based on desired vehicle type {vehicle_type}")
        return None
    
    def select_ride(self, username, origin, destination, seat, selection_strategy):
        user = self.check_user_registration(username)
        if selection_strategy.lower() == "most vacant":
            booking_id = self.search_based_on_vacancy(origin, destination, seat)
        else:
            booking_id = self.search_based_on_vehicle(origin, destination, seat, selection_strategy)
        if booking_id is not None:
            self.offeredRides[booking_id]["vehicle"].set_availability(user)
            return booking_id
        return None
    
    def end_ride(self, booking_id):
        user = self.offeredRides[booking_id]["vehicle"].get_availability()
        self.offeredRides[booking_id]["vehicle"].set_availability()
        user.set_rides_taken()
        # print(f'Ride for User: {user.name} ended')
    
    def print_ride_stats(self):
        print("###########################################################################################")
        print("#############################        STATS          #######################################")
        print("###########################################################################################")
        print("User \t Rides Taken \tRides Offered")
        for usr in self.users:
            print(f"{usr.name} \t\t{usr.rides_taken}\t\t{usr.rides_offered}")
        print("###########################################################################################")
    
    def print_offered_rides(self):
        for offer in self.offeredRides:
            print(offer["user"], offer["origin"], offer["destination"], offer["vehicle"])

ride = Ride()