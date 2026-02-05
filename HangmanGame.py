import random
words = ["python", "apple", "banana", "guitar", "hangman"]


word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("\nWord: ", " ".join(guessed))
    guess = input("Guess a letter: ").lower()
   
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if "_" not in guessed:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)