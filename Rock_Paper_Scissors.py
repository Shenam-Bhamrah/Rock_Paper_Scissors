#!/usr/bash/env python3
""" A program that allows users to choose 2 players from 4 different
options and play Rock,Paper ans Scissors game between them as well as
displays score in each round and finally anounce the winner """

moves = ['rock', 'paper', 'scissors']


class Player:
    """This player class is a parent class for all the players in the
    game"""
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class AllRockP(Player):
    """A player that always plays rocks and returns the value "rock"
    each time it is called."""
    def move(self):
        return 'rock'


class RandomP(Player):
    """ A player that makes moves randomly and is a subclass of
    Player class.It returns random moves each time."""
    def move(self):
        """ths function returns random moves each time out of the moves
        list."""
        import random
        mymove = random.choice(moves)
        return mymove


class ReflectiveP(Player):
    """ A subclass of player class that remembers and returns what other
    players's last move was."""
    def __init__(self):
        "this function contains initializers"
        self.m = "rock"

    def learn(self, my_move, their_move):
        """this function takes the moves of both players as inputs and stores
        the move of opponent player"""
        self.m = their_move

    def move(self):
        """this function returns the move of opponent player as this players
        current move"""
        move = self.m
        return move


class CyclicP(Player):
    """A subclass of player class that cycles through 3 moves and returns
    them in a cyclic order."""
    def __init__(self):
        "this function contains initializers"
        self.m = "rock"
        self.num = 0

    def move(self):
        """this move function returns moves in cyclical order"""
        self.num += 1
        self.index = moves.index(self.m) + self.num
        self.len = len(moves)
        if self.index % self.len == 0:
            return moves[0]
        elif self.index % self.len == 1:
            return moves[1]
        elif self.index % self.len == 2:
            return moves[2]
        else:
            return moves[0]


class HumanP(Player):
    """ A Human player that asks from valid input from user and returns
    that value."""
    def move(self):
        """this move function asks for an input from the user and returns
        valid move"""
        while True:
            mymove = input("Please enter your move:").lower()
            if mymove in moves:
                return mymove
            else:
                return self.move()
            break


class Game:
    """Game class that has 2 chosen players as inputs and has methods to
    play game rounds,count scores and announce winners."""
    def __init__(self, P1, P2):
        """this function takes the two types of chosen players as inputs
        and stores them in variables"""
        self.P1 = P1
        self.P2 = P2
        self.point1 = 0
        self.point2 = 0

    def beats(self, move1, move2):
        """this function keeps a track of each move by two placers,compares
        then and  returns the points of each player"""
        if (move1 == "rock" and move2 == "scissors") or \
           (move1 == "scissors" and move2 == "paper") or \
           (move1 == 'paper' and move2 == "rock"):
            print("Player1 is the winner ")
            self.point1 += 1
        elif (move2 == "rock" and move1 == "scissors") or \
             (move2 == "scissors" and move1 == "paper") or \
             (move2 == 'paper' and move1 == "rock"):
            print("Player2 is the winner ")
            self.point2 += 1
        else:
            print("Draw")
        print(f"Scores:Player 1: {self.point1} Player 2: {self.point2}")
        return (self.point1, self.point2)

    def scores(self, move1, move2):
        """this function takes the points of eaach player from the beats
        function and counts them to reveal points after each round."""
        self.s = self.beats(move1, move2)
        return self.s

    def play_round(self):
        """this function calls the move function of each player and displays
        them.It also calls the remeber function for specific players"""
        move1 = self.P1.move()
        move2 = self.P2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.P1.learn(move1, move2)
        self.P2.learn(move2, move1)
        self.final = self.scores(move1, move2)

    def play_game(self):
        """this function marks the start of the game and calls the play_round
        function in a loop,compares the total points of each players and
        announces final winner"""
        print("Game start!")
        for round in range(5):
            print(f"\n Round {round}:")
            self.play_round()
            if self.final[0] > self.final[1]:
                print("\n Player1 Is The Winner!!")
            elif self.final[0] < self.final[1]:
                print("\n Player2 Is The Winner!!")
            else:
                print("\n Draw!!")
        print(f"Final Scores: \n Player1:{self.final[0]} \
              Player2: {self.final[1]}\n")
        print("------------Game over-------------!")


if __name__ == '__main__':
    allplayers = [AllRockP(), RandomP(), CyclicP(), HumanP(), ReflectiveP()]

    def int_check(value):
        try:
            int(value)
        except ValueError:
            return False
        return True

    print("Select 2 Players from the following list:\n"
          "0:AllRock  1:Random  2.Cyclic  3.Human  4.Reflective\n")

    player1 = input("Enter Your First Choice (0-4):")
    while not (int_check(player1) and int(player1) >= 0 and int(player1) <= 4):
        player1 = input("\nInvalid First Choice\n Enter Choice(0-4):")

    player2 = input("Enter Your Second Choice (0-4):")
    while not (int_check(player2) and int(player2) >= 0 and int(player2) <= 4):
        player2 = input("\nInvalid Second Choice\n Enter Choice(0-4):")

    game = Game(allplayers[int(player1)], allplayers[int(player2)])
    game.play_game()
