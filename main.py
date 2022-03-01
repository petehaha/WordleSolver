import string
import random
from collections import defaultdict

with open("wordle-answers-alphabetical.txt", "r") as file:
    words = file.readlines()

# Computes probability for all letters and returns words which contain them.
def rebalance(probs={}, numPasses=0):
    if probs:
        for key, val in probs.items():
            letterProbabilites[key] = val

    totalLetters = sum(letterProbabilites.values())
    for key in letterProbabilites.keys():
        letterProbabilites[key] = letterProbabilites[key] / totalLetters


    mostProbableKeys = sorted(letterProbabilites, key=letterProbabilites.get, reverse=True)
    if numPasses == 0:
        topKeys = frozenset(mostProbableKeys[:15])  #
    else:
        topKeys = frozenset(mostProbableKeys[:15+numPasses])

    wordList = []
    for letter in mostProbableKeys:
        for word in wordsAsLetters.keys():
            if word.issubset(topKeys):
                mostProbableWord = wordsAsLetters[word]
                wordList.extend(mostProbableWord)
        if len(wordList) != 0:
            break
        else:
            topKeys.add(letter)

    return wordList

def validateWord(word, wordList, numPasses=0):
    validatedWordList = []
    
    # Record letters that can't be at given index.
    for ind, letter in enumerate(list(word)):
        if letter.islower():
            lettersNotAtInd[ind].append(letter)
            
    for w in wordList:
        badWord = False
        
        # Makes sure the words contain all the known (yellow) letters
        for letter in lettersInWord:
            if letter not in w:
                badWord = True
                
        # Remove word if letters are not correct position 
        for ind, letter in enumerate(list(word)):
            if letter.isupper() and w[ind] != letter.lower():
                badWord = True
            elif letter.islower() and w[ind] in lettersNotAtInd[ind]:
                badWord = True
            else:
                pass
            
        if not badWord:
            validatedWordList.append(w)
    
    # If no words are found, increment counter
    if len(validatedWordList) == 0:
        numPasses += 1
    return numPasses, validatedWordList


def getMoreWords(history, prevList, numPasses=0):
    numPasses += 1
    wordList = rebalance(numPasses=numPasses)
    numPasses, validatedList = validateWord(history[-1], wordList)
    while len(validatedList) == 0 or prevList == validatedList:
        numPasses += 1
        wordList = rebalance(probs, numPasses)
        numPasses, validatedList = validateWord(history[-1], wordList, numPasses)

    return numPasses, validatedList

letterProbabilites = {key: 0 for key in list(string.ascii_lowercase)}
lettersNotAtInd = d = [[] for x in range(5)]
lettersInWord = set([])
wordsAsLetters = defaultdict(list)

fiveLetterWords = [word.strip('\n') for word in words if len(word) == 6]
for word in fiveLetterWords:
    wordsAsLetters[frozenset(word)].append(word)
    for letter in list(word):
        letterProbabilites[letter] += 1

wordList = rebalance()
history = []
numPasses = 0

while(True):
    word = list(input("Whats the result? Lowercase if wrong position, Uppercase if correct, Underscore if unknown."
                      "If no words, hit enter and if finished, type done.\n"))
    if not word:
        numPasses, validatedList = getMoreWords(history, validatedList, numPasses)
        print(numPasses)
        print(validatedList)
        continue
    elif word == "done":
        exit()
    else:
        pass

    history.append(word)

    wrongLetters = list(input("Wrong Letters?\n"))

    probs = {}

    for letter in word:
        if letter == "_":
            pass
        else:
            lettersInWord.add(letter.lower())
            probs[letter.lower()] = 10

    for letter in wrongLetters:
        probs[letter] = 0

    numPasses = 0
    wordList = rebalance(probs, numPasses)
    numPasses, validatedList = validateWord(word, wordList)
    while len(validatedList) == 0:
        wordList = rebalance(probs, numPasses)
        numPasses, validatedList = validateWord(word, wordList, numPasses)
    random.shuffle(validatedList)
    print(sorted(validatedList, key=lambda x: len(set(x)), reverse=True))

