import copy 
import math 
import sys
class board:
    board=[[0, 0, 0] for _ in range(3)]

    def actions(self,board):
        possible_action=set()
        for i in range(3):
            for j in range(3):
                if board[i][j]==0:
                    possible_action.add((i,j))

        return possible_action
        

    def result(self,board,action):
        new_result=copy.deepcopy(board)
        new_result[action[0]][action[1]]=self.player(board)
        return new_result


    def player(self,board):
        count_x = 0
        count_o = 0

        for row in board:
            for element in row:
                if element == 1:
                    count_x += 1
                elif element == -1:
                    count_o += 1

        if count_x > count_o:
            return -1
        else:
            return 1
        
    def winner(self,board):

        for i in range (3):
            for button_list in board:
                a=button_list[0]
                if a!=0:
                    if all(x == a for x in button_list):
                        return a
    
        for col_index in range(3):
            first_element=board[0][col_index]
            if first_element!=0:
                if all (row[col_index]== first_element for row in board):
                    return first_element

        if board[1][1]!=0:
            if all(board[i][i] == board[0][0] for i in range(3)):
                return board[0][0]

        
            if all(board[i][len(board) - 1 - i] == board[0][len(board) - 1] for i in range(len(board))):
                return board[0][2]
        
        return None
        
    
    def terminal(self,board):
        draw=0
        for row in board:
            for element in row :
                if element ==0:
                   draw=1


        if self.winner(board) is not None or draw==0:
            return True
        else:
            return False
        

    def utility(self,board):
        if self.terminal(board):
            if self.winner(board)==1:
                return 1
            
            elif self.winner(board)==-1:
                return -1
            else:
                return 0
            


    def minimax(self,board):
        if self.terminal(board):
            return 
        else:
            if self.player(board) == 1:
                value, move = self.max_value(board)
                return move
            elif self.player(board)==-1:
                value, move = self.min_value(board)
                return move
            
    def max_value(self,board):
        if self.terminal(board):
            return self.utility(board), None

        v = float('-inf')
        move = None
        for action in self.actions(board):
            aux, act = self.min_value(self.result(board, action))
            if aux > v:
                v = aux
                move = action
                if v == 1:
                    return v, move

        return v, move


    def min_value(self,board):
        if self.terminal(board):
            return self.utility(board), None

        v = float('inf')
        move = None
        for action in self.actions(board):
            aux,act = self.max_value(self.result(board, action))
            if aux < v:
                v = aux
                move = action
                if v == -1:
                    return v, move

        return v, move
    
def main():
    boar=[[1,-1,1],[-1,1,0],[-1,0,0]]

    init=board()
    move =init.minimax(boar)
    print (init.winner(board))
if __name__=="__main__":
    main()