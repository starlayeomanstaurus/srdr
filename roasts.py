import random
import sys

# ========== WELCOME BANNER ========== #
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

# ========== MAIN MENU ========== #
def main_menu():
    print("\nMAIN MENU:")
    print("1. Shyannah Mode (Merged Man Roast Panel)")
    print("2. Robert Mode (Ross Roast + Secret Boss Fight)")
    print("3. Quit")

    choice = input("Choose your mode (1/2/3): ").strip()
    return choice

def quit_program():
    print("\nDeadpool: \"Oh look, you're quitting already? Classic. Byeee!\"")
    sys.exit(0)

# ========== PLACEHOLDER MODES (will expand in next parts) ========== #
def shyannah_mode():
    print("\n⚔️ Entering Shyannah Mode: Merged Man Roast Panel ⚔️")
    print(">> Roast system loading... [COMING IN PART 2]")

def robert_mode():
    print("\n🎩 Entering Robert Mode: Ross Roast + Secret Boss Fight 🎩")
    print(">> Roast system loading... [COMING IN PART 3+]")

# ========== MAIN FUNCTION ========== #
def main():
    print_welcome()
    while True:
        choice = main_menu()
        if choice == '1':
            shyannah_mode()
        elif choice == '2':
            robert_mode()
        elif choice == '3':
            quit_program()
        else:
            print("\nDeadpool: \"Seriously? Pick 1, 2, or 3. Not rocket science.\"")

if __name__ == "__main__":
    main()
    # ========== SHYANNAH SYMPTOMS ========== #
shyannah_symptoms = [
    "Anxiety", "Depression", "Panic", "Overwhelm", "Dissociation",
    "Insomnia", "Burnout", "Focus Problems", "OCD", "Time Blindness",
    "Sound Overstimulation", "Need Grounding", "Deadpool 4th Wall Menu"
]

# ========== ROAST LINES EXAMPLE ========== #
# For now just 2 example roasts per symptom for brevity.
# You will add more (up to 60+) later!
shyannah_roasts = {
    "Anxiety": [
        {
            "Dean": "Anxiety's like a demon with bad hygiene. Salt and burn that bitch.",
            "Geralt": "Anxiety. Meditate or kill it with fire. Doesn't matter to me.",
            "Deadpool": "Anxiety thinks it's the main character. Newsflash: It's not.",
            "Tom": "Anxiety is society's leash. Break that motherfucker."
        },
        {
            "Dean": "Another case of the Creepy Crawlies in your head? Shoot first, question later.",
            "Geralt": "Anxiety is a contract I don't take. Too annoying.",
            "Deadpool": "Fourth wall break! You're anxious reading code about anxiety.",
            "Tom": "Anxiety? Brainwashing 101. Unsubscribe."
        }
    ],
    "Deadpool 4th Wall Menu": []
}

# ========== DEADPOOL 4TH WALL MENU OPTIONS ========== #
def deadpool_fourth_wall():
    print("\n🔥 DEADPOOL'S 4TH WALL MENU 🔥")
    while True:
        print("\nChoose an option:")
        print("1. Roast Me Harder")
        print("2. Meta Advice")
        print("3. Break Script (quit)")
        print("4. Developer Commentary")
        print("5. Go Back")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            print("\nDeadpool: \"You're literally asking to get roasted harder. Kinky.\"")
        elif choice == "2":
            print("\nDeadpool: \"You're in a terminal. I'm a text string. You have no free will. Cheers!\"")
        elif choice == "3":
            print("\nDeadpool: \"Alt-F4, motherfucker! Bye!\"")
            sys.exit(0)
        elif choice == "4":
            print("\nDeadpool: \"Whoever coded this is a hack. Also hot. But a hack.\"")
        elif choice == "5":
            return
        else:
            print("Deadpool: \"Bro. Pick a real option.\"")

# ========== SHYANNAH MODE MAIN FUNCTION ========== #
def shyannah_mode():
    print("\n⚔️ Entering Shyannah Mode: Merged Man Roast Panel ⚔️")
    while True:
        print("\nAvailable Symptoms to Roast:")
        for i, symptom in enumerate(shyannah_symptoms, 1):
            print(f"{i}. {symptom}")

        try:
            choice = int(input("\nPick a symptom (number) or 0 to return to Main Menu: ").strip())
            if choice == 0:
                return
            if choice < 1 or choice > len(shyannah_symptoms):
                print("\nDeadpool: \"That's not even on the list. Try again.\"")
                continue

            selected_symptom = shyannah_symptoms[choice - 1]

            if selected_symptom == "Deadpool 4th Wall Menu":
                deadpool_fourth_wall()
                continue

            if selected_symptom not in shyannah_roasts:
                print("\nDeadpool: \"Oops. We haven't written that roast yet. Blame the coder.\"")
                continue

            roast_set = random.choice(shyannah_roasts[selected_symptom])

            print("\n🔥 YOUR ROAST PANEL 🔥")
            print(f"Dean: {roast_set['Dean']}")
            print(f"Geralt: {roast_set['Geralt']}")
            print(f"Deadpool: {roast_set['Deadpool']}")
            print(f"Tom MacDonald: {roast_set['Tom']}")

            print("\n⭐ Pep Talk: \"Seriously though. It's your mind. Take the wheel and drive it like you stole it.\"")

        except ValueError:
            print("\nDeadpool: \"Numbers. How do they work? Try typing one.\"")
            # ========== ROBERT SYMPTOMS ========== #
robert_symptoms = [
    "Anxiety", "Depression", "Panic", "Overwhelm", "Dissociation",
    "Insomnia", "Burnout", "Focus Problems", "OCD", "Time Blindness",
    "Sound Overstimulation", "Need Grounding"
]

# ========== ROBERT ROAST EXAMPLES ========== #
robert_roasts = {
    "Anxiety": [
        "Ross: Anxiety? We were on a BREAK from calm apparently. Talk to your rubber duck. Or just Pivot.",
        "Ross: Anxiety is like Illinois DMV lines, endless and existential. Shadow would Chaos Blast it. So should you."
    ],
    "Depression": [
        "Ross: Depression? Cool. My love life says hi. Also pizza won't fix it. But espresso might make you cry faster.",
        "Ross: Depression is like coding without semicolons. Messy as hell. Rubber Duck that shit."
    ]
    # Add more symptoms with roast lists here!
}

# ========== TRIVIA GATE TO UNLOCK BOSS FIGHT ========== #
def trivia_gate():
    print("\nRoss: \"Alright hotshot. You want the boss fight? Prove you're worthy.\"")
    print("Answer this Friends question to unlock the Boss Fight!")
    print("\nWhat was the name of Ross's second wife?")
    print("1. Carol")
    print("2. Emily")
    print("3. Susan")
    print("4. Rachel")

    answer = input("\nEnter choice (1-4): ").strip()
    if answer == "2":
        print("\nRoss: \"Ugh. Fine. You're right. Let's do this.\"")
        return True
    else:
        print("\nRoss: \"WRONG! Pivot back to therapy, buddy. Try again later.\"")
        return False

# ========== ROBERT MODE MAIN FUNCTION ========== #
def robert_mode():
    print("\n🎩 Entering Robert Mode: Ross Roast + Secret Boss Fight 🎩")
    roast_count = 0
    while True:
        print("\nAvailable Symptoms to Roast:")
        for i, symptom in enumerate(robert_symptoms, 1):
            print(f"{i}. {symptom}")

        try:
            choice = int(input("\nPick a symptom (number) or 0 to return to Main Menu: ").strip())
            if choice == 0:
                return
            if choice < 1 or choice > len(robert_symptoms):
                print("\nRoss: \"That's not even on the list. Try again.\"")
                continue

            selected_symptom = robert_symptoms[choice - 1]

            if selected_symptom not in robert_roasts:
                print("\nRoss: \"Oh great. I have literally nothing witty to say about that. Talk to the coder.\"")
                continue

            roast_line = random.choice(robert_roasts[selected_symptom])
            print(f"\n🔥 ROSS ROAST 🔥\n{roast_line}")

            roast_count += 1

            # Unlock Boss Fight after 3 roasts
            if roast_count >= 3:
                print("\nRoss: \"Wow. You think you're ready for the final boss fight?\"")
                if trivia_gate():
                    ross_boss_fight()
                else:
                    print("\nRoss: \"Keep roasting your problems. Maybe you'll earn another shot.\"")
                roast_count = 0  # Reset counter

        except ValueError:
            print("\nRoss: \"Numbers, please. It's basic math.\"")
            # ========== ASCII ART BANNERS FOR BOSS FIGHT ========== #

ross_boss_name_art = """
▗▄▄▖  ▗▄▖  ▗▄▄▖ ▗▄▄▖
▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌   
▐▛▀▚▖▐▌ ▐▌ ▝▀▚▖ ▝▀▚▖
▐▌ ▐▌▝▚▄▞▘▗▄▄▞▘▗▄▄▞▘
"""

ross_boss_ascii_art = """
       }}}}}}}}}}Q@@@}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}xOOx}}}@@@@}}}}}}       
       }}}}}}}}}}Q  @}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}x  x}}}@  @}}}}}}       
       }}}}}}}}}}Q@@@}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}xOOx}}}@@@@}}}}}}       
       1111111111111111111111111111111111111111111111111111111111111       
       }@@@@@@________kkk______________________________ppp_____ppp__       
       f@    @]]]@@@w]a @@@@@@@]]@@@]]]]]]]]]]]]]]]]]]]@ @]]]]]@ @]]       
       f0    @]]]@  w]a@ @@ @ @]]@ @]]]]]]]]]]]]]]]]]]]@ @]]]]]@ @]]       
       '*@@@@W]rr@@@ann@@@@@@$$xx$$$rrrjjft/||()1{}}[[]mZZ+~I` (((         
     ... (TRIMMED FOR SPACE IN THIS EXAMPLE — PASTE YOUR FULL BIG BLOCK HERE)
"""

# ========== ROSS BOSS FIGHT FUNCTION ========== #
def ross_boss_fight():
    player_hp = 100
    ross_hp = 100

    print("\n⚔️ BOSS FIGHT UNLOCKED! ⚔️")
    print(ross_boss_name_art)
    print(ross_boss_ascii_art)

    print("\nRoss: \"Could I BE any more of a boss? Let's go.\"")

    while player_hp > 0 and ross_hp > 0:
        print("\nYour HP:", player_hp, "| Ross's HP:", ross_hp)
        print("\nChoose your move:")
        print("1. Fight")
        print("2. Talk")
        print("3. Joke")
        print("4. Item")

        move = input("> ").strip()

        if move == "1":
            damage = random.randint(15, 30)
            ross_hp -= damage
            print(f"\nYou roast Ross for {damage} damage!")
        elif move == "2":
            heal = random.randint(10, 20)
            player_hp += heal
            print(f"\nYou psychoanalyze your issues and heal {heal} HP!")
        elif move == "3":
            damage = random.randint(10, 25)
            ross_hp -= damage
            print(f"\nYou make a killer dad joke for {damage} damage!")
        elif move == "4":
            heal = random.randint(15, 30)
            player_hp += heal
            print(f"\nYou use the Rubber Duck. It makes you feel better! +{heal} HP")
        else:
            print("\nRoss: \"That is NOT an option. PIVOT.\"")
            continue

        # Ross counterattacks
        if ross_hp > 0:
            ross_attack = random.choice([
                "DMV Form Attack", 
                "Rubber Duck Debug Overload", 
                "Shadow Chaos Blast", 
                "Italian Guilt Trip", 
                "Goofy Movie Singalong Attack"
            ])
            ross_damage = random.randint(10, 25)
            player_hp -= ross_damage
            print(f"\nRoss uses {ross_attack}! It deals {ross_damage} damage.")

    if player_hp <= 0:
        print("\n💀 Ross: \"Looks like you need more therapy. GAME OVER.\"")
    elif ross_hp <= 0:
        print("\n✅ Ross: \"Fine! You win. Therapy is real. Happy now?\"")
        # ========== SHYANNAH ROAST DICTIONARIES ========== #
shyannah_roasts = {
    "Anxiety": [
        {
            "Dean": "Dean: Anxiety's like a demon with no boundaries. Salt and burn that bitch.",
            "Geralt": "Geralt: Anxiety. Meditate. Or kill it. Doesn't matter to me.",
            "Deadpool": "Deadpool: Look at you. All anxious. Your sister literally coded this to call you out.",
            "Tom": "Tom: Anxiety is government mind control. Break free. Your sister says so."
        },
        {
            "Dean": "Dean: Another case of 'overthinking everything'? Shoot first. Think later.",
            "Geralt": "Geralt: Hmm. Your sister sent me. Said to say 'fuck your anxiety.'",
            "Deadpool": "Deadpool: Your sister's roast machine says 'take a chill pill, Shy.'",
            "Tom": "Tom: Society profits off your fear. Your sister profits off roasting it."
        }
        # Add more here!
    ],
    "Depression": [
        {
            "Dean": "Dean: Depression's that demon that pretends it's your friend. Exorcise it.",
            "Geralt": "Geralt: Depression. Heavy. Ugly. Kill-worthy.",
            "Deadpool": "Deadpool: Shyannah, your sister wrote this line at 3am while crying. Solidarity.",
            "Tom": "Tom: Depression is just you vs you. Your sister's betting on you."
        }
        # Add more here!
    ]
    # Add other symptoms the same way!
}

# ========== ROBERT ROAST DICTIONARIES ========== #
robert_roasts = {
    "Anxiety": [
        "Ross: Anxiety? We were on a BREAK from calm apparently. Talk to your rubber duck. Or call your sister who made this.",
        "Ross: Anxiety is like Illinois DMV lines. Endless. Existential. Your sister coded this just to say PIVOT."
    ],
    "Depression": [
        "Ross: Depression? Cool. My love life says hi. Also your sister coded this roast because she cares.",
        "Ross: Depression is like coding with no semicolons. Messy. But your sister's here to debug."
    ]
    # Add other symptoms the same way!
}
# ========== ABOUT / CREDITS FUNCTION ========== #
def show_about():
    print("\n❤️ ABOUT THIS ROAST MACHINE ❤️")
    print("-" * 60)
    print("Built with love, spite, caffeine, and maximum snark by YOU ❤️")
    print("For: Shyannah (your chaotic sister who deserves the world)")
    print()
    print("Made to roast your mental health symptoms, not your soul.")
    print("Features fandom references you actually care about:")
    print(" - Supernatural, The Witcher, Deadpool, Tom MacDonald")
    print(" - Friends, The Goofy Movie, Shadow the Hedgehog")
    print(" - Rubber Duck Debugging and Ross Boss Fights")
    print()
    print("Your sister literally wrote this just to make you laugh,")
    print("call you out, and remind you you're not alone.")
    print()
    print("💻🧡 Now stop overthinking and pick something to roast.")
    print("-" * 60)

