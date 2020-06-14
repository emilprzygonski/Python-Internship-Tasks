class IllegalCarError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


class Cars:
    person_mass = 70

    def __init__(self, pax, mass, gear):

        self.pax_count = pax
        self.car_mass = mass
        self.gear_count = gear
        self.total_mass = mass + pax * self.person_mass
        if (pax < 1 or pax > 5):
            raise IllegalCarError("Number of passengers can't be less than 1 and more than 5")
        if (mass > 2000):
            raise IllegalCarError("Car mass cannot be greater than 2000 kg")

