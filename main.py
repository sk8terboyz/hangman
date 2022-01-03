
from tkinter import ttk
from tkinter import *
import random
# from PIL import ImageTk, Image

def startup():
    try:
        menuRoot = Tk()
        menuFrame = ttk.Frame(menuRoot, padding=5)
        menuGrid = menuFrame.grid()
        
        menuRoot.geometry("385x385") 

        # Create buttons for starting menu
        solo = ttk.Button(menuFrame, text="Singleplayer", command=singlePlayer).grid(column=0, row=0, ipadx=150, ipady=45, pady=2, sticky=N)
        multi = ttk.Button(menuFrame, text="Multiplayer", command=enterWord).grid(column=0, row=1, ipadx=150, ipady=45, pady=2, sticky=N)
        exit = ttk.Button(menuFrame, text="Exit Game", command=menuRoot.destroy).grid(column=0, row=2, ipadx=150, ipady=45, pady=2, sticky=N)

        # Run GUI
        menuRoot.mainloop()
    except:
        loadError()

def singlePlayer():
    try:
        gameRoot = Tk()
        gameFrame = ttk.Frame(gameRoot, padding=20)
        gameGrid = gameFrame.grid()

        # Set default size of game window
        gameRoot.geometry("1240x640")

        # Get the word from the dictionary of random words
        punctuation = '!"#$%^&*()_-=+\':;<>@/[\\]{\}`~0123456789\t\n\r\x0b\x0c'
        fn = "words.txt"
        if(fn):
            # Open file - auto close file
            with open(fn) as f:
                lines = f.readlines()
                word = lines[random.randint(0, len(lines))].strip(punctuation).lower()
                print(word)

        # Create letter spaces for the new word
        j = 1
        i = 1
        if len(word) > 9:
            whitespace1 = ttk.Label(gameRoot, text="\t\t").grid(column=0, row=1)
        else:
            whitespace2 = ttk.Label(gameRoot, text="\t\t\t\t").grid(column=0, row=1)
        for letter in word:
            if(letter in punctuation):
                wordError()
                break
            else:
                # print(i)
                label1 = ttk.Label(gameRoot, text="_____").grid(column=i, row=j)
                i += 1

        # Create buttons for each letter
        alph1 = ttk.Button(gameRoot, text="A", command= lambda: guessLetter('A', word, gameRoot)).grid(column=1, row=3, ipadx=2, ipady=2)
        alph2 = ttk.Button(gameRoot, text="B", command= lambda: guessLetter('B', word, gameRoot)).grid(column=2, row=3, ipadx=2, ipady=2)
        alph3 = ttk.Button(gameRoot, text="C", command= lambda: guessLetter('C', word, gameRoot)).grid(column=3, row=3, ipadx=2, ipady=2)
        alph4 = ttk.Button(gameRoot, text="D", command= lambda: guessLetter('D', word, gameRoot)).grid(column=4, row=3, ipadx=2, ipady=2)
        alph5 = ttk.Button(gameRoot, text="E", command= lambda: guessLetter('E', word, gameRoot)).grid(column=5, row=3, ipadx=2, ipady=2)
        alph6 = ttk.Button(gameRoot, text="F", command= lambda: guessLetter('F', word, gameRoot)).grid(column=6, row=3, ipadx=2, ipady=2)
        alph7 = ttk.Button(gameRoot, text="G", command= lambda: guessLetter('G', word, gameRoot)).grid(column=7, row=3, ipadx=2, ipady=2)
        alph8 = ttk.Button(gameRoot, text="H", command= lambda: guessLetter('H', word, gameRoot)).grid(column=8, row=3, ipadx=2, ipady=2)
        alph9 = ttk.Button(gameRoot, text="I", command= lambda: guessLetter('I', word, gameRoot)).grid(column=9, row=3, ipadx=2, ipady=2)
        alph10 = ttk.Button(gameRoot, text="J", command= lambda: guessLetter('J', word, gameRoot)).grid(column=1, row=4, ipadx=2, ipady=2)
        alph11 = ttk.Button(gameRoot, text="K", command= lambda: guessLetter('K', word, gameRoot)).grid(column=2, row=4, ipadx=2, ipady=2)
        alph12 = ttk.Button(gameRoot, text="L", command= lambda: guessLetter('L', word, gameRoot)).grid(column=3, row=4, ipadx=2, ipady=2)
        alph13 = ttk.Button(gameRoot, text="M", command= lambda: guessLetter('M', word, gameRoot)).grid(column=4, row=4, ipadx=2, ipady=2)
        alph14 = ttk.Button(gameRoot, text="N", command= lambda: guessLetter('N', word, gameRoot)).grid(column=5, row=4, ipadx=2, ipady=2)
        alph15 = ttk.Button(gameRoot, text="O", command= lambda: guessLetter('O', word, gameRoot)).grid(column=6, row=4, ipadx=2, ipady=2)
        alph16 = ttk.Button(gameRoot, text="P", command= lambda: guessLetter('P', word, gameRoot)).grid(column=7, row=4, ipadx=2, ipady=2)
        alph17 = ttk.Button(gameRoot, text="Q", command= lambda: guessLetter('Q', word, gameRoot)).grid(column=8, row=4, ipadx=2, ipady=2)
        alph18 = ttk.Button(gameRoot, text="R", command= lambda: guessLetter('R', word, gameRoot)).grid(column=9, row=4, ipadx=2, ipady=2)
        alph19 = ttk.Button(gameRoot, text="S", command= lambda: guessLetter('S', word, gameRoot)).grid(column=1, row=5, ipadx=2, ipady=2)
        alph20 = ttk.Button(gameRoot, text="T", command= lambda: guessLetter('T', word, gameRoot)).grid(column=2, row=5, ipadx=2, ipady=2)
        alph21 = ttk.Button(gameRoot, text="U", command= lambda: guessLetter('U', word, gameRoot)).grid(column=3, row=5, ipadx=2, ipady=2)
        alph22 = ttk.Button(gameRoot, text="V", command= lambda: guessLetter('V', word, gameRoot)).grid(column=4, row=5, ipadx=2, ipady=2)
        alph23 = ttk.Button(gameRoot, text="W", command= lambda: guessLetter('W', word, gameRoot)).grid(column=5, row=5, ipadx=2, ipady=2)
        alph24 = ttk.Button(gameRoot, text="X", command= lambda: guessLetter('X', word, gameRoot)).grid(column=6, row=5, ipadx=2, ipady=2)
        alph25 = ttk.Button(gameRoot, text="Y", command= lambda: guessLetter('Y', word, gameRoot)).grid(column=7, row=5, ipadx=2, ipady=2)
        alph26 = ttk.Button(gameRoot, text="Z", command= lambda: guessLetter('Z', word, gameRoot)).grid(column=8, row=5, ipadx=2, ipady=2)
        
        # Button for guessing
        submit = ttk.Button(gameRoot, text="Guess", command=lambda: makeGuess(word)).grid(column=9, row=5, ipadx=2, ipady=2)

    except:
        loadError()
    print("single player")

