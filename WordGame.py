#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    for ch in word:
        if letter == ch:
            return True
    
    return False

def inSpot(letter, word, spot):
    correctLetter = word[spot]
    if letter == correctLetter:
        return True
    else:
        return False

def rateGuess(guess, word):
    feedback = ""
    for idk in range(5):
        myLetter = guess[idk]
        if inSpot(myLetter, word, idk) == True:
            feedback = feedback + myLetter.upper() #Correct spot
        elif inWord(myLetter, word) == True:
            feedback = feedback + myLetter.lower() #wrong spot
        else:
            feedback = feedback + "*"
    return feedback


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    
    guessNum = 1
    while guessNum <= 6:
        validWord = False
        while validWord == False:
            myGuess = input("Guess the 5 letter word: ")
            myGuess = myGuess.lower()
            if myGuess not in wordList:
                print("Word not in list")
            else:
                validWord = True

        feedback = rateGuess(myGuess, todayWord)
        print(feedback)
        if feedback == todayWord.upper():
            print("You guessed the word in " + str(guessNum) + " tries")
            guessNum = guessNum + 6
            win = True
        guessNum = guessNum + 1

    print("the word was", todayWord)
    #User should get 6 guesses to guess

    print("see ya")
    #Ask user for their guess
    #Give feedback using on their word:





if __name__ == '__main__':
  main()
