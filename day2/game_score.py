class Bet:
    bet = None
    action_score = 0

    def __init__(self, bet):
        if bet in ["A", "X"]:
            self.bet = "rock"
            self.action_score = 1
        elif bet in ["B", "Y"]:
            self.bet = "paper"
            self.action_score = 2
        elif bet in ["C", "Z"]:
            self.bet = "scissors"
            self.action_score = 3

    def __gt__(self, other):
        if self.bet == "rock" and other.bet == "scissors":
            return True
        elif self.bet == "paper" and other.bet == "rock":
            return True
        elif self.bet == "scissors" and other.bet == "paper":
            return True
        else:
            return False

    def __eq__(self, other):
        return self.bet == other.bet


class Game:

    def __init__(self, opponent, my_bet):
        self.opponent = Bet(opponent)
        self.my_bet = Bet(my_bet)
        self.score = 0

    def play(self):
        if self.opponent > self.my_bet:
            self.score = 0
        elif self.opponent == self.my_bet:
            self.score = 3
        else:
            self.score = 6
        self.score += self.my_bet.action_score


def load_games(filename):
    games = []
    with open(filename, "r") as game_input:
        for game in game_input:
            opponent = game.split(" ")[0]
            my_bet = game.split(" ")[1][0]
            game = Game(opponent, my_bet)
            game.play()
            games.append(game.score)

    return games


if __name__ == "__main__":
    games = load_games("input.txt")
    print(sum(games))
