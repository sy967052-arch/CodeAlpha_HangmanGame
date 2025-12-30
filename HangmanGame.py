import random

# List of words to choose from
words = ["python", "hangman", "coding", "computer", "keyboard"]

# Hangman visual stages
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed and others as underscores"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_hangman():
    """Main game function"""
    # Choose a random word
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.")
    print(f"You have {max_incorrect} incorrect guesses allowed.\n")
    
    # Main game loop
    while incorrect_guesses < max_incorrect:
        # Display current state
        print(hangman_stages[incorrect_guesses])
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
        
        # Check if word is complete
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 Congratulations! You won! The word was '{word}'")
            return
        
        # Get player input
        guess = input("\nGuess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        # Add guess to list
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in word:
            print(f"✓ Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"✗ Sorry, '{guess}' is not in the word.")
    
    # Game over - player lost
    print(hangman_stages[incorrect_guesses])
    print(f"\n💀 Game Over! The word was '{word}'")

# Start the game
if __name__ == "__main__":
    play_hangman()
    
    # Option to play again
    while input("\nPlay again? (yes/no): ").lower() == "yes":
        print("\n" + "="*40 + "\n")
        play_hangman()