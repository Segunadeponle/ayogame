

class AyoGame:

    def __init__(self):
        self.initialise()
        
    def initialise(self):
        self.board = [4 for i in range(12)]
        self.first_player = True
        self.player1 = 0
        self.player2 = 0
        

    def display(self):
            
        for i in range(12,6,-1):
            print(i,end="\t")
        print()
        for i in range(11,5,-1):
            print(self.board[i],end="\t")
        print()
        print()
        for i in range(6):
            print(self.board[i],end="\t")
        print()

        for i in range(1,7):
            print(i,end="\t")
        print()
        print("==============================================")
        print("Player 1 =", self.player1, " Player 2 =", self.player2)
        print("==============================================")
        print()

    def choose(self):
        if self.first_player:
            print("Player 1 enter a number between 1 and 6 inclusive")
            
        else:
            print("Player 2 enter a number between 7 and 12 inclusive")    
        pos = int(input("Please enter the number of the location you want to play: "))-1
        if not self.first_player and 0<=pos<=5:
            raise "invalid entry"
        elif self.first_player and 6<=pos<=11:
            raise "invalid entry"
        self.last_hole = pos

            
       
    def move(self):
        hand = self.board[self.last_hole]
        self.board[self.last_hole] = 0
        while hand>0:
            self.last_hole = (self.last_hole+1)%12
            self.board[self.last_hole]+=1
            hand-=1
    
    def gain(self):
        if self.first_player and 6<=self.last_hole<=11:
            if self.can_gain(self.last_hole) :
                current_hole = self.last_hole
                
                while current_hole>=6:
                    if not self.can_gain(current_hole):
                        break
                    self.player1 += self.board[current_hole]
                    self.board[current_hole] = 0
                    current_hole-=1
            
        elif (not self.first_player) and 0<=self.last_hole<=5:
            if self.can_gain(self.last_hole) :
                current_hole = self.last_hole
                
                while current_hole>=0:
                    if not self.can_gain(current_hole):
                        break
                    self.player2 += self.board[current_hole]
                    self.board[current_hole] = 0
                    current_hole-=1
        
    def can_gain(self,hole):
        return self.board[hole]==2 or self.board[hole]==3
    def is_chosen_hole_empty(self):
        return self.board[self.last_hole] == 0
    def can_continue_round(self):
        return self.board[self.last_hole]!=1
    def next_player(self):
        self.first_player = not self.first_player
def main():
    ayo = AyoGame()
    ayo.display()
    while True:
        ayo.choose()
        if ayo.is_chosen_hole_empty():
            continue
        ayo.move()    
        ayo.gain()
        ayo.display()
        ayo.next_player()
if __name__ =='__main__':
    main()
