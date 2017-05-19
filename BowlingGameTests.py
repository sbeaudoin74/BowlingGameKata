import unittest

from Main import Game


class BowlingGameTests(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def rollMany(self, n, pins):
        for index in range(0, n, 1):  # Remember Python does '<' for indexing by default
            self.g.roll(pins)

    # Test for a gutter game
    def test_gutterGame(self):
        self.rollMany(20, 0)
        self.assertEquals(0, self.g.score())

    # Test for cumulative score of all ones
    def test_testAllOnes(self):
        self.rollMany(20, 1)
        self.assertEquals(20, self.g.score())

    # Test for Spare
    def test_testOneSpare(self):
        self.rollSpare()
        self.g.roll(3)
        self.rollMany(17,0)
        self.assertEquals(16, self.g.score())

    # Test for Strike
    def test_testOneStrike(self):
        self.rollStrike()
        self.g.roll(3)
        self.g.roll(4)
        self.rollMany(16,0)
        self.assertEquals(24, self.g.score())

    # Test for a perfect game
    def test_testPerfectGame(self):
        self.rollMany(12,10)
        self.assertEquals(300, self.g.score())

    # Test for an unfortunate game
    def test_testAllSpares(self):
        self.rollMany(21,5)
        self.assertEquals(150, self.g.score())

    # Test for a realistic game
    def test_testRandomGame(self):
        self.g.roll(9)
        self.g.roll(1)   #1
        self.g.roll(10)  #2
        self.g.roll(8)
        self.g.roll(0)   #3
        self.g.roll(4)
        self.g.roll(5)   #4
        self.g.roll(10)  #5
        self.g.roll(0)
        self.g.roll(0)   #6
        self.g.roll(7)
        self.g.roll(1)   #7
        self.g.roll(3)
        self.g.roll(2)   #8
        self.g.roll(10)  #9
        self.g.roll(4)
        self.g.roll(6)   #Spare!
        self.g.roll(9)

        self.assertEquals(117, self.g.score())

    def rollStrike(self):
        self.g.roll(10)

    def rollSpare(self):
        self.g.roll(5)
        self.g.roll(5)
