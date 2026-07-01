word = "cat"

for i in range(3):
    guess = input("Guess a letter: ")
    if guess in word:
        print("Correct")
    else:
        print("Wrong")

print("The word was", word)