#10/01/2019 Valarie Harrison
#Lecture

#Hi Ho! Cherry-O game simulation


import random

spinnerChoice = [-1,-2,-3,-4,+2,+2,+10]
cherryOnTree = 10


turns = 0
turns +=1

print turns

for i in range(100):
    while cherryOnTree > 0:
        spinIndex = random.randrange(0,len(spinnerChoice))
        spinResult = spinnerChoice[spinIndex]
        print "you spun", spinResult
        cherryOnTree = spinResult + cherryOnTree #cherryOnTree += spinResult
        
        if cherryOnTree > 10:
            cherryOnTree = 10
        elif cherryOnTree < 0:
            cherryOnTree = 0
    #    print "you now have %d on your tree" %(cherryOnTree)
        print "you now have", cherryOnTree, "cherries on your tree."
        turns += 1
        print "you spun", turns, "times."

#***************************************************************************************************************
#Run game 100 times and get average of number of spins to win the game.

import random
spinnerChoice = [-1,-2,-3,-4,+2,+2,+10]
turnToWin = []
for i in range(100):
    turns = 0
    cherryOnTree = 10
    while cherryOnTree > 0:
        spinIndex = random.randrange(0,len(spinnerChoice))
        spinResult = spinnerChoice[spinIndex]
    #    print "you spun", spinResult
        cherryOnTree = spinResult + cherryOnTree #cherryOnTree += spinResult
        
        if cherryOnTree > 10:
            cherryOnTree = 10
        elif cherryOnTree < 0:
            cherryOnTree = 0
    #    print "you now have %d on your tree" %(cherryOnTree)
    #    print "you now have", cherryOnTree, "cherries on your tree."
        turns += 1
    #    print "you spun", turns, "times."
    turnToWin.append(turns)
print turnToWin
print "It took and average of", sum(turnToWin)/len(turnToWin), "spins to win the game out of 100 games."

#*****************************************************************************************************
#Find prime numbers between 10 and 20

for num in range(10,21):
    for i in range (2,num):
        if num%i == 0:
            j=num/i
            print "%d equals %d * %d" % (num,i,j)
            break
        else:
            print num, "is a prime number"
            