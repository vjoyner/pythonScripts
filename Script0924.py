#09/24/2019 Valarie Harrison
#Lecture Script

#Loop
#   WHILE loop
##i = 1
##while i<6:
##    print i
##    i = i+1 #i+=1
##
##print "out of while loop"
##
##var = [1,2,3,4,5,"apple"]
##for i in var:
##    print i
##
##var = ["banana","apple","kiwi"]
##for i in var:
##    print "kwon"
##
##print range(5)
##for i in range(5):
##    print "kwon", i
##
###for i in range (0,100,2)
##    
##print range(0,100,2)
##for i in range (0,10,2):
##    print "even number is", i

##i = 1
##while i < 6:
##    print "loop number",i
##    if i ==3:
##        break
##    print "after break",i
##    i += 1
##print "out of while"

##i = 1
##while i < 5:
##    print i
##    i += 1
##else:
##    print "this is else line"
##
##for i in range (5):
##    print i
##    if i ==3:
##        break
##
##for i in "python":
##    print i
##
##for i in "python":
##    print "kwon"

#review raw_input
import random
options = ["R","P","S"]
computerChoice = options[random.randrange(0,3)]
userChoice = raw_input("Let's play RPS game, type RPS")
while (computerChoice == "R"):
    if userChoice == "S":
        print "computer wins"
        break
    elif userChoice == "P":
        print "user win"
        break
    else:
        print "tie"
        break

while (computerChoice == "P"):
    if userChoice == "R":
        print "computer wins"
        break
    elif userChoice == "S":
        print "user win"
        break
    else:
        print "tie"
        break
    
while (computerChoice == "S"):
    if userChoice == "P":
        print "computer wins"
        break
    elif userChoice == "R":
        print "user win"
        break
    else:
        print "tie"
        break
