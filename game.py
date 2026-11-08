class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def make_move(self, position):
        if position < 0 or position > 8:
            raise ValueError("Position must be between 0 and 8.")
        if self.board[position] != " ":
            raise ValueError("Position already taken.")
        self.board[position] = self.current_player

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def winner(self):
        lines = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for a, b, c in lines:
            if self.board[a] != " " and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def is_draw(self):
        return self.winner() is None and all(cell != " " for cell in self.board)


def _print_board(board):
    for row in range(3):
        start = row * 3
        print(f" {board[start]} | {board[start + 1]} | {board[start + 2]} ")
        if row < 2:
            print("---+---+---")


def main():
    game = TicTacToe()
    while True:
        _print_board(game.board)
        raw = input(f"Player {game.current_player}, pick 0-8: ").strip()
        try:
            position = int(raw)
            game.make_move(position)
        except (ValueError, TypeError) as exc:
            print(f"Invalid move: {exc}")
            continue

        winner = game.winner()
        if winner:
            _print_board(game.board)
            print(f"Player {winner} wins!")
            break
        if game.is_draw():
            _print_board(game.board)
            print("It's a draw!")
            break
        game.switch_player()


if __name__ == "__main__":
    main()
