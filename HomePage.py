from tkinter import *
from tkinter import scrolledtext 
import os


class HomePage:

    exitPressed = False

    def __init__(self):
        
        self.root = Tk()

        #Set Screen size
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.title("SOCIAL INJUSTICE TRIVIA")

        #Declare Name Label
        self.nameLabel = Label(self.root, text = "Enter your name")
        self.nameLabel.place(x = 675, y = 425)

        #Declare Name input Box
        self.nameInput = Entry(self.root)
        self.nameInput.place(x = 650, y = 450)

        #Declare PLay button
        self.playButton = Button(self.root, text = "PLAY", command = self.startGame)
        self.playButton.place(x = 700, y = 525)

        #Declare Header Label
        self.headerLabel = Label(self.root, text = "WELCOME TO THE GAME", bg = "blue", height = 5, width = 75)
        self.headerLabel.place(x = 425, y = 100)

        #Declare Question Label
        instructions = '''
                          Welcome to the Social Injustice Trivia! In this game
                          you will answer questions about various social injustices in the world.
                          Every question that you answer correctly will earn you points,
                          with each question being worth more than the last. The game ends when you
                          incorrectly answer a question. Good luck!
                        '''


        self.questionLabel = Label(self.root, text = instructions, wraplength = 600, justify = "center", height = 5, width = 75, bg = "gray")
        self.questionLabel.place(x = 425, y = 300)
        
        #Declare Leaderboard
        self.leaderboard = scrolledtext.ScrolledText(self.root, wrap = WORD,  width = 50,  height = 10) 

        f = open("Scores.txt", 'r')
        mylist = f.readlines()
        for i in mylist:
            i.strip('\n')


        names = []
        points = []

        for line in mylist:
            for c in line.split():
                if c.isalpha():
                    names.append(c)
                elif c.isnumeric():
                    points.append(c)
        
        f.close()

        while len(points) > 0:
            maxPoint = max(points)
            self.leaderboard.insert(INSERT, names[points.index(maxPoint)] + "\t" +str(maxPoint)+ "\n")
            names.remove(names[points.index(maxPoint)])
            points.remove(maxPoint)



        self.leaderboard.config(state=DISABLED)
        self.leaderboard.place(x = 575, y = 650)

        #Declare Leaderboard Label
        self.leaderboardLabel = Label(self.root, text = "LEADERBOARD", font = ("Times New Roman", 30), bg= 'gray', fg = "black")
        self.leaderboardLabel.place(x = 625, y = 600)
        
        #Main loop
        self.root.mainloop()

    def clicked(self):
        self.nextButton.place(x = 750, y = 650)
        self.nextButton.pack()

    def startGame(self):        
        if self.nameInput.get() == "":
            self.invalidName = Label(self.root, text = "*Invalid Name*", fg = "red")
            self.invalidName.place(x = 670, y = 485)

        else:
            playGame = True
            self.name = self.nameInput.get()
            self.root.destroy()