import os

def action_downstairs():
    os.system('clear')
    print(f"You see your mom on the couch watching TV.\n")
    while True:
        option_living_room = input(f"""What do you want to do?
=====================
1. Go upstairs
2. Watch TV
3. Talk to mom
4. Go outside 

""")
        if option_living_room == "1":
            room = input("You go to your room")
            from bedroom import action_room
            action_room()
        elif option_living_room == "2":
            TV_text1 = input(f"There's a movie on TV.")
            TV_text2 = input(f"It looks like there's a toy cowboy and astronaut arguing with each other.")
            TV_text3 = input(f"I better get going. \n")
            os.system('clear')
        elif option_living_room == "3":
            mom_text1 = input(f"Mom: All boys leave home someday. It said so on TV.")
            mom_text2 = input(f"The professor next door is looking for you. \n")
            os.system('clear')
        elif option_living_room == "4":
            leave = input("You leave the house.")
            from home_town import action_home_town
            action_home_town()
        else:
            nothing = input(f"Choose something to do!\n")
            os.system('clear')

            