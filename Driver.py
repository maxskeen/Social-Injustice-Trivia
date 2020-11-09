import random
import Screen
import HomePage

#Possible answer choices (4 per dictionary)
answers = [{"Native Americans": True, "African Americans": False, "Hispanics": False, "Jews": False},
           {"Jim Crow Laws": True, "National Defense Education Act": False, "Civil Right act": False, "Bob Laser Law": False},
           {"Black Lives Matter Movement": True, "LGBTQ+ Rights": False, "Support of Immigration": False, "Voter Rights": False},
           {"19th Amendment": True, "13th Amendment": False, "18th Amendment": False, "21 Amendment": False},
           {"Rwanda": True, "Kenya": False, "Nigeria": False, "Sudan": False},
           {"I.C.E": True, "D.A.C.A": False, "T.S.A": False, "F.B.I": False},
           {"Uyghur Muslims": True, "Buddhists": False, "Indo-Persians": False, "Chinese Catholics": False},
           {"600k-800k": True, "300k-500k": False, "900k-1mil": False, "100k-300k": False},
           {"Stonewall Inn": True, "The Green Mill": False, "The Pulse Knight Club": False, "Sazerac Bar": False},
           {"46¢": True, "40¢": False, "51¢": False, "33¢": False}
]

#Our questions
questions = ["The Trail of Tears was a mass removal of which ethnic group from their land in North America as colonizers overtook it?",
             "What was the name of the law(s) that was used to segregate African Americans from Caucasians in America?",
             "George Floyd's death in early 2020 caused nationwide protests in support of which movement?",
             "What was the amendment that gave women the right to vote?",
             "In what coutry did the Hutu slaughter nearly 1 million members of the Tutsi tribe in the early 90's?",
             "What is the name of the governmental body that has been criticized in the past due to harsh treatment of undocumented Hispanic immigrants?",
             "Which ethnoreligious culture is being forced into detention camps and forced into suppression in China?",
             "About how many men, women, and children are trafficked across international borders yearly?",
             "What was the name of the bar in which police raided in the late 60's which incited the namesake riotes performed by the LGBTQ community in New York City?",
             "The wage difference between white men and Hispanic women is about how many cents per dollar?"
]

#Reasonings for the correct answer 
explainations = ["Answer: Native Americans\nIn 1838 and 1839, as part of Andrew Jackson's Indian removal policy, the Cherokee nation was forced to give up its lands east of the Mississippi River and to migrate to an area in present-day Oklahoma.",
                 "Answer: Jim Crow Laws\nJim Crow Laws were legalized in America around 1865 right after the 13th amendment was ratified. This law would remain in effect for another 100 years until the supreme court ruled that in the case \"Brown v. Board of Education,\" that the educational segregation was unconstitutional.",
                 "Answer: Black Lives Matter Movement\nAn international social movement, formed in the United States in 2013, dedicated to fighting racism and anti-Black violence, especially in the form of police brutality. In the case of George Floyd's death, the movement became globally known and inspired many members of the community and the world to act upon anti-racists.",
                 "Answer: 19th Amendment\nOn May 21, 1919, after the Women's suffrage movement the house found that women should have the right to vote. The senate soon followed suit after two weeks of deliberation, giving a better and equal social equality to men and women of America.",
                 "Answer: Rwanda\nIn the span of just 100 days of gunfire, this mass genocide created mass revolutions and multiple wars between the Hutus and the Rwandan Patriotic Front, RPF. Through these sets of events, today's Rwanda is governed by President Kagame who throughout his years in office has changed policies throughout the country using the UN Security Council to expedite the process of prosecuting the mass genocide members in 2002.",
                 "Answer: I.C.E.\nThe Immigration and Customs Enforcement's mission is to protect America from the cross-border crime and illegal immigration that threatens national security. As reported by the New York Times, \"Local law enforcement officials have refused to cooperate with their office’s investigations because of the politics of immigration.\" In light of this situation, government agencies are trying to dissolve the agency because of the lack of empathy and handling of immigrants.",
                 "Answer: Uyghur Muslims\nFor an unknown amount of time, the Uyghur Muslim culture has to follow strict rules on birthrate. In the objection of getting an abortion or taking Birth control parameters, they are moved to these camps where they are either removed, or worse, killed. In spite of these measures, the UN defines this measure as a possible cultural genocide, \"where action should be implemented soon,\" says Adrian Zenz in an NPR interview.",
                 "Answer: 600k-800k\nOf the 600 to 800 thousand traffics, 70 percent are female and 50 percent are children, all of which were forced with the means of either debt bondage or slavery. In response to high numbers of trafficking, The U.S. Government issued the Victim of Trafficking and Violence Protection Act of 2000 and reauthorized this act in 2003 in order to have a better handle on the situation.",
                 "Answer: Stonewall Inn\nIn the 1960s through the late 2000s, LGBTQ rights were not upheld to the standard that they are today. Being able to hold hands, dance with, or even have any other physical contact with the same sex was illegal. In the case of The Stonewall Inn, LGBTQ patrons were not allowed to be served alcohol until later when protesters found this denial of service unlawful. Today there are many LGBT rights organizations which protect members from further discrmination such as the GLAAD, Human Rights Campaign, and PFlag. Due to these organizations' efforts, the legalization of same-sex marriage has also been implemented by former President Barack Obama in 2015.",
                 "Answer: 46¢\nDuring the time from 2018 to 2020, a study was found that although the wage difference between White Men and Hispanic Women is 46 cents, this gap is expected to increase to up to $1,121,440 within 40 years. Many activists are working diligently to equalize the wages between all races."
]

#Point System
points = [100, 2000, 5000, 25000, 50000, 75000, 100000, 250000, 500000, 1000000]

#Randomizes Answers
btn1 = 0
btn2 = 0
btn3 = 0
btn4 = 0
list1 = []


def run():
    x = HomePage.HomePage()
    name = x.name
    play(name)


def play(name):
    prizeMoney = 0
    i = 1
    #Randomizes Answers and Assigns True boolean to correct answer
    for choices in answers:
        for answer in choices:
            a = random.randint(1, 4)

            while a in list1:
                a = random.randint(1, 4)

            if a == 1:
                if len(list1)==0:
                    ansBtn1 = True 
                else:
                    ansBtn1 = False
                btn1 = answer
            elif a == 2:
                if len(list1)==0:
                    ansBtn2 = True 
                else:
                    ansBtn2 = False
                btn2 = answer
            elif a == 3:
                if len(list1)==0:
                    ansBtn3 = True 
                else:
                    ansBtn3 = False
                btn3 = answer
            elif a == 4:
                if len(list1)==0:
                    ansBtn4 = True 
                else:
                    ansBtn4 = False
                btn4 = answer

            list1.append(a)
        list1.clear()
        #Creates Screen
        b = Screen.Screens(i, name, prizeMoney, explainations[i-1], questions[i-1], btn1, ansBtn1, btn2, ansBtn2, btn3, ansBtn3, btn4, ansBtn4)
        if not b.nextPressed:
            return prizeMoney
        prizeMoney = points[i-1]
        if prizeMoney == 1000000:
            f = open('Scores.txt', 'a')
            f.write('\n' + name + ' '+str(prizeMoney))
            f.close()
        i += 1
    return prizeMoney
    
run()