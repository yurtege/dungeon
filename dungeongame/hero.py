from character import Character
from weapon import w1
from armor import a1
from level import current_room



class Hero(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health = 200
        self.weapon = w1
        self.armor = a1
        self.inv_wep = []   #inventory for weapons
        self.inv_arm = []   #inventory for armors
        self.current_room = current_room
        self.resqued_hostages = 0

#CHOOSİNG WHICH ITEM TO USE FROM INVENTORY
    def choose(self):
        print("Choose the item you want to use")
        for a, b in enumerate(self.inv_wep):
            print(a + 1, b.name)
        for a, b in enumerate(self.inv_arm):
            print(a + 4, b.name)
        while True:
            try:
                choice = int(input("My choice is(if you done choosing just write :100 ) >>"))
                if choice <= 3:
                    self.choose_wep(choice)
                    print(f"Hero is using {self.inv_wep[choice - 1].name}")
                elif 100 > choice > 3:
                    self.choose_arm(choice)
                    print(f"Hero is wearing {self.inv_arm[choice - 4].name}")
                elif choice == 100:
                    print("Done..")
                    break
            except Exception:
                print("You cant do that. Pls enter a valid number.")

#CHOOSİNG WEAPONS
    def choose_wep(self, secim):
        self.weapon = self.inv_wep[secim-1]
#CHOOSİNG ARMORS
    def choose_arm(self, secim):
        self.armor = self.inv_arm[secim-4]

#ATTACK METHOD
    def attack(self, hedef):
        self.health -= hedef.weapon.real_damage * self.armor.power
        hedef.health -= self.weapon.real_damage * hedef.armor.power
        hedef.health = max(0, hedef.health)
        self.health = max(0, self.health)
#FIGHT METHOD
    def fight(self):
        while self.current_room.mon[0].health > 0 and self.health > 0:
            input("Press 'ENTER' to attack")
            self.attack(self.current_room.mon[0])
            print(f"Hero's HP: {self.health}")
            print(f"Monsters HP: {self.current_room.mon[0].health}")
        if self.health <= 0:
            print("You are dead")
        elif self.current_room.mon[0].health <= 0:
            print(f"Monster is dead\nIt's items: 1-{self.current_room.mon[0].weapon.name} 2-{self.current_room.mon[0].armor.name}")
            self.current_room.stor_wep.append(self.current_room.mon[0].weapon)
            self.current_room.stor_arm.append(self.current_room.mon[0].armor)
            print(f"{self.current_room.hostage} hostages resqued.")
            self.resque()

#RESQUING HOSTAGES FROM MONSTERS
    def resque(self):
        self.resqued_hostages += self.current_room.hostage

#PICKING OR LEAVING THE ITEMS
    def pick(self):
        while True:
            g = input("Which item?(1 ,2, 12(both) )")
            if g == '1' and len(self.inv_wep) < 3:
                print(f"You've picked {self.current_room.mon[0].weapon.name}")
                self.inv_wep.append(self.current_room.mon[0].weapon)
                self.current_room.stor_wep.remove(self.current_room.mon[0].weapon)
                break

            elif g == '2' and len(self.inv_arm) < 3:
                print(f"You've picked {self.current_room.mon[0].armor.name}")
                self.inv_arm.append(self.current_room.mon[0].armor)
                self.current_room.stor_arm.remove(self.current_room.mon[0].armor)
                break
            elif g == '12' and (len(self.inv_wep) < 3 and len(self.inv_arm) < 3):
                print(f"You've picked {self.current_room.mon[0].weapon.name} and {self.current_room.mon[0].armor.name}")
                self.inv_wep.append(self.current_room.mon[0].weapon)
                self.inv_arm.append(self.current_room.mon[0].armor)
                self.current_room.stor_wep.remove(self.current_room.mon[0].weapon)
                self.current_room.stor_arm.remove(self.current_room.mon[0].armor)
                break
            elif len(self.inv_wep) == 3 or len(self.inv_arm) == 3:
                print("Your inv full for it. Pls drop something first.")
                print(f"Hero's {len(self.inv_wep)} weapons and {len(self.inv_arm)} armors")
                break
            else:
                print("Pls select between choices")
#DROPPING ITEMS FROM INVENTORY
    def drop(self):
        while True:
            print("Weapons to drop>>>")
            for a, b in enumerate(self.inv_wep):
                print(a+1, b.name)
            print("Armors to drop>>>")
            for a, b in enumerate(self.inv_arm):
                print(a+4 ,b.name)
            try:
                drop_name = int(input("Chose the items you want to drop..(to quit write: '100')"))
                if drop_name <= 3:
                    print(f"You dropped {self.inv_wep[drop_name - 1].name}")
                    self.current_room.stor_wep.append(self.inv_wep[drop_name - 1])
                    self.inv_wep.remove(self.inv_wep[drop_name - 1])
                elif 3 < drop_name < 99:
                     print(f"You dropped {self.inv_arm[drop_name - 4].name}")
                     self.current_room.stor_arm.append(self.inv_arm[drop_name - 4])
                     self.inv_arm.remove(self.inv_arm[drop_name - 4])
                elif drop_name == 100:
                    print("Done")
                    break
            except Exception:
                print("You can't drop it..")
#MOVING BETWEEN ROOMS
    def move(self):
        print("Available doors>>")
        for v in range(len(self.current_room.doors)):
            print(f"Door{v + 1} = {self.current_room.doors[v].name}")
        while True:
            choice = input("I choose (first_door, second_door .... :")
            if choice == 'first_door':
                self.current_room = self.current_room.doors[0]
                print(f"You are in {self.current_room.name}")
                break
            elif choice == 'second_door':
                self.current_room = self.current_room.doors[1]
                print(f"You are in {self.current_room.name}")
                break
            elif choice == 'third_door':
                self.current_room = self.current_room.doors[2]
                print(f"You are in {self.current_room.name}")
                break
            elif choice == 'fourth_door':
                self.current_room = self.current_room.doors[3]
                print(f"You are in {self.current_room.name}")
                break
            else:
                print("Pls choose the right door")
        print(f"There is monster {self.current_room.mon[0].name}")
        print(f"MonsterHp: {self.current_room.mon[0].health}  HeroHp: {self.health}")
#COLLECTING ITEMS FROM THE GROUND
    def collect(self):
        print("Weapons >>>")
        for s, h in enumerate(self.current_room.stor_wep):
            print(s + 1, h.name)
        for a, b in enumerate(self.current_room.stor_arm):
            print(a + 4, b.name)
        while True:
            try:
                f = int(input("Collect among the available numbers?(1-2-3..(If you're done write: 100))"))
                if f in (1, 3) and len(self.inv_wep) < 3:
                    self.inv_wep.append(self.current_room.stor_wep[f - 1])
                    print(f"You collected {self.current_room.stor_wep[f - 1].name}")
                    self.current_room.stor_wep.remove(self.current_room.stor_wep[f - 1])
                    break
                elif f == 100:
                    break
                elif f in (4, 6) and len(self.inv_arm) < 3:
                    self.inv_arm.append(self.current_room.stor_arm[f - 4])
                    print(f"You collected {self.current_room.stor_arm[f - 4].name}")
                    self.current_room.stor_arm.remove(self.current_room.stor_arm[f - 4])
                    break
                elif len(self.inv_wep) >= 3 and f in (1, 3):
                    print("Your weapon inventory is full")
                    break
                elif len(self.inv_arm) >= 3 and f in (4, 99):
                    print("Your armor inventory is full")
                    break

            except Exception:
                print("Pls choose available one(s)")