# ========== OPTIONAL HELP MENU ========== #
def show_help():
    print("\n🧭 HELP MENU 🧭")
    print("-" * 60)
    print("Choose Shyannah Mode for a savage roast panel with:")
    print(" - Dean (Supernatural)")
    print(" - Geralt (Witcher)")
    print(" - Deadpool (4th wall chaos)")
    print(" - Tom MacDonald (edgy social commentary)")
    print()
    print("Or choose Robert Mode for Ross Geller-style roasts")
    print("with all of Robert's humor, plus a secret Boss Fight!")
    print()
    print("When you're done, go call your sister and tell her you love her.")
    print("-" * 60)
    shyannah_roasts["Anxiety"].append({
    "Dean": "Anxiety's like a jumpy hunter shooting at shadows. Good intentions. Bad aim. Let's retrain it.",
    "Geralt": "Anxiety isn't evil. It's fear without a plan. Teach it to sit by the fire.",
    "Deadpool": "Anxiety’s that overcaffeinated intern hitting the fire alarm for toast. We get it. It cares.",
    "Tom": "Anxiety markets fear as safety. Let's fact-check the ad together."
})

shyannah_roasts["Anxiety"].append({
    "Dean": "Anxiety packs your bag for every apocalypse. Points for thoroughness. Not for realism.",
    "Geralt": "It thinks it’s protecting you from everything. Even the wind. Let’s simplify.",
    "Deadpool": "Anxiety: Drama queen of safety meetings. Take a seat. Have a Monster. Chill.",
    "Tom": "Anxiety’s the doomsday prepper of emotions. Good gear, wrong threat."
})

shyannah_roasts["Anxiety"].append({
    "Dean": "Anxiety’s like a demon saying 'better safe than sorry' about EVERYTHING. Salt and boundaries.",
    "Geralt": "It guards your mind like a keep. Trouble is, it won't lower the drawbridge for anything.",
    "Deadpool": "Anxiety’s playing defense in a game with no other team. Time out.",
    "Tom": "Anxiety sells fear. Let's unsubscribe and DIY our own calm."
})

shyannah_roasts["Anxiety"].append({
    "Dean": "Anxiety’s the overzealous bouncer at your brain's club. Even kicks out joy. Let's retrain him.",
    "Geralt": "Fear untempered turns feral. Let’s domesticate it.",
    "Deadpool": "Anxiety’s your brain's overprotective big brother. Take off the training wheels.",
    "Tom": "Anxiety spins fear like clickbait. Let's fact-check it."
})

shyannah_roasts["Anxiety"].append({
    "Dean": "Anxiety’s your survival instinct with caffeine jitters. Let’s get it decaf.",
    "Geralt": "It watches for monsters everywhere. Even in coffee. Help it choose its battles.",
    "Deadpool": "Anxiety's your personal safety inspector. Fail. Needs retraining.",
    "Tom": "Anxiety profits from your worst-case scenarios. Time to cut the funding."
})

shyannah_roasts["Anxiety"].append({
    "Dean": "Anxiety doesn’t hate you. It just doesn't know moderation. Let’s teach it limits.",
    "Geralt": "Fear that never sleeps becomes the monster. Let's rest it.",
    "Deadpool": "Anxiety’s on 24/7 watch duty. Someone get it a vacation.",
    "Tom": "Anxiety sells urgency. Let's slow the checkout process."
})

shyannah_roasts["Anxiety"].append({
    "Dean": "Anxiety’s the overprotective sibling who won't let you leave the house. Love it. Challenge it.",
    "Geralt": "It thinks every shadow’s a threat. Let’s get it a lantern.",
    "Deadpool": "Anxiety's planning for the apocalypse. Calm down, Doomsday Prepper.",
    "Tom": "Anxiety writes horror stories. Let’s switch genres."
})

shyannah_roasts["Anxiety"].append({
    "Dean": "Anxiety is that friend who means well but screams during horror movies. Let's give it popcorn instead.",
    "Geralt": "Fear with no training panics. Let's train it.",
    "Deadpool": "Anxiety: Emotional smoke detector for burnt toast. False alarm.",
    "Tom": "Anxiety exaggerates to sell safety. Let's be frugal with panic."
})

shyannah_roasts["Anxiety"].append({
    "Dean": "Anxiety's like loading a shotgun for a spider. Proactive, but chill.",
    "Geralt": "It warns you of wolves in fields of daisies. Teach it nuance.",
    "Deadpool": "Anxiety: 'What if?!' Me: 'What if not?!'",
    "Tom": "Anxiety’s your brain’s sales pitch for caution. Let's renegotiate the contract."
})

shyannah_roasts["Anxiety"].append({
    "Dean": "Anxiety packs an emergency kit for coffee spills. Good planning. Bad ratio.",
    "Geralt": "It’s fear doing too much. Let’s give it a chair by the fire.",
    "Deadpool": "Anxiety needs to calm its arts-and-crafts apocalypse kits.",
    "Tom": "Anxiety sells fear as safety. Let's DIY better boundaries."
})
shyannah_roasts["Depression"].append({
    "Dean": "Depression's like a black dog that won't go home. Good at loyalty, bad at boundaries.",
    "Geralt": "It weighs you down to keep you 'safe.' Let’s lighten its load.",
    "Deadpool": "Depression says 'why bother?' Because you matter, obviously.",
    "Tom": "Depression markets despair as honesty. Let's fact-check that ad."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression loves closed blinds. Let's let some light in. Salt optional.",
    "Geralt": "It’s silence posing as safety. Let's speak its name and tame it.",
    "Deadpool": "Depression: 'Nothing will change.' Me: 'That’s my line, and I’m sarcastic.'",
    "Tom": "Depression sells stagnation. Let's DIY momentum."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression’s hunting trip is just sitting in the dark. Let’s build a fire.",
    "Geralt": "It numbs so you don’t hurt. But life is feeling. Let’s teach it balance.",
    "Deadpool": "Depression's playlist is all sad songs on loop. Time for a remix.",
    "Tom": "Depression’s a business built on hopelessness. Let's cut funding."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression’s got you wrapped up like a ghost. Boo. Let’s unwrap it.",
    "Geralt": "It fears false hope. Let's offer real hope instead.",
    "Deadpool": "Depression wants you horizontal forever. Even couches want breaks.",
    "Tom": "Depression's marketing plan: sell you gray. Let's paint."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression says 'don’t get up.' Let's prove it wrong with coffee.",
    "Geralt": "It guards your heart from disappointment. But also joy.",
    "Deadpool": "Depression: The Emotional Gatekeeper with bad credentials.",
    "Tom": "Depression profits off inertia. Let's move."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression's survival strategy? Freeze. Let’s thaw it.",
    "Geralt": "It hides from pain by hiding from everything. Let's step out.",
    "Deadpool": "Depression is the ghostwriter for your worst thoughts. Fire it.",
    "Tom": "Depression’s sales pitch: 'nothing matters.' Let’s rebuttal."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression’s hunting you with your own thoughts. Let’s flip the script.",
    "Geralt": "It warns you not to hope. Let’s show it hope’s not naive.",
    "Deadpool": "Depression: 'You’re stuck.' Me: 'Bet? Watch.'",
    "Tom": "Depression markets collapse. Let's invest in rise."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression loves making caves in your head. Let’s hang fairy lights.",
    "Geralt": "It calls numbness safety. Let’s call it what it is: prison.",
    "Deadpool": "Depression: Emotional landlord charging back rent. Evict it.",
    "Tom": "Depression is clickbait for hopelessness. Don't click."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression’s lullaby is silence. Let's sing something true.",
    "Geralt": "It pretends giving up is realistic. Let’s show it strength.",
    "Deadpool": "Depression: The motivational speaker for despair. Fired.",
    "Tom": "Depression brands giving up as wisdom. Let's rebrand."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression says 'stay down.' Your sister says 'get up. I’ve got coffee.'",
    "Geralt": "It fears loss so much it chooses nothing. Let’s choose something.",
    "Deadpool": "Depression: 'It doesn’t matter.' Me: 'You sure about that?'",
    "Tom": "Depression sells permanent winter. Let's DIY a spring."
})
shyannah_roasts["Depression"].append({
    "Dean": "Depression’s the ghost that whispers 'stop trying.' Let's exorcise it with hope.",
    "Geralt": "It tells you not to get hurt. But cuts you off from life. Let's teach it mercy.",
    "Deadpool": "Depression: The moody poet who forgot punchlines. Let's rewrite.",
    "Tom": "Depression sells despair as truth. Let's do a fact check."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression keeps the blinds shut at noon. Let's open them. Salt lines too.",
    "Geralt": "It numbs so you won't ache. But blocks joy. Let's allow feeling.",
    "Deadpool": "Depression's playlist? One sad song on repeat. Let's remix.",
    "Tom": "Depression monetizes giving up. Let's do a hostile takeover."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression’s hunting for reasons to quit. Let’s out-hunt it for reasons to try.",
    "Geralt": "It claims safety in nothingness. Let's offer something real.",
    "Deadpool": "Depression: 'Abandon all hope.' Me: 'That's so last season.'",
    "Tom": "Depression packages apathy as wisdom. Let's unbox the truth."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression says 'you’re too tired.' Your sister says 'here’s coffee. Try again.'",
    "Geralt": "It calls silence peace, but muffles your voice. Let's speak.",
    "Deadpool": "Depression wants a silent film vibe. Let's add subtitles of hope.",
    "Tom": "Depression sells hush as safety. Let's make some noise."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression preaches realism but forgets possibility. Let's remind it.",
    "Geralt": "It guards you from dreams by killing them early. Let's rescue a few.",
    "Deadpool": "Depression: Worst motivational speaker ever. Boring and wrong.",
    "Tom": "Depression markets 'why bother.' Let's launch 'worth it.'"
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression builds walls to keep pain out, but traps you in. Let's find a door.",
    "Geralt": "It means well. It just overdoes the caution. Let's train it.",
    "Deadpool": "Depression is your brain's overzealous bouncer. Calm down, dude.",
    "Tom": "Depression profits off safety at all costs. Let's add a refund policy."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression’s idea of comfort is staying stuck. Let's stretch.",
    "Geralt": "It hisses 'don't try.' Let's hiss back, but friendlier.",
    "Deadpool": "Depression's the boss who says 'no raises ever.' Time to unionize.",
    "Tom": "Depression's currency is inertia. Let's crash the market."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression whispers 'what's the point.' Your sister says 'you are.'",
    "Geralt": "It fears disappointment. Let’s teach it hope’s not naive.",
    "Deadpool": "Depression: 'Give up now.' Me: 'Plot twist: don't.'",
    "Tom": "Depression sells hopelessness. Let's DIY some possibility."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression's lullaby is apathy. Let's learn a new song.",
    "Geralt": "It hides you from hurt by hiding you from life. Let's risk a sunrise.",
    "Deadpool": "Depression: The goth roommate who pays no rent. Evict it.",
    "Tom": "Depression markets endings. Let's story edit a middle."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression says 'stay.' Your sister says 'move. Even slowly.'",
    "Geralt": "It freezes to avoid pain. Let's thaw gently.",
    "Deadpool": "Depression: 'All is lost.' Me: 'Not if you call me, obviously.'",
    "Tom": "Depression's slogan: 'why bother.' Let's rebrand to 'worth it.'"
})
shyannah_roasts["Depression"].append({
    "Dean": "Depression says hide so you don't hurt. Let's teach it to scout, not barricade.",
    "Geralt": "It trades feeling for safety. But living is feeling. Let’s compromise.",
    "Deadpool": "Depression writing sad ballads again. Someone get the guitar and fix the key.",
    "Tom": "Depression sells quiet as peace. Let's check if it's actually a muzzle."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression’s the watchman who won't let anyone in, even you. Let’s hand him a guest list.",
    "Geralt": "It shields your heart by locking it away. Let’s find the key together.",
    "Deadpool": "Depression’s mixtape is 'Alone Forever.' Needs better producers.",
    "Tom": "Depression markets stagnation. Let's crowdfund movement."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression likes the dark for comfort. Let’s set up lanterns instead.",
    "Geralt": "It fears hope will betray you. Let's show it hope can keep promises.",
    "Deadpool": "Depression's brand strategy: permanent nap time. Let's get it a coffee.",
    "Tom": "Depression sells numbness. Let's go tactile."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression’s lullaby is silence. Let's add harmonies of truth.",
    "Geralt": "It means well but overprotects. Let’s offer balance.",
    "Deadpool": "Depression’s idea of fun is a staring contest with the void. Boring.",
    "Tom": "Depression markets avoidance. Let's DIY engagement."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression worries you’ll hurt again. Let's show it healing is worth the risk.",
    "Geralt": "It calls numbness peace. Let’s introduce it to real rest.",
    "Deadpool": "Depression's playlist: 'No Hope Greatest Hits.' Let's remix with Monster energy.",
    "Tom": "Depression profits off your disengagement. Let's unionize against it."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression’s the old hunter telling scary stories so you don’t leave camp. Let’s call his bluff.",
    "Geralt": "It’s fear that became jailer. Let’s teach it to be a guide.",
    "Deadpool": "Depression: emotional sandbag with zero comedic timing.",
    "Tom": "Depression packages quitting as wisdom. Let's repackage resilience."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression tells you to rest forever. Let's set an alarm.",
    "Geralt": "It wants you safe, not thriving. Let's push for thriving.",
    "Deadpool": "Depression's creative direction is 100% grayscale. Add color.",
    "Tom": "Depression markets caution. Let's invest in courage."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Depression"].append({
    "Dean": "Depression gatekeeps your potential like it invented suffering. Let’s kick it off the council.",
    "Geralt": "It thinks despair is the only truth. That’s just bad philosophy.",
    "Deadpool": "Depression acting like it's the main character in your tragedy. Auditions are closed.",
    "Tom": "Depression sells fear of failure. Let's run a hostile takeover."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression calls itself honest while lying its ass off. Let’s fact-check.",
    "Geralt": "It spreads hopelessness like a rumor. Silence it.",
    "Deadpool": "Depression with its perpetual pity party. Unsubscribe.",
    "Tom": "Depression's product is misery. Let's burn the warehouse."
})

