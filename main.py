print("Starting a game of Hangman.")
from random import randint
valid1 = 0
x = 0
hg = 0
valid2 = 0


valid27000 = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

valid30 = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
    "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"
]


valid900 = ["3", "4", "5", "6", "7", "8", "9", "10"]


allwords = [
    "dog", "cat", "man", "woman", "incomprehensible", "cucumber", "celebrity", "epidemic",
    "pencilcase", "fifty", "penny", "orangutan", "caramel", "yesterday", "garbage", "astronaut", "apartment", "walking", "they"]

y = len(allwords)
validwords = []

while valid1 == 0:
    attempts = input("How many incorrect attempts do you want? [1-25] ")
    if attempts not in valid30:
        print("Not a valid number from 1 to 25")
    else:
        valid1 = 1
        attempts = int(attempts)
   
while valid2 == 0:
    minlen = input("What's the minimum length of the word? [3-10] ")
    if minlen not in valid900:
        print("Not a valid number from 3 to 10")
    else:
        valid2 = 1
        minlen = int(minlen)
        
while x in range(-1, y - 1):
    x = x + 1
    lenx = int(len(allwords[x]))
    valid3 = max(lenx, minlen)
    if valid3 == lenx:
        validwords.append(allwords[x])


wordnm = randint(0, len(validwords) - 1)
word = validwords[wordnm]
wordlen = len(word)


guess = []
wordlist = []



for x in range(0, wordlen):
    x = x + 1
    guess.append("*")
    wordlist.append(word[x - 1])


while attempts > 0:
    print(guess)
    guess1 = input("Enter your guess: ")
    if guess1 not in valid27000:
        print(
            "This is not a valid guess. Try inputting a lowercase English letter"
        )

    else:
        if guess1 not in wordlist:
            if attempts != 1:
                print("This letter is not in the word. Try again")

            else:
                print(
                    "This letter is not in the word. You have ran out of attempts. The word was " + word)
            attempts = attempts - 1
      
        else:
            print("This letter is in the word")
            while hg in range(0, len(wordlist)):
                if wordlist[hg] == guess1:
                    guess[hg] = guess1
                hg = hg + 1
                if guess == wordlist:
                    print("You won! Congrats. The word is " + word)
                    while True:
                        aohuni = 1
            hg = 0
