intro = "The land has been captured by the isopod king. After many years you have reached his castle, you must asscend to the top floor and kill the isopod king"
print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("please type in all capitals")
again = "Try again"
print("welcome to isopod adventure")
name = input("what is your name")
loop = True
while loop == True:
    load_save = input("would you like to load your previous save")
    if load_save == "YES":
        with open('objs.pkl', "rb") as f:  # Python 3: open(..., 'rb')
            obj0 = pickle.load(f)
            print(obj0)
        
        loop = False
    elif load_save == "NO":
        player_xp = 0
        potions = 5
        character = True
        loop = False
        while character == True:
            class_ = input("please select a class \n KNIGHT \n MAGE \n THIEF")
            if class_ == "KNIGHT":
                con_1 = input("the knight has a 20 damage sword and a shield \nit also has increased health but slower speed \nwould you like to pick this class \n YES        NO")
                if con_1 == "YES":
                    max_health = 150
                    player_health = 150
                    player_speed = 2
                    shield = True
                    melee_damage = 20
                    magic_damage = 0
                    melee = True
                    magic = False
                    character = False
                    loop1 = True
                elif con_1 == "NO":
                    character = True

                else:
                    print(again)
                    character = True
            elif class_ == "MAGE":
                con_2 = input("the mage has a 25 damage staff\n it has defult health but quicker speed\nwould you like to pick this class\n YES     NO")
                if con_2 == "YES":
                    max_health = 100
                    player_health = 100
                    player_speed = 10
                    shield = False
                    magic_damage = 25
                    melee_damage = 0
                    melee = False
                    magic = True
                    character = False
                    loop1 = True
                elif con_2 == "NO":
                    character = True
                else:
                    print(again)
                    chatacter = True
            elif class_ == "THIEF":
                con_3 = input("the thief has a 10 damage sword and a 15 damage wand\n it has defult helth and defult speed\n would you like to pick this class\n YES    NO")
                if con_3 == "YES":
                    player_speed = 5
                    max_health = 100
                    player_health = 100
                    sheild = False
                    magic_damage = 15
                    melee_damage = 10
                    melee = True
                    magic = True
                    character = False
                    loop1 = True
                elif con_3 == "NO":
                    character = True
                else:
                    print(again)
                    character = True

            
                
        while loop1 == True:
            difficulty = input("please select a difficulty \n EASY  NORMAL  HARD")
            if difficulty == "EASY":
                boss_level = 25
                iso = "juvinile isopod"
                loop1 = False
                level_= True
            elif difficulty == "NORMAL":
                boss_level = 50
                iso = "adolesent isopod"
                loop1 = False
                level_ = True
            elif difficulty == "HARD":
                boss_level = 100
                iso = "isopod"
                loop1 = False
                level_ = True
            else:
                print(again)
        while level_ == True:
            print(intro)
            level = 1
            level_ = False
        levels = True
        while levels == True:
            import random
            level_1 = random.randint(1, 4)
            if level == boss_level:
                print("boss")
            else:
                if player_health <= 0:
                    print("you died")
                    exit()
                else:
                    pot = True
                    while pot == True:
                        
                        potion_use = input("would you like to heal")
                        if potion_use == "YES":
                            if potions > 0:
                                potion_health = max_health / 5
                                player_health = player_health + potion_health
                                potions = potions - 1
                                pot = False
                            else:
                                print("no potions")
                                pot = False
                        elif potion_use == "NO":
                            print (str(potions) + "potions remainig")
                            pot = False
                        else:
                            print(again)

            
                    if level_1 == 1:
                        import random
                        monster_type = random.randint(1, 3)
                        if monster_type == 1:
                                monster = iso
                        elif monster_type == 2:
                                monster = "skeleton"
                        elif monster_type == 3:
                                monster = "slime"
                        damage_times = 1
                        monster_health = level * 100
                        monster_damage = level * 10
                        melee_weapon_damage = melee_damage * damage_times
                        magic_weapon_damage = magic_damage * damage_times
                        shield_reflect = monster_damage / 10
                        monster_speed = level * 2
                        potion_health = max_health / 5
                        high = level * 20
                        low = level * 1
                        import random
                        monster_xp = random.randint(low, high)
                        if player_speed > monster_speed:
                                battle = False
                                while battle == False:
                                    if monster_health <= 0:
                                        print("you killed the " + monster)
                                        player_xp = player_xp + monster_xp
                                        print(str(monster_xp) + " xp gained")
                                        player_xp = player_xp + monster_xp
                                        print("xp = " + str(player_xp))
                                        if player_xp >= 100:
                                                skill = input("level up \n select a skill to level up \n ATTACK/HEALTH/SPEED")
                                                if skill == "HEALTH":
                                                        player_health = player_health + 20
                                                        max_health = max_health + 20
                                                        player_xp = player_xp - 100
                                                        battle = True
                                                elif skill == "SPEED":
                                                        player_speed = player_speed + 1
                                                        player_xp = player_xp - 100
                                                        battle = True
                                                elif skill == "ATTACK":
                                                        damage_time = damage_times + 0.1
                                                        player_xp = player_xp - 100
                                                        battle = True
                                                else:
                                                        print("try again")

                                    elif player_health <= 0:
                                        print("you died")
                                        battle = True
                                    else:
                                        print("---YOU ENCOUNTERED A MONSTER---")
                                        print(monster + " health " + str(monster_health))
                                        print(name + " health " + str(player_health))
                                        move = input("what would you like to do?\nATTACK   DEFEND\nHEAL     ESCAPE\n(please use all capitals)")
                                        if move == "ATTACK":
                                                attack_type = input("MELEE/MAGIC")
                                                if attack_type == "MELEE":
                                                        if melee == True:
                                                                print("you attacked the " + monster)
                                                                monster_health = monster_health - melee_weapon_damage
                                                                print(monster + " attacks")
                                                                player_health = player_health - monster_damage
                                                        else:
                                                                print("you dont have a melee weapon")
                                                                print(monster + " attacks")
                                                                player_health = player_health - monster_damage
                                                elif attack_type == "MAGIC":
                                                        if magic == True:
                                                                print("you attacked the " + monster)
                                                                monster_health = monster_health - magic_weapon_damage
                                                                print(monster + " attacks")
                                                                player_health = player_health - monster_damage
                                                        else:
                                                                print("you dont have a melee weapon")
                                                                print(monster + " attacks")
                                                                player_health = player_health - monster_damage
                                                else:
                                                        print("try again")
                                        elif move == "DEFEND":
                                                 if sheild == True:
                                                        import random
                                                        chance = random.randint(0, 100)
                                                        if chance > 50:
                                                                print("you stoped the attack")
                                                                monster_health = monster_health - shield_reflect
                                                        elif chance <= 50:
                                                                print("block failed")
                                                                player_health = player_health - monster_damage
                                                                
                                                 elif shield == False:
                                                    print("you havent got a shield")
                                                    player_health = player_health - monster_damage
                                        elif move == "HEAL":
                                                if potions <= 0:
                                                        print("you have no potions")
                                                        player_health = player_health - monster_damage
                                                else:
                                                        potions = potions - 1
                                                        player_health = player_health + potion_health
                                                        print("potion used")
                                                        player_health = player_health - monster_damage
                                                        if player_health > max_health:
                                                            player_health = max_health
                                                        else:
                                                               battle = False
                                        elif move == "ESCAPE":
                                                import random
                                                escape = random.randint(0, 100)
                                                if escape < 50:
                                                        battle = True
                                                else:
                                                        print("you could not escape")

                                        else:
                                                print("try again")
                        else:
                                battle = False
                                while battle == False:
                                         if monster_health <= 0:
                                                print("you killed the " + monster)
                                                player_xp = player_xp + monster_xp
                                                print(str(monster_xp) + " xp gained")
                                                player_xp = player_xp + monster_xp
                                                print("xp = " + str(player_xp))
                                                if player_xp >= 100:
                                                        skill = input("level up \n select a skill to level up \n ATTACK/HEALTH/SPEED")
                                                        if skill == "HEALTH":
                                                                player_health = player_health + 20
                                                                max_health = max_health + 20
                                                                player_xp = player_xp - 100
                                                                battle = True
                                                        elif skill == "SPEED":
                                                                player_speed = player_speed + 1
                                                                player_xp = player_xp - 100
                                                                battle = True
                                                        elif skill == "ATTACK":
                                                                damage_time = damage_times + 0.1
                                                                player_xp = player_xp - 100
                                                                battle = True
                                                        else:
                                                                print("try again")

                                         elif player_health <= 0:
                                                print("you died")
                                                battle = True
                                         else:
                                                print(monster + " health " + str(monster_health))
                                                print(name + " health " + str(player_health))
                                                move = input("what would you like to do?\nATTACK   DEFEND\nHEAL     ESCAPE\n(please use all capitals)")
                                                if move == "ATTACK":
                                                        attack_type = input("MELEE/MAGIC")
                                                        if attack_type == "MELEE":
                                                                if melee == True:
                                                                        print("you attacked the " + monster)
                                                                        monster_health = monster_health - melee_weapon_damage
                                                                        print(monster + " attacks")
                                                                        player_health = player_health - monster_damage
                                                                else:
                                                                    print("you dont have a melee weapon")
                                                                    print(monster + " attacks")
                                                                    player_health = player_health - monster_damage
                                                        elif attack_type == "MAGIC":
                                                                if magic == True:
                                                                        print("you attacked the " + monster)
                                                                        monster_health = monster_health - magic_weapon_damage
                                                                        print(monster + " attacks")
                                                                        player_health = player_health - monster_damage
                                                                else:
                                                                    print("you dont have a melee weapon")

                                                                    print(monster + " attacks")
                                                                    player_health = player_health - monster_damage
                                                        else:
                                                                print("try again")
                                                elif move == "DEFEND":   
                                                        if sheild == True:
                                                                import random
                                                                chance = random.randint(0, 100)
                                                                if chance > 50:
                                                                  print("you stoped the attack")
                                                                  monster_health = monster_health - shield_reflect
                                                                elif chance <= 50:
                                                                        print("block failed")
                                                                        player_health = player_health - monster_damage
                                                        elif shield == False:
                                                                print("you havent got a shield")
                                                                player_health = player_health - monster_damage
                                                elif move == "HEAL":
                                                        if potions <= 0:
                                                                print("you have no potions")
                                                        else:
                                                                potions = potions - 1
                                                                player_health = player_health - monster_damage
                                                                player_health = player_health + potion_health
                                                                print("potion used")
                                                                player_health = player_health - monster_damage
                                                                if player_health > max_health:
                                                                        player_health = max_health
                                                                else:
                                                                        battle = False
                                                                                             
                                                elif move == "ESCAPE":
                                                        import random
                                                        escape = random.randint(0, 100)
                                                        if escape < 50:
                                                                battle = True
                                                        else:
                                                                print("you could not escape")
                                                                        
                                                        
                                                else:
                                                        print("try again")
                    elif level_1 == 2:
                        print("you found a ladder leading to the next floor")
                        level = level+1
                        player_health = max_health

                    elif level_1 == 3:
                        trap_damage = max_health / 10
                        import random
                        trap = random.randint(1, 2)
                        if trap == 1:
                            a_trap = True
                            b_trap = False
                        else:
                            b_trap = True
                            a_trap = False
                        door = input("you encounter two doors. do you go through door a or b")
                        if door == "A":
                            if a_trap == True:
                                print("it was a trap")
                                player_health = player_health - trap_damage
                            else:
                                print("you go through the door")
                        elif door == "B":
                            if b_trap == True:
                                print("it was a trap")
                                player_health = player_health - trap_damage
                            else:
                                print("you go through the door")
                    elif level_1 == 4:
                        ope = input("you find an old wooden chest, do you open it")
                        if ope == "YES":
                            import random
                            loot_type = random.randint(0, 9)
                            if loot_type == 1:
                                print("loot")
else:
    print(again)
