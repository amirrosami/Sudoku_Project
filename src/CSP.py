import copy
import math
def IsConsistent(row,col,value,board):
        n=len(board)
        #check Row
        for j in range(n):
            if board[row][j] == value and j !=col:
                return False
            
    # check column
        for i in range(n):
            if board[i][col] == value and i !=row :
                return False
    
    # check  SubBox
        n_subBox=int(math.sqrt(n))
        box_row = (row // n_subBox) * n_subBox
        box_col= (col // n_subBox) * n_subBox
        for i in range(n_subBox):
            for j in range(n_subBox):
                if board[box_row + i][box_col + j] == value and row!=box_row + i and col!=box_col + j:
                    return False
        return True
    
def Select_Best_UnAssigned_Variable(board,domain):
        n=len(board)       
        for i in range(n):
            for j in range(n):
                if board[i][j]==0:
                    return i,j
        return None,None    
    
def IsGameOver(board):
    n=len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                return False
    return True


def GetDomain(i,j,domain):
    domain[i][j].sort()
    return domain[i][j]
    


def printBoard(board):
        n=len(board)
        for i in range (n):
            print(board[i])
        print("*********************\n\n")

def RestoreRemovedValues(domain:list[list[list]],removedValues:list,n:int):
    
    for item in removedValues:
        domain[item[0]][item[1]].append(item[2])
    for i in range(n):
        for j in range(n):
            domain[i][j].sort()
        
        

def ForwardChecking(board:list[list],domain:list[list[list]])->(bool,list,list):
    n=len(board)
    removedvalues=[]
    for i in range(n):
        for j in range(n):
            for value in domain[i][j]:
                if IsConsistent(i, j, value, board)==False:
                    domain[i][j].remove(value)
                    removedvalues.append((i,j,value))
                    if len(domain[i][j])==0:
                        return False,removedvalues
    return True,removedvalues
    
def Backtrack(board,domain):
    if IsGameOver(board):
        return True
    i,j=Select_Best_UnAssigned_Variable(board,domain)
    for value in GetDomain(i, j, domain): 
        if IsConsistent(i,j,value,board):
            board[i][j]=value
            if Backtrack(board,domain):
                return True
            
            board[i][j]=0
    return False 


def Backtrack_FC(board,domain):
        if IsGameOver(board):
            return True
        i,j=Select_Best_UnAssigned_Variable(board,domain)
        for value in GetDomain(i, j, domain): 
            if IsConsistent(i,j,value,board):
                board[i][j]=value
                fc_result,removed_values=ForwardChecking(board, domain)
                if fc_result:
                    if Backtrack_FC(board,domain):
                        return True
                RestoreRemovedValues(domain, removed_values,len(board))
                board[i][j]=0
        return False 
    