##numOfTest=int(input("Enter number of scores:"))
##score1=float(input("enter score 1:"))
##score2=float(input("enter score 2:"))
##scoreTotal=score1+score2
##avg=scoreTotal/2
##print(avg)


numOfTestScores=int(input("Enter number of scores:"))
x=0
scoreTotal=0
while x<numOfTestScores:
    score=float(input("Enter a score:"))
    scoreTotal+=score
    x+=1
    
average=scoreTotal/numOfTestScores
totalSentence= "The average of the {} scores entered is {:.2f}%."
print(totalSentence.format(numOfTestScores,average))
