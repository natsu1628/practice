from User import UserNotProvided


class VehicleTypeNotProvided(Exception):
    pass

class VehicleLicensePlateNotProvided(Exception):
    pass

class VehicleAlreadyRegistered(Exception):
    pass

class VehicleNotRegistered(Exception):
    pass

class Vehicle(object):
    def __init__(self, user, vehicle_type, license_plate, availability=None):
        if not user:
            raise UserNotProvided("User is not provided during vehicle registration")
        if not vehicle_type:
            raise VehicleTypeNotProvided("Vehicle Type is not provided during vehicle registration")
        if not license_plate:
            raise VehicleLicensePlateNotProvided("Vehicle License Plate is not provided during vehicle registration")
        
        self.user = user
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.availability = availability
        self.available_seats = 0

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_license_plate(self):
        return self.license_plate

    def get_availability(self):
        return self.availability

    def set_availability(self, user=None):
        self.availability = user
    
    def set_available_seats(self, seats):
        self.available_seats = seats

    def __str__(self):
        return f"User: {self.user.name}, vehicle type: {self.vehicle_type}, license plate: {self.license_plate}, available seats: {self.available_seats}, availability: {self.availability}"