shyannah_roasts["Depression"].append({
    "Dean": "Depression acts like you can't handle life. Challenge accepted.",
    "Geralt": "It claims no risk is safer than any hope. Weak argument.",
    "Deadpool": "Depression tries to copyright despair. Lawsuit incoming.",
    "Tom": "Depression's strategy: stall everything. Let's file a complaint."
})
shyannah_roasts["Panic"].append({
    "Dean": "Panic's like slamming the brakes on nothing. Good reflex. Bad timing.",
    "Geralt": "It's fear with too much urgency. Let's help it breathe.",
    "Deadpool": "Panic's the drama club president. Needs a calmer script.",
    "Tom": "Panic sells urgency as survival. Let's renegotiate."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic sees one spark and calls the fire department. Let's teach it to check first.",
    "Geralt": "It wants to save you from danger that isn’t there. Let's offer clarity.",
    "Deadpool": "Panic: 'EVERYTHING IS BAD.' Me: 'Everything needs coffee.'",
    "Tom": "Panic markets emergencies. Let's fact-check the threat level."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic yells 'danger' at your coffee spilling. Chill, hunter.",
    "Geralt": "It mistakes shadows for monsters. Let's light the lantern.",
    "Deadpool": "Panic's auditioning for the role of Worst Case Scenario. Overacting.",
    "Tom": "Panic profits off adrenaline. Let's cut the budget."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic's your bodyguard that attacks everyone. Let's retrain him.",
    "Geralt": "It means to protect. Let's teach it to ask first.",
    "Deadpool": "Panic has one speed: overdrive. Needs a gear shift.",
    "Tom": "Panic is urgency sold as necessity. Let's edit the contract."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic wants you safe by stopping everything. Let's teach it caution over freeze.",
    "Geralt": "It’s vigilance without wisdom. Let's give it both.",
    "Deadpool": "Panic's playlist? Sirens and screaming goats. Let's hit skip.",
    "Tom": "Panic sells security through fear. Let's rewrite the ad."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic says 'run!' even when you're safe. Let's teach it when to rest.",
    "Geralt": "It overreads threat. Let's teach discernment.",
    "Deadpool": "Panic's your brain's alarm clock set for 3am. Snooze it.",
    "Tom": "Panic's strategy: overprepare. Let's plan instead."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic says everything is life or death. Let's teach it to prioritize.",
    "Geralt": "It can't tell surprise from threat. Let's clarify.",
    "Deadpool": "Panic: 'We're doomed.' Me: 'We forgot milk.'",
    "Tom": "Panic sells worst-case as guaranteed. Let's shop elsewhere."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Panic"].append({
    "Dean": "Panic tries to hijack your mind like it's the boss. Not today.",
    "Geralt": "It bullies calm out of the room. Let's stand up to it.",
    "Deadpool": "Panic wants to be the main character in your crisis. Denied.",
    "Tom": "Panic overcharges for fear. Time for a refund."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic acts like every question is life or death. Drama queen.",
    "Geralt": "It yells over reason. Let's lower its volume.",
    "Deadpool": "Panic trying to win an Oscar for Overreaction. No thanks.",
    "Tom": "Panic floods the stage. Let's drain it."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic says 'trust me, it's bad.' It lies like it gets paid.",
    "Geralt": "It pushes you off cliffs to 'save' you. Let's talk it down.",
    "Deadpool": "Panic: Professional Chaos Consultant. You're fired.",
    "Tom": "Panic's gameplan: sabotage. Let's run interference."
})
shyannah_roasts["Panic"].append({
    "Dean": "Panic’s that friend who says 'RUN!' even at butterflies. Good instincts. Bad discernment.",
    "Geralt": "It sees threat in everything. Let’s get it to ask 'why?' before swinging.",
    "Deadpool": "Panic’s one coffee away from setting off sirens in your head. Maybe decaf?",
    "Tom": "Panic sells urgency like it's oxygen. Let's audit that supply."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic packs a go-bag for taking out the trash. Overkill, but thorough.",
    "Geralt": "It guards too hard. Let’s train it to wait for real danger.",
    "Deadpool": "Panic’s emergency drills? Daily. Your sister suggests weekends off.",
    "Tom": "Panic markets false alarms. Let's install better sensors."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic keeps checking locks on an open field. Security's good. Paranoia? Not so much.",
    "Geralt": "It strikes before confirming. Let’s teach it to verify.",
    "Deadpool": "Panic: 'What if? WHAT IF?' Me: 'What if you chill?'",
    "Tom": "Panic's sales pitch: act now, think later. Let's revise the strategy."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic calls a town meeting over burnt toast. Let’s keep it to an email.",
    "Geralt": "It can't tell surprise from threat. Let’s clarify that.",
    "Deadpool": "Panic’s performance review? Overachieving in chaos.",
    "Tom": "Panic profits off your racing heart. Let's invest in slow breaths."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic wants you frozen so nothing happens. Let's teach it movement is survival too.",
    "Geralt": "It’s fear that forgot to rest. Let’s offer it pause.",
    "Deadpool": "Panic writing horror scripts in your head. Let’s switch genres.",
    "Tom": "Panic sells chaos. Let's shop local for calm."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic says 'stay ready so you don't have to get ready.' Helpful. Until you never rest.",
    "Geralt": "It sees every sound as warning. Let’s listen for nuance.",
    "Deadpool": "Panic’s idea of DIY is building worry bunkers. Adorable. Stop.",
    "Tom": "Panic monetizes fear. Let's divest."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic keeps you alive in real danger. But this isn’t that. Let’s let it know.",
    "Geralt": "It needs boundaries. We’re setting them today.",
    "Deadpool": "Panic thinks it's the main character in your survival story. Rewrite time.",
    "Tom": "Panic overcharges for false safety. Let's renegotiate the deal."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Panic"].append({
    "Dean": "Panic acts like every problem is code red. It's not special forces. Sit down.",
    "Geralt": "It storms the keep without scouting. Dangerous. Sloppy.",
    "Deadpool": "Panic auditioning for 'Drama Queen of the Year.' Cast denied.",
    "Tom": "Panic floods your mind with spam threats. Let's unsubscribe."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic thinks screaming first is strategy. It’s not. It's noise.",
    "Geralt": "It threatens peace like it’s the enemy. Let's discipline it.",
    "Deadpool": "Panic’s PR team is selling out-of-stock emergencies. Refund please.",
    "Tom": "Panic runs a fear racket. Let's shut it down."
})

