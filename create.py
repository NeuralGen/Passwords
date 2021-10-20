import random
import pyvariable
import time
import string

Numbers = [1,2,3,4,5,6,7,8,9,0] + list(string.ascii_lowercase)[10:17]

def randomize_capitalization(string):
    lst = list(string)
    for i in lst:
        num = random.randint(0,1)
        if num == 0:
            lst[lst.index(i)] = i.lower()
        else:
            lst[lst.index(i)] = i.upper()
        time.sleep(random.randint(1, 4)/10)

    for i in lst:
        if i == " ":
            lst[lst.index(i)] = "_"

    lst.insert(0, "_")
    lst.append("_")
            
    randomized = "".join(lst)
    return randomized


def makeItDifficult(string):
    if len(list(string)) < 3:
        n = 4
    else:
        n = random.randint(2,6)
    lst = list(string)
    for i in range(n):
        num = random.randint(0,1)
        if num == 0:
            lst.insert(0, random.choice(Numbers))
        else: lst.append(random.choice(Numbers))
        time.sleep(random.choice([0.1, 0.2]))

    for i in lst:
        lst[lst.index(i)] = str(i)

    return "".join(lst)


def create(name):
    return makeItDifficult(randomize_capitalization(name))



name = str(input("Enter a keyword: "))
print("")
while True:
    print("\nCreating...")
    passWord = create(name)
    print("New Password :  " + passWord)
    state = input("Do you like it? (y/n) : ").lower()[0]
    if state == "y":
        break


data = pyvariable.LocalVariable()
data.save(str(input("\nEnter a name for password : ")), passWord)
print("Password saved!")
