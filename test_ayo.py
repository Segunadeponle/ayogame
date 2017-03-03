import unittest
import ayo
class AyoTest(ayo.AyoGame):
    index = 0
    pots = [5, 10, 4, 9, 5, 10, 3, 6, 5, 10, 4, 6, 5, 6, 2, 6, 4, 8, 1, 10, 4, 8, 3, 6, 4, 11, 5, 9, 0, 8, 2, 6, 3, 6, 5, 6, 1, 10, 1, 7, 3, 11, 2, 9, 3, 11, 0, 10, 1, 6, 0, 7, 3, 11, 2, 8, 3, 9, 4]
    def __init__(self):
        ayo.AyoGame.__init__(self)

    def choose_random(self):

        self.last_hole = self.pots[self.index]
        self.index+=1

class AyoTestCase(unittest.TestCase):

    def setUp(self):
        self.ayo = AyoTest()

    def test_random_play(self):
        while True:
            self.ayo.choose_random()

            self.assertFalse(self.ayo.invalid,"That is an invalid input.")
            self.assertFalse(self.ayo.is_chosen_hole_empty(),"The choosen hole is empty")
            self.ayo.move()
            self.ayo.gain()
            # self.ayo.display()
            if self.ayo.goal_state():
                self.assertEqual(self.ayo.player1,26)
                self.assertEqual(self.ayo.player2,0)
                self.assertEqual(self.ayo.goal_state(),1)
                break

            self.ayo.next_player()


    def test_board_size(self):
        self.assertEqual(len(self.ayo.board),12)
    def tearDown(self):
        pass
