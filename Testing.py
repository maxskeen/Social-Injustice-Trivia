import random

#d = {"1800": False, "1900": True, "1800": False, "1900": True}

d = {True: "1800", False: "1850", False: "1900", False: "1950"}
button1 = 0
button2 = 0
button3 = 0
button4 = 0
list1 = []

for i in d.keys():
    

    a = random.randint(1, 4)

    while a in list1:
        a = random.randint(1, 4)
    
    if a == 1:
        button1 = d[i]
    elif a == 2:
        button2 = d[i]
    elif a == 3:
        button3 = d[i]
    elif a == 4:
        button4 = d[i]

    list1.append(a)

print(f"\n\n\n\nbutton1: {button1}")
print(f"button2: {button2}")
print(f"button3: {button3}")
print(f"button4: {button4}")