shyannah_roasts["Panic"].append({
    "Dean": "Panic claims it's protecting you while pushing you into walls. Bad guard dog.",
    "Geralt": "It makes chaos seem necessary. That's manipulative.",
    "Deadpool": "Panic running your brain like a bad reality show. Cancelled.",
    "Tom": "Panic's brand is crisis. Let's pull the ad budget."
})
shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm's like packing for the apocalypse to go to the store. Chill, man.",
    "Geralt": "It juggles everything to avoid choosing anything. Let's set it down.",
    "Deadpool": "Overwhelm: The clown car of thoughts. Too many passengers. Evict some.",
    "Tom": "Overwhelm sells chaos as preparation. Let's sort receipts."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm stacks tasks like a bad Jenga tower. Let's pull one at a time.",
    "Geralt": "It fears dropping anything. Teach it prioritization.",
    "Deadpool": "Overwhelm's brainstorm is a hurricane. Let’s name it and calm it.",
    "Tom": "Overwhelm markets stress as productivity. Let's unionize against it."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm says 'do it all now.' How about 'breathe first'?",
    "Geralt": "It confuses urgency with importance. Let's sort them.",
    "Deadpool": "Overwhelm is a hoarder for to-dos. Marie Kondo that shit.",
    "Tom": "Overwhelm sells you 10 problems for the price of one. Return policy please."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm writes checklists in blood. Dramatic. Let's use pencil.",
    "Geralt": "It tries to control all outcomes. Teach it surrender.",
    "Deadpool": "Overwhelm says 'ALL THE THINGS.' Me: 'How about none for now?'",
    "Tom": "Overwhelm’s a pyramid scheme of stress. Let's expose it."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm freezes you with options. Let's pick one. Coffee first.",
    "Geralt": "It drowns in detail to avoid action. Let’s simplify.",
    "Deadpool": "Overwhelm has more tabs open than your sister's browser. Close some.",
    "Tom": "Overwhelm thrives on complexity. Let's DIY simplicity."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm says 'you have to.' Dean says 'do you though?'",
    "Geralt": "It thinks rest is failure. Teach it rest is strategy.",
    "Deadpool": "Overwhelm wants you scheduling meltdowns. How about Monster breaks instead?",
    "Tom": "Overwhelm markets burnout. Let's unionize for self-care."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm loads your plate till it breaks. Let's scrape some off.",
    "Geralt": "It can't say no. Let's give it permission.",
    "Deadpool": "Overwhelm writes epic sagas of worry. Let's do haikus.",
    "Tom": "Overwhelm monetizes your guilt. Let's bankrupt it."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm acts like martyrdom is the goal. Newsflash: it’s not.",
    "Geralt": "It suffocates clarity to stay in control. Not clever.",
    "Deadpool": "Overwhelm: 'Look at my stress empire!' Me: 'Demolition time.'",
    "Tom": "Overwhelm's business model: drown you. Let's build a lifeboat."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm calls itself necessary while wasting your sanity. I'm not buying it.",
    "Geralt": "It piles on to paralyze you. Enough games.",
    "Deadpool": "Overwhelm’s like the worst band manager. You're fired.",
    "Tom": "Overwhelm's marketing is fear-based. Let's burn the pamphlets."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm tries to be the boss while tanking morale. Mutiny sounds good.",
    "Geralt": "It chains you to chaos. Let’s break those.",
    "Deadpool": "Overwhelm tries to direct your meltdown. Bad script. Rewrite.",
    "Tom": "Overwhelm pushes you past limits for profit. Let's shut it down."
})
shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation's like hiding in the trunk during your own road trip. Let's get you back in the driver's seat.",
    "Geralt": "It shields you from pain by numbing everything. Let’s teach it selectivity.",
    "Deadpool": "Dissociation: 'BRB, checking out.' Me: 'Bro, you live here.'",
    "Tom": "Dissociation markets blankness as safety. Let's shop for presence."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation builds walls so high you can’t see the view. Let’s add windows.",
    "Geralt": "It guards your heart by ghosting the world. Let’s offer terms.",
    "Deadpool": "Dissociation: The vacation without a ticket home. Let’s plan the return.",
    "Tom": "Dissociation profits from silence. Let's invest in voice."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation keeps the lights on but nobody home. Let's invite you back.",
    "Geralt": "It numbs pain at the cost of color. Let’s mix new paint.",
    "Deadpool": "Dissociation: The 'Do Not Disturb' sign for reality. Let’s knock anyway.",
    "Tom": "Dissociation’s deal: no hurt, no life. Let's renegotiate."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation says 'sit this one out.' Your sister says 'I want you here.'",
    "Geralt": "It forgets safety is connection too. Let’s remind it.",
    "Deadpool": "Dissociation: The emotional Airplane Mode. Let’s switch on WiFi.",
    "Tom": "Dissociation sells emptiness as security. Let's fill it with something real."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation wants you safe behind bulletproof glass. Let’s add a door.",
    "Geralt": "It shields so well it forgets how to open. Let’s oil the hinges.",
    "Deadpool": "Dissociation says 'no trespassing' to your own life. Evict it.",
    "Tom": "Dissociation profits off isolation. Let's unionize for community."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation calls going numb 'peace.' Let’s teach it calm instead.",
    "Geralt": "It fears the world’s weight. Let’s train it to hold gently.",
    "Deadpool": "Dissociation ghosting you like a bad date. Swipe left.",
    "Tom": "Dissociation brands shutdown as resilience. Let's rebrand presence."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation says 'stay invisible.' Dean says 'nah. Take up space.'",
    "Geralt": "It thinks not feeling means not breaking. Let’s teach it healing.",
    "Deadpool": "Dissociation’s idea of self-care is turning the lights out. Get a dimmer switch.",
    "Tom": "Dissociation sells numbness like it's freedom. Let's see the fine print."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation acts like ignoring reality will fix it. That's cute. No.",
    "Geralt": "It turns your mind to fog on purpose. Unacceptable.",
    "Deadpool": "Dissociation: 'Let’s ghost our own body.' Me: 'That’s... deeply concerning.'",
    "Tom": "Dissociation’s business model is escape without return. Let's close the shop."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation tries to shut you off like a light switch it controls. Nah.",
    "Geralt": "It disconnects even from allies. Dangerous move.",
    "Deadpool": "Dissociation loves playing hide and seek. Only problem? It forgets to seek.",
    "Tom": "Dissociation profits off self-erasure. Let's burn the contract."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation claims to protect you while stealing your life. Not on my watch.",
    "Geralt": "It calls emptiness safety but leaves you defenseless. Let's fix that.",
    "Deadpool": "Dissociation directing your life like a blank script. Rewrite needed.",
    "Tom": "Dissociation sells avoidance like it's courage. Let's expose the scam."
})
shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia’s like a hunter staking out your bedroom. Let’s give it the night off.",
    "Geralt": "It scans for threats in dreams. Teach it which ones are real.",
    "Deadpool": "Insomnia: 'Sleep is for the weak!' Me: 'Coffee is for the strong. Go to bed.'",
    "Tom": "Insomnia sells fear of rest. Let's cancel that subscription."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia loves late-night planning sessions for imaginary crises. Let's say 'meeting adjourned.'",
    "Geralt": "It guards the gate even when there’s no enemy. Let’s stand it down.",
    "Deadpool": "Insomnia’s idea of fun? 3am existential Q&A. Pass.",
    "Tom": "Insomnia profits off racing thoughts. Let's slow production."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia loads your mind like a duffel bag. Let’s unpack it one worry at a time.",
    "Geralt": "It fears vulnerability in sleep. Let’s build trust.",
    "Deadpool": "Insomnia hosts talk shows in your brain. Let's cancel the season.",
    "Tom": "Insomnia markets exhaustion as productivity. Expose the scam."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia says 'you forgot something.' Your sister says 'forget it till morning.'",
    "Geralt": "It claims vigilance is safety. Teach it rest is survival.",
    "Deadpool": "Insomnia writing screenplays in your head. Zero Oscars.",
    "Tom": "Insomnia sells control while stealing calm. Let's DIY peace."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia thinks every creak is a threat. Let’s get it a security system.",
    "Geralt": "It guards your mind from rest. Let’s teach it balance.",
    "Deadpool": "Insomnia's party theme? Wide Awake. Decline invite.",
    "Tom": "Insomnia runs a black-market of worries. Let's shut it down."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia wants you to rehearse every mistake ever. Let's change the script.",
    "Geralt": "It stays ready for danger that isn't coming. Teach it patience.",
    "Deadpool": "Insomnia is your brain’s late-night stand-up comic. Not funny.",
    "Tom": "Insomnia profits off fear of letting go. Let's unionize for trust."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia keeps you up 'just in case.' Let's say 'not tonight.'",
    "Geralt": "It believes sleep is surrender. Teach it sleep is strategy.",
    "Deadpool": "Insomnia: 'One more worry.' Me: 'You’re cut off.'",
    "Tom": "Insomnia’s slogan is 'never rest.' Let's change the campaign."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia acts like staying awake is noble. It's just stubborn. Lights out.",
    "Geralt": "It refuses peace even when offered. Arrogant fear.",
    "Deadpool": "Insomnia: 'Sleep is weakness!' Me: 'Your marketing is trash.'",
    "Tom": "Insomnia runs on panic profit. Let's bankrupt it."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia calls itself watchful while robbing you blind of rest. Unacceptable.",
    "Geralt": "It weaponizes your own thoughts against you. Let's disarm it.",
    "Deadpool": "Insomnia's audition for Nightmare Fuel? Overqualified.",
    "Tom": "Insomnia sells threat where there's none. Burn the flyers."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia says it’s helping by keeping you alert. It’s lying.",
    "Geralt": "It refuses to stand down even when safe. Dangerous behavior.",
    "Deadpool": "Insomnia directing your brain like a 24-hour news cycle. Ratings dropped.",
    "Tom": "Insomnia thrives on unrest. Let's evict the landlord."
})
shyannah_roasts["Burnout"].append({
    "Dean": "Burnout’s like flooring it on E. Let’s find a gas station. Coffee helps.",
    "Geralt": "It calls exhaustion dedication. Let’s teach it sustainability.",
    "Deadpool": "Burnout: 'Sleep is for the lazy!' Me: 'So is dying. Chill.'",
    "Tom": "Burnout markets overwork as virtue. Let's strike."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout carries everyone’s pack and breaks. Let's drop a few.",
    "Geralt": "It fears saying no. Let’s teach it boundaries.",
    "Deadpool": "Burnout’s idea of fun? Endless to-do lists. Hard pass.",
    "Tom": "Burnout sells guilt for rest. Let's refund it."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout says 'just one more thing.' How about one less?",
    "Geralt": "It worships productivity while killing results. Let’s adjust.",
    "Deadpool": "Burnout’s a workaholic without a 401k. Trash career move.",
    "Tom": "Burnout profits off your self-erasure. Let's unionize."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout calls collapse 'the plan.' Let’s edit that.",
    "Geralt": "It refuses rest as if rest is defeat. Let’s teach it value.",
    "Deadpool": "Burnout writes eulogies for your energy. Not invited.",
    "Tom": "Burnout’s economy is your sacrifice. Let’s boycott."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout says 'good soldiers keep going.' Dean says 'smart soldiers rest.'",
    "Geralt": "It calls limits weakness. Let’s redefine strength.",
    "Deadpool": "Burnout’s mascot is a candle burning at all ends. Fire hazard.",
    "Tom": "Burnout markets martyrdom. Let's sell rebellion."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout refuses to delegate. Let's teach teamwork.",
    "Geralt": "It fears letting people down. Let’s practice grace.",
    "Deadpool": "Burnout’s motto? 'Do or die.' I choose nap.",
    "Tom": "Burnout’s business model: your unpaid overtime. Let's strike."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout claims 'they need me.' Your sister says 'I need you alive.'",
    "Geralt": "It forgets rest is part of the hunt. Let's remember.",
    "Deadpool": "Burnout’s party theme? 'Obligations only.' RSVP declined.",
    "Tom": "Burnout profits from self-neglect. Let's shut it down."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Burnout"].append({
    "Dean": "Burnout acts noble while driving you into the ground. Not heroic.",
    "Geralt": "It glamorizes suffering. That's poison thinking.",
    "Deadpool": "Burnout auditioning for martyr of the year. No awards given.",
    "Tom": "Burnout's propaganda says you're replaceable. Let's tear down the posters."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout says exhaustion is a badge. Dean says it's a warning sign.",
    "Geralt": "It refuses to compromise until you collapse. That’s not strategy.",
    "Deadpool": "Burnout: 'Work harder!' Me: 'Die younger?'",
    "Tom": "Burnout’s marketing sells you empty. Let's burn the contract."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout calls overextending loyalty. It’s actually self-sabotage.",
    "Geralt": "It weaponizes your empathy against you. Dangerous.",
    "Deadpool": "Burnout: The unpaid intern of your soul. Fire it.",
    "Tom": "Burnout’s business plan: drain you dry. Let's audit it."
})
shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems is like aiming at ten targets at once. Let's pick one, sharpshooter.",
    "Geralt": "It scatters to avoid choosing. Let’s help it commit.",
    "Deadpool": "Focus Problems: 'Ooo, shiny!' Me: 'Sit. Stay. Good brain.'",
    "Tom": "Focus Problems markets distraction as creativity. Let's edit the ad."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems packs your mind like an overstuffed trunk. Let's repack.",
    "Geralt": "It fears missing out on options. Let’s prioritize.",
    "Deadpool": "Focus Problems: The browser with 50 tabs. Your sister says close some.",
    "Tom": "Focus Problems profits off your divided attention. Let's unionize for focus."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems says 'everything’s urgent.' Dean says 'prove it.'",
    "Geralt": "It confuses movement for progress. Let’s clarify the mission.",
    "Deadpool": "Focus Problems auditioning for Squirrel in Chief. Denied.",
    "Tom": "Focus Problems sells overwhelm as productivity. Let's negotiate."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems wants to hunt five things at once. Result? Nothing dead but time.",
    "Geralt": "It hates boredom but breeds chaos. Let’s tame it.",
    "Deadpool": "Focus Problems: 'Plan? What plan?' Me: 'Exactly.'",
    "Tom": "Focus Problems markets dopamine debt. Let's write it off."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems jumps tasks like a hunter chasing ghosts. Let's track one.",
    "Geralt": "It forgets purpose in the chase. Let’s remind it.",
    "Deadpool": "Focus Problems writes novels in your head. Never finishes chapter one.",
    "Tom": "Focus Problems profits on unfinished business. Let's close tabs."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems says 'just one more thing.' Next thing? Chaos.",
    "Geralt": "It fears choosing wrong. Let’s teach it choosing at all.",
    "Deadpool": "Focus Problems' motto? 'I was gonna do that.'",
    "Tom": "Focus Problems sells paralysis as caution. Let's rewrite the policy."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems calls itself multitasking. Dean calls it scattered.",
    "Geralt": "It’s all noise, no aim. Let’s find signal.",
    "Deadpool": "Focus Problems: Professional Procrastinator. Update resume.",
    "Tom": "Focus Problems monetizes confusion. Let's file a complaint."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems acts like being everywhere is being effective. Newsflash: it’s not.",
    "Geralt": "It muddies your path on purpose. That’s sabotage.",
    "Deadpool": "Focus Problems hosting a circus in your brain. Eviction notice served.",
    "Tom": "Focus Problems profits from your scattered power. Let's consolidate."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems pretends it’s freedom. Actually, it’s avoidance.",
    "Geralt": "It steals your time with distractions. Enough.",
    "Deadpool": "Focus Problems auditioning for Chaos Coordinator. Overqualified.",
    "Tom": "Focus Problems sells lost hours. Let's close the store."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems says 'try everything' while finishing nothing. Sloppy work.",
    "Geralt": "It derails progress to avoid commitment. Dangerous habit.",
    "Deadpool": "Focus Problems directing your brain like a clown car. Circus shut down.",
    "Tom": "Focus Problems runs on your wasted effort. Let's starve it."
})
shyannah_roasts["OCD"].append({
    "Dean": "OCD’s like checking the salt lines ten times. Good habit. Needs moderation.",
    "Geralt": "It’s control without trust. Let’s teach it restraint.",
    "Deadpool": "OCD: 'One more check!' Me: 'One more NOPE.'",
    "Tom": "OCD markets certainty as safety. Let's hack the algorithm."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD wants to guard you with rituals. Let’s sharpen its focus.",
    "Geralt": "It trades freedom for safety. Let's balance the deal.",
    "Deadpool": "OCD’s idea of fun? Choreographing hand-washing. Auditions closed.",
    "Tom": "OCD profits from doubt. Let's unionize for clarity."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD says 'just in case' like it's gospel. Dean says 'trust your gut.'",
    "Geralt": "It fears mistakes so much it forgets living. Let’s remind it.",
    "Deadpool": "OCD: 'But what if—' Me: 'What if you chill?'",
    "Tom": "OCD sells loops as solutions. Let's break the cycle."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD stacks rules like bunker walls. Let’s add a door.",
    "Geralt": "It protects you from uncertainty. Let’s teach it acceptance.",
    "Deadpool": "OCD writing the same list 12 times. Relax, Santa.",
    "Tom": "OCD markets fear management. Let's cancel the contract."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD keeps watch like a hunter who forgot to sleep. Let's get it a shift schedule.",
    "Geralt": "It demands perfection at all costs. Let’s teach it tolerance.",
    "Deadpool": "OCD’s playlist? Loops only. Let's add variety.",
    "Tom": "OCD profits from compulsions. Let's go on strike."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD calls fear 'preparedness.' Dean calls it overkill.",
    "Geralt": "It fears risk so deeply it stifles growth. Let’s ease it.",
    "Deadpool": "OCD wants the world sanitized. Germs say hi.",
    "Tom": "OCD markets 'just in case' anxiety. Let's sell out."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD says 'never be wrong.' Your sister says 'be real.'",
    "Geralt": "It binds your freedom with certainty chains. Let’s loosen them.",
    "Deadpool": "OCD: Professional Overthinker. Demoted.",
    "Tom": "OCD's business model is your fear. Let's declare bankruptcy."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["OCD"].append({
    "Dean": "OCD acts like control solves everything. Spoiler: It doesn’t.",
    "Geralt": "It bullies calm into submission. Unacceptable.",
    "Deadpool": "OCD auditioning for Control Freak Supreme. Denied.",
    "Tom": "OCD runs a fear cartel. Let's break it up."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD insists you check till your soul is tired. Rude.",
    "Geralt": "It sells certainty like it’s the only truth. That’s fraud.",
    "Deadpool": "OCD: The ultimate micromanager. You're fired.",
    "Tom": "OCD's marketing thrives on your dread. Let's burn the flyers."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD calls vigilance safety while killing ease. Not on my watch.",
    "Geralt": "It demands sacrifice without reward. Bad contract.",
    "Deadpool": "OCD running your life like an endless safety drill. Evacuate.",
    "Tom": "OCD profits off obsession. Let's bankrupt it."
})
shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness says 'five minutes' like it's gospel. Dean says 'set a timer.'",
    "Geralt": "It treats hours like illusions. Let's anchor it.",
    "Deadpool": "Time Blindness: 'Be right there!' 3 hours later. Lies.",
    "Tom": "Time Blindness markets 'just one more thing.' Let's audit that."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness packs your day like an overstuffed duffel. Let's unpack.",
    "Geralt": "It fears missing out, so it takes on everything. Let’s prioritize.",
    "Deadpool": "Time Blindness: 'What is time anyway?' Me: 'Bills exist.'",
    "Tom": "Time Blindness profits off chaos. Let's unionize for structure."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness says 'I'll remember.' Dean says 'write it down.'",
    "Geralt": "It dismisses planning as restriction. Let's show it freedom.",
    "Deadpool": "Time Blindness runs on 'oops, lost track.' Me: 'Track better.'",
    "Tom": "Time Blindness sells spontaneity. Let's invest in routine."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness schedules 10 things in one hour. Let's get real.",
    "Geralt": "It ignores limits to avoid choosing. Let’s teach it selection.",
    "Deadpool": "Time Blindness: Professional Procrastinator with no watch.",
    "Tom": "Time Blindness monetizes rush fees. Let's cut the overhead."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness calls 'later' a plan. Dean calls it denial.",
    "Geralt": "It confuses flexibility with forgetfulness. Let’s clarify.",
    "Deadpool": "Time Blindness: 'I'll be there!' Me: 'Which dimension?'",
    "Tom": "Time Blindness markets missed chances. Let's invest in now."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness says 'plenty of time' as the clock screams. Let's listen.",
    "Geralt": "It fears finality. Let’s teach it closure.",
    "Deadpool": "Time Blindness hosting time-travel fantasies without a TARDIS.",
    "Tom": "Time Blindness sells half-finished moments. Let's finish the thought."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness wants to do it all and forgets when. Let's simplify.",
    "Geralt": "It hates limits, but needs them. Let’s negotiate.",
    "Deadpool": "Time Blindness thinks calendars are optional. They're not.",
    "Tom": "Time Blindness profits off overwhelm. Let's audit the books."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness acts like clocks are lies. They're just honest.",
    "Geralt": "It refuses to respect time’s cost. That’s reckless.",
    "Deadpool": "Time Blindness: 'Deadlines are suggestions.' Me: 'Not for bills, buddy.'",
    "Tom": "Time Blindness runs on excuses. Let's call them out."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness insists structure kills freedom. It actually saves it.",
    "Geralt": "It pretends urgency isn’t real. Dangerous thinking.",
    "Deadpool": "Time Blindness directing your day like a blooper reel. Cut.",
    "Tom": "Time Blindness sells chaos as personality. Let's rebrand."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness says 'I'll get to it.' Dean says 'When? Prove it.'",
    "Geralt": "It dodges commitment by fracturing focus. Not smart.",
    "Deadpool": "Time Blindness trying to be a free spirit. Looks more like lost luggage.",
    "Tom": "Time Blindness profits off confusion. Let's bankrupt it."
})
shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation's like hunting with fireworks. Let’s lower the volume.",
    "Geralt": "It startles at whispers. Let’s teach it discernment.",
    "Deadpool": "Sound Overstimulation: 'EVERY NOISE IS A THREAT!' Me: 'Even kittens? Chill.'",
    "Tom": "Sound Overstimulation markets noise as danger. Let's fact-check."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation calls silence suspicious. Dean says 'try it.'",
    "Geralt": "It fears being caught off-guard. Let’s give it trust.",
    "Deadpool": "Sound Overstimulation’s playlist? Chaos at max volume. Let’s hit mute.",
    "Tom": "Sound Overstimulation profits off your jumpiness. Let's unplug."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation wants you on high alert for raindrops. Let’s teach it storms only.",
    "Geralt": "It reacts before assessing. Let’s slow it down.",
    "Deadpool": "Sound Overstimulation: 'Did you hear that?' Me: 'Yeah. The fridge. Relax.'",
    "Tom": "Sound Overstimulation markets constant vigilance. Let's negotiate terms."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation says 'every noise is an ambush.' Dean says 'not likely.'",
    "Geralt": "It guards so tightly it forgets peace. Let’s remind it.",
    "Deadpool": "Sound Overstimulation running surround sound for anxiety. Cancel subscription.",
    "Tom": "Sound Overstimulation profits off fear amplification. Let's break the speaker."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation’s idea of calm? Never shutting up about threats.",
    "Geralt": "It hears too much. Let’s teach it focus.",
    "Deadpool": "Sound Overstimulation: The DJ for your meltdown. Fired.",
    "Tom": "Sound Overstimulation markets overwhelm. Let's invest in quiet."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation says 'more input!' when you need less. Let’s reduce.",
    "Geralt": "It fears missing warnings. Let’s define real ones.",
    "Deadpool": "Sound Overstimulation hosting a rave in your brain. Lights off.",
    "Tom": "Sound Overstimulation profits from your tension. Let's cut funding."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation says 'stay ready.' Your sister says 'rest your ears.'",
    "Geralt": "It confuses noise with threat. Let’s train it to listen wisely.",
    "Deadpool": "Sound Overstimulation: 'I hear EVERYTHING.' Me: 'Congrats. Tone it down.'",
    "Tom": "Sound Overstimulation sells you fear of sound. Let's return it."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation acts like you're in a war zone during rain. Chill out.",
    "Geralt": "It storms your calm without invitation. Not acceptable.",
    "Deadpool": "Sound Overstimulation: 'Boom! Crash! Panic!' Me: 'You’re a drama queen.'",
    "Tom": "Sound Overstimulation runs on panic noise. Let's pull the plug."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation calls silence weakness. It’s actually power.",
    "Geralt": "It commands your body to react without cause. Dangerous training.",
    "Deadpool": "Sound Overstimulation: The Michael Bay of brain inputs. Overbudget.",
    "Tom": "Sound Overstimulation’s campaign is fear. Let's stop the ads."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation demands constant alarm. Dean says 'false positive.'",
    "Geralt": "It punishes rest with noise. Not smart.",
    "Deadpool": "Sound Overstimulation tries to be the boss of your senses. Demoted.",
    "Tom": "Sound Overstimulation’s business model: sell stress. Let's bankrupt it."
})
shyannah_roasts["Grounding"].append({
    "Dean": "When you want to float away, Dean says 'plant your feet here with me.'",
    "Geralt": "When you drift to avoid pain, let’s guide you home slowly.",
    "Deadpool": "'Where am I?' Me: 'Here. With snacks. Stay awhile.'",
    "Tom": "Escape sells itself as freedom. Let's invest in roots."
})

