# Hangman-Game
Hangman Game Code Explanation

This Python code implements a simple Hangman game where the player has to guess a randomly chosen word from a predefined list.

1. Importing the necessary module:
   - The 'random' module is imported to choose a random word from the word list.

2. Defining the word list:
   - A list named 'word_list' contains a collection of words that can be used for the game.

3. Choosing a random word:
   - The 'random.choice()' function selects a random word from the 'word_list'.

4. Initializing variables:
   - 'word_guessed' is initialized to contain underscores (_) representing the unknown letters of the word.
   - 'false_guess' keeps track of the number of incorrect guesses made by the player.

5. Main game loop:
   - The game consists of a loop where the player can input guesses until they win or lose.
   - The loop iterates for a maximum of 12 times (can be adjusted).
   
6. Guessing letters:
   - The player enters a letter as a guess.
   - If the guessed letter is correct, it replaces the corresponding underscore in 'word_guessed'.
   - If the guessed letter is incorrect, the player receives a penalty, and a part of the hangman figure is drawn.
   
7. Checking win and lose conditions:
   - If the player correctly guesses all the letters in the word before making 6 false guesses, they win.
   - If the player makes 6 false guesses without guessing the word, they lose.

8. Displaying feedback:
   - Throughout the game, the current state of 'word_guessed' is printed to show the player's progress.
   - Hangman figures are printed to visually represent the number of false guesses made.
   - When the game ends, a message is printed to indicate whether the player won or lost, along with the correct word if they lose.

9. End of the game:
   - After printing the result, the game loop ends, and the program terminates.

