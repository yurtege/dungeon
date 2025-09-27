from random import randint
import random
from monster import Monster
from armor import armors
from weapon import weapons
from room import Room


class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.rooms = []
        self.generate_level()

#CREATING A LEVEL
    def generate_level(self):
        m = randint(2,4)  #number of corridors
        corridors = []
        for a in range(m):
            n = randint(3,6)  #number of rooms for each corridor
            corridor = []
            for b in range(n):
                room = Room(f"L{self.level_number}_R{a}{b}")  #numbering rooms
                monster = Monster(f"m{b}{self.level_number}", self.level_number ** 2 + randint(5,8))    #monster creation
                monster.weapon = random.choice(weapons)   #monsters weapons
                monster.armor = random.choice(armors)   #monsters armors
                room.add_monster(monster)
                room.add_hostage()
                if corridor:
                    corridor[-1].connect(room)            #connecting rooms
                self.rooms.append(room)
                corridor.append(room)
            corridors.append(corridor)


        for a in range(len(corridors)- 1):           #connecting coridors
            r1 = random.choice(corridors[a])
            r2 = random.choice(corridors[a + 1])
            r1.connect(r2)

#LEVEL CREATİON AND CURRENT ROOM
levels = []
for l in range(1,17):
    levels.append(Level(l))
for l in range(1,16):
    levels[l-1].rooms[-1].connect(levels[l].rooms[0])
current_level = levels[0]
current_room = current_level.rooms[0]