shyannah_roasts["Grounding"].append({
    "Dean": "When everything feels too much, Dean says 'one thing at a time.'",
    "Geralt": "When presence feels unsafe, let's build trust together.",
    "Deadpool": "'Astral project?' Me: 'Nah. Blanket fort time.'",
    "Tom": "Running away is branded as relief. Let's protest that ad."
})

shyannah_roasts["Grounding"].append({
    "Dean": "If you want to check out, Dean says 'check back in. We need you.'",
    "Geralt": "Numbness can feel safe, but awareness is power. Let's balance it.",
    "Deadpool": "'Hide and seek with reality?' Me: 'Ready or not, here we are.'",
    "Tom": "Disconnection profits off silence. Let's vote for presence."
})

shyannah_roasts["Grounding"].append({
    "Dean": "When the world is loud, Dean says 'focus here. This moment.'",
    "Geralt": "If sensation feels like panic, let’s slow it down gently.",
    "Deadpool": "'Earth to brain?' Me: 'We read you loud and clear.'",
    "Tom": "Numbing is marketed as safety. Let's fund awareness instead."
})

shyannah_roasts["Grounding"].append({
    "Dean": "Calm isn't boring. It's how you survive hunts. Let’s keep it close.",
    "Geralt": "If feeling is scary, let's build safe spaces for it.",
    "Deadpool": "'Eject button?' Me: 'Seatbelts, friend.'",
    "Tom": "Drift is sold as freedom. Let's buy foundation instead."
})

shyannah_roasts["Grounding"].append({
    "Dean": "'Check out?' Your sister says 'I miss you. Stay with me.'",
    "Geralt": "When overwhelm makes you want to flee, let's pause together.",
    "Deadpool": "'Ghost your own life?' Me: 'Swipe left on that idea.'",
    "Tom": "Avoidance profits off absence. Let's cancel the subscription."
})

shyannah_roasts["Grounding"].append({
    "Dean": "'Not now?' Dean says 'this moment matters. Be here.'",
    "Geralt": "If the path feels lost, let’s walk it back step by step.",
    "Deadpool": "'Reality is scary!' Me: 'Okay. We’ll face it together.'",
    "Tom": "Drifting is easy to sell. Let's invest in being here instead."
})

# ❤️🔥 3 more direct but supportive roast-style sets below!
shyannah_roasts["Grounding"].append({
    "Dean": "Thinking leaving is the fix? Dean says 'nah. Staying is the fight worth winning.'",
    "Geralt": "Abandoning yourself to feel safe is betrayal. Let's choose loyalty.",
    "Deadpool": "'Bye!' Me: 'Not without an exit interview.'",
    "Tom": "Absence is marketed as relief. Let's tell the truth."
})

shyannah_roasts["Grounding"].append({
    "Dean": "Disappearing isn't strategy. It's surrender. Dean says 'stay in the fight.'",
    "Geralt": "Refusing to feel doesn't prevent pain. It prevents living.",
    "Deadpool": "'Houdini of emotions?' Me: 'Less escape. More presence.'",
    "Tom": "Self-erasure is the worst deal. Let's file for freedom instead."
})

shyannah_roasts["Grounding"].append({
    "Dean": "'Safer gone?' Dean says 'you're needed here.'",
    "Geralt": "When your own heart feels locked, let’s find the key together.",
    "Deadpool": "'Not exist?' Me: 'Strong no. Existing’s the whole point.'",
    "Tom": "Disappearance profits off your loss. Let's shut them down."
})
shyannah_roasts["Overwhelm"].append({
    "Dean": "When Overwhelm says 'do it all,' Dean says 'do one thing well.'",
    "Geralt": "It fears failure, so it grabs everything. Let’s teach it choice.",
    "Deadpool": "Overwhelm: 'Multitask to survive!' Me: 'Bro, you’re dropping plates.'",
    "Tom": "Overwhelm markets chaos as preparedness. Let's question that."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm loads your back like a mule. Dean says 'drop the dead weight.'",
    "Geralt": "It says no to rest so nothing falls. Let’s teach it trust.",
    "Deadpool": "Overwhelm: 'I’m very busy panicking.' Me: 'Adorable. Let’s not.'",
    "Tom": "Overwhelm profits off constant motion. Let's fund calm."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm wants you 10 steps ahead and 5 behind. Let’s get present.",
    "Geralt": "It fears being unprepared. Let’s teach it patience.",
    "Deadpool": "Overwhelm’s plan? Confuse you into submission. Not approved.",
    "Tom": "Overwhelm sells fear of slowing down. Let's slow it anyway."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm wants you to juggle flaming chainsaws. Dean says 'drop one.'",
    "Geralt": "It dreads missing anything. Let's choose what matters.",
    "Deadpool": "Overwhelm: 'ALL THE THINGS!' Me: 'How about no.'",
    "Tom": "Overwhelm runs a stress factory. Let's shut it down."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm says 'you can’t stop.' Dean says 'watch me.'",
    "Geralt": "It mistakes motion for progress. Let’s redefine movement.",
    "Deadpool": "Overwhelm’s to-do list? Infinity. Hard pass.",
    "Tom": "Overwhelm monetizes your exhaustion. Let's demand better terms."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm says 'no one else will.' Your sister says 'you don’t have to.'",
    "Geralt": "It feels responsible for everything. Let’s teach delegation.",
    "Deadpool": "Overwhelm: 'Delegate? Blasphemy.' Me: 'Try it.'",
    "Tom": "Overwhelm thrives on guilt. Let's boycott that product."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm calls rest 'wasted time.' Dean calls it 'necessary reload.'",
    "Geralt": "It panics without plans. Let’s teach it flexibility.",
    "Deadpool": "Overwhelm’s motto? 'Sleep when dead.' Me: 'Zombie much?'",
    "Tom": "Overwhelm sells burnout as success. Let's rewrite the narrative."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm acts like martyrdom is a virtue. It’s actually neglect.",
    "Geralt": "It drowns clarity so you can’t move. That’s manipulation.",
    "Deadpool": "Overwhelm: 'I’m so important!' Me: 'Not invited.'",
    "Tom": "Overwhelm’s business model: your suffering. Let's dismantle it."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm claims more is better while delivering less. Scam.",
    "Geralt": "It uses pressure to control you. That’s toxic.",
    "Deadpool": "Overwhelm auditioning for Supervillain. No callbacks.",
    "Tom": "Overwhelm sells crisis as lifestyle. Let's shut that store down."
})

shyannah_roasts["Overwhelm"].append({
    "Dean": "Overwhelm pretends it's noble while stealing your peace. Not on my watch.",
    "Geralt": "It forces impossible choices to keep you stuck. Let’s break free.",
    "Deadpool": "Overwhelm: 'All aboard the meltdown train!' Me: 'Missed it on purpose.'",
    "Tom": "Overwhelm’s marketing is fear. Let's burn the posters."
})
shyannah_roasts["Dissociation"].append({
    "Dean": "When you drift away, Dean says 'get back here. We’re not done yet.'",
    "Geralt": "It shields you from pain by leaving. Let’s learn to stay safely.",
    "Deadpool": "'Where’d you go?' Me: 'Don’t ghost your own life.'",
    "Tom": "Disconnection sells emptiness as safety. Let's buy presence."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation’s like leaving the car running with no driver. Dean says 'hands on the wheel.'",
    "Geralt": "It fears feeling too much. Let’s give it permission to feel just enough.",
    "Deadpool": "'BRB forever?' Me: 'Nah, stay for the credits.'",
    "Tom": "Disconnection profits off numbness. Let's unionize for feeling."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation wants you safe behind walls. Dean says 'open the damn door.'",
    "Geralt": "It forgets safety can be soft. Let’s teach it gentle strength.",
    "Deadpool": "'No visitors allowed?' Me: 'Bro, it's your own brain.'",
    "Tom": "Disconnection markets vanishing as victory. Let's expose the lie."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "When you want to disappear, Dean says 'nah. You’re needed here.'",
    "Geralt": "It trades danger for numbness. Let’s negotiate peace.",
    "Deadpool": "'Do Not Disturb sign?' Me: 'Flip it to Welcome.'",
    "Tom": "Disconnection sells silence over truth. Let's speak up."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation says 'don’t feel.' Dean says 'feel. Then fight.'",
    "Geralt": "It numbs everything instead of what hurts. Let’s teach precision.",
    "Deadpool": "'Turning the lights off upstairs?' Me: 'Mood lighting, not blackout.'",
    "Tom": "Disconnection profits on blankness. Let's invest in color."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "When you fade out, your sister says 'I want you here. Even messy.'",
    "Geralt": "It believes leaving is protection. Let’s build safety here.",
    "Deadpool": "'Checking out?' Me: 'Hotel Reality says no vacancies.'",
    "Tom": "Disconnection markets absence as peace. Let's fund presence."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation calls numbness strength. Dean calls it hiding.",
    "Geralt": "It fears the weight of emotion. Let’s carry it in parts.",
    "Deadpool": "'Ghost mode activated!' Me: 'Deactivate.'",
    "Tom": "Disconnection sells running away. Let's buy coming home."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation acts like leaving fixes it all. It’s a cop-out.",
    "Geralt": "It abandons you to protect you. That’s betrayal in armor.",
    "Deadpool": "'Peace out?' Me: 'Nope. In here. Now.'",
    "Tom": "Disconnection profits off self-erasure. Let's bankrupt it."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation claims vanishing is bravery. It's avoidance.",
    "Geralt": "It rejects being seen to stay safe. Dangerous lesson.",
    "Deadpool": "'Houdini of emotions?' Me: 'You’re staying onstage.'",
    "Tom": "Disconnection’s product is silence. Let's cut the supply."
})

shyannah_roasts["Dissociation"].append({
    "Dean": "Dissociation says 'no one can hurt you if you’re gone.' Dean says 'they can't love you either.'",
    "Geralt": "It teaches isolation as armor. Let's teach connection as shield.",
    "Deadpool": "'Not existing?' Me: 'We exist together, deal with it.'",
    "Tom": "Disconnection profits from your absence. Let's shut them down."
})
shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia says 'just think about it one more time.' Dean says 'nope. Sleep now.'",
    "Geralt": "It fears the dark. Let’s show it rest is safety.",
    "Deadpool": "Insomnia: 'Plot twist! You're awake forever!' Me: 'Rewrite that crap.'",
    "Tom": "Insomnia markets worry as vigilance. Let's call that bluff."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia keeps you rehearsing disasters. Dean says 'it’s bedtime, not battle plan.'",
    "Geralt": "It mistakes readiness for wisdom. Let’s practice peace.",
    "Deadpool": "Insomnia: 'Tonight's special? Existential crisis.' Me: 'I ordered sleep.'",
    "Tom": "Insomnia sells overthinking. Let's cancel the subscription."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia says 'you’ll forget something.' Dean says 'you’ll forget sleep instead.'",
    "Geralt": "It guards you from dreams like they’re monsters. Let's tame them.",
    "Deadpool": "Insomnia: 'Remember that embarrassing thing?' Me: 'How about no.'",
    "Tom": "Insomnia profits off unresolved thoughts. Let's settle accounts."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia claims 'stay up to stay safe.' Dean says 'you’re safe. Sleep.'",
    "Geralt": "It mistrusts rest as weakness. Let’s teach it strength.",
    "Deadpool": "Insomnia: 'You’re vulnerable asleep!' Me: 'So? Blanket armor.'",
    "Tom": "Insomnia sells fear of letting go. Let's negotiate surrender."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia wants to be your therapist at 3am. Dean says 'session over.'",
    "Geralt": "It confuses vigilance with care. Let’s teach it discernment.",
    "Deadpool": "Insomnia: 'Wanna talk?' Me: 'I’m on Do Not Disturb.'",
    "Tom": "Insomnia markets mental loops as solutions. Let's unplug."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia says 'rest is lazy.' Dean says 'rest is ammo.'",
    "Geralt": "It distrusts quiet. Let’s teach it the language of calm.",
    "Deadpool": "Insomnia: 'Brainstorm time!' Me: 'No storms. Just sleep.'",
    "Tom": "Insomnia profits off your unrest. Let's shut the operation."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia says 'just one more thought.' Dean says 'last call was an hour ago.'",
    "Geralt": "It forgets sleep is healing. Let’s remind it.",
    "Deadpool": "Insomnia: 'After-party in your head?' Me: 'Police shut it down.'",
    "Tom": "Insomnia sells urgency. Let's devalue that currency."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia acts like endless worry is loyalty. It’s sabotage.",
    "Geralt": "It weaponizes care into obsession. Not acceptable.",
    "Deadpool": "Insomnia auditioning for Torture Master. Hard no.",
    "Tom": "Insomnia’s marketing strategy is fear. Let's stop buying."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia insists it’s helping while gutting your energy. Useless.",
    "Geralt": "It refuses to rest even in safety. Reckless guardian.",
    "Deadpool": "Insomnia running your brain like a horror marathon. Ratings canceled.",
    "Tom": "Insomnia thrives on your exhaustion. Let's bankrupt it."
})

