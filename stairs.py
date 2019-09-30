# Code your functions here!
#def downStairs(numberofStairs):



# def downStairs(numberofStairs):
#      for i in range(numberofStairs + 1):
#          stair = "#" * i
#          print (stair)

# downStairs(6)



def downStairs(numberofStairs):
    for x in range(numberofStairs+1):
        toPrint = ""
        for z in range (1, x+1):
            toPrint = toPrint + "#"
        for y in range (1, numberofStairs-x+1):
            toPrint = toPrint + " "
        print(toPrint)
    
downStairs(6)

#This code prints the #s first and then adds the appropriate number of spaces. Technically, spaces are not necessary for this code


def upStairs(numberofStairs):
    for x in range(numberofStairs+1):
        toPrint = ""
        for z in range(1, numberofStairs - x + 1):
            toPrint = toPrint + " "
        for y in range (1, x + 1):
            toPrint = toPrint + "#"
        print(toPrint)
        
#This code prints the spaces first and then adds the appropriate number of #s behind

upStairs(5)

def midStairs(numberofStairs):
    for x in range(1, numberofStairs +1):
        spaceUpStair = ""
        spaceDownStair = ""
        sharpUpStair = ""
        sharpDownStair = ""
        for y in range (1, numberofStairs-x+1):
            spaceUpStair = spaceUpStair + " "
            spaceDownStair = spaceDownStair + " "
        for z in range (1, x + 1):
            sharpUpStair = sharpUpStair + "#"
            sharpDownStair = sharpDownStair + "#"
            
        print (spaceUpStair + sharpUpStair + " " + sharpDownStair + spaceDownStair)
        
midStairs(6)

# Basically, you have a bunch of empty strings. Then, you say that you want spaces equal to the number of stairs - your current iteration and
# + 1 for the sake of range. This adds the appropriate number of spaces before or after your sharps. Since the sharps increase with the iteration,
# spaces naturally decrease with each iteration. 

# The second for loop is the one that adds the sharps, adding more sharps with each iteration.

# Lastly, you print the arranged empty strings in the appropriate order to form back-to-back staircases. 

# Order: Spaces, sharps, a space down the center, and then sharps, spaces. 