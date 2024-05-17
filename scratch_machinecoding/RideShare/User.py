class UserNameNotProvided(Exception):
    pass

class UserSexNotProvided(Exception):
    pass

class UserAgeNotProvided(Exception):
    pass

class UserAlreadyRegistered(Exception):
    pass

class UserNotProvided(Exception):
    pass

class UserNotRegistered(Exception):
    pass


class User(object):
    def __init__(self, name, sex, age):
        if not name:
            raise UserNameNotProvided("User name is not provided during registration")
        if not sex:
            raise UserSexNotProvided("User Sex is not provided during registration")
        if not age:
            raise UserAgeNotProvided("User Age is not provided during registration")

        self.name = name
        self.sex = sex
        self.age = age
        self.rides_offered = 0
        self.rides_taken = 0

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age
    
    def get_rides_offered(self):
        return self.rides_offered

    def get_rides_taken(self):
        return self.rides_taken
    
    def set_rides_offered(self):
        self.rides_offered += 1

    def set_rides_taken(self):
        self.rides_taken += 1
    
    def __str__(self):
        return f"User Name: {self.name}, Sex: {self.sex}, Age: {self.age}, Rides offered: {self.rides_offered}, Rides Taken: {self.rides_taken}"
