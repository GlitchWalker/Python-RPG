from classes.game import Person, bcolors
from classes.magic import Spell

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

# Instantiate People
player = Person(460, 65, 60, 34, [fire, thunder, ice, meteor, cure, cura, pray])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An enemy attacks!" + bcolors.ENDC)

while running:
    print("--------------------------")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg)
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic:")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()


        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " attacks for", str(magic_dmg), "HP." + bcolors.ENDC)
        elif spell.type == "charge":
            player.charge(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " charges", str(magic_dmg), "MP." + bcolors.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(bcolors.FAIL + "Enemy attacks for", str(enemy_dmg) + bcolors.ENDC)

    print("==========================")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)

    print("--------------------------")

    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    print("==========================")
    if enemy.get_hp() == 0:
        print (bcolors.OKGREEN + "You win!!" + bcolors.ENDC)
        running = False

    elif player.get_hp() == 0:
        print(bcolors.FAIL + "The enemy has defeated you!! GAME OVER" + bcolors.ENDC)
        running = False

'''
Various testing tools I wanted to keep to hand


print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))

'''
