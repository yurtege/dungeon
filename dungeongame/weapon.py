#RANGE VALUES
close_range = 1
mid_range = 2
long_range = 3

class Weapon:
    def __init__(self, name, ranged, value, damage):
        self.name = name
        self.ranged = ranged
        self.value = value
        self.damage = damage

class CloseRanged(Weapon):
    def __init__(self, name,ranged, value, damage):
        super().__init__(name,ranged, value, damage)
        self.real_damage = self.damage * self.ranged

class MidRanged(Weapon):
    def __init__(self, name, ranged, value, damage):
        super().__init__(name,ranged, value, damage)
        self.real_damage = self.damage * self.ranged

class LongRanged(Weapon):
    def __init__(self, name,ranged, value, damage):
        super().__init__(name, ranged, value, damage)
        self.real_damage = self.damage * self.ranged

w1 = CloseRanged("Fist", close_range, 0, 5)
w2 = CloseRanged("Knife", close_range, 5, 10)
w3 = MidRanged("Small Axe", mid_range, 10, 15)
w4 = MidRanged("Big Axe", mid_range, 15, 20)
w5 = LongRanged("Arrow", long_range, 15, 20)
w6 = LongRanged("Shotgun", long_range, 20, 30)
weapons = [w1,w2,w3,w4,w5,w6]