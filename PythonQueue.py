numberOfNames=0
names=[]
run=True
def addNames():
    x=0
    while x<numberOfNames:
        acceptedName=input("Enter a name:")
        names.append(acceptedName)
        x=x+1

def printNames():
    y=0
    nameLength=len(names)
    while y<=nameLength-1:
        print(names.pop(0))
        y=y+1
        
while run==True:
    print("Enter '-99' to end the program")
    numberOfNames=int(input("Enter the amount of names you would like to add to the list:"))
    if numberOfNames!=-99:
        addNames()
        printNames()
        names=[]
        print("The program is complete. Enter information to run again.")

    else:
        print("Thank you for using this program. Have a nice day!")
        run=False





    
