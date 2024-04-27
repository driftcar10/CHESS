class Piece():
    def __init__(self,color,xpos,ypos):
        self.color=color
        self.ypos=ypos
        self.xpos=xpos
    
class king():
    def __init__(self,color,xpos, ypos, board,move_king,move_tower):
        super().__init__(self, color, xpos, ypos)
        self.board = board
        self.move_king = move_king
        self.move_tower = move_tower
        
    def move(self):
        move = input("WHERE DO YOU WANT TO PLACE YOUR KING? TYPE UP, DOWN, DIAG_LEFT_UP, DIAG_LEFT_DOWN, DIAG_RIGHT_UP, DIAG_RIGHT_DOWN, CASTLE_LEFT, CASTLE_RIGHT:")
        if move = "UP":
            if (self.ypos+1)!=9 and board[self.xpos][self.ypos+1] == "0":
                board[self.xpos][self.ypos+1] = "K":
                board[self.xpos][self.ypos] = 0
            else:
                print("YOU CANNOT DO THAT")
                
        elif move = "DOWN":
            if (self.ypos-1)!=-1 and board[xpos][ypos-1] == "0":
                board[xpos][self.ypos-1] = "K":
                board[xpos][self.ypos] = "0"
            else:
                print("YOU CANNOT DO THAT")
                
        elif move = "DIAG_LEFT_DOWN":
            if (self.ypos+1) != 9 and (self.xpos-1) != 0 and  board[xpos-1][ypos+1] == "0":
                board[xpos-1][self.ypos+1] = "K"
                board[xpos][self.ypos] = "0"
            else:
                print("YOU CANNOT DO THAT")
                
        elif move = "DIAG_LEFT_UP":
            if (self.ypos-1) != 0 and (self.xpos-1) != 0 and board[xpos-1][ypos-1] == "0":
                board[xpos-1][self.ypos-1] = "K":
                board[xpos][self.ypos] = "0"
            else:
                print("YOU CANNOT DO THAT")
                
        elif move = "DIAG_RIGHT_UP":
            if (self.ypos-1) != 0 and (self.xpos+1) != 9 and board[xpos+1][ypos-1] == "0":
                board[xpos+1][self.ypos-1] = "K":
                board[xpos][self.ypos] = "0"
            else:
                print("YOU CANNOT DO THAT")
                
        elif move = "DIAG_RIGHT_DOWN":
            if (+1) != 9 and (self.xpos+1) != 9 and board[xpos+1][ypos+1] == "0":
                board[xpos+1][self.ypos+1] = "K":
                board[xpos][self.ypos] = "0"
            else:
                print("YOU CANNOT DO THAT")
                
        elif move = "CASTLE_RIGHT":
            if board[xpos][self.ypos-1] == "0":
                board[xpos][self.ypos-1] = "K":
            else:
                print("YOU CANNOT DO THAT")
                
        elif move = "CASTLE_LEFT":
            if board[xpos][self.ypos-1] == "0":
                board[xpos][self.ypos-1] = "K":
            else:
                print("YOU CANNOT DO THAT")
                
        else:
            print("NO SUCH COMMAND")
board = [
        ["0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0"],
        ]
