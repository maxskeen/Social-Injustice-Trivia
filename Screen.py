from tkinter import *

class Screens:

    nextPressed = False

    def __init__(self, qNum):
        
        self.root = Tk()

        #Set Screen size
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        #self.root.geometry("1920x1080")
        self.root.title("SOCIAL INJUSTICE TRIVIA")

        self.qNum = qNum

        #Declare Answer Choice Buttons
        self.btn1 = Button(self.root, text = "Button 1", command = self.clicked, height = 5, width = 25)
        self.btn1.place(x = 500, y = 575)

        self.btn2 = Button(self.root, text = "Button 2", command = self.clicked, height = 5, width = 25)
        self.btn2.place(x = 750, y = 575)

        self.btn3 = Button(self.root, text = "Button 3", command = self.clicked, height = 5, width = 25)
        self.btn3.place(x = 500, y = 650)

        self.btn4 = Button(self.root, text = "Button 4", command = self.clicked, height = 5, width = 25)
        self.btn4.place(x = 750, y = 650)

        #Declare Next Button
        self.nextButton = Button(self.root, text = "Next", height = 5, width = 10, command = self.nextScreen)

        #Declare Header Label
        self.headerLabel = Label(self.root, text = "Question: " + str(qNum), bg = "blue", height = 5, width = 75)
        self.headerLabel.place(x = 425, y = 100)

        #Declare Question Label
        self.questionLabel = Label(self.root, text = 'HELLO', height = 5, width = 75, bg = "blue")
        self.questionLabel.place(x = 425, y = 450)

        #Main loop
        self.root.mainloop()

    def clicked(self):
        print("I click")
        self.nextButton.place(x = 750, y = 650)
        self.nextButton.pack()

    def nextScreen(self):
        nextPressed = True
        self.root.destroy()