def multiplayer(playerMadeWord):
    try:
        print("multiplayer")

        mpRoot = Tk()
        mpFrame = ttk.Frame(mpRoot, padding=20)
        mpGrid = mpFrame.grid()

        # Set default size of game window
        mpRoot.geometry("1240x640")

        # Make sure the word is in the correct format
        punctuation = '!"#$%^&*()_-=+\':;<>@/[\\]{\}`~0123456789\t\n\r\x0b\x0c'
        word = playerMadeWord.strip(punctuation).lower()

        # Create letter spaces for the new word
        j = 1
        i = 1
        if len(word) > 9:
            whitespace1 = ttk.Label(mpRoot, text="\t\t").grid(column=0, row=1)
        else:
            whitespace2 = ttk.Label(mpRoot, text="\t\t\t\t").grid(column=0, row=1)
        for letter in word:
            label1 = ttk.Label(mpRoot, text="_____").grid(column=i, row=j)
            i += 1

        # Create buttons for each letter
        alph1 = ttk.Button(mpRoot, text="A", command= lambda: guessLetter('A', word, mpRoot)).grid(column=1, row=2, ipadx=2, ipady=2)
        alph2 = ttk.Button(mpRoot, text="B", command= lambda: guessLetter('B', word, mpRoot)).grid(column=2, row=2, ipadx=2, ipady=2)
        alph3 = ttk.Button(mpRoot, text="C", command= lambda: guessLetter('C', word, mpRoot)).grid(column=3, row=2, ipadx=2, ipady=2)
        alph4 = ttk.Button(mpRoot, text="D", command= lambda: guessLetter('D', word, mpRoot)).grid(column=4, row=2, ipadx=2, ipady=2)
        alph5 = ttk.Button(mpRoot, text="E", command= lambda: guessLetter('E', word, mpRoot)).grid(column=5, row=2, ipadx=2, ipady=2)
        alph6 = ttk.Button(mpRoot, text="F", command= lambda: guessLetter('F', word, mpRoot)).grid(column=6, row=2, ipadx=2, ipady=2)
        alph7 = ttk.Button(mpRoot, text="G", command= lambda: guessLetter('G', word, mpRoot)).grid(column=7, row=2, ipadx=2, ipady=2)
        alph8 = ttk.Button(mpRoot, text="H", command= lambda: guessLetter('H', word, mpRoot)).grid(column=8, row=2, ipadx=2, ipady=2)
        alph9 = ttk.Button(mpRoot, text="I", command= lambda: guessLetter('I', word, mpRoot)).grid(column=9, row=2, ipadx=2, ipady=2)
        alph11 = ttk.Button(mpRoot, text="K", command= lambda: guessLetter('K', word, mpRoot)).grid(column=2, row=3, ipadx=2, ipady=2)
        alph10 = ttk.Button(mpRoot, text="J", command= lambda: guessLetter('J', word, mpRoot)).grid(column=1, row=3, ipadx=2, ipady=2)
        alph12 = ttk.Button(mpRoot, text="L", command= lambda: guessLetter('L', word, mpRoot)).grid(column=3, row=3, ipadx=2, ipady=2)
        alph13 = ttk.Button(mpRoot, text="M", command= lambda: guessLetter('M', word, mpRoot)).grid(column=4, row=3, ipadx=2, ipady=2)
        alph14 = ttk.Button(mpRoot, text="N", command= lambda: guessLetter('N', word, mpRoot)).grid(column=5, row=3, ipadx=2, ipady=2)
        alph15 = ttk.Button(mpRoot, text="O", command= lambda: guessLetter('O', word, mpRoot)).grid(column=6, row=3, ipadx=2, ipady=2)
        alph16 = ttk.Button(mpRoot, text="P", command= lambda: guessLetter('P', word, mpRoot)).grid(column=7, row=3, ipadx=2, ipady=2)
        alph17 = ttk.Button(mpRoot, text="Q", command= lambda: guessLetter('Q', word, mpRoot)).grid(column=8, row=3, ipadx=2, ipady=2)
        alph18 = ttk.Button(mpRoot, text="R", command= lambda: guessLetter('R', word, mpRoot)).grid(column=9, row=3, ipadx=2, ipady=2)
        alph20 = ttk.Button(mpRoot, text="T", command= lambda: guessLetter('T', word, mpRoot)).grid(column=2, row=4, ipadx=2, ipady=2)
        alph19 = ttk.Button(mpRoot, text="S", command= lambda: guessLetter('S', word, mpRoot)).grid(column=1, row=4, ipadx=2, ipady=2)
        alph21 = ttk.Button(mpRoot, text="U", command= lambda: guessLetter('U', word, mpRoot)).grid(column=3, row=4, ipadx=2, ipady=2)
        alph22 = ttk.Button(mpRoot, text="V", command= lambda: guessLetter('V', word, mpRoot)).grid(column=4, row=4, ipadx=2, ipady=2)
        alph23 = ttk.Button(mpRoot, text="W", command= lambda: guessLetter('W', word, mpRoot)).grid(column=5, row=4, ipadx=2, ipady=2)
        alph24 = ttk.Button(mpRoot, text="X", command= lambda: guessLetter('X', word, mpRoot)).grid(column=6, row=4, ipadx=2, ipady=2)
        alph25 = ttk.Button(mpRoot, text="Y", command= lambda: guessLetter('Y', word, mpRoot)).grid(column=7, row=4, ipadx=2, ipady=2)
        alph26 = ttk.Button(mpRoot, text="Z", command= lambda: guessLetter('Z', word, mpRoot)).grid(column=8, row=4, ipadx=2, ipady=2)
        
        # Button for guessing
        submit = ttk.Button(mpRoot, text="Guess", command= lambda: makeGuess(word)).grid(column=9, row=4, ipadx=2, ipady=2)
    except:
        loadError()

