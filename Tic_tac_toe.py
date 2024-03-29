def placer(plane, choice, side):		#function to place user's choice on the field
    splitSide1, splitSide2 = choice[0], choice[1]
    if side == "X":
        sider=1
    elif side == "O":
        sider=-1
    plane[splitSide1][splitSide2] = sider
    return plane

def printer(plane):		                    #function to print out the current board
    for w in range(len(plane)):
        for e in range(len(plane)):
            if plane[w][e]== 1:
                print('{:>3}'.format('X'), end="")
            elif plane[w][e] == -1:
                print('{:>3}'.format('O'), end="")
            elif plane[w][e] == 0:
                print('{:>3d}'.format((len(plane)*w+e)), end="")
        print("")

def listSum(numList):		            #Function to add elements of a list together
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listSum(numList[1:])    
    
def winnerFind(plane, side):		#check for a winner in 3 different ways:
    
	#check for row win by adding values to see if they're equal to the length of the playing plane
    tempVar=[]
    for g in range(len(plane)):
        if listSum(plane[g]) == len(plane) or listSum(plane[g]) == -int(len(plane)):
            print("Winner:", side)
            exit()
       
    #check for column win by adding values:
    for t in range(len(plane)):
        for u in range(len(plane)):
            tempVar.append(plane[u][t])
        if listSum(tempVar)== len(plane) or listSum(tempVar)== -int(len(plane)):
            print("Winner:", side)
            exit()
        else:
            tempVar=[]
    tempVar=[]
	
    #check for diagonally downward wins
    for a in range(len(plane)):
        tempVar.append(plane[a][a])
    if listSum(tempVar)== len(plane) or listSum(tempVar)== -int(len(plane)):
        print("Winner:", side)
        exit()
	
    #check for diagonally upward wins
    tempVar=[]
    for s in range(len(plane)):
        tempVar.append(plane[-s-1][s])
    if listSum(tempVar)== len(plane) or listSum(tempVar)== -int(len(plane)):
        print("Winner:", side)
        exit()

def choiceTrans(choice, plane):		#"translate" human input into more easily computable values
    findHelp=0
    for p in range(len(plane)):
        for i in range(len(plane)):
            if findHelp == choice:
                return p,i
            findHelp+=1
			
def endOfGame(plane):		#check whether all positions are taken up
    counter=0
    for x in range(len(plane)):
        for y in range(len(plane)):
            if plane[x][y] == 0:
                counter=counter
            else:
                counter+=1
    if counter == (len(plane) * len(plane)):
        print("Winner: None")
        exit()


def main():		#Main function selects active side (always X) and calls corresponding functions
    side="X"
    print("Size -->", end="")
    size=int(input())
    plane=[]
    for g in range(size):               #create initial (empty) 2-Dimensional array with user-chosen size
        plane.append([0]*size)
    printer(plane)
    
    while True: 
        if side=="X":
            print("X--> ", end="")
        if side=="O":
            print("O--> ", end="")
			
        choice=int(input())
        choice=choiceTrans(choice, plane)       #choice "translates" user input into computeable values
        plane=placer(plane, choice, side)         #Places user's choice on the array with a 1 for X and a -1 for O
        printer(plane)                                        #Prints (now modified) array to screen, replacing empty locations with a corresponding number  
        winnerFind(plane, side)                         #Finds the winner based on whether the absolute value of the sum of a line is equal to the length of the array
        
        if side == "X":     
            side="O"
        elif side=="O":
            side="X"
        endOfGame(plane)                                #Checks whether the field is full. Only executes after winnerFind() in order to make sure when the field is full, no one has won yet
main()