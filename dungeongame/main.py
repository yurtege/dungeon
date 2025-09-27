from hero import Hero
from level import current_level

hero = Hero(input("Pls Enter A Name>> "))
#GREETING AND START
message = (f"WELCOME TO THE DUNGEON {hero.name} \nTotal rooms:{len(current_level.rooms)}"
           f"\nYou are in {hero.current_room.name}\nThere is monster {hero.current_room.mon[0].name}\nHero's HP: {hero.health}\nMonsters HP: {hero.current_room.mon[0].health}")

print(message)
while hero.health > 0:
    answer = input("Do you wanna move/fight/home/collect/drop/choose \n>")
# MOVING BETWEEN ROOMS
    if answer.lower() == 'move' and hero.current_room.mon[0].health <= 0:
        hero.move()
    elif answer.lower() == 'move' and hero.current_room.mon[0].health > 0:
        print("You can't move between rooms before killing the monster!")

#FIGHTING
    elif answer.lower() == 'fight':
        hero.fight()

#TAKING THE MONSTERS ITEMS
        while True:
            answer2 = input("Pick/Leave? >")
            if answer2.lower() == 'pick':
                hero.pick()
                break
            elif answer2.lower() == 'leave':
                print("Items are captured by the current room")
                break
            else:
                print("Pls write 'pick' or 'leave' ")

    elif answer.lower() == 'fight' and hero.current_room.mon[0].health <= 0:
        print("You already killed the monster. Pls move or go home")
#QUIT
    elif answer.lower() == 'home' or hero.health <= 0:
        print("Game Over")
        break

#COLLECTING ITEMS
    elif answer.lower() == 'collect' and (len(hero.current_room.stor_wep) > 0 or len(hero.current_room.stor_arm) > 0):
        hero.collect()
    elif answer.lower() == 'collect' and (len(hero.current_room.stor_wep) <= 0 and len(hero.current_room.stor_arm) <=0):
        print("There isn't any item on the floor")

#DROPPİNG İTEMS
    elif answer.lower() == 'drop':
        hero.drop()

#CHOOSING THE ITEM
    elif answer.lower() == 'choose':
        hero.choose()
    else:
        print("You can't do that .d")

#TOTAL SCORE
total_score = 0
for a in hero.inv_wep:
    total_score += a.value
for a in hero.inv_arm:
    total_score += a.value
print(f"Total score is: {total_score + hero.resqued_hostages}")







