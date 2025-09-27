class Armor:
    def __init__(self, name, power, value):
        self.name = name
        self.power = power
        self.value = value


a1 = Armor("lether armor", 0.9, 3)
a2 = Armor("bulletproof armor", 0.8, 5)
a3 = Armor("chainmail armor", 0.7, 10)
a4 = Armor("sensei armor", 0.6, 20)
a5 = Armor("god armor", 0.5, 30)
armors = [a1, a2, a3, a4, a5]