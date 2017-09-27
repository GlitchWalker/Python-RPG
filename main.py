from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
ice = Spell("Ice", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White MAgic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create Charge Magic
pray = Spell("Pray", 0, 30, "charge")

# Create some Items
potion = Item("Potion", "potion", "Heals small amount of HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals large amount of HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals insane amount of HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
megalixer = Item("Megelixer", "elixer", "Fully restores HP/MP of entire party", 9999)

grenade = Item("Grenade", "attack", "Deals a lot of damage", 500)

player_magic = [fire, thunder, ice, meteor, cure, cura, pray]
player_items = [{"item": potion, "nmb": 15}, {"item": hipotion, "nmb": 5},
                {"item": superpotion, "nmb": 2}, {"item": elixer, "nmb": 1},
                {"item": grenade, "nmb": 10}]

# Instantiate People
player1 = Person("Ronius :", 3260, 65, 60, 34, player_magic, player_items)
player2 = Person("Valos  :", 4160, 65, 60, 34, player_magic, player_items)
player3 = Person("Rydiana:", 3089, 65, 60, 34, player_magic, player_items)

enemy1 = Person("Imp    :", 1250, 130, 560, 325, [], [])
enemy2 = Person("Magus  :", 12000, 65, 45, 250, [], [])
enemy3 = Person("Imp    :", 1250, 130, 560, 325, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]
running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An enemy attacks!" + bcolors.ENDC)

print("==========================")
for enemy in enemies:
    enemy.get_enemy_stats()

print("\n")

while running:
    print("==========================")

    print("NAME          HP                                                           MP")
    print("----          --                                                           --")
    for player in players:
        player.get_stats()

    print("\n")
    print("==========================")
    for player in players:
        player.choose_action()
        choice = input("Choose action for " + player.name.replace(" ", ""))
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)

            print("--------------------------")
            print(bcolors.FAIL + str(player.name.replace(" " + ":", "")), "attacks " + enemies[enemy].name.replace(" " + ":", ""), " for", dmg,  bcolors.ENDC)

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has been defeated.")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose Magic:")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()


            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)
            print("--------------------------")

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":

                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)

                print(bcolors.OKBLUE + spell.name + " cast on " + enemies[enemy].name.replace(" ", "") + " for ", str(magic_dmg), "HP." + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has been defeated.")
                    del enemies[enemy]

            elif spell.type == "charge":
                player.charge(magic_dmg)
                print(bcolors.OKBLUE + spell.name + " charges", str(magic_dmg), "MP." + bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item:")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["nmb"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue

            player.items[item_choice]["nmb"] -= 1

            if item.type == "potion":
                player.heal(item.dmg)
                print("--------------------------")
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.dmg), "HP" + bcolors.ENDC)
            elif item.type == "elixer":
                if item.name == "Megalixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.heal(player.maxhp)
                    player.charge(player.maxmp)

                print("--------------------------")
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.dmg), "HP" + bcolors.ENDC)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.dmg), "MP" + bcolors.ENDC)
            elif item.type == "attack":

                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(item.dmg)

                print(bcolors.FAIL + item.name + " used on " + enemies[enemy].name.replace(" ", "") + " for", str(item.dmg) + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has been defeated.")
                    del enemies[enemy]


        print("--------------------------")

    enemy_choice = 1
    target = random.randrange (0, 2)

    enemy_dmg = enemies[0].generate_damage()
    players[target].take_damage(enemy_dmg)
    print(bcolors.FAIL + str(enemies[target].name.replace(" ", "")), "attacks", str(players[target].name.replace(" ", "")), "for", str(enemy_dmg) + bcolors.ENDC)

    print("==========================")

    for enemy in enemies:
        enemy.get_enemy_stats()

    print("\n")

    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    if defeated_enemies == 2:
        print (bcolors.OKGREEN + "You win!!" + bcolors.ENDC)
        running = False

    elif defeated_players == 2:
        print(bcolors.FAIL + "The enemy has defeated you!! GAME OVER" + bcolors.ENDC)
        running = False

'''
Various testing tools I wanted to keep to hand


print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))

'''
