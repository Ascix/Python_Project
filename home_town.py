import os

def action_home_town():
    os.system('clear')
    print(f"Ah, some fresh air!\n")
    while True:
        option_home_town = input(f"""What do you want to do?
=====================
1. Go home
2. Talk to little girl
3. Talk to man
4. Go to the Lab 

""")
        if option_home_town == "1":
            home = input("You walk home.")
            from living_room import action_downstairs
            action_downstairs()
        elif option_home_town == "2":
            girl_text1 = input("Little girl: I'm raising Pokemon too!")
            girl_text2 = input("When they get strong, they can protect me!\n")
            os.system('clear')
        elif option_home_town == "3":
            man_text1 = input("Man: Technology is incredible!\n")
            os.system('clear')
        elif option_home_town == "4":
            lab_text1 = input("You head into the lab.")
            from lab import action_lab
            action_lab()
        else:
            nothing = input(f"Choose something to do!\n")
            os.system('clear')
