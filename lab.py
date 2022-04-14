import os
import config

def nickname():
    os.system('clear')
    while True:
        nickname1 = input(f"""Do you want to give a nickname to Pikachu?
=====================    
1. Yes
2. No

""")
        if nickname1 == "1":
            config.pikachu_name = input("Give Pikachu a nickname: ").lower().capitalize()
            if (len(config.pikachu_name) < 1):
                print("\n")
                print("Please enter a nickname!\n")
                os.system('clear')
            else:
                nickname2 = input(f"{config.pikachu_name} loves their nickname!")
                break
        elif nickname1 == "2":
            break
        else:
            nothing = input("Please choose an option!\n")
            os.system('clear')


def action_lab():
    os.system('clear')
    print("You see a bunch of people in lab coats around.\n")
    while True:
        option_lab = input(f"""What do you want to do?
=====================
1. Talk to lab assistant
2. Talk to professor
3. Talk to rival
4. Leave the lab 

""")
        if option_lab == "1":
            assistant_text1 = input(f"Assistant: I study Pokemon under the professor \n")
            os.system('clear')
        elif option_lab == "2":
            prof_text1 = input(f"Professor: Ah {config.player_name}, you're finally here!") 
            prof_text2 = input("You can have this Pokemon I caught earlier.")
            prof_text3 = input(f"{config.player_name} received a Pikachu!\n")
            nickname()
            action_lab2()
        elif option_lab == "3":
            rival_text1 = input(f"{config.rival_name}: What took you so long to get here?\n")
            os.system('clear')
        elif option_lab == "4":
            lab_text1 = input(f"You leave the lab. \n")
            from home_town import action_home_town
            action_home_town()
        else:
            nothing1 = input(f"Choose something to do!\n")
            os.system('clear')

def action_lab2():
    os.system('clear')
    while True:
        option_lab2 = input(f"""What do you want to do?
=====================
1. Talk to lab assistant
2. Talk to professor
3. Talk to rival
4. Leave the lab 

""")
        if option_lab2 == "1":
            assistant_text1 = input(f"Assistant: I study Pokemon under the professor \n")
            os.system('clear')
        elif option_lab2 == "2":
            prof_text3 = input(f"Professor: If a wild Pokemon appears, your Pokemon can fight against it!\n")
            os.system('clear')
        elif option_lab2 == "3":
            rival_text3 = input(f"{config.rival_name}: Heh, my Pokemon look's a lot stronger.\n")
            os.system('clear')
        elif option_lab2 == "4":
            bb = input(f"Wait {config.player_name}! Let's check out our pokemon!")
            bb1 = input(f"Come on, I'll take you on!")
            os.system('clear')
            prebattle = input(f"{config.rival_name} wants to fight!\n")
            rival_pokemon = input(f"{config.rival_name} sent out Eevee!\n")
            your_pokemon = input(f"Go {config.pikachu_name}!\n")
            from battle1 import battle
            battle()
        else:
            nothing = input(f"Choose something to do!\n")
            os.system('clear')

def action_lab3():
    os.system('clear')
    text = input(f"{config.rival_name}: Okay! I'll make my Pokemon fight to toughen it up!")
    text2 = input(f"{config.player_name}! Gramps! Smell ya later!\n")
    while True:
        option_lab3 = input(f"""What do you want to do?
=====================
1. Talk to lab assistant
2. Talk to professor
3. Leave the lab 

""")
        if option_lab3 == "1":
            assistant_text1 = input(f"Assistant: I study Pokemon under the professor \n")
            os.system('clear')
        elif option_lab3 == "2":
            prof_text4 = input(f"Professor: Good job on your first battle!")
            prof_text5 = input(f"I see a future champion in you!\n")
            os.system('clear')
        elif option_lab3 == "3":
            lab_text1 = input(f"You leave the lab. \n")
            from home_town2 import action_home_town2
            action_home_town2()
        else:
            nothing = input(f"Choose something to do!\n")
            os.system('clear')