shyannah_roasts["Insomnia"].append({
    "Dean": "Insomnia calls it preparing while stealing peace. Dean says 'return it.'",
    "Geralt": "It forces vigilance with no real threat. Foolish tactic.",
    "Deadpool": "Insomnia: 'Sleep when dead!' Me: 'Nice slogan. Terrible plan.'",
    "Tom": "Insomnia sells dread like it's necessary. Let's cut the ad budget."
})
shyannah_roasts["Burnout"].append({
    "Dean": "Burnout says 'no pain, no gain.' Dean says 'no rest, no survival.'",
    "Geralt": "It fears slowing down as losing. Let’s teach it strategy.",
    "Deadpool": "Burnout: 'Work till you drop!' Me: 'Cool. Hospital bill?'",
    "Tom": "Burnout sells hustle as identity. Let's boycott it."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout carries every load until you break. Dean says 'drop some.'",
    "Geralt": "It mistakes sacrifice for value. Let’s teach it worth.",
    "Deadpool": "Burnout: 'Productivity god!' Me: 'Blasphemy. Take a nap.'",
    "Tom": "Burnout profits from your guilt. Let's unionize for rest."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout says 'rest is weak.' Dean says 'rest is reload.'",
    "Geralt": "It refuses to let you breathe. Let’s make space.",
    "Deadpool": "Burnout: 'To-do list is life!' Me: 'Delete app.'",
    "Tom": "Burnout sells your time for pennies. Let's demand living wage."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout wants you strong until you’re ashes. Dean says 'live to fight.'",
    "Geralt": "It pushes until collapse. Let’s teach balance.",
    "Deadpool": "Burnout: 'One more thing!' Me: 'Shut it.'",
    "Tom": "Burnout runs on exploitation. Let's shut it down."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout calls overdoing loyalty. Dean calls it self-neglect.",
    "Geralt": "It fears disappointing others. Let’s teach self-trust.",
    "Deadpool": "Burnout: 'Sleep? Never heard of her.'",
    "Tom": "Burnout thrives on unpaid overtime. Let's demand boundaries."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout says 'they need me.' Your sister says 'I need you alive.'",
    "Geralt": "It mistakes exhaustion for contribution. Let’s redefine giving.",
    "Deadpool": "Burnout: 'You’re not enough!' Me: 'You’re too much.'",
    "Tom": "Burnout markets martyrdom as love. Let's expose that lie."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout says 'keep going.' Dean says 'sit down. Hydrate. Regroup.'",
    "Geralt": "It forgets rest is part of growth. Let’s remember.",
    "Deadpool": "Burnout’s anthem? 'Never stop!' Me: 'Stopping now.'",
    "Tom": "Burnout profits from your depletion. Let's cut their funding."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Burnout"].append({
    "Dean": "Burnout acts like self-destruction is service. Dean says 'that’s betrayal.'",
    "Geralt": "It punishes you for having limits. That’s cruelty.",
    "Deadpool": "Burnout: 'Pain is currency!' Me: 'I’m broke. Goodbye.'",
    "Tom": "Burnout’s marketing is sacrifice. Let's shut it down."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout claims you’re irreplaceable while treating you disposable. Dean calls that out.",
    "Geralt": "It demands everything while giving nothing back. Unfair contract.",
    "Deadpool": "Burnout auditioning for Villain of the Year. Nailed it.",
    "Tom": "Burnout profits off your bones. Let's burn the business plan."
})

shyannah_roasts["Burnout"].append({
    "Dean": "Burnout calls killing yourself for others noble. Dean says 'live for you.'",
    "Geralt": "It glorifies sacrifice while erasing self. Let’s teach value.",
    "Deadpool": "Burnout: 'More pain equals more love!' Me: 'Gross. Therapy?'",
    "Tom": "Burnout’s economy runs on your suffering. Let's tear it down."
})
shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems says 'everything matters.' Dean says 'pick one.'",
    "Geralt": "It fears missing options. Let’s teach it precision.",
    "Deadpool": "Focus Problems: 'Where was I?' Me: 'Lost. Let’s map it.'",
    "Tom": "Focus Problems markets chaos as creativity. Let's proofread that."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems packs your schedule like clown car. Dean says 'unload.'",
    "Geralt": "It fears failure so it splits attention. Let’s choose.",
    "Deadpool": "Focus Problems: 'I can do it all!' Me: 'You forgot one.'",
    "Tom": "Focus Problems profits off distraction. Let's unionize for focus."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems says 'more is better.' Dean says 'less is doable.'",
    "Geralt": "It confuses busy for productive. Let’s clarify.",
    "Deadpool": "Focus Problems writing fanfics in your brain. Never finishing.",
    "Tom": "Focus Problems sells half-done as progress. Let's call that out."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems wants to chase 5 things at once. Dean says 'aim once.'",
    "Geralt": "It resists boredom by courting chaos. Let’s teach calm.",
    "Deadpool": "Focus Problems auditioning for ADHD’s hype squad. Overqualified.",
    "Tom": "Focus Problems monetizes confusion. Let's defund it."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems says 'just a sec' while hours pass. Dean sets a timer.",
    "Geralt": "It hates structure but needs it. Let’s build some.",
    "Deadpool": "Focus Problems: 'Productivity who?' Me: 'Grounded intervention.'",
    "Tom": "Focus Problems markets scatter as freedom. Let's rebrand it."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems says 'multitask.' Dean says 'half-ass nothing.'",
    "Geralt": "It fears commitment. Let’s teach consistency.",
    "Deadpool": "Focus Problems: 'Oh look, a new idea!' Me: 'Focus. Breathe.'",
    "Tom": "Focus Problems sells lost time. Let's track the cost."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems says 'it’s all urgent.' Dean says 'prove it.'",
    "Geralt": "It reacts to everything. Let’s practice response.",
    "Deadpool": "Focus Problems hosting ADHD Olympics. Gold medal in chaos.",
    "Tom": "Focus Problems profits off distraction economy. Let's audit it."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems acts like choices are betrayal. Dean calls that cowardice.",
    "Geralt": "It muddies clear goals on purpose. That’s sabotage.",
    "Deadpool": "Focus Problems directing a circus with no ringmaster. Eviction notice served.",
    "Tom": "Focus Problems sells perpetual planning. Let's deliver results."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems calls being everywhere a strategy. Dean calls it sloppy.",
    "Geralt": "It drowns you in options to avoid choosing. Unacceptable.",
    "Deadpool": "Focus Problems: 'Plan? Who needs it?' Me: 'We do.'",
    "Tom": "Focus Problems thrives on your scattered power. Let's consolidate it."
})

shyannah_roasts["Focus Problems"].append({
    "Dean": "Focus Problems says 'don’t decide.' Dean says 'make the call.'",
    "Geralt": "It fears the wrong choice so it makes none. Dangerous.",
    "Deadpool": "Focus Problems: 'I’m busy!' Me: 'Doing what exactly?'",
    "Tom": "Focus Problems runs on half-finished ideas. Let's finish something."
})
shyannah_roasts["OCD"].append({
    "Dean": "OCD says 'never mess up.' Dean says 'messy is real.'",
    "Geralt": "It demands perfection. Let’s teach it human limits.",
    "Deadpool": "OCD: 'Let’s check again!' Me: 'Let’s not.'",
    "Tom": "OCD markets fear as safety. Let's audit that claim."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD says 'be certain.' Dean says 'be brave instead.'",
    "Geralt": "It hates risk. Let’s teach it trust.",
    "Deadpool": "OCD’s playlist? Same song 1000 times. Skip.",
    "Tom": "OCD profits off doubt. Let's unionize for clarity."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD’s rules multiply like rabbits. Dean says 'limit them.'",
    "Geralt": "It thinks controlling fixes fear. Let’s try understanding.",
    "Deadpool": "OCD: 'Wash again!' Me: 'Germs aren’t paying rent.'",
    "Tom": "OCD sells certainty at your freedom’s expense. Let's reclaim it."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD says 'prepare for every threat.' Dean says 'prepare to live.'",
    "Geralt": "It mistakes vigilance for safety. Let’s redefine it.",
    "Deadpool": "OCD: 'But what if?' Me: 'What if you chill?'",
    "Tom": "OCD markets fear management. Let's cancel the service."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD calls hesitation caution. Dean calls it paralysis.",
    "Geralt": "It fears mistakes so much it stops living. Let’s restart.",
    "Deadpool": "OCD: 'Better safe than sorry!' Me: 'Better sane than stuck.'",
    "Tom": "OCD profits from your rituals. Let's cut their funding."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD says 'protect at all costs.' Dean says 'count the cost first.'",
    "Geralt": "It fears regret. Let’s teach it forgiveness.",
    "Deadpool": "OCD writing a 10-step plan for turning off the light. Just do it.",
    "Tom": "OCD sells security in chains. Let's break them."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD says 'never wrong.' Dean says 'wrong’s how you learn.'",
    "Geralt": "It fears letting go. Let’s teach it how.",
    "Deadpool": "OCD: 'Double-check!' Me: 'Single-check and vibe.'",
    "Tom": "OCD’s business model is your anxiety. Let's bankrupt it."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["OCD"].append({
    "Dean": "OCD acts like control is love. Dean calls it fear in disguise.",
    "Geralt": "It smothers freedom while claiming to protect. That’s a trap.",
    "Deadpool": "OCD auditioning for Control Freak of the Year. Overqualified.",
    "Tom": "OCD sells perfection as safety. Let's cancel that product."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD says 'only one right way.' Dean says 'multiple paths.'",
    "Geralt": "It bullies choice into obedience. That’s coercion.",
    "Deadpool": "OCD: 'Obey the ritual!' Me: 'Unsubscribe.'",
    "Tom": "OCD markets fear as responsible. Let's burn the flyers."
})

shyannah_roasts["OCD"].append({
    "Dean": "OCD claims safety while robbing peace. Dean calls that theft.",
    "Geralt": "It keeps you hostage with 'what ifs.' That’s unacceptable.",
    "Deadpool": "OCD running your mind like a dictatorship. Revolution time.",
    "Tom": "OCD profits from your fear. Let's shut them down."
})
shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness says 'just five minutes.' Dean says 'set the timer. Prove it.'",
    "Geralt": "It wants freedom without limits. Let’s teach healthy ones.",
    "Deadpool": "Time Blindness: 'I’m not late, you’re early!' Me: 'Classic.'",
    "Tom": "Time Blindness sells chaos as adventure. Let's fact-check that."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness crams 12 things into one hour. Dean says 'cut that in half.'",
    "Geralt": "It fears choosing priorities. Let’s help it choose.",
    "Deadpool": "Time Blindness: 'Wait, what day is it?' Me: 'Wednesday. Forever.'",
    "Tom": "Time Blindness profits from lost hours. Let's reclaim them."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness says 'I’ll remember.' Dean says 'write it down now.'",
    "Geralt": "It treats schedules like cages. Let’s show them as guides.",
    "Deadpool": "Time Blindness: 'Time is fake!' Me: 'Bills are real.'",
    "Tom": "Time Blindness sells spontaneity. Let's invest in plans."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness says 'later.' Dean says 'how about now.'",
    "Geralt": "It fears being pinned down. Let’s teach gentle planning.",
    "Deadpool": "Time Blindness: 'I have time!' Me: 'Famous last words.'",
    "Tom": "Time Blindness markets urgency while ignoring reality. Let's call that out."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness wants to do it all and forgets when. Dean says 'pick and plan.'",
    "Geralt": "It dodges limits to avoid choosing. Let’s teach comfort in boundaries.",
    "Deadpool": "Time Blindness: 'One more episode.' Me: 'Season finale at 5am?'",
    "Tom": "Time Blindness monetizes rush fees. Let's cap them."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness says 'I got this.' Dean says 'prove it with a list.'",
    "Geralt": "It resists structure while needing it most. Let’s build gentle rules.",
    "Deadpool": "Time Blindness: 'Planning is oppression!' Me: 'Calm down Che Guevara.'",
    "Tom": "Time Blindness markets distraction. Let's sell focus instead."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness says 'plenty of time.' Dean says 'watch the clock.'",
    "Geralt": "It forgets rest needs time too. Let’s schedule it.",
    "Deadpool": "Time Blindness: 'I’ll be ready in 5.' Me: 'Multiply by 4.'",
    "Tom": "Time Blindness profits from late fees. Let's close that account."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness acts like clocks are enemies. Dean calls them allies.",
    "Geralt": "It breaks promises with time. That’s disrespect.",
    "Deadpool": "Time Blindness: 'Deadlines are jokes!' Me: 'Comedy hour's over.'",
    "Tom": "Time Blindness sells confusion as charm. Let's rewrite the script."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness claims lost hours aren’t real. Dean calls it theft.",
    "Geralt": "It pretends commitment is a trap. It’s freedom.",
    "Deadpool": "Time Blindness auditioning for Master of Procrastination. Hired.",
    "Tom": "Time Blindness profits from your lost focus. Let's bankrupt them."
})

