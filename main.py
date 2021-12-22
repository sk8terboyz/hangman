
from tkinter import ttk
from tkinter import *
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
        
        # Create letter spaces for the new word
        word = "letters"
        punctuation = "`~!@#$%^&*()_-+='\"[]{\};:/?.>,<0123456789"
        j, i = 1
        if len(word) > 9:
            i = 0
        for letter in word:
            if(letter in punctuation):
                wordError()
                break
            else:
                print("good")
                label1 = ttk.Label(gameRoot, text="__").grid(column=i, row=j)
                i += 1

        # Create buttons for each letter
        alph1 = ttk.Button(gameRoot, text="A", command= lambda: guessLetter('A')).grid(column=1, row=3, ipadx=2, ipady=2)
        alph2 = ttk.Button(gameRoot, text="B", command= lambda: guessLetter('B')).grid(column=2, row=3, ipadx=2, ipady=2)
        alph3 = ttk.Button(gameRoot, text="C", command= lambda: guessLetter('C')).grid(column=3, row=3, ipadx=2, ipady=2)
        alph4 = ttk.Button(gameRoot, text="D", command= lambda: guessLetter('D')).grid(column=4, row=3, ipadx=2, ipady=2)
        alph5 = ttk.Button(gameRoot, text="E", command= lambda: guessLetter('E')).grid(column=5, row=3, ipadx=2, ipady=2)
        alph6 = ttk.Button(gameRoot, text="F", command= lambda: guessLetter('F')).grid(column=6, row=3, ipadx=2, ipady=2)
        alph7 = ttk.Button(gameRoot, text="G", command= lambda: guessLetter('G')).grid(column=7, row=3, ipadx=2, ipady=2)
        alph8 = ttk.Button(gameRoot, text="H", command= lambda: guessLetter('H')).grid(column=8, row=3, ipadx=2, ipady=2)
        alph9 = ttk.Button(gameRoot, text="I", command= lambda: guessLetter('I')).grid(column=9, row=3, ipadx=2, ipady=2)
        alph10 = ttk.Button(gameRoot, text="J", command= lambda: guessLetter('J')).grid(column=1, row=4, ipadx=2, ipady=2)
        alph11 = ttk.Button(gameRoot, text="K", command= lambda: guessLetter('K')).grid(column=2, row=4, ipadx=2, ipady=2)
        alph12 = ttk.Button(gameRoot, text="L", command= lambda: guessLetter('L')).grid(column=3, row=4, ipadx=2, ipady=2)
        alph13 = ttk.Button(gameRoot, text="M", command= lambda: guessLetter('M')).grid(column=4, row=4, ipadx=2, ipady=2)
        alph14 = ttk.Button(gameRoot, text="N", command= lambda: guessLetter('N')).grid(column=5, row=4, ipadx=2, ipady=2)
        alph15 = ttk.Button(gameRoot, text="O", command= lambda: guessLetter('O')).grid(column=6, row=4, ipadx=2, ipady=2)
        alph16 = ttk.Button(gameRoot, text="P", command= lambda: guessLetter('P')).grid(column=7, row=4, ipadx=2, ipady=2)
        alph17 = ttk.Button(gameRoot, text="Q", command= lambda: guessLetter('Q')).grid(column=8, row=4, ipadx=2, ipady=2)
        alph18 = ttk.Button(gameRoot, text="R", command= lambda: guessLetter('R')).grid(column=9, row=4, ipadx=2, ipady=2)
        alph19 = ttk.Button(gameRoot, text="S", command= lambda: guessLetter('S')).grid(column=1, row=5, ipadx=2, ipady=2)
        alph20 = ttk.Button(gameRoot, text="T", command= lambda: guessLetter('T')).grid(column=2, row=5, ipadx=2, ipady=2)
        alph21 = ttk.Button(gameRoot, text="U", command= lambda: guessLetter('U')).grid(column=3, row=5, ipadx=2, ipady=2)
        alph22 = ttk.Button(gameRoot, text="V", command= lambda: guessLetter('V')).grid(column=4, row=5, ipadx=2, ipady=2)
        alph23 = ttk.Button(gameRoot, text="W", command= lambda: guessLetter('W')).grid(column=5, row=5, ipadx=2, ipady=2)
        alph24 = ttk.Button(gameRoot, text="X", command= lambda: guessLetter('X')).grid(column=6, row=5, ipadx=2, ipady=2)
        alph25 = ttk.Button(gameRoot, text="Y", command= lambda: guessLetter('Y')).grid(column=7, row=5, ipadx=2, ipady=2)
        alph26 = ttk.Button(gameRoot, text="Z", command= lambda: guessLetter('Z')).grid(column=8, row=5, ipadx=2, ipady=2)
        
        # Button for guessing
        submit = ttk.Button(gameRoot, text="Guess", command=makeGuess).grid(column=9, row=4, ipadx=2, ipady=2)

        # Display hanging stand
        # canvas = Canvas(gameRoot, width = 640, height = 480).grid(column=0, row=0)
        # base = ImageTk.PhotoImage(Image.open("/imgs/base.png"))
        # canvas.create_image(20, 20, anchor=NW, image=base)

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

        # Create letter spaces for the new word

        # Create buttons for each letter
        alph1 = ttk.Button(mpRoot, text="A", command= lambda: guessLetter('A')).grid(column=1, row=2, ipadx=2, ipady=2)
        alph2 = ttk.Button(mpRoot, text="B", command= lambda: guessLetter('B')).grid(column=2, row=2, ipadx=2, ipady=2)
        alph3 = ttk.Button(mpRoot, text="C", command= lambda: guessLetter('C')).grid(column=3, row=2, ipadx=2, ipady=2)
        alph4 = ttk.Button(mpRoot, text="D", command= lambda: guessLetter('D')).grid(column=4, row=2, ipadx=2, ipady=2)
        alph5 = ttk.Button(mpRoot, text="E", command= lambda: guessLetter('E')).grid(column=5, row=2, ipadx=2, ipady=2)
        alph6 = ttk.Button(mpRoot, text="F", command= lambda: guessLetter('F')).grid(column=6, row=2, ipadx=2, ipady=2)
        alph7 = ttk.Button(mpRoot, text="G", command= lambda: guessLetter('G')).grid(column=7, row=2, ipadx=2, ipady=2)
        alph8 = ttk.Button(mpRoot, text="H", command= lambda: guessLetter('H')).grid(column=8, row=2, ipadx=2, ipady=2)
        alph9 = ttk.Button(mpRoot, text="I", command= lambda: guessLetter('I')).grid(column=9, row=2, ipadx=2, ipady=2)
        alph10 = ttk.Button(mpRoot, text="J", command= lambda: guessLetter('J')).grid(column=1, row=3, ipadx=2, ipady=2)
        alph11 = ttk.Button(mpRoot, text="K", command= lambda: guessLetter('K')).grid(column=2, row=3, ipadx=2, ipady=2)
        alph12 = ttk.Button(mpRoot, text="L", command= lambda: guessLetter('L')).grid(column=3, row=3, ipadx=2, ipady=2)
        alph13 = ttk.Button(mpRoot, text="M", command= lambda: guessLetter('M')).grid(column=4, row=3, ipadx=2, ipady=2)
        alph14 = ttk.Button(mpRoot, text="N", command= lambda: guessLetter('N')).grid(column=5, row=3, ipadx=2, ipady=2)
        alph15 = ttk.Button(mpRoot, text="O", command= lambda: guessLetter('O')).grid(column=6, row=3, ipadx=2, ipady=2)
        alph16 = ttk.Button(mpRoot, text="P", command= lambda: guessLetter('P')).grid(column=7, row=3, ipadx=2, ipady=2)
        alph17 = ttk.Button(mpRoot, text="Q", command= lambda: guessLetter('Q')).grid(column=8, row=3, ipadx=2, ipady=2)
        alph18 = ttk.Button(mpRoot, text="R", command= lambda: guessLetter('R')).grid(column=9, row=3, ipadx=2, ipady=2)
        alph19 = ttk.Button(mpRoot, text="S", command= lambda: guessLetter('S')).grid(column=1, row=4, ipadx=2, ipady=2)
        alph20 = ttk.Button(mpRoot, text="T", command= lambda: guessLetter('T')).grid(column=2, row=4, ipadx=2, ipady=2)
        alph21 = ttk.Button(mpRoot, text="U", command= lambda: guessLetter('U')).grid(column=3, row=4, ipadx=2, ipady=2)
        alph22 = ttk.Button(mpRoot, text="V", command= lambda: guessLetter('V')).grid(column=4, row=4, ipadx=2, ipady=2)
        alph23 = ttk.Button(mpRoot, text="W", command= lambda: guessLetter('W')).grid(column=5, row=4, ipadx=2, ipady=2)
        alph24 = ttk.Button(mpRoot, text="X", command= lambda: guessLetter('X')).grid(column=6, row=4, ipadx=2, ipady=2)
        alph25 = ttk.Button(mpRoot, text="Y", command= lambda: guessLetter('Y')).grid(column=7, row=4, ipadx=2, ipady=2)
        alph26 = ttk.Button(mpRoot, text="Z", command= lambda: guessLetter('Z')).grid(column=8, row=4, ipadx=2, ipady=2)
        
        # Button for guessing
        submit = ttk.Button(mpRoot, text="Guess", command= lambda: makeGuess()).grid(column=9, row=4, ipadx=2, ipady=2)
    except:
        loadError()

def enterWord():
    print("Enter the word for others to guess")
    newWordRoot = Tk()
    newWordFrame = ttk.Frame(newWordRoot, padding=50)
    newWordGrid = newWordFrame.grid()

    # Label to explain
    label1 = ttk.Label(newWordRoot, text="Welcome!").grid(column=1, row=1, ipady=5, ipadx=5)
    label2 = ttk.Label(newWordRoot, text="Only use letters in the English Alphabet, no punctuation. (caps don't matter)").grid(column=2, row=1, ipady=5, ipadx=5)
    label3 = ttk.Label(newWordRoot, text="Enter word here:").grid(column=1, row=2, ipady=5, ipadx=5)

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

def guessLetter(letter):
    print(letter)

def makeGuess():
    print("guessing")

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