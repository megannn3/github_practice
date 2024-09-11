import random
import time

def display_status(runner_position, tagger_position, tags):
    print(f"\nRunner is at position {runner_position}.")
    print(f"Tagger is at position {tagger_position}.")
    print(f"Tags: {tags}")

def move_player(position):
    # Move player to a new random position between 0 and 9
    return random.randint(0, 9)

def tag_game():
    print("Welcome to the Console Game of Tag!")
    print("The game is played on a linear track with 10 positions (0 to 9).")
    print("The tagger will try to tag the runner by moving to the same position.")
    
    # Initial positions
    runner_position = random.randint(0, 9)
    tagger_position = random.randint(0, 9)
    
    tags = 0
    game_running = True
    
    while game_running:
        display_status(runner_position, tagger_position, tags)
        
        # Move tagger
        print("\nTagger's turn!")
        input("Press Enter to move the tagger...")
        tagger_position = move_player(tagger_position)
        
        # Check if tagger has tagged the runner
        if tagger_position == runner_position:
            tags += 1
            print(f"Tagger tagged the runner! Total tags: {tags}")
            runner_position = random.randint(0, 9)  # Move the runner to a new position
            print(f"Runner moves to position {runner_position}.")
        
        # Move runner
        print("\nRunner's turn!")
        input("Press Enter to move the runner...")
        runner_position = move_player(runner_position)
        
        # Check if runner has been tagged
        if tagger_position == runner_position:
            tags += 1
            print(f"Runner was tagged! Total tags: {tags}")
            runner_position = random.randint(0, 9)  # Move the runner to a new position
            print(f"Runner moves to position {runner_position}.")
        
        # Ask if players want to continue
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            game_running = False

    print(f"\nGame Over! Total tags: {tags}")

if __name__ == "__main__":
    tag_game()
