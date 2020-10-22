import webbrowser as wb
import time
import string
import random

from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

class Arena(object):
    def __init__(self):
        """
        Arenas track all current players in the game as well as their scores

        self.players is a dict mapping players to their scores

        """
        self.players = {}
    
    def addPlayer(self, player):
        self.players.setdefault(player, 0)

    def updateScores(self):
        for player in self.players.keys():
            self.players[player] = player.getScore()
    
    def showScores(self):
        for player in self.players.keys():
            print(player.getName() + " somehow has " +
            str(player.getScore()) + " points.")
        
    
class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.level = 1
    
    def addScore(self, word):
        self.score += len(word)
    
    def getScore(self):
        return self.score

    def getName(self):
        return self.name

def loadWords(level):
    """
    Input: Level (integer) of difficulty for current round, from 1-4 inclusive

    Output: A list of words to be used for the round

    """
    WORDLIST1 = "/Users/adityakuroodi/Desktop/theBee/words.txt"    # 6th grade
    WORDLIST2 = "/Users/adityakuroodi/Desktop/theBee/words2.txt"    # 7th
    WORDLIST3 = "/Users/adityakuroodi/Desktop/theBee/words3.txt"    # high school
    WORDLIST4 = "/Users/adityakuroodi/Desktop/theBee/words4txt"     # death
    
    levelmap = {1: WORDLIST1, 2: WORDLIST2, 3: WORDLIST3, 4: WORDLIST4}   # maps level to different text files to generate the right word list


    inFile = open(levelmap[level], 'r')
    
    wordList = []
    for line in inFile:
        line = line.splitlines()
        line = line[0].split('\t')
        wordList += line
        
    return wordList[:-1]        # splice off last "word" which is actually a blank space in our raw txt files


def lookupWord(word):
    """
    Opens a new tab in Chrome pointing to a dictionary lookup of the word.
    Assumes word is of type string
    
    """    
    print("Looking up word...\n")
    #deleteTab() # closes last open tab

    # Open new tab with word
    dictURL = "https://dictionary.com/browse/"
    wordURL = dictURL + word.lower()
    wb.open(wordURL)

    action = input("Done looking up word? [Y/N]\n ")

    if action.lower() == 'n':
        lookupWord(word)
    elif action.lower() == 'y':
        return

def playRound(level, words, arena):

    for player in arena.players.keys():
        print(player.getName() + " you're up \n")
        word = random.choice(words)
        lookupWord(word)
        x = input("Guessed correctly? [Y/N]\n")
        if x.lower() == 'n':
            continue
        if x.lower() == 'y':
            player.addScore(word)
        print("On to the next player!\n")




def runBee():
    # Setup the playing field by adding all the players to the Arena
    arena = Arena()
    friends = ["Kuroodi", "Vikram", "Aahana"]
    random.shuffle(friends)
    beeRound = 1

    for friend in friends:
        arena.addPlayer(Player(friend))

    # Each game will consist of 4 rounds, tibreakers occur after 4th round
    while beeRound < 2:
        print("Start of round " + str(beeRound) + '\n')

        # Load appropriate word list for each round
        words = loadWords(beeRound)

        playRound(beeRound, words, arena)

        arena.updateScores()

        print("And the scores for round " + str(beeRound) + " are:\n" )
        arena.showScores()
        beeRound+=1


    


runBee()