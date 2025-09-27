from random import randint


class Room:
    def __init__(self, name):
        self.name = name
        self.doors = []
        self.mon = []
        self.stor_wep = []
        self.stor_arm = []
        self.hostage = 0
#CONNECTING THE ROOMS
    def connect(self, other):
        self.doors.append(other)
        other.doors.append(self)
#ADDING RANDOM MONSTERS TO ROOMS
    def add_monster(self, target):
        self.mon.append(target)
    def add_hostage(self):
        self.hostage += randint(0,1)


