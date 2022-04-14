import os
from living_room import action_downstairs

def action_room():
    os.system('clear')
    print("You arrive in your room.\n")
    while True:
        option_room = input(f"""What do you want to do?
=====================
1. Lay in bed
2. Play games
3. Go downstairs 

""")
        if option_room == "1":
            bed_text = input(f"A nice, comfy bed. I wish I could sleep in, but we gotta get going! \n")
            os.system('clear')
        elif option_room == "2":
            game_text = input(f"Maybe just 1 more level, but we gotta go afterwards! \n")
            os.system('clear')
        elif option_room == "3":
            downstairs_text = input(f"You walk down to the living room. \n")
            action_downstairs()
        else:
            nothing = input(f"Choose something to do!\n")
            os.system('clear')