def enterWord():
    newWordRoot = Tk()
    newWordFrame = ttk.Frame(newWordRoot, padding=50)
    newWordGrid = newWordFrame.grid()

    # Label to explain
    label1 = ttk.Label(newWordRoot, text="Welcome!").grid(column=1, row=1, ipady=5, ipadx=5)
    label2 = ttk.Label(newWordRoot, text="Only use letters in the English Alphabet, no punctuation. (caps don't matter)").grid(column=2, row=1, ipady=5, ipadx=5)
    label3 = ttk.Label(newWordRoot, text="\tEnter word here:").grid(column=1, row=2, ipady=5, ipadx=5)

    # Entry for user to type in
    entry1 = ttk.Entry(newWordRoot)
    entry1.grid(column=2, row=2, ipady=5, ipadx=5)

    # Button to log entry and exit window
    newWord = ""
    entrySubmit = ttk.Button(newWordRoot, text="Submit", command= lambda: saveWord()).grid(column=3, row=2, ipady=5, ipadx=5)

    def saveWord():
        newWord = entry1.get()
        newWordRoot.destroy()
        multiplayer(newWord)

def guessLetter(letter, word, root):
    print(letter)
    match = False
    index = 0
    print(word)
    for letters in word:
        if letter.lower() == letters:
            showLetter(letter, index, root)
            match = True
        index += 1
    if match == False:
        failedLetterGuess(letter, root)

