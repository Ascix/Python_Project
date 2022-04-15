import os
import config

def action_home_town2():
    os.system('clear')
    print(f"I see mom standing outside the house.\n")
    while True:
        option_home_town = input(f"""What do you want to do?
=====================
1. Talk to mom
2. Talk to little girl
3. Talk to man
4. Go to the Lab
5. Leave town

""")
        if option_home_town == "1":
            mom = input(f"Mom: {config.player_name}, I heard you have a Pokemon now!")
            mom2 = input(f"I guess it's finally time for you leave home.")
            mom3 = input("Please take care of yourself!")
            os.system('clear')
        elif option_home_town == "2":
            girl_text1 = input("Little girl: I'm raising Pokemon too!")
            girl_text2 = input("When they get strong, they can protect me!\n")
            os.system('clear')
        elif option_home_town == "3":
            man_text1 = input("Man: Technology is incredible!\n")
            os.system('clear')
        elif option_home_town == "4":
            lab_text1 = input("You head into the lab.")
            from lab import action_lab4
            action_lab4()
        elif option_home_town == "5":
            journey = input("You leave town.")
            from end import ending
            ending()
        else:
            nothing = input(f"Choose something to do!\n")
            os.system('clear')
