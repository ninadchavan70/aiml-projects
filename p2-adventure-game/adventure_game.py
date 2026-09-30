# Task 1: Set up the project
# Actions:
# • Open VS Code and create a new folder for your project
# • Inside the folder, create a new Python file named adventure_game.py
# • Add an inline comment to describe the purpose of the script
# • Run a simple print statement to confirm that the setup is working

# Purpose: Run a text-based adventure game in which the player searches for treasure.

# Simple print statement confirming that the project setup is working.
print("Adventure Game loaded successfully!")

# Task 2: Create a function to start the game
# Actions:
# • Define the function start_game() to display the game introduction
# • Ask the player for their name and store it in a variable
# • Provide the player with an initial choice (explore a forest or enter a cave)
# • Use GitHub Copilot to generate the function body
def start_game():
    print("Welcome to the Adventure Game!")
    player_name = input("Please enter your name: ")
    print(f"Hello, {player_name}! You are about to embark on an exciting journey.")
    
    choice = input("Do you want to explore a forest or enter a cave? (forest/cave): ").strip().lower()
    
    if choice == "forest":
        print("You venture into the forest, surrounded by towering trees and the sounds of wildlife.")

        # Additional forest exploration logic can be added here
        forest_path()

    elif choice == "cave":
        print("You step into the dark cave, feeling the cool air and hearing the echoes of dripping water.")

        # Additional cave exploration logic can be added here
        cave_path()

    else:
        print("Invalid choice. Please choose either 'forest' or 'cave'.")
        start_game()  # Restart the game if the choice is invalid


# Task 3: Create the forest path
# Actions:
# • Define the function forest_path() that describes the forest scenario
# • Provide the player with choices (follow a river or climb a tree)
# • Use an if-else structure to handle player choices
def forest_path():
    print("You are now in the forest. The sunlight filters through the leaves, creating a serene atmosphere.")
    choice = input("Do you want to follow a river or climb a tree? (river/tree): ").strip().lower()
    
    if choice == "river":
        print("You follow the river, enjoying the sound of flowing water and spotting fish swimming by.")

        # Additional river exploration logic can be added here
        print("You soon find a bridge, and upon crossing it find the treasure!")

    elif choice == "tree":
        print("You climb a tall tree, getting a bird's-eye view of the forest and spotting wildlife below.")

        # Additional tree climbing logic can be added here
        print("A branch breaks and you fall down, ending your quest.")

    else:
        print("Invalid choice. Please choose either 'river' or 'tree'.")
        forest_path()  # Restart the forest path if the choice is invalid

# Task 4: Create the cave path
# Actions:
# • Define the function cave_path() that describes the cave scenario
# • Provide the player with choices (light a torch or proceed in the dark)
# • Use conditionals to determine the outcome
def cave_path():
    print("You are now in the cave. The darkness is thick, and you can hear the sound of dripping water echoing through the tunnels.")
    choice = input("Do you want to light a torch or proceed in the dark? (torch/dark): ").strip().lower()
    
    if choice == "torch":
        print("You light a torch, illuminating the cave walls and revealing ancient carvings and hidden passages.")

        # Additional torch lighting logic can be added here
        print("As you go further, you are able to find the treasure!")

    elif choice == "dark":
        print("You proceed in the dark, relying on your senses to navigate through the cave. You feel a sense of adventure and mystery.")

        # Additional dark exploration logic can be added here
        print("However, you soon lose your way and your quest ends.")

    else:
        print("Invalid choice. Please choose either 'torch' or 'dark'.")
        cave_path()  # Restart the cave path if the choice is invalid



# Task 5: Run the adventure game
# Actions:
# • Call start_game() to begin the adventure
# • Ensure the program runs in a loop until the player completes their journey
# • Provide an option to restart the game after completion
def run_game():
    while True:
        start_game()
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Thank you for playing the Adventure Game! Goodbye!")
            break


if __name__ == "__main__":
    run_game()
