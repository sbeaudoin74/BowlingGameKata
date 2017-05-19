class Game:

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        scoreTotal = 0
        roll = 0

        for frame in range(10):
            if self.isStrike(roll):
                scoreTotal += self.strikeBonus(roll)
                roll += 1

            elif self.isSpare(roll):
                scoreTotal += self.spareBonus(roll)
                roll += 2

            else:
                scoreTotal += self.rolls[roll] + self.rolls[roll+1]
                roll += 2

        return scoreTotal

    def isSpare(self, roll):
        return self.rolls[roll] + self.rolls[roll+1] == 10

    def spareBonus(self, roll):
        return 10 + self.rolls[roll+2]

    def isStrike(self, roll):
        return self.rolls[roll] == 10

    def strikeBonus(self, roll):
        return 10 + self.rolls[roll+1] + self.rolls[roll+2]