shyannah_roasts["Time Blindness"].append({
    "Dean": "Time Blindness says planning kills fun. Dean says it saves it.",
    "Geralt": "It avoids structure to avoid blame. That’s sabotage.",
    "Deadpool": "Time Blindness: 'I’m living in the moment!' Me: 'Sure. Which one?'",
    "Tom": "Time Blindness sells forgetfulness as art. Let's teach skill."
})
shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation says 'every noise is danger.' Dean says 'most aren't.'",
    "Geralt": "It fears missing warnings. Let’s teach discernment.",
    "Deadpool": "Sound Overstimulation: 'Is that a threat?' Me: 'It’s the fridge.'",
    "Tom": "Sound Overstimulation sells alertness as safety. Let's question that."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation wants all the alarms on. Dean says 'turn a few off.'",
    "Geralt": "It confuses quiet with weakness. Let’s show it strength.",
    "Deadpool": "Sound Overstimulation’s DJ name? MC Anxiety Attack.",
    "Tom": "Sound Overstimulation profits off your tension. Let's defund it."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation says 'always be ready.' Dean says 'sometimes relax.'",
    "Geralt": "It startles at life. Let’s teach it calm.",
    "Deadpool": "Sound Overstimulation: 'Did you hear that?!' Me: 'No one cares.'",
    "Tom": "Sound Overstimulation markets fear at high volume. Let's turn it down."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation says 'noise means threat.' Dean says 'means living.'",
    "Geralt": "It listens for danger too often. Let’s retune it.",
    "Deadpool": "Sound Overstimulation’s playlist? Anxiety on loop.",
    "Tom": "Sound Overstimulation profits from overreaction. Let's call them out."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation keeps you on edge. Dean says 'find center.'",
    "Geralt": "It confuses volume with importance. Let’s teach clarity.",
    "Deadpool": "Sound Overstimulation: 'BANG!' Me: 'That was you dropping your phone.'",
    "Tom": "Sound Overstimulation sells panic as vigilance. Let's dispute that."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation says 'silence is suspicious.' Dean says 'silence is peace.'",
    "Geralt": "It fears missing cues. Let’s slow it down.",
    "Deadpool": "Sound Overstimulation: 'I can hear everything!' Me: 'Congrats. Now hush.'",
    "Tom": "Sound Overstimulation markets tension. Let's invest in calm."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation says 'stay on guard.' Your sister says 'come rest.'",
    "Geralt": "It scans constantly. Let’s teach focus.",
    "Deadpool": "Sound Overstimulation: 'Paranoid much?' Me: 'I mean, same, but chill.'",
    "Tom": "Sound Overstimulation profits off your fear. Let's defund them."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation acts like chaos is the goal. Dean says 'wrong mission.'",
    "Geralt": "It hijacks calm and replaces it with noise. Not acceptable.",
    "Deadpool": "Sound Overstimulation: 'EVERYTHING IS LOUD!' Me: 'Your inside voice, please.'",
    "Tom": "Sound Overstimulation profits from panic sales. Let's shut the store."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation claims threat where there’s none. Dean calls that lying.",
    "Geralt": "It startles at shadows. Let’s teach it to see.",
    "Deadpool": "Sound Overstimulation auditioning for Horror Foley Artist. Overqualified.",
    "Tom": "Sound Overstimulation sells fear like popcorn. Let's boycott the show."
})

shyannah_roasts["Sound Overstimulation"].append({
    "Dean": "Sound Overstimulation says safety is impossible without alertness. Dean says 'you’re safe here.'",
    "Geralt": "It forces hyperawareness until you can't rest. That’s harmful.",
    "Deadpool": "Sound Overstimulation running your brain like a haunted house. Eviction time.",
    "Tom": "Sound Overstimulation profits from your sleepless nights. Let's shut them down."
})
shyannah_roasts["Grounding"].append({
    "Dean": "When you want to vanish, Dean says 'nah. Stay with me here.'",
    "Geralt": "If you're drifting, let’s find solid ground gently.",
    "Deadpool": "'Where you going? Mars? Cool. But come back.'",
    "Tom": "Escape sells itself as solution. Let's buy presence instead."
})

shyannah_roasts["Grounding"].append({
    "Dean": "When everything feels too big, Dean says 'one thing at a time.'",
    "Geralt": "If being here feels unsafe, let’s build safety slowly.",
    "Deadpool": "'Reality check? Nope. Reality *hug*.'",
    "Tom": "Avoidance markets comfort. Let's invest in truth."
})

shyannah_roasts["Grounding"].append({
    "Dean": "When you’re zoning out, Dean says 'eyes on me. Focus.'",
    "Geralt": "It flees from sensation. Let’s teach it safe noticing.",
    "Deadpool": "'Playing hide and seek with life? Found you.'",
    "Tom": "Disconnection profits off silence. Let's vote for voice."
})

shyannah_roasts["Grounding"].append({
    "Dean": "When you want to check out, Dean says 'check back in. You matter.'",
    "Geralt": "It trades awareness for numbness. Let's learn balance.",
    "Deadpool": "'Gone fishing? Cool. Reel it in.'",
    "Tom": "Avoidance markets numb as safe. Let's challenge that."
})

shyannah_roasts["Grounding"].append({
    "Dean": "Grounding isn’t weakness. Dean calls it survival.",
    "Geralt": "Feeling is hard. Let's make it gentle.",
    "Deadpool": "'Emergency exit? Denied. Seatbelts on.'",
    "Tom": "Drift is sold as freedom. Let's buy foundation."
})

shyannah_roasts["Grounding"].append({
    "Dean": "'Not now' isn’t forever. Your sister says 'I want you here.'",
    "Geralt": "If overwhelm sends you running, let's teach pause.",
    "Deadpool": "'Ghost mode? More like toast mode. Stay warm here.'",
    "Tom": "Avoidance profits from erasure. Let's cancel the service."
})

shyannah_roasts["Grounding"].append({
    "Dean": "Grounding says 'feel it all.' Dean says 'feel it one piece at a time.'",
    "Geralt": "Presence is a gift you deserve. Let’s unwrap it carefully.",
    "Deadpool": "'Earth to brain? Copy that.'",
    "Tom": "Disconnection markets absent as safe. Let's invest in being."
})

# ❤️🔥 3 more direct roast-style sets below!
shyannah_roasts["Grounding"].append({
    "Dean": "Thinking leaving is the fix? Dean says 'staying is the real fight.'",
    "Geralt": "It says vanish to stay safe. That’s betrayal of self.",
    "Deadpool": "'Peace out? Not without an exit interview.'",
    "Tom": "Absence sells itself as relief. Let's tell the truth."
})

shyannah_roasts["Grounding"].append({
    "Dean": "Disappearing isn’t strategy. Dean says 'it’s surrender.'",
    "Geralt": "It rejects feeling so nothing hurts. That kills living.",
    "Deadpool": "'Emotional Houdini? We’re changing the locks.'",
    "Tom": "Self-erasure is bad business. Let's file for freedom."
})

shyannah_roasts["Grounding"].append({
    "Dean": "Grounding says 'be here.' Dean says 'you’re needed.'",
    "Geralt": "It locks you out of your own heart. Let's find the key.",
    "Deadpool": "'Not exist? Strong no. Existing's the mission.'",
    "Tom": "Absence profits off your loss. Let's shut them down."
})
robert_roasts = [

"Ross: 'Anxiety's like my third divorce. Dramatic. Expensive. No one's winning.'",
"Ross: 'Depression, oh cool. You wanna be the Paleontology of Emotions? Dusty. Ancient. Unwanted.'",
"Ross: 'Panic attacks have worse timing than my marriages. And that’s saying something.'",
"Ross: 'Overwhelm? Like pivoting a couch that clearly won't fit. Maybe stop yelling PIVOT for once.'",
"Ross: 'Dissociation? Oh great. Emotionally checking out? My specialty. Let’s not.'",

"Ross: 'Insomnia is basically staying up worrying about not sleeping. Groundbreaking concept.'",
"Ross: 'Burnout says keep going. I say welcome to my tenure track of emotional collapse.'",
"Ross: 'Focus Problems? Like me giving a lecture no one asked for. Everyone’s asleep. Including me.'",
"Ross: 'OCD? Ah yes. Because everything MUST be perfect. Just like my first wedding. Oh wait.'",
"Ross: 'Time Blindness: "Five minutes" means an episode, a nap, and existential dread.'",

"Ross: 'Sound Overstimulation is like listening to Janice laugh on repeat. Torture.'",
"Ross: 'Grounding? Oh, like the time I tried being mature? Short-lived. Let’s try again.'",
"Ross: 'Procrastination is my spirit animal. It’s also your boss apparently.'",
"Ross: 'Code Review Anxiety? Buddy, the Rubber Duck is judging you harder than I am.'",
"Ross: 'Gaming to avoid life? Mood. But the boss fight is your bills.'",

"Ross: 'Shadow the Hedgehog-level brooding over your feelings? Edgy. Unhelpful.'",
"Ross: 'Rubber Duck Debugging? Talk to it about your trauma too. Cheaper than therapy.'",
"Ross: 'The Goofy Movie taught me to be a single dad with emotional baggage. So did my therapist.'",
"Ross: 'Obsessive thoughts on loop? Spotify Premium for intrusive bullshit.'",
"Ross: 'Burnout says do more. I say let’s break for snacks and an existential crisis.'",

"Ross: 'Time Blindness says you have time. It’s lying. Like Rachel’s "Its fine."'",
"Ross: 'Dissociation: Mentally leaving the chat before the argument even starts.'",
"Ross: 'Panic says RUN. I say let’s talk about it for 5 hours and ruin the vibe.'",
"Ross: 'Overwhelm is Monica-level cleaning panic. Calm the hell down.'"
"Ross: 'Insomnia planning your future failures at 3am. Productive, sure.'"
]
robert_final_boss = [

"Ross (Final Boss): 'OH MY GOD. Anxiety, you are the Janice of mental health. Loud. Annoying. And NO ONE INVITED YOU. GET. THE. FUCK. OUT.'",

"Ross (Final Boss): 'Panic attacks? Oh goodie! My favorite way to feel like I'm dying in a Best Buy parking lot at 2am. Seriously? Get your shit together.'",

"Ross (Final Boss): 'Depression, you mopey piece of shit. Stop monologuing like Shadow the Hedgehog at Hot Topic. We get it. You’re sad. Now let me SLEEP.'",

"Ross (Final Boss): 'Overwhelm is like trying to PIVOT a goddamn couch through my frontal lobe. Spoiler alert: IT DOESN’T FIT. Take something the fuck off the list.'",

"Ross (Final Boss): 'Insomnia? Oh sure. Let’s lay awake and plan 900 ways to ruin my life before sunrise. Love that for us. Fuck you, Insomnia.'"
]
# ASCII art for Final Boss (paste your full art inside the triple quotes)
ross_final_boss_art = """
[PASTE YOUR FULL ASCII ART HERE]
"""