def showLetter(letter, index, root):
    # Print the correct letter above the lines placed earlier
    whitespace = ttk.Label(root, text="\t\t\t\t").grid(column=0, row=0)
    label = ttk.Label(root, text=letter).grid(column=index+1, row=0)

# global var for imgs to be displayed
arms = 0
legs = 0
base = 0
head = 0
body = 0
attempts = 1

def failedLetterGuess(letter, root):
    print("failed letter: " + letter)
    global base, body, head, arms, legs, attempts
    # Make failed attempts variable to track which pics have already been displayed and which ones need to still be displayed
    if base == 0:
        print("display base")
        base += 1
    elif head == 0:
        print("display head")
        head += 1
    elif body == 0:
        print("display body")
        body += 1
    elif arms == 0:
        print("display right arm")
        arms += 1
    elif legs == 0:
        print("display right leg")
        legs += 1
    elif arms == 1:
        print("display left arm")
        arms += 1
    elif legs == 1:
        print("display left leg")
        legs += 1
    # Display each letter as a guessed wrong letter (may need to be done where the root is created so it can be added to)
    label = ttk.Label(root, text=letter).grid(column=attempts, row=7, ipady=20, ipadx=5)
    attempts += 1
    

def makeGuess(word):
    print("guessing")
    guessRoot = Tk()
    guessFrame = ttk.Frame(guessRoot, padding=50)
    guessGrid = guessFrame.grid()

    # Label to explain
    label1 = ttk.Label(guessRoot, text="Ready to answer?").grid(column=1, row=1, ipady=5, ipadx=5)
    label2 = ttk.Label(guessRoot, text="Only use letters in the English Alphabet, no punctuation. (caps don't matter)").grid(column=2, row=1, ipady=5, ipadx=5)
    label3 = ttk.Label(guessRoot, text="\tEnter word here:").grid(column=1, row=2, ipady=5, ipadx=5)

    # Entry for user to type in
    entry1 = ttk.Entry(guessRoot)
    entry1.grid(column=2, row=2, ipady=5, ipadx=5)

    # Button to log entry and exit window
    entrySubmit = ttk.Button(guessRoot, text="Submit", command=lambda: saveGuess()).grid(column=3, row=2, ipady=5, ipadx=5)

    def saveGuess():
        guessedWord = entry1.get()
        guessRoot.destroy()
        guessed(guessedWord, word)

def guessed(guessed, word):
    if(guessed.lower() == word.lower()):
        winner()
    else:
        incorrect()

def winner():
    winnerRoot = Tk()
    winnerFrame = ttk.Frame(winnerRoot, padding=100)
    winnerGrid = winnerFrame.grid()

    # Label to explain
    label1 = ttk.Label(winnerRoot, font=("Arial", 32), text="YOU WON").grid(column=1, row=1, ipady=5, ipadx=5)

    # Button to exit window
    exitButton = ttk.Button(winnerRoot, text="Exit", command=winnerRoot.destroy).grid(column=1, row=2, ipady=5, ipadx=5)

def incorrect():
    incorrectRoot = Tk()
    incorrectFrame = ttk.Frame(incorrectRoot, padding=100)
    incorrectGrid = incorrectFrame.grid()

    # Label to explain
    label1 = ttk.Label(incorrectRoot, text="You were incorrect in this guess!").grid(column=1, row=1, ipady=5, ipadx=5)

    # Button to log entry and exit window
    guessedWord = ""
    entrySubmit = ttk.Button(incorrectRoot, text="Got it!", command=incorrectRoot.destroy).grid(column=3, row=2, ipady=5, ipadx=5)

def loadError():
    # display error message to user
    eRoot = Tk()
    eFrame = ttk.Frame(eRoot, padding=20)
    eGrid = eFrame.grid()
    eRoot.geometry("350x100")
    eLabel = ttk.Label(eFrame, text="Loading error. Please restart the application.").grid(column=1, row=0)
    eBtn = ttk.Button(eFrame, text="Close", command=eRoot.destroy).grid(column=1, row=1)

def wordError():
    # display error message to user
    weRoot = Tk()
    weFrame = ttk.Frame(weRoot, padding=20)
    weGrid = weFrame.grid()
    weRoot.geometry("350x100")
    eLabel = ttk.Label(weFrame, text="A word was entered with punctuation that is not permitted.").grid(column=1, row=0)
    eBtn = ttk.Button(weFrame, text="Close", command=weRoot.destroy).grid(column=1, row=1)

startup()