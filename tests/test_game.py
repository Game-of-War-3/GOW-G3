import unittest

from game import TicTacToe


class TicTacToeTests(unittest.TestCase):
    def test_make_move_places_current_player_symbol(self):
        game = TicTacToe()
        game.make_move(0)
        self.assertEqual(game.board[0], "X")

    def test_make_move_rejects_taken_position(self):
        game = TicTacToe()
        game.make_move(0)
        with self.assertRaises(ValueError):
            game.make_move(0)

    def test_make_move_rejects_invalid_position(self):
        game = TicTacToe()
        with self.assertRaises(ValueError):
            game.make_move(9)

    def test_winner_detects_three_in_row(self):
        game = TicTacToe()
        game.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertEqual(game.winner(), "X")

    def test_draw_when_board_full_without_winner(self):
        game = TicTacToe()
        game.board = [
            "X", "O", "X",
            "X", "O", "O",
            "O", "X", "X",
        ]
        self.assertTrue(game.is_draw())


if __name__ == "__main__":
    unittest.main()
