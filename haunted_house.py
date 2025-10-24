#!/usr/bin/env python3
"""
A spooky Halloween-themed choose your own adventure game!
Welcome to the haunted house...
"""

def main():
    print("🎃 Welcome to the HAUNTED HOUSE! 🎃")
    print("=" * 50)
    print("\nYou stand before an old, creaky mansion on Halloween night.")
    print("The wind howls through the dead trees, and thunder rumbles overhead.")
    print("The front door is slightly ajar, and you can hear strange noises from within...")
    print()
    
    # Initial choice variable
    initial_choice = ""
    
    # First question - use while loop for input validation
    while initial_choice not in ["1", "2"]:
        print("What do you do?")
        print("1. Enter through the front door")
        print("2. Sneak around to the back of the house")
        initial_choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if initial_choice not in ["1", "2"]:
            print("\n❌ Invalid choice! Please enter 1 or 2.\n")
    
    # Branch based on initial choice using if/else statements
    if initial_choice == "1":
        # Path 1: Front door
        print("\n" + "=" * 50)
        print("You push open the heavy front door...")
        print("It creaks loudly as you step into a dusty foyer.")
        print("A grand staircase rises before you, and to your left is a dimly lit hallway.")
        print("You hear scratching sounds coming from upstairs.")
        print()
        
        # Second choice for path 1
        path1_choice = ""
        while path1_choice not in ["1", "2"]:
            print("What do you do next?")
            print("1. Climb the creaky staircase")
            print("2. Explore the dark hallway")
            path1_choice = input("\nEnter your choice (1 or 2): ").strip()
            
            if path1_choice not in ["1", "2"]:
                print("\n❌ Invalid choice! Please enter 1 or 2.\n")
        
        # Branch for second level choice
        if path1_choice == "1":
            print("\n" + "=" * 50)
            print("You start climbing the staircase...")
            print("Each step groans under your weight...")
            print()
            # TODO: New programmers - complete this path!
            print("🔮 TO BE CONTINUED... 🔮")
            print("(New programmers: Add your own spooky ending here!)")
            
        else:  # path1_choice == "2"
            print("\n" + "=" * 50)
            print("You cautiously walk down the hallway...")
            print("Portraits on the walls seem to watch you...")
            print()
            # TODO: New programmers - complete this path!
            print("🔮 TO BE CONTINUED... 🔮")
            print("(New programmers: Add your own spooky ending here!)")
    
    else:  # initial_choice == "2"
        # Path 2: Back of house
        print("\n" + "=" * 50)
        print("You carefully make your way around the side of the mansion...")
        print("Thorny bushes scratch at your clothes as you creep along.")
        print("You reach the backyard and see a cellar door and a greenhouse.")
        print("Strange green light glows from inside the greenhouse.")
        print()
        
        # Second choice for path 2
        path2_choice = ""
        while path2_choice not in ["1", "2"]:
            print("What do you do next?")
            print("1. Open the cellar door")
            print("2. Investigate the glowing greenhouse")
            path2_choice = input("\nEnter your choice (1 or 2): ").strip()
            
            if path2_choice not in ["1", "2"]:
                print("\n❌ Invalid choice! Please enter 1 or 2.\n")
        
        # Branch for second level choice
        if path2_choice == "1":
            print("\n" + "=" * 50)
            print("You pull open the heavy cellar door...")
            print("Cold air rushes up from the darkness below...")
            print()
            # TODO: New programmers - complete this path!
            print("🔮 TO BE CONTINUED... 🔮")
            print("(New programmers: Add your own spooky ending here!)")
            
        else:  # path2_choice == "2"
            print("\n" + "=" * 50)
            print("You approach the greenhouse...")
            print("The green light pulses rhythmically...")
            print()
            # TODO: New programmers - complete this path!
            print("🔮 TO BE CONTINUED... 🔮")
            print("(New programmers: Add your own spooky ending here!)")
    
    print("\n" + "=" * 50)
    print("Thanks for playing! Happy Halloween! 👻")
    print("=" * 50)


if __name__ == "__main__":
    main()
