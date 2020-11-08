import Screen

points = 0
answers =  [{"1800": False, "1900": True, "1800": False, "1900": True},
            {"1800": False, "1900": True, "1800": False, "1900": True},
            {"1800": False, "1900": True, "1800": False, "1900": True},
            {"1800": False, "1900": True, "1800": False, "1900": True},
            {"1800": False, "1900": True, "1800": False, "1900": True},
            {"1800": False, "1900": True, "1800": False, "1900": True},
            {"1800": False, "1900": True, "1800": False, "1900": True},
            {"1800": False, "1900": True, "1800": False, "1900": True},
            {"1800": False, "1900": True, "1800": False, "1900": True},
            {"1800": False, "1900": True, "1800": False, "1900": True}]

questions = ["The Trail of Tears was a mass removal of which ethnic group from their land in North America as colonizers overtook it?",
             "What was the name of the law(s) that was used to segregate African Americans from Caucasians in America?",
             "George Floyd's death in early 2020 caused nationwide protests in support of which movement?",
             "4 What was the amendment that gave women the right to vote?",
             "In what coutry did the Hutu slaughter nearly 1 million members of the Tutsi tribe in the early 90's?",
             "What is the name of the governmental body that has been criticized in the past due to harsh treatment of undocumented Hispanic immigrants?",
             "Which ethnoreligious culture is being forced into detention camps and forced into suppression in China?",
             "About how many men, women, and children are trafficked across international borders yearly?",
             "What was the name of the bar in which police raided in the late 60's which incited the namesake riotes performed by the LGBTQ community in New York City?",
             "The wage difference between white men and Hispanic women is about how many cents per dollar?"
]


explainations = ["In 1838 and 1839, as part of Andrew Jackson's Indian removal policy, the Cherokee nation was forced to give up its lands east of the Mississippi River and to migrate to an area in present-day Oklahoma.",
                 "Jim Crow Laws were legilized in America around 1865 right after the 13th amendment was ratified. This law will remain in effect for another 100 years until the supreme court ruled that in the case \"Brown v. Board of Education,\" that the educational segregation was unconstitutional.",
                 "A international social movement, formed in the United States in 2013, dedicated to fighting racism and anti-Black violence, especially in the form of police brutality. In the case of George Floyd's death, the movement became globally know and inspired many memebers of the community and the world to act upon anti-racism acts.",
                 "On May 21, 1919 after the Womenes suffrage movement the house found that women should have the right to vote. The senate soon followed pursuit after 2 weeks to also create the amendment later giving a better and equal social equality to men and women of America.",
                 "","","","","",""]



def play():
    for i in range(1, 11):
        b = Screen.Screens(i)
        points += (points * 2)
    
play()

# window = tk.Tk()
# window.geometry('500x500')


# label = tk.Label(text = "Clicked")
# button = tk.Button(master, text = "Click me", command = callback)



# label.pack()
# button.pack()

# window.mainloop()