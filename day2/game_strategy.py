import enum


class Bets(enum.Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class Strategies(enum.Enum):
    WIN = "Z"
    LOSE = "X"
    DRAW = "Y"


class Strategy:

    strategy: Strategies

    def __init__(self, strategy):
        self.strategy = strategy

    def get_bet(self, opponent_bet):
        if self.strategy == Strategies.WIN:
            return self.win_strategy(opponent_bet)
        elif self.strategy == Strategies.LOSE:
            return self.lose_strategy(opponent_bet)
        else:
            return self.draw_strategy(opponent_bet)

    @staticmethod
    def win_strategy(opponent_bet):
        if opponent_bet.bet == Bets.ROCK:
            return Bet.from_bet(Bets.PAPER)
        elif opponent_bet.bet == Bets.PAPER:
            return Bet.from_bet(Bets.SCISSORS)
        else:
            return Bet.from_bet(Bets.ROCK)

    @staticmethod
    def lose_strategy(opponent_bet):
        if opponent_bet.bet == Bets.ROCK:
            return Bet.from_bet(Bets.SCISSORS)
        elif opponent_bet.bet == Bets.PAPER:
            return Bet.from_bet(Bets.ROCK)
        else:
            return Bet.from_bet(Bets.PAPER)

    @staticmethod
    def draw_strategy(opponent_bet):
        return Bet.from_bet(opponent_bet.bet)

    def __repr__(self):
        return f"Strategy({self.strategy.value})"


class Bet:
    bet = None
    action_score = 0

    def __init__(self, bet):
        if bet == "A":
            self.bet = Bets.ROCK
            self.action_score = 1
        elif bet == "B":
            self.bet = Bets.PAPER
            self.action_score = 2
        elif bet == "C":
            self.bet = Bets.SCISSORS
            self.action_score = 3

    @classmethod
    def from_bet(cls, bet: Bets):
        return cls(bet.value)

    def __gt__(self, other):
        if self.bet is Bets.ROCK and other.bet is Bets.SCISSORS:
            return True
        elif self.bet is Bets.PAPER and other.bet is Bets.ROCK:
            return True
        elif self.bet is Bets.SCISSORS and other.bet is Bets.PAPER:
            return True
        else:
            return False

    def __eq__(self, other):
        return self.bet == other.bet

    def __repr__(self):
        return f"Bet({self.bet})"


class Game:

    def __init__(self, opponent, my_bet):
        self.opponent = Bet(opponent)
        self.my_bet = Bet(my_bet)
        self.score = 0

    @classmethod
    def from_strategy(cls, opponent_bet, strategy):
        strategy = Strategy(strategy)
        my_bet = strategy.get_bet(Bet(opponent_bet))
        return cls(opponent_bet, my_bet.bet.value)

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
            strategy = Strategies(game.split(" ")[1][0])
            game = Game.from_strategy(opponent, strategy)
            game.play()
            games.append(game.score)

    return games


if __name__ == "__main__":
    games = load_games("input.txt")
    print(sum(games))
