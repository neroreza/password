import string
import random
# ----------------
# code

def createdpass(lentghpass):
    paslist = []
    pas = string.ascii_letters + string.digits + "/*-+=-)(&^%$#@!~/><|"
    for _ in range( lentghpass):
        password = random.choice(pas)
        paslist.append(password)

    finalpass = "".join(paslist)
    print(finalpass)

# for replay

while True:
    lentgh=int(input("pleas enter lentgh of password  :  "))
    createdpass(lentgh)
    quiz= input(" do you want a nother password ? (y/n)")
    if quiz.lower()=="y":
        continue
    else :
        break

