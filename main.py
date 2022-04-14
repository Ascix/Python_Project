from bedroom import action_room
import config

def ask_name():
    while True:
        config.player_name = input("First, please enter your name: ").lower().capitalize()
        if (len(config.player_name) < 1):
            print("Please enter your name!")
        else:
            welcome_text4 = input(f"Right! So your name is {config.player_name}!")
            break

def ask_name2():
    while True:
        config.rival_name = input("Erm, what was his name again?: ").lower().capitalize()
        if (len(config.rival_name) < 1):
            print("Please enter your rival's name!")
        else:
            rival_text1 = input(f"That's right! I remember now!") 
            rival_text2 = input(f"His name is {config.rival_name}!")
            break       

def start():
    input("""  _____      _                                                          
 |  __ \    | |                                                         
 | |__) |__ | | _____ _ __ ___   ___  _ __                              
 |  ___/ _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \                             
 | |  | (_) |   <  __/ | | | | | (_) | | | |                            
 |_|   \___/|_|\_\___|_| |_| |_|\___/|_| |_|                            
  _____       _   _                  __      __           _             
 |  __ \     | | | |                 \ \    / /          (_)            
 | |__) |   _| |_| |__   ___  _ __    \ \  / /__ _ __ ___ _  ___  _ __  
 |  ___/ | | | __| '_ \ / _ \| '_ \    \ \/ / _ \ '__/ __| |/ _ \| '_ \ 
 | |   | |_| | |_| | | | (_) | | | |    \  /  __/ |  \__ \ | (_) | | | |
 |_|    \__, |\__|_| |_|\___/|_| |_|     \/ \___|_|  |___/_|\___/|_| |_|
         __/ |                                                          
        |___/                                                           
press enter to continue""")
    welcome_text1 = input("Professor: Hello there! Welcome to the world of Pokemon!")
    welcome_text2 = input("This world is inhabited by creatures called Pokemon!")
    welcome_text3 = input("For some people, Pokemon are pets. Others use them for fights.")
    ask_name()
    welcome_text4 = input("You've been rivals with my grandson since you were a baby.")
    ask_name2()
    welcome_text5 = input(f"{config.player_name}! Your very own Pokemon legend is about to unfold!")
    welcome_text6 = input("A world of dreams and adventures with Pokemon awaits! Let's go!")
    welcome_text7 = input("")
    action_room()

start()