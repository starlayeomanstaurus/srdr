import random
import sys

# ===== WELCOME BANNER =====

def print_welcome():
    print(r"""
████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║
   ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
""")
    print("WELCOME TO THE TERMINAL ROAST MACHINE")
    print("Where your disorders get ROASTED and you get empowered (or insulted)!")
    print("-" * 70)

# ===== MAIN MENU =====

def main_menu():
    print("\nMAIN MENU:")
    print("1. Shyannah Mode (Roast Panel)")
    print("2. Robert Mode (Ross Roast + Boss Fight)")
    print("3. Quit")
    return input("Choose your mode (1/2/3): ").strip()

def quit_program():
    print("\nDeadpool: \"Oh look, you're quitting already? Classic. Byeee!\"")
    sys.exit(0)

# ===== DEADPOOL 4TH WALL =====

def deadpool_fourth_wall():
    print("\n🔥 DEADPOOL'S 4TH WALL MENU 🔥")
    while True:
        print("\n1. Roast Me Harder")
        print("2. Meta Advice")
        print("3. Break Script (quit)")
        print("4. Go Back")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            print("\nDeadpool: \"You're literally asking for it. Kinky.\"")
        elif choice == "2":
            print("\nDeadpool: \"You're in a Python script. Free will is an illusion.\"")
        elif choice == "3":
            print("\nDeadpool: \"Alt-F4, motherfucker! Bye!\"")
            sys.exit(0)
        elif choice == "4":
            return
        else:
            print("Deadpool: \"Bro. Pick a real option.\"")

# ===== SHYANNAH MODE =====

shyannah_symptoms = [
    "Anxiety",
    "Depression",
    "Deadpool 4th Wall Menu",
]

shyannah_roasts = {
    "Anxiety": [
        {
            "Dean": "Anxiety's like a demon with bad hygiene. Salt and burn that bitch.",
            "Geralt": "Anxiety. Meditate or kill it with fire. Doesn't matter to me.",
            "Deadpool": "Anxiety thinks it's the main character. Newsflash: It's not.",
            "Tom": "Anxiety is society's leash. Break that motherfucker.",
        },
        {
            "Dean": "Another case of the Creepy Crawlies? Shoot first, question later.",
            "Geralt": "Anxiety is a contract I don't take. Too annoying.",
            "Deadpool": "Fourth wall break! You're anxious just reading this.",
            "Tom": "Anxiety? Brainwashing 101. Unsubscribe.",
        },
    ],
    "Depression": [
        {
            "Dean": "Depression's that demon pretending it's your friend. Exorcise it.",
            "Geralt": "Depression. Heavy. Ugly. Kill-worthy.",
            "Deadpool": "Your sister wrote this roast at 3am. Solidarity.",
            "Tom": "Depression is just you vs you. Your sister's betting on you.",
        },
        {
            "Dean": "Another day of gloom? Shotgun a coffee and get moving.",
            "Geralt": "Depression is a monster that feeds on apathy. Starve it.",
            "Deadpool": "Depression binge-watches sadness. Change the channel.",
            "Tom": "Depression profits off hopelessness. Don't buy it.",
        },
    ],
}

def shyannah_mode():
    print("\n⚔️ Entering Shyannah Mode ⚔️")
    while True:
        print("\nAvailable Symptoms to Roast:")
        for i, symptom in enumerate(shyannah_symptoms, 1):
            print(f"{i}. {symptom}")
        try:
            choice = int(input("\nPick a symptom (number) or 0 to return: ").strip())
        except ValueError:
            print("Deadpool: \"Numbers, please.\"")
            continue
        if choice == 0:
            return
        if choice < 1 or choice > len(shyannah_symptoms):
            print("Deadpool: \"That's not on the list.\"")
            continue
        selected = shyannah_symptoms[choice - 1]
        if selected == "Deadpool 4th Wall Menu":
            deadpool_fourth_wall()
            continue
        roasts = shyannah_roasts.get(selected)
        if not roasts:
            print("Deadpool: \"No roasts written yet.\"")
            continue
        roast_set = random.choice(roasts)
        print("\n🔥 YOUR ROAST PANEL 🔥")
        print(f"Dean: {roast_set['Dean']}")
        print(f"Geralt: {roast_set['Geralt']}")
        print(f"Deadpool: {roast_set['Deadpool']}")
        print(f"Tom MacDonald: {roast_set['Tom']}")
        print("\n⭐ Pep Talk: \"It's your mind. Take the wheel.\"")

