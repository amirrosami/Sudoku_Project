from CSP import *

board1=[[9,0,0,0,0,0,2,0,0],
        [0,8,0,0,0,7,0,9,0],
        [6,0,2,0,0,0,5,0,0],
        [0,7,0,0,6,0,0,0,0],
        [0,0,0,9,0,1,0,0,0],
        [0,0,0,0,2,0,0,4,0],
        [0,0,5,0,0,0,6,0,3],
        [0,9,0,4,0,0,0,7,0],
        [0,0,6,0,0,0,0,0,0]
       ]
board2=[
    [0,4,0,1],
    [3,0,4,0],
    [1,0,0,4],
    [0,2,1,0]
    ]


def MainTest1():
    n=4
    Variables=[[0 for j in range(n)] for i in range(n)] 
    Domain=[[[d for d in range(1,n+1)] for i in range(n) ] for j in range(n)]
    Variables=board2
    result=Backtrack_FC(Variables,Domain)
    print("result : ",result)
    printBoard(Variables)

def MainTest2():
    n=9
    Variables=[[0 for j in range(n)] for i in range(n)] 
    Domain=[[[d for d in range(1,n+1)] for i in range(n) ] for j in range(n)]
    Variables=board1
    result=Backtrack_FC(Variables,Domain)
    print("result : ",result)
    printBoard(Variables)


def MainTest3():
    n=9
    Variables=[[0 for j in range(n)] for i in range(n)] 
    Domain=[[[d for d in range(1,n+1)] for i in range(n) ] for j in range(n)]
    Variables=board1
    result=Backtrack(Variables,Domain)
    print("result : ",result)
    printBoard(Variables)

    

def Main():
    n=int( input("n : "))
    c=int(input("number of cells you want to fill : "))
    Variables=[[0 for j in range(n)] for i in range(n)] 
    Domain=[[[d for d in range(1,n+1)] for i in range(n) ] for j in range(n)]
    initialValidation=True
    for i in range(c):
        filledcell=input("row ,col,value :").split(",")
        row=int(filledcell[0])
        col=int(filledcell[1])
        value=int(filledcell[2]) 
        Variables[row][col]=value
        if IsConsistent(row,col,value,Variables) ==False:
            initialValidation=False
    print("Your initial Board : ")
    printBoard(Variables)
    input("Enter any key to Solve...")
    if initialValidation:
        result=Backtrack_FC(Variables, Domain)
        if result :
            print("!!!!Solved Successfully\nYour Board :\n")
            printBoard(Variables)
        else:
            print("\n!!!Oooops Unsolveable ")
             
        
    else:
        print(" !!!Oooops Unsolveable\n Cells You Filled Are InConsistent ")
        
    
    
    
#Execution:
Main()

