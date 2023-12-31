class Board:
    
    winners = [
        # Diagonal
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)],
        # Horizontal
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # Vertical
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)]
    ] 

    def __init__(self, start_turn='X'):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.turn = start_turn

    def copy_of(self):
        board = Board()
        board.turn = self.turn
        board.board = [[p for p in r]for r in self.board]
        return board

    def render_board(self, placeholder = False) -> None:

        chars = []

        for m in range(9):
            r, c = self._int_to_rc(m)
            curr = f"{m} " if placeholder else "  "
            if self.board[r][c] == 'X':
                curr = '👻'
            elif self.board[r][c] == 'O':
                curr = '🎃'
            chars.append(curr)
        
        view =  "┌────┬────┬────┐\n"
        view +=f"│ {chars[0]} │ {chars[1]} │ {chars[2]} │\n"
        view += "├────┼────┼────┤\n"  
        view +=f"│ {chars[3]} │ {chars[4]} │ {chars[5]} │\n"
        view += "├────┼────┼────┤\n"  
        view +=f"│ {chars[6]} │ {chars[7]} │ {chars[8]} │\n"
        view += "└────┴────┴────┘\n"

        print(view)

    """
    Returns either:
      X - When X has won the game
      O - When O has won the game
      = - When the game has finished with a draw
      None - When the game is not in a terminal state
    """  
    def is_terminal(self):
       
        # Check for a clear winner
        for candidate in self.winners:
            line = [self.board[c[0]][c[1]] for c in candidate]
            if line == ['X', 'X', 'X']:
                return 'X'
            elif line == ['O', 'O', 'O']:
                return 'O'
          
        # If no further moves and no winner - it is a draw. 
        if self.valid_moves() == []:
           return '='
        
        # Otherwise, the show must go on!
        return None

    def valid_moves(self) -> list[int]:
        moves = []
        for m in range(9):
            row, col = self._int_to_rc(m)
            if not self.board[row][col]:
                moves.append(m)
        return moves
    
    def _int_to_rc(self, index: int) -> tuple[int, int]:
        return (index // 3, index % 3) 

    def place(self, move: int) -> None:
        row, col = self._int_to_rc(move)
        if move not in self.valid_moves():
            # Making an invalid move means you lose your turn ;)
            print("Trying to make an invalid move!")
        else:
            self.board[row][col] = self.turn
            self.turn = 'O' if self.turn == 'X' else 'X'

