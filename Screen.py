from tkinter import *

class Screen:

    def __init__(self, root, qNum):

        #Set Screen size
        root.geometry("1920x1080")
        root.title("SOCIAL INJUSTICE TRIVIA")

        self.qNum = qNum

        #Declare Answer Choice Buttons
        self.btn1 = Button(root, text = "Hfef", command = self.clicked, height = 25, width = 25)
        self.btn1.place(x = 500, y = 100)
        #self.btn1.pack()

        self.btn2 = Button(root, text = "fe")
        self.btn2.pack()
        self.btn3 = Button(root, text = "ef")
        self.btn3.pack()
        self.btn4 = Button(root, text = "ef")
        self.btn4.pack()

        #Declare Next Button
        self.nextButton = Button(root, text = "")
        self.nextButton.pack()

        #Declare Header Label
        self.headerLabel = Label(root, text = "Question: " + str(qNum))
        self.headerLabel.pack(side = "top")

        #Declare Question Label
        self.questionLabel = Label(root, text = '')
        self.questionLabel.pack()

        #Main loop
        root.mainloop()

    def clicked(self):
        print("I click")


    #d = {"1800": False, "1900": True}