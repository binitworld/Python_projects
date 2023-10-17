import random

def choose_random_word():
    word_list = ["python", "hangman", "programming", "challenge", "developer"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_random_word()
    guessed_letters = []
    attempts = 6  # You can adjust the number of allowed attempts

    print("Welcome to Hangman!")
    
    while True:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            if set(word) == set(guessed_letters):
                print(f"Congratulations, you've won! The word was: {word}")
                break
        else:
            print("Incorrect guess.")
            attempts -= 1
            if attempts == 0:
                print(f"You're out of attempts. The word was: {word}")
                break

if __name__ == "__main__":
    hangman()
￼Enter
