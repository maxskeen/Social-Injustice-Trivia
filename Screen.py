import time
from tkinter import *
import HomePage

class Screens:

    nextPressed = False

    def __init__(self, qNum, playerName, prizeMoney, explanation, question, btn1txt, btn1ans, btn2txt, btn2ans, btn3txt, btn3ans, btn4txt, btn4ans):
        
        self.root = Tk()
        self.nextPressed = False
        self.playerName = playerName
        self.playerInfo = playerName + ': $' + str(prizeMoney)
        self.btn1ans = btn1ans
        self.btn2ans = btn2ans
        self.btn3ans = btn3ans
        self.btn4ans = btn4ans
        self.qNum = qNum
        index = 1
        self.points = [100, 2000, 5000, 25000, 50000, 75000, 100000, 250000, 500000, 1000000]
        self.cashWon = 0
        self.prizeMoney = prizeMoney

        #Set Screen size
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.title("SOCIAL INJUSTICE TRIVIA")
        self.root.configure(bg = 'grey')

        #Declare Answer Choice Buttons
        self.btn1 = Button(self.root, text = btn1txt, command = self.clicked1, height = 5, width = 25)
        self.btn1.place(x = 500, y = 575)

        self.btn2 = Button(self.root, text = btn2txt, command = self.clicked2, height = 5, width = 25)
        self.btn2.place(x = 750, y = 575)

        self.btn3 = Button(self.root, text = btn3txt, command = self.clicked3, height = 5, width = 25)
        self.btn3.place(x = 500, y = 650)

        self.btn4 = Button(self.root, text = btn4txt, command = self.clicked4, height = 5, width = 25)
        self.btn4.place(x = 750, y = 650)

        #Declare Next Button
        self.nextButton = Button(self.root, text = "Next", height = 5, width = 10, command = self.nextScreen)

        #Declare Exit Button
        self.exitButton = Button(self.root, text = "Exit", height = 5, width = 10, command = self.exitScreen)

        #Declare Header Label
        self.headerLabel = Label(self.root, text = "Question: " + str(qNum), wraplength = 500, justify = 'center', bg = "blue", height = 5, width = 75, fg = 'white')
        self.headerLabel.place(x = 425, y = 100)

        #Declare Question Label
        self.questionLabel = Label(self.root, text = question, wraplength = 500, justify = 'center', height = 5, width = 75, bg = "blue", fg = 'white')
        self.questionLabel.place(x = 425, y = 450)

        #Declare Explanation Label
        self.explanationLabel = Label(self.root, text = explanation, wraplength = 500, justify = 'center', height = 10, width = 75, bg = 'red', fg = 'white')

        #Declares Player's Name and cash takeaway
        self.player = Label(self.root, 
                            text = self.playerInfo, 
                            font = ('Copperplate Gothic', 20), 
                            bg = 'black', 
                            fg = 'white'
        )
        self.player.place(x=1, y = 1)
        self.player = Listbox(self.root,
                              height = 10,
                              width = 15,
                              bg = 'black',
                              fg = 'white',
                              font = ('Copperplate Gothic', 20)
        )
        self.player.place(x=1240, y = 1)
        for i in self.points[::-1]:
            if len(self.points)-index+1 == 10:
                self.player.insert(index, str(len(self.points)-index+1)+'  $'+str(i))
            else:
                self.player.insert(index, '   '+str(len(self.points)-index+1)+'  $'+str(i))
            index+=1
        for j in range(9, 9-qNum, -1):
            if 10-j==qNum:
                self.player.itemconfig(j, fg='#DC143C') #change to crimson red
            else:
                self.player.itemconfig(j, fg='#32CD32') #change to lime green
            

        #Main loop
        self.root.mainloop()

    def clicked1(self):
        if self.btn1ans:
            self.nextButton.place(x = 750, y = 650)
            self.nextButton.pack()
            self.explanationLabel.place(x=425, y = 250)
        else:
            self.exitButton.place(x = 750, y = 650)
            self.exitButton.pack()
            self.explanationLabel.place(x=425, y = 250)

    
    def clicked2(self):
        if self.btn2ans:
            self.nextButton.place(x = 750, y = 650)
            self.nextButton.pack()
            self.explanationLabel.place(x=425, y = 250)
        else:
            self.exitButton.place(x = 750, y = 650)
            self.exitButton.pack()
            self.explanationLabel.place(x=425, y = 250)

    def clicked3(self):
        if self.btn3ans:
            self.nextButton.place(x = 750, y = 650)
            self.nextButton.pack()
            self.explanationLabel.place(x=425, y = 250)
        else:
            self.exitButton.place(x = 750, y = 650)
            self.exitButton.pack()
            self.explanationLabel.place(x=425, y = 250)

    def clicked4(self):
        if self.btn4ans:
            self.nextButton.place(x = 750, y = 650)
            self.nextButton.pack()
            self.explanationLabel.place(x=425, y = 250)
        else:
            self.exitButton.place(x = 750, y = 650)
            self.exitButton.pack()
            self.explanationLabel.place(x=425, y = 250)


    def nextScreen(self):
        self.nextPressed = True
        self.root.destroy()
    
    def exitScreen(self):
        f = open('Scores.txt', 'a')
        f.write('\n' + self.playerName + ' '+str(self.points[self.qNum-2]))
        f.close()
        self.root.destroy()