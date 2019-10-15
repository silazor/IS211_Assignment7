import logging
import random
import sys
from pprint import pprint

class Game_Play:
    def __init__(self):
        self.winner = None
        self.player_objects = []
        self.num_players = 2

    def start_game(self):
        for each_player in range(1, self.num_players+1):
            (p, a) = self.get_player_info(each_player)
            player = Player()
            player.make_player(p, a)
            self.player_objects.append(player)

        return random.choice(self.player_objects)

    def is_winner(self, player):
        if player.score >= 100 or (player.current_roll_total + player.score) >= 100:
            print(f"{player.name} won!")
            sys.exit(0)

    def get_next_player(self, current_player):
        for i in range(0, self.num_players):
            if current_player.name == self.player_objects[i].name:
                if i == self.num_players-1:
                    i=0
                else:
                    i+=1
                return self.player_objects[i]

    def roll_or_hold(self, current_player):
        answer = input(f"Player {current_player.name}: Score {current_player.score}, roll(r) or hold(h)? ")
        if answer != 'r' and answer != 'h':
            print("You must answer with a lowercase r or h")
            answer = input(f"r or h: ")
            self.roll_or_hold(current_player)
        if answer == 'r':
            return True
        else:
            return False

    def get_player_info(self, each_player):
        p = input(f"Player {each_player} Enter your name:")
        a = input(f"Player {each_player} Enter your age:")
        return (p, a)

class Player:
    def __init__(self):
        self.score = 0
        self.current_roll_total = 0

    def make_player(self, name, age):
        self.name = name
        self.age =  age

    def update_score(self, player, current_roll_total):
        self.score = self.score + self.current_roll_total
        print(f"Current score for {player.name} is {self.score}")

    def update_current_roll_total(self, player, current_roll):
        self.current_roll_total = self.current_roll_total + current_roll
        print(f"Current roll is {current_roll}. Current turn score for {player.name} is {self.current_roll_total} and saved score is {player.score}")

class Turn():

    def roll_dice(self):
        roll = random.randint(1,6)
        return roll

    def is_roll_a_one(self, current_roll):
        if current_roll == 1:
            return True
        else:
            return False

def main():
    logging.info("Start Game:")
    new_game = Game_Play()
    turn = Turn()
    current_player = new_game.start_game()
    logging.info(f"current player: {current_player.name}")
    random.seed(0)

    while True:
    #for i in range(0,500):
        # Ask current_player to roll
        if new_game.roll_or_hold(current_player):
            #ROLL
            current_roll = turn.roll_dice()
            #current_roll = 90
            logging.info(f"Current roll is {current_roll}")
            # Check if it's a one and if so, got to next player
            if turn.is_roll_a_one(current_roll):
                logging.info(f"Current roll is {current_roll} and user is {current_player.name} GO TO NEXT USER.")
                next_player = new_game.get_next_player(current_player)
                print(f"You rolled a 1: next player up is {next_player.name}")
                current_player = next_player
                current_player.current_roll_total = 0
            # if not, update score and check if we have a winner
            else:
                logging.info(f"Current roll is {current_roll} and user is {current_player.name} UPDATE SCORE.")
                current_player.update_current_roll_total(current_player, current_roll)
                new_game.is_winner(current_player)
        else:
            #HOLD and PASS
            print(f"Current roll total is {current_player.current_roll_total}")
            new_game.is_winner(current_player)
            current_player.update_score(current_player, current_player.update_current_roll_total)
            next_player = new_game.get_next_player(current_player)
            current_player = next_player
            current_player.current_roll_total = 0
        # repeat until we have a winner

if __name__ == '__main__':
    logging.basicConfig(filename='pig.log',level=logging.INFO, filemode='w')
    main()
