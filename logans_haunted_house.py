"""
A spooky Halloween-themed choose your own adventure game! (Brought to you by Ghouls WhoOooOoo CoOoooOOoode)
Welcome to the haunted house...
"""

def main():
    print("🎃 Welcome to the HAUNTED HOUSE! 🎃")
    print("=" * 50)
    print("\nIt's Halloween night, and instead of trick-or-treating or drinking spookily too many potions at a party,")
    print(" you've found yourself on the front doorstep of the old, abandoned mansion at the edge of OU campus. Thunder rumbles ")
    print("in the clouds above, and you swear you hear a soft whispering in the wind around you, which cuts through your clothes with an icy chill.")
    print(" As you gaze at the house before you, you notice the front door is slightly ajar...")
    print()
    print("What do you do?")
    print("1. Enter through the front door")
    print("2. Try to get in through the window")
    
    # Initial choice variable
    initial_choice = ""
    
    # First question
    while initial_choice not in ["1", "2"]:
        initial_choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if initial_choice not in ["1", "2"]:
            print("\n❌ Invalid choice! Please enter 1 or 2.\n")
    
    # Branch based on initial choice using if/else statements
    if initial_choice == "1":
        # Path 1: Front door
        print("\n" + "=" * 50)
        print("You push open the heavy front door...")
        print("It creeeaaaaks open under your touch. As you enter, your footsteps echo on the dusty wooden floor.")
        print("To your left, you see a beautiful, dust-covered grand piano, with several keys missing.")
        print("To your right, you see a spiraling wooden staircase.")
        print("As you walk further, all of the sudden you hear what sounds like a mournful, drawn-out howl coming from above you.")
        print("It could be the wind, but you have an awful feeling that the sound came from upstairs...")
        print()
        print("What do you do next?")
        print("1. Go upstairs to investigate the sound")
        print("2. Play a jam on the piano")
        
        # Second choice for path 1
        path1_choice = ""
        while path1_choice not in ["1", "2"]:
            path1_choice = input("\nEnter your choice (1 or 2): ").strip()
            
            if path1_choice not in ["1", "2"]:
                print("\n❌ Invalid choice! Please enter 1 or 2.\n")
        
        # Branch for second level choice
        if path1_choice == "1":
            print("\n" + "=" * 50)
            print("You start climbing the staircase...")
            print("Each step groans under your weight, but eventually, you reach the top. There, you find two doors.")
            print()
            print("Which door do you choose?")
            print("1. The door on the left")
            print("2. The door on the right")
            door_choice = ""
            while door_choice not in ["1", "2"]:
                door_choice = input("\nEnter your choice (1 or 2): ").strip()
                
                if door_choice not in ["1", "2"]:
                    print("\n❌ Invalid choice! Please enter 1 or 2.\n")

            if door_choice == "1":
                print("\n" + "=" * 50)
                print("INSERT YOUR SPOOKY ENDING FOR LEFT DOOR HERE!")
                print("CHOICE 1")
                print("CHOICE 2")
                left_door_choice = ""
                # TODO: New programmers - complete this path!
            else:
                print("\n" + "=" * 50)
                print("INSERT YOUR SPOOKY ENDING FOR RIGHT DOOR HERE!")
                print("CHOICE 1")
                print("CHOICE 2")
                right_door_choice = ""
                # TODO: New programmers - complete this path!
            
        else:  # path1_choice == "2"
            print("\n" + "=" * 50)
            print("Ignoring the sound, you walk over to the grand piano, taking a seat at the creaky bench in front of it.")
            print("Though the piano looks certainly past its prime, you decide to try playing a couple keys.")
            print("To your surprise, the piano is perfectly in tune! Excited by this development, you play a little tune.")
            print("The piano is your loyal companion, and you understand its every need and whim. Before you know it, the tune is really picking up!")
            print("So enraptured by the song, you hardly even notice when another figure sits on the bench beside you, turning your solo-jam into a duet.")
            print("The figure has rotting, green skin, and an affinity for brains.")
            print("You also don't notice when a figure dressed all in black appears from a nearby coffin, taking out a violin.")
            print("Before you know it, you've got a full quartet formed in the center of the house... and you sound pretty good!")
            print("Even when you realize, you don't seem to mind. You spend the rest of the night playing with your newfound musical friends.")
            print()
            print("GAME OVER! You played the monster mash, and it was a graveyard smash. Try again to see what other haunts await you in the house!")

    
    else:  # initial_choice == "2"
        # Path 2: Back of house
        print("\n" + "=" * 50)
        print("Not one to trust an open door, you make your way to the side of the house.")
        print("Thorns claw at your legs as you trudge along. Eventually, you find a nice big rock to break the window with.")
        print("You use the rock to shatter the glass, and carefully climb through the jagged, makeshift entrance.")
        print("You fall on a spike trap and die!")
        print()
        print("GAME OVER! YOU DIED! Maybe we'll see you again as a ghost... Try again to see if you can make it farther than a single step!")
    
    print("\n" + "=" * 50)
    print("Thanks for playing! Happy Halloween! 👻")
    print("=" * 50)


if __name__ == "__main__":
    main()
