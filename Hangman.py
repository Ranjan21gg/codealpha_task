import random

def hangman():
    # 1. Predefined list of words
    words = ["python", "hangman", "game", "random", "string"]
    word = random.choice(words)  # Randomly choose a word
    guessed_letters = []  # Keep track of guessed letters
    attempts = 6  # Max incorrect guesses allowed
    
    print("🎯 Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print(f"You have {attempts} incorrect guesses allowed.\n")

    # Convert word into list of underscores
    display_word = ["_"] * len(word)

    while attempts > 0:
        # Show current progress
        print("Word: ", " ".join(display_word))
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Remaining attempts: {attempts}")

        guess = input("Enter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet letter.\n")
            continue
        if guess in guessed_letters:
            print("⚠ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!\n")
            # Reveal correct letter(s)
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess
        else:
            print("❌ Wrong guess!\n")
            attempts -= 1

        # Check win condition
        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("💀 You ran out of attempts! The word was:", word)

# Run the game
hangman()