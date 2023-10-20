
import random
comp= random.randint(1,3)
w=0
t=0
o=0
user=input("computer:rock(r) paper(p) and scissors(s)? \n you:rock(r) paper(p) and scissors(s)? ")

if comp==1:                          #rock paper scissor-- aj<a>y--
    comp="r"
    t="rock"
elif comp==2:
    comp="p"
    t="paper"
elif comp==3:
    comp="s"
    t="scissors"
else:
    comp="none"



if comp==user:
    print(comp,"=",user,"Game Tie")


elif comp=="r":
    if user=="p":
        w=2 
        o="paper"
    elif user=="s":
        w=1 
        o="scissors"
         
elif comp=="p":
    if user=="r":
        w=1
        o="rock"
    elif user=="s":
        w=2
        o="scissors"
elif comp=="s":
    if user=="r":
        w=2
        o="rock"
    elif user=="p":
        w=1
        o="paper"  

       
else:
    print("invalid")

l=o

print("computers choice = ",t) 
print("your choice = ",l)  



if w==1:
    print("COMPUTER WON")

elif w==2:
    print("YOU WON") 

      
    