Project 1: Hangman Game
Description
A classic word-guessing game where players guess letters to reveal a hidden word from a list of five options. Players have six incorrect guesses before losing. The game displays a progressive ASCII hangman figure, tracks guessed letters, validates input, and shows word progress with underscores and revealed letters. It provides instant feedback and allows replay after each round.
Features

5 predefined words to guess
6 incorrect guesses limit
Visual ASCII hangman stages
Input validation (single letters only)
Duplicate guess prevention
Real-time word progress display
Win/loss detection
Replay option

How to Run
bashpython hangman.py
How to Play

The game will randomly select a word
Guess one letter at a time
Correct guesses reveal letters in the word
Incorrect guesses add to the hangman figure
Win by completing the word before 6 wrong guesses
Choose to play again after each game

Key Concepts Demonstrated

Random selection (random.choice())
While loops for game flow
If-else conditional statements
String manipulation
List operations
Input validation
Function definitions

Example Gameplay
Welcome to Hangman!
Try to guess the word one letter at a time.

Word: _ _ _ _ _ _
Guessed letters: None
Incorrect guesses remaining: 6

Guess a letter: p
✓ Good guess! 'p' is in the word.
