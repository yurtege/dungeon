from character import Character

class Monster(Character):
    def __init__(self, name, health):
        super().__init__(name)
        self.weapon = ""
        self.armor = ""
        self.health = health