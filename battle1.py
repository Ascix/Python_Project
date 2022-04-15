import random
import math
import os
import config

eevee_hp = [20]

pikachu_hp = [18]

def battle_stats():
    os.system('clear') 
    print(f"""Eevee
HP: {eevee_hp[-1]}/{eevee_hp[0]}

            {config.pikachu_name}
            HP: {pikachu_hp[-1]}/{pikachu_hp[0]}""")
    print("\n")

def thundershock():
    thundershock_text = input(f"{config.pikachu_name} used Thundershock!")
    if random.randint(1,3) == 1:
        damage = 4.0
        if random.randint(1,16) == 1:
            print("A critical hit!")
            final_damage = damage * 1.5
            eevee_hp.append(eevee_hp[-1] - int(final_damage))
        else:
            eevee_hp.append(eevee_hp[-1] - int(damage))
    elif random.randint(1,3) == 2:
        damage = 5.0
        if random.randint(1,16) == 1:
            print("A critical hit!")
            final_damage = damage * 1.5
            eevee_hp.append(eevee_hp[-1] - int(final_damage))
        else:
            eevee_hp.append(eevee_hp[-1] - int(damage))
    else:
        damage = 6.0
        if random.randint(1,16) == 1:
            print("A critical hit!")
            final_damage = damage * 1.5
            eevee_hp.append(eevee_hp[-1] - int(final_damage))
        else:
            eevee_hp.append(eevee_hp[-1] - int(damage))

def tackle():
    tackle_text = input("Enemy Eevee used Tackle!")
    if random.randint(1,2) == 1:
        damage = 5.0
        if random.randint(1,16) == 1:
            print("A critical hit!")
            final_damage = damage * 1.5
            pikachu_hp.append(pikachu_hp[-1] - int(final_damage))
        else:
            pikachu_hp.append(pikachu_hp[-1] - int(damage))
    else:
        damage = 6.0
        if random.randint(1,16) == 1:
            print("A critical hit!")
            final_damage = damage * 1.5
            pikachu_hp.append(pikachu_hp[-1] - int(final_damage))
        else:
            pikachu_hp.append(pikachu_hp[-1] - int(damage))
    
    battle_stats()

def growl():
    battle_stats()
    text_growl1 = input(f"{config.pikachu_name} used Growl!")
    text_growl2 = input("Enemy Eevee's attack fell!")
    
def tail_whip():
    battle_stats()
    text_tail1 = input("Enemy Eevee used Tail Whip!")
    text_tail2 = input(f"{config.pikachu_name}'s defense fell!")
    battle_stats()

def enemy_turn():
    if random.randint(1,2) == 1:
        tackle()
        end_battle2()
        battle()
    else:
        tail_whip()
        battle()
        
def end_battle1():
    if eevee_hp[-1] <= 0:
        eevee_faint = input("Enemy Eevee fainted!")
        win = input(f"{config.player_name} defeated {config.rival_name}!")
        win2 = input(f"{config.rival_name}: What? Unbelievable! I picked the wrong Pokemon!")
        from lab import action_lab3
        action_lab3()
    else:
        enemy_turn()

def end_battle2():
    if pikachu_hp[-1] <= 0:
        pikachu_faint = input(f"{config.pikachu_name} fainted!")
        lose = input(f"{config.rival_name} defeated {config.player_name}!")
        lose2 = input(f"{config.rival_name}: Heh, piece of cake!")
        from lab import action_lab3
        action_lab3()
    else:
        battle()

def battle():
    while eevee_hp[-1] > 0 or pikachu_hp[-1] > 0:
        battle_stats()
        battle_options = input(f"""What do you want to do?
=====================
1. Fight
2. Item
3. PKMN
4. Run 

""")
        if battle_options == "1":
            battle_stats()
            while eevee_hp[-1] > 0 or pikachu_hp[-1] > 0:
                attack = input(f"""Choose an attack
=====================
1. Thundershock
2. Growl

""")
                if attack == "1":
                    battle_stats()
                    thundershock()
                    battle_stats()
                    end_battle1()
                elif attack == "2":
                    battle_stats()
                    growl()
                    battle_stats()
                    enemy_turn()
                else:
                    choose_attack = input("Choose an attack!")
                    battle_stats()
        elif battle_options == "2":
            item_text = input(f"You have no items!\n")
        elif battle_options == "3":
            pkmn_text = input(f"You have no other Pokemon!\n")
        elif battle_options == "4":
            run_text = input(f"You cannot run from a trainer battle!\n")
        else:
            nothing = input(f"Choose something to do!\n")