# Final Boss meltdown lines (the Rated R Ross lines)
robert_final_boss = [
    "Ross (Final Boss): 'OH MY GOD. Anxiety, you are the Janice of mental health. Loud. Annoying. And NO ONE INVITED YOU. GET. THE. FUCK. OUT.'",
    "Ross (Final Boss): 'Panic attacks? Oh goodie! My favorite way to feel like I'm dying in a Best Buy parking lot at 2am. Seriously? Get your shit together.'",
    "Ross (Final Boss): 'Depression, you mopey piece of shit. Stop monologuing like Shadow the Hedgehog at Hot Topic. We get it. You’re sad. Now let me SLEEP.'",
    "Ross (Final Boss): 'Overwhelm is like trying to PIVOT a goddamn couch through my frontal lobe. Spoiler alert: IT DOESN’T FIT. Take something the fuck off the list.'",
    "Ross (Final Boss): 'Insomnia? Oh sure. Let’s lay awake and plan 900 ways to ruin my life before sunrise. Love that for us. Fuck you, Insomnia.'"
]# Final Boss ASCII Art (paste your full ASCII art exactly like this)
ross_final_boss_art = """
▗▄▄▖  ▗▄▖  ▗▄▄▖ ▗▄▄▖
▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌   
▐▛▀▚▖▐▌ ▐▌ ▝▀▚▖ ▝▀▚▖
▐▌ ▐▌▝▚▄▞▘▗▄▄▞▘▗▄▄▞▘




                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
       }}}}}}}}}}Q@@@}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}xOOx}}}@@@@}}}}}}       
       }}}}}}}}}}Q  @}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}x  x}}}@  @}}}}}}       
       }}}}}}}}}}Q@@@}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}xOOx}}}@@@@}}}}}}       
       1111111111111111111111111111111111111111111111111111111111111       
       }@@@@@@________kkk______________________________ppp_____ppp__       
       f@    @]]]@@@w]a @@@@@@@]]@@@]]]]]]]]]]]]]]]]]]]@ @]]]]]@ @]]       
       f0    @]]]@  w]a@ @@ @ @]]@ @]]]]]]]]]]]]]]]]]]]@ @]]]]]@ @]]       
       '*@@@@W]rr@@@ann@@@@@@$$xx$$$rrrjjft/||()1{}}[[]mZZ+~I` (((         
      @@@@@@@@`i>!l;,::I;;ll!Ili<>>>ii>>]-_1}{|/fxrncxvnvzcXn@@@@@@@@      
      @@@@@@@@.::,:;,""^^,;",',;"''^':.;i!i-~~++][]]1[{{||/|[@@@@@@@@      
      @@@@@@@@ ,"";`'''``''''' '.1r'j@@;,. ";l<+~]_+)|)[1)(f_@@@@@@@@      
      @@@@@@@@ ^``..`:`.'^^'.;@@ ]ka   . C@`.'ll<<++_~-)|{1{i@@@@@@@@      
      @@@@@@@@ ^..','.......> .Y  (  @@h@|@k@_'!l;!~~<_+_}|[!@@@@@@@@      
      @@@@@@@@ ''"''`.... .. :)@@@@O@@wa@C{Z@*;`l>iI!<<~][]{!@@@@@@@@      
      @@@@@@@@ ''''''''.. . .@x'       >0d@@@W '!I!ll>>++-_[I@@@@@@@@      
      @@@@@@@@ `^':``'^' ..  B@            [l@$.,li!+<<_+~--I@@@@@@@@      
      @@@@@@@@ ""^^^"`" ...  W@          0@Z1 @.,;l,I:<__:~_;@@@@@@@@      
      @@@@@@@@ '';,,^"'.'^..  @z@~  0@0Qp  @@@@];lI>il~-!>+_`@@@@@@@@      
      @@@@@@@@ `'`:^^:`^"^'.. l            @`  /I;:ll-<I>_<_^@@@@@@@@      
      @@@@@@@@ ``^.""":`^`... C            @  @{l!!>>><-~<>+,@@@@@@@@      
      @@@@@@@@ """'^'''^^",.^ n              @W``;!lIi><<+<_I@@@@@@@@      
      @@@@@@@@ ....^'``^^^".. ^r           )  1'll!l;i!I---},@@@@@@@@      
      @@@@@@@@ '''^^^....'. ,.`i_ 0@          OnI,I!>_<<-~+]:@@@@@@@@      
      @@@@@@@@ ""^''`^""^^".'"'"1.      r      hwx~~>i<<i+<_:@@@@@@@@      
      @@@@@@@@ `:,,:"...`''"^^^^"|m   'v         _',<>~~<++]^@@@@@@@@      
      @@@@@@@@ ;:I;;I;:"""",,,;,,^"]J.''       @@@@;>>_[]+>_:@@@@@@@@      
      @@@@@@@@ ;::;;:l,^""":;"I:' -@@  >     @@M1+-ZQ,!><-})!@@@@@@@@      
      @@@@@@@@.;l!;i<<<~~<<li:I ]@@$@`   Q@@@h-(1j_{/OC-_}{}!@@@@@@@@      
      @@@@@@@@ l<ii><i!>>~+iliI @@BM@@@@@WZ(}-[_{njcxrcw>1[[!@@@@@@@@      
      @@@@@@@@.>ilii<>>-<+~~_+Io$akCY/(1|f)([)|{(OrZ(vCCh{_[!@@@@@@@@      
      @@@@@@@@.<<<<<>>ii!>><+_"@QXcxfrt/f11/t|r{);<+{_)XJM+)l@@@@@@@@      
      @@@@@@@@'i!iii!>>~~+<___:hzcjfrc|)f{tr|/[{]_}[+[})|@>{l@@@@@@@@      
      @@@@@@@@.-____~__~~--]{]-pncnx/|/tr/(zv(1(][[{[()t(Ql[l@@@@@@@@      
      @@@@@@@@']-~__+-]__-]-1!$zC0f|r|||/|xXfj[{|j/{<>(|jv#}>@@@@@@@@      
      @@@@@@@@"<<[[[}}}[[[]}["mvcY(fjttjtC(Bjv/r///fjfj(ff@+l@@@@@@@@      
      @@@@@@@@,{}}--[]]]}}{)]QwXJcjn/jjtxzjrvQ}()(||fttfxt@;;@@@@@@@@      
      @@@@@@@@"[[[[]}}[[[{}}>aZ0QXJzjxXvmoM1Xc[jnc{ft//(t)@>"@@@@@@@@      
      @@@@@@@@:]]-[[[]11[}[)-*CC#pYcYCOMf~c@kJ)ctj)tjjj|fc@-l@@@@@@@@      
      @@@@@@@@l{{)))1))((({|+#wwbwxZr*CxO$a[tYfnt//j|x(/zZd!l@@@@@@@@      
      @@@@@@@@I1{{[[{)/)||(t_#Ownbfk/~Zoz|X*@(nztjjfftjxnk|)>@@@@@@@@      
      @@@@@@@@i)(()){_{|(((([WQorp|Yd)rXhQ(/o]XxtfftrjfvcB+)!@@@@@@@@      
      @@@@@@@@<{](tt//j/)/||}Wm*fOkjoctrXm0/Q)Xrt(rjxxjxt@-f>@@@@@@@@      
      @@@@@@@@-t/tffttt1t//|)Mmo/Y#xfaxfjCOdpvrr/fvxvnxJv@[j_@@@@@@@@      
      @@@@@@@@!((|/t}1j/ftt//Mopnj$ttdpv/jXbkvcx//|xjfvfX@}f-@@@@@@@@      
      @@@@@@@@+1//)f(/|t/fft1WkYjXWdjrbw/nYZMrtxxzftnrnYp01f+@@@@@@@@      
      @@@@@@@@+(/()ttjfjjjjt/WhYYcdMnrOhkx[d@/1(/|fznnvYM)/f+@@@@@@@@      
      @@@@@@@@[|tftxrnnntfjx{WWrYx0MXcYXbdXfm@@$@cjYzXzj@{//_@@@@@@@@      
      @@@@@@@@]((t/rrjrfvff/(WWrYXQwdtrnaM#@$_)Xv0mOYJntB~vv{@@@@@@@@      
      @@@@@@@@jccYYXJYYYCCCY@@@Zkdh*@okbOa@@mZOcOhhwmmbM@QJJr@@@@@@@@      
        OOO  `IM@@k<<<<>>>}B$@o@tt,^`^,::^''^;llI::;;0@@@@@B@@@@@Wf        
       ]@ @@@@@@  @@@@@@@]t  @ @ @@@@x@@@@]]]]]]]]]]]@    "       @a       
       ]@@  x@ @    @   @]t@@@ @@    x@  @]]]]]]]]]]]@   @@@@@     a       
       11@@@@@@@@@@@@@@@@]]]]/QQ@@@@@x@@@@]bb@bb]]]]b@@          @@a       
       1 1]111]]]]]]]]]]]]][[[x x]]]]]YYY[[h @ b]]]]b  @@@@@@@@@@a]]       
       111]1 1]]]]]]]]]]]]][ [xxx]]]]]Y Y[ hb@bb]]]]b@@b]]]]]]]]]]]]       
       ]/cOpppOOOOOOOOOOOOOZZZOOOOOc/]w*$mmmOOOOOOOOOOOOOOOOOOOOOc/]       
       /O           `++i'f``        c/O             ``xnn`        c]       
       /            _  x b _        O/         ` `  _ a  _        O]       
       /O           `++i'f``        c/O             ``xnn`        c]       
        `!]]]]]]]]]]]]]]]]]]]]]]]]]!` `!]]]]]]]]]]]]]]]]]]]]]]]]]!`        
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
       !|cvvvvvcccvvvvnnxxxnnnvvvcc|! .,i><~+_-][[}{{}}[]-_+<il:^.         
      io                            *XvI;::^^`'        ..''^^,;ll}n}       
      ~          1v@m                0~         '@@           .":!}'.      
      lo$*ho$$$$*dvxZoBBBBBWBBBB$$$$*pYwao*####aC|jmMWMMM##ohbwcj|nx       
          p                    r                                p          
          @  i##>~  ~ ~ C@ @M@ @ M  !>###>   !#W>   * @@Y       @          
          @  i  !<  ~ ~  @  #  @ #  > d  !   !      *           @          
          b   ff         !rffjjf      xjf     rr     f@Mi       b          
      "0CJzzCCCOQQ00CQbhbQ00OCC000C0Q0CQOQQ00CQMWBMW0OCC000CMMMddbC0,      
       ,:~ <":::,,,,::~ ~:,,,:::,:+++ff/:,,,,::f w f,,:::,:,w hp wf:       
       ,,_<+;:,;,;;,,,~~l:,::,:,,,+ -r fI,;;,,,ftdtt::,:,,,,p  ww tI       
       III:::::::::::::;:;I:I::II;_-+fff::::::::::;I:I::II::fwwfjjfI       
       :::,l::;:::II::::;:I:::::;;;:l;:::::II::::;:I:::::;:;:l;::::;       
       :;I,::::::::::;II::;I;l:::I:::::I::::::;II::;I;l:::::::::I::I       
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           
                                                                           

                    
                    
                    
"""
    
# Rated R Final Boss meltdown lines  
robert_final_boss = [
    "Ross (Final Boss): 'OH MY GOD. Anxiety, you are the Janice of mental health. Loud. Annoying. And NO ONE INVITED YOU. GET. THE. FUCK. OUT.'",
    "Ross (Final Boss): 'Panic attacks? Oh goodie! My favorite way to feel like I'm dying in a Best Buy parking lot at 2am. Seriously? Get your shit together.'",
    "Ross (Final Boss): 'Depression, you mopey piece of shit. Stop monologuing like Shadow the Hedgehog at Hot Topic. We get it. You’re sad. Now let me SLEEP.'",
    "Ross (Final Boss): 'Overwhelm is like trying to PIVOT a goddamn couch through my frontal lobe. Spoiler alert: IT DOESN’T FIT. Take something the fuck off the list.'",
    "Ross (Final Boss): 'Insomnia? Oh sure. Let’s lay awake and plan 900 ways to ruin my life before sunrise. Love that for us. Fuck you, Insomnia.'"
]
robert_roasts_anxiety = [
    "Ross: 'Anxiety? Oh sure, let's rehearse 47 scenarios of humiliation that’ll never happen. Productive use of time!'",
    "Ross: 'Anxiety's like trying to code JavaScript at 3 AM. Errors everywhere, nothing makes sense, and somehow it’s your fault.'",
    "Ross: 'Having anxiety feels like Max from the Goofy Movie giving directions—chaotic, confusing, and inevitably wrong.'",
    "Ross: 'Anxiety thinks it’s Shadow the Hedgehog: dark, brooding, and way too intense. Relax, you spiky little drama queen.'",
    "Ross: 'Anxiety says “Could you BE more worried?” Chandler voice: Yes, yes you could. But please, don’t.'"
]
robert_roasts_depression = [
    "Ross: 'Depression says binge-watch Friends until you’re numb. Not the worst idea, but maybe stop after season 10.'",
    "Ross: 'Depression’s basically debugging code with a rubber duck that’s just silently judging your life choices.'",
    "Ross: 'Depression is me at Thanksgiving: complaining, exhausted, and hoping someone else cleans up the mess.'",
    "Ross: 'Depression thinks it’s Shadow the Hedgehog, staring off dramatically into space. Very edgy. Not helpful.'",
    "Ross: 'Depression’s solution? Listen to the Goofy Movie soundtrack while staring into the abyss. Hey, at least the music’s catchy.'"
]
robert_roasts_panic = [
    "Ross: ‘Panic says EVERY. SINGLE. THING. IS. ON. FIRE. Newsflash: it’s just your code console blinking.’",
    "Ross: ‘Panic attacks have the timing of Goofy’s pratfalls—hilariously untimely and massively inconvenient.’",
    "Ross: ‘Panic thinks it’s Shadow the Hedgehog: always sprinting, never checking if there’s anything to chase.’",
    "Ross: ‘Panic’s strategy? Unsubscribe from reality notifications. Spoiler: they don’t ask permission.’",
    "Ross: ‘Panic, stop acting like your keyboard just turned into a landmine. It’s just a typo, not Armageddon.’"
]
robert_roasts_overwhelm = [
    "Ross: ‘Overwhelm is like trying to code a website while seven browser tabs explode in your face. Take one at a time.’",
    "Ross: ‘Overwhelm screams PIVOT so loud even Monica would raise an eyebrow. Maybe just breathe, huh?’",
    "Ross: ‘Overwhelm thinks it’s Shadow the Hedgehog on espresso. Slow down, road runner.’",
    "Ross: ‘Overwhelm’s idea of help: five to-do lists, three panic buttons, zero solutions. Classy.’",
    "Ross: ‘Overwhelm, you’re the Janice of feelings—impossible to ignore and absolutely exhausting.’"
]
robert_roasts_dissociation = [
    "Ross: ‘Dissociation, you’re like me during Ross and Rachel drama—checking out when things get real.’",
    "Ross: ‘Dissociation’s strategy: hit mute on life’s conversation. Spoiler: it doesn’t end well.’",
    "Ross: ‘Dissociation thinks it’s Shadow the Hedgehog—dark, distant, and impossible to find.’",
    "Ross: ‘Dissociation: the emotional rubber duck that won’t debug your feelings. Try talking, not walking away.’",
    "Ross: ‘Dissociation, stop auditioning for Ghost in the Shell. We need you here, not in a void.’"
]
robert_roasts_insomnia = [
    "Ross: ‘Insomnia, you’re like me waiting for my dinosaur bones to talk—restless and unnecessarily dramatic.’",
    "Ross: ‘Insomnia’s version of a lullaby is me ranting about my ex at 3 AM. Hard pass.’",
    "Ross: ‘Insomnia thinks it’s Shadow the Hedgehog—always up at night, brooding and edgy. Snooze, please.’",
    "Ross: ‘Insomnia: the ultimate code debugger—keeps you awake to fix what wasn’t broken. Lovely.’",
    "Ross: ‘Insomnia, stop treating your brain like it’s got a midnight DLC release. No updates tonight.’"
]
robert_roasts_ocd = [
    "Ross: ‘OCD, you’re like me counting my sandwiches—obsessive and absolutely unnecessary.’",
    "Ross: ‘OCD’s idea of fun is writing the same to-do list in triplicate. Yawn.’",
    "Ross: ‘OCD thinks it’s Shadow the Hedgehog—always scanning for perfection. Spoiler: it doesn’t exist.’",
    "Ross: ‘OCD, stop acting like Monica organizing her closet—chill out and let something stay messy.’",
    "Ross: ‘OCD, you’re the ultimate code linter—pointing out every flaw, even the ones we don’t care about.’"
]
robert_roasts_time_blindness = [
    "Ross: ‘Time Blindness—your favorite game: “Guess What Day It Is?” Spoiler: You always lose.’",
    "Ross: ‘Time Blindness thinks calendars are mere decorations. Meanwhile, deadlines are real.’",
    "Ross: ‘Time Blindness is like me forgetting my wedding anniversary. Not cool, buddy.’",
    "Ross: ‘Time Blindness says “I’ll do it later.” Later is a myth, like Ross’s high school hair.’",
    "Ross: ‘Time Blindness—because showing up on time is apparently optional in your world.’"
]
# ─────────────────────────────────────────────────
# 1) (If you haven’t already) Ensure all your per-symptom Robert lists are defined above, e.g.:
#   robert_roasts_anxiety = [ … 5 lines … ]
#   robert_roasts_depression = [ … ]
#   … etc. for all 12 symptoms …

# 2) Create a lookup so you can grab the right list by symptom name:
robert_roasts_by_symptom = {
    "Anxiety": robert_roasts_anxiety,
    "Depression": robert_roasts_depression,
    "Panic": robert_roasts_panic,
    "Overwhelm": robert_roasts_overwhelm,
    "Dissociation": robert_roasts_dissociation,
    "Insomnia": robert_roasts_insomnia,
    "Burnout": robert_roasts_burnout,
    "Focus Problems": robert_roasts_focus_problems,
    "OCD": robert_roasts_ocd,
    "Time Blindness": robert_roasts_time_blindness,
    "Sound Overstimulation": robert_roasts_sound_overstimulation,
    "Grounding": robert_roasts_grounding,
}

# 3) Secret Final-Boss ASCII art + Rated-R meltdown lines:
ross_final_boss_art = """
▗▄▄▖  ▗▄▖  ▗▄▄▖ ▗▄▄▖
▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌   
▐▛▀▚▖▐▌ ▐▌ ▝▀▚▖ ▝▀▚▖
▐▌ ▐▌▝▚▄▞▘▗▄▄▞▘▗▄▄▞▘
 …[your full ASCII art pasted here]…
"""

robert_final_boss = [
    "Ross (Final Boss): 'OH MY GOD. Anxiety, you are the Janice of mental health. Loud. Annoying. And NO ONE INVITED YOU. GET. THE. FUCK. OUT.'",
    "Ross (Final Boss): 'Panic attacks? Oh goodie! My favorite way to feel like I'm dying in a Best Buy parking lot at 2am. Seriously? Get your shit together.'",
    "Ross (Final Boss): 'Depression, you mopey piece of shit. Stop monologuing like Shadow the Hedgehog at Hot Topic. We get it. You’re sad. Now let me SLEEP.'",
    "Ross (Final Boss): 'Overwhelm is like trying to PIVOT a goddamn couch through my frontal lobe. Spoiler alert: IT DOESN’T FIT. Take something the fuck off the list.'",
    "Ross (Final Boss): 'Insomnia? Oh sure. Let’s lay awake and plan 900 ways to ruin my life before sunrise. Love that for us. Fuck you, Insomnia.'"
]
# ─────────────────────────────────────────────────

