from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 100},
         {"name": "Ice", "cost": 10, "dmg": 124}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

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
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

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
