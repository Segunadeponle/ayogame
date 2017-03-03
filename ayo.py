"""
adeponle segun			120407005
ekwuribe chisom			110407019
ibekwe chidera			120407022
oturugbu kenneth		120407045
richard-chukkas prowess		120407049
onwuchekwa oscar kalu		130407038
efe yvonne ojiri		120407036
emehin oluwatobi isreal		120407017

"""
import random


class AyoGame:
    def __init__(self):
        self.initialise()

    def initialise(self):
        self.board = [4] * 12  # [4 for i in range(12)]
        self.first_player = True
        self.player1 = 0
        self.player2 = 0
        self.invalid = False

    def display(self):

        for i in range(12, 6, -1):
            print(i, end="\t")
        print()
        for i in range(11, 5,  -1):
            print(self.board[i], end="\t")
        print()
        print()
        for i in range(6):
            print(self.board[i], end="\t")
        print()

        for i in range(1, 7):
            print(i, end="\t")
        print()
        print("==============================================")
        print("Player 1 =", self.player1, " Player 2 =", self.player2)
        print("==============================================")
        print()

    def choose(self):
        self.invalid = False
        if self.first_player:
            print("Player 1 enter a number between 1 and 6 inclusive")

        else:
            print("Player 2 enter a number between 7 and 12 inclusive")
        try:
            pos = int(input("Please enter the number of the location you want to play: ")) - 1

        except ValueError:
            self.invalid = True
            return

        if not self.first_player and 0 <= pos <= 5:
            self.invalid = True
        elif self.first_player and 6 <= pos <= 11:
            self.invalid = True
        self.last_hole = pos

    def choose_random(self):
        if self.first_player:
            self.last_hole = random.randrange(0, 6)
            while self.board[self.last_hole] == 0:
                self.last_hole = random.randrange(0, 6)
                # print("Player 1 choose ",self.last_hole)

        else:
            self.last_hole = random.randrange(6, 12)
            while self.board[self.last_hole] == 0:
                self.last_hole = random.randrange(6, 12)
                # print("Player 2 choose ",self.last_hole)

        

    def choose_best_pot(self):
        p = 0
        opponent_score = {}
        while self.board[p] == 0:
            p += 1
        m = [(0,p)]

        # print("Start")
        current_state = self.board.copy()
        r = range(6) if self.first_player else range(6, 12)
        for i in r:
            self.last_hole = i
            self.move()
            v = self.value(self.last_hole)
            last_hole = self.last_hole
            opponent_score[i] = self.check_opponets_score()
            self.last_hole = last_hole
            self.board = current_state.copy()
            if self.board[i]!=0:
               m.append((v,i))

            # if v>m[0]:
            #     m = (v,i)
            #     print("(v,i)",m)
        r = range(6) if self.first_player else range(6, 12)

        self.last_hole = max([(v-opponent_score[x][0],x) for (v,x) in m if self.board[x] != 0])[1]

        # self.display()

    def check_opponets_score(self):
        self.next_player()
        p = 0
        while self.board[p] == 0:
            p += 1
        m = [(0,p)]

        # print("Start")
        current_state = self.board.copy()
        r = range(6) if self.first_player else range(6, 12)
        for i in r:
            self.last_hole = i
            self.move()
            v = self.value(self.last_hole)
            self.board = current_state.copy()
            if self.board[i]!=0:
               m.append((v,i))
            # if v>m[0]:
            #     m = (v,i)
            #     print("(v,i)",m)
        self.next_player()
        return max(m)
    def value(self,x):

        player1 = 0
        player2 = 0
        if self.first_player:
            if self.can_gain(x):
                current_hole = x

                while current_hole >= 6:
                    if not self.can_gain(current_hole):
                        break
                    player1 += self.board[current_hole]
                    self.board[current_hole] = 0
                    current_hole -= 1
            return player1

        elif (not self.first_player):
            if self.can_gain(x):
                current_hole = x

                while current_hole >= 0:
                    if not self.can_gain(current_hole):
                        break
                    player2 += self.board[current_hole]
                    self.board[current_hole] = 0
                    current_hole -= 1
            return player2


    def move(self):
        hand = self.board[self.last_hole]
        self.board[self.last_hole] = 0
        while hand > 0:
            self.last_hole = (self.last_hole + 1) % 12
            self.board[self.last_hole] += 1
            hand -= 1

    def gain(self):
        if self.first_player and 6 <= self.last_hole <= 11:
            if self.can_gain(self.last_hole):
                current_hole = self.last_hole

                while current_hole >= 6:
                    if not self.can_gain(current_hole):
                        break
                    self.player1 += self.board[current_hole]
                    self.board[current_hole] = 0
                    current_hole -= 1

        elif (not self.first_player) and 0 <= self.last_hole <= 5:
            if self.can_gain(self.last_hole):
                current_hole = self.last_hole

                while current_hole >= 0:
                    if not self.can_gain(current_hole):
                        break
                    self.player2 += self.board[current_hole]
                    self.board[current_hole] = 0
                    current_hole -= 1

    def can_gain(self, hole):
        return self.board[hole] == 2 or self.board[hole] == 3

    def is_chosen_hole_empty(self):
        return self.board[self.last_hole] == 0

    def can_continue_round(self):
        return self.board[self.last_hole] != 1

    def next_player(self):
        self.first_player = not self.first_player

    def goal_state(self):
        if self.player1 > 24 or self.player2 > 24:
            if self.player1 > 24:
                return 1
            else:
                return 2

        elif sum(self.board[0:6]) == 0 or sum(self.board[6:12]) == 0:
            if self.player1 > self.player2:
                return 1
            else:
                return 2

        elif abs(self.player1 - self.player2) > sum(self.board):
            if self.player1 > self.player2:
                return 1
            else:
                return 2
        elif sum(self.board) < 3:
            if self.player1 > self.player2:
                return 1
            else:
                return 2
        else:
            return 0

    def goal_state_new(self):
        if self.player1 > 24 or self.player2 > 24:
            if self.player1 > 24:
                return (1, "if self.player1>24 or self.player2>24:")
            else:
                return (2, "if self.player1>24 or self.player2>24:")

        elif sum(self.board[0:6]) == 0 or sum(self.board[6:12]) == 0:
            if self.player1 > self.player2:
                return (1, " elif sum(self.board[0:6])==0 or sum(self.board[6:12])==0 :")
            else:
                return (2, " elif sum(self.board[0:6])==0 or sum(self.board[6:12])==0 :")

        elif abs(self.player1 - self.player2) > sum(self.board):
            if self.player1 > self.player2:
                return (1, "elif abs(self.player1 - self.player2) >sum(self.board):")
            else:
                return (2, "elif abs(self.player1 - self.player2) >sum(self.board):")
        elif sum(self.board) < 3:
            if self.player1 > self.player2:
                return (1, "elif sum(self.board) < 3:")
            else:
                return (2, "elif sum(self.board) < 3:")
        else:
            return (0,)


