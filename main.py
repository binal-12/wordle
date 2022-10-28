import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.text.splitlines();

words = []

for i in WORDS:
    if len(i) == 5:
        words.append(i)

word = random.choice(words)


print("Hello, Lets play Wordle. \nPress any enter to begin!")
input();
print("=================")
print("There will be a five letter word you have tp guess for.")
print("You will get six tries to guess that word.")
print("If the letter is in word and in correct position the box will turn green,")
print("If the letter is in word but not in correct position the box will turn red")
print("If the letter is not in the word, the box will turn grey")
print("\n")


white = "⬜️"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

data = []
userTry = 0
userWord = ""

for i in range(6):
    temp = []
    for j in range(5):
        temp.append(" "+'-1')
    data.append(temp)


def printData():
    print("\n")
    for i in data: 
        for j in i:
            if j[1] == '0':
                print(j[0], end=" ")
            elif j[1] == '1':
                print(f"{bcolors().WARNING}{j[0]}{bcolors().ENDC}", end=" ")
            elif j[1] == '2':
                print(f"{bcolors().OKGREEN}{j[0]}{bcolors().ENDC}", end =" ")
            else:
                print(j[0], end =" ")
        print("")
    print("\n")

def takeinput():
    s = input("Enter your guess: ")
    while(len(s) != 5):
        print("Invalid input, please enter a five letter word.")
        s = input("Enter your guess: ")
    return s

def checkGame(s):
    if s == word:
        return True
    return False


printData()
while userTry < 6:
    userWord = takeinput()
    userWord = userWord[0:min(len(userWord),5)]
    for i in range(5):
        if userWord[i] == word[i]:
            data[userTry][i] = userWord[i] + '2'
        elif userWord[i] in word:
            data[userTry][i] = userWord[i] + '1'
        else:
            data[userTry][i] = userWord[i] + '0'

    printData()
    if checkGame(userWord):
        print(f"You guessed the word in {userTry} try(ies).")
        break
    userTry += 1

if not checkGame(userWord):
    print(f"The correct guess was {bcolors().OKGREEN}{word}{bcolors().ENDC}.")