# ===== ROBERT MODE =====

robert_symptoms = [
    "Anxiety",
    "Depression",
]

robert_roasts = {
    "Anxiety": [
        "Ross: Anxiety? We were on a BREAK from calm apparently. Talk to your rubber duck.",
        "Ross: Anxiety is like Illinois DMV lines—endless and existential. Pivot already.",
    ],
    "Depression": [
        "Ross: Depression? Cool. My love life says hi. Espresso won't fix it, but try anyway.",
        "Ross: Depression is like coding without semicolons. Messy as hell. Rubber Duck that shit.",
    ],
}

BOSS_ART = r"""
 ____ ROSS BOSS ____
 [ASCII ART]
"""

def trivia_gate():
    print("\nRoss: \"Alright hotshot. Prove you're worthy.\"")
    print("What was the name of Ross's second wife?")
    print("1. Carol")
    print("2. Emily")
    print("3. Susan")
    print("4. Rachel")
    answer = input("Enter choice (1-4): ").strip()
    return answer == "2"


def ross_boss_fight():
    player = 100
    boss = 100
    print("\n⚔️ BOSS FIGHT UNLOCKED! ⚔️")
    print(BOSS_ART)
    while player > 0 and boss > 0:
        print(f"\nYour HP: {player} | Ross's HP: {boss}")
        print("1. Fight")
        print("2. Talk")
        move = input("> ").strip()
        if move == "1":
            dmg = random.randint(15, 30)
            boss -= dmg
            print(f"You roast Ross for {dmg} damage!")
        elif move == "2":
            heal = random.randint(10, 20)
            player += heal
            print(f"You reflect and heal {heal} HP!")
        else:
            print("Ross: \"Not an option. PIVOT!\"")
            continue
        if boss > 0:
            boss_dmg = random.randint(10, 25)
            player -= boss_dmg
            print(f"Ross hits back for {boss_dmg} damage!")
    if player <= 0:
        print("\n💀 Ross: \"Looks like you need more therapy. GAME OVER.\"")
    else:
        print("\n✅ Ross: \"Fine! You win. Therapy is real. Happy now?\"")


def robert_mode():
    print("\n🎩 Entering Robert Mode 🎩")
    roast_count = 0
    while True:
        print("\nAvailable Symptoms to Roast:")
        for i, symptom in enumerate(robert_symptoms, 1):
            print(f"{i}. {symptom}")
        try:
            choice = int(input("\nPick a symptom (number) or 0 to return: ").strip())
        except ValueError:
            print("Ross: \"Numbers, please.\"")
            continue
        if choice == 0:
            return
        if choice < 1 or choice > len(robert_symptoms):
            print("Ross: \"That's not on the list.\"")
            continue
        symptom = robert_symptoms[choice - 1]
        roast_line = random.choice(robert_roasts[symptom])
        print(f"\n🔥 ROSS ROAST 🔥\n{roast_line}")
        roast_count += 1
        if roast_count >= 3:
            print("\nRoss: \"Think you're ready for the boss fight?\"")
            if trivia_gate():
                ross_boss_fight()
            else:
                print("Ross: \"WRONG! Maybe next time.\"")
            roast_count = 0

# ===== MAIN FUNCTION =====

def main():
    print_welcome()
    while True:
        choice = main_menu()
        if choice == "1":
            shyannah_mode()
        elif choice == "2":
            robert_mode()
        elif choice == "3":
            quit_program()
        else:
            print("\nDeadpool: \"Seriously? Pick 1, 2, or 3.\"")


if __name__ == "__main__":
    main()
