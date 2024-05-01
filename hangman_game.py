import random

word_list = [
    "Banana", "Castle", "Guitar", "Dragon", "Mermaid",
    "Parrot", "Puzzle", "Rocket", "Spirit", "Wisdom",
    "Desert", "Flower", "Jungle", "Magnet", "Orphan",
    "Rocket", "Spirit", "Square", "Tunnel", "Winter"
]

word = random.choice(word_list)
word_guessed = "_"
false_guess = 0

for i in range(len(word)-1):
    word_guessed = word_guessed + "_"
for i in range(12):
    print(word_guessed)
    character_chosed = input("Enter an alphabet: ")
    in_bolean = False
    for x in range(len(word)):
        if character_chosed == word[x].lower():
            in_bolean = True
            word_guessed = word_guessed[:x] + character_chosed + word_guessed[x + 1:]
    if in_bolean == False:
        false_guess += 1 
        if false_guess == 1:
            print("  _______\n |/     |\n |\n |\n |\n |\n_|_")
        elif false_guess == 2:
            print("  _______\n |/     |\n |     (_)\n |\n |\n |\n_|_")
        elif false_guess == 3:
            print("  _______\n |/     |\n |     (_)\n |      |\n |      |\n |\n_|_")
        elif false_guess == 4:
            print("  _______\n |/     |\n |     (_)\n |     \|/\n |      |\n |\n_|_")
        elif false_guess == 5:
            print("  _______\n |/     |\n |     (_)\n |     \|/\n |      |\n |     / \n_|_")
        elif false_guess == 6:
            print("  _______\n |/     |\n |     (_)\n |     \|/\n |      |\n |     / \ \n_|_")
            print("The word was", word)
            print("You Lost 😔")
            break
    if word_guessed == word.lower():
        print("Congratulation you guessed the word", word, "without doing false guesses!")
        break

