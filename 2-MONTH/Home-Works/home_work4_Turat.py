class TimeDesk:
    def __init__(self, seconds):
        self.seconds = seconds

    def show_time(self):
        days = int(self.seconds / (24 * 60 * 60))
        self.seconds -= days * 24 * 60 * 60
        hours = int(self.seconds / 60 / 60)
        self.seconds -= hours * 60 * 60
        minutes = int(self.seconds / 60)
        self.seconds -= minutes * 60
        return f"{days} days, {hours} hours, {minutes} minutes, {self.seconds} seconds"

    def show_your_time(self):
        seconds = int(input("Enter the number of seconds: "))
        d = TimeDesk(seconds)
        return d.show_time()

    def __str__(self):
        return f"Seconds: {self.seconds}\n"


oclock = TimeDesk(1000)

print(oclock.show_your_time())


#########################################################################################################################################################################


class Tor:
    def __init__(self, name, surname, family):
        self.name = name
        self.surname = surname
        self.family = family

    @property
    def full_information(self):

        info = self.surname + " " + self.name + " " + self.family
        return info

    @full_information.setter
    def full_information(self, info):
        self.name, self.surname, self.family = info.split()

    @full_information.deleter
    def full_information(self):
        self.surname = None
        self.name = None
        self.family = None
        print("Full information deleted! ")

    def __str__(self):
        return f"\nName: {self.name}\n"\
               f"\nSurname: {self.surname}\n"\
               f"\nFamily: {self.family}\n"


Loki = Tor(name='Tor', surname='Ragareg', family='Gods')

print(Loki)

print(Loki.full_information)

Loki.full_information = "Tor GodFather Ragnareg"

print(Loki.full_information)

print(Loki.full_information)

print(Loki.full_information)

class TorsAge():
    @staticmethod
    def age(age):
        if age >= 18:
            return True
        else:
            return False

print("~" * 30)
print(TorsAge.age(18))

