import numpy as np
import holes
from enum import Enum

__all__ = [
    "Move_Values",
    "Board"
]

class Move_Values(Enum):
    Wrong_Side = 0
    End_Of_Turn = 1
    Move_Again = 2 # landed in ulo on last piece
    No_Pieces = 3
    Move_From_Ulo = 4

class Board:
    def __init__(self, board_type: str = "sungkala"):
        if board_type == "mancala":
            self.board = holes.Holes(12, 4)
        elif board_type == "sungka":
            self.board = holes.Holes(14, 4)
        elif board_type == "sungkala":
            self.board = holes.Sungkala_Holes(12, 4)
        else:
            print("Ya done fucked up. Enter something reasonable, like 'mancala' or 'sungka' or 'sungkala'.")

    def count(self, hole: int) -> int:
        return self.board.count(hole)

    def right(self, hole: int) -> int:
        return self.board.right(hole)

    def board_sum(self) -> int:
        '''

        :return: sum of pieces left on board (not in ulos)
        '''
        ulo_cnt_p0 = self.board.ulo_count(True)
        ulo_cnt_p1 = self.board.ulo_count(False)
        return ((len(self.board.holes) - 2) * self.board.holes[0].original_pieces) - (ulo_cnt_p0 + ulo_cnt_p1)

    def all_right(self, hole: int) -> np.ma.masked_array:
        pieces = self.count(hole)
        right = []
        ulo_mask = []
        for piece in range(pieces):
            right.append(self.right(hole + piece))
            if (hole + piece == len(self.board.holes) - 1) or (hole + piece == int((len(self.board.holes) / 2) - 1)):
                ulo_mask.append(True)
            else:
                ulo_mask.append(False)

        right_ma = np.ma.masked_array(right)
        right_ma.mask = ulo_mask

        return right_ma

    def move(self, hole: int, side: bool):
        result = self._move(hole, side)
        if result == 0:
            print("Trying to move from wrong side of the board")
        elif result == 1:
            print("End of Turn")
        elif result == 2:
            print("Move again")
        elif result == 3:
            print("Trying to move from hole with no pieces")
        elif result == 4:
            print("Trying to move from ulo")
        else:
            print("Wtf happened?")

    # player 0 = [0:ulo_0], player 1 = [ulo_0 + 1: ulo_1]
    # side: True = player 0
    # side: False = player 1
    def _move(self, hole: int, side: bool) -> int:
        if side:
            if hole >= int(len(self.board.holes) / 2) and hole <= len(self.board.holes - 1):
                return Move_Values["Wrong_Side"].value
            else:
                val = self.board.move(hole=hole, side=side)
        else:
            if hole >= 0 and hole <= int((len(self.board.holes) / 2) - 1):
                return Move_Values["Wrong_Side"].value
            else:
                val = self.board.move(hole=hole, side=side)

        if val == 0:
            return Move_Values["No_Pieces"].value
        elif val == 2:
            return Move_Values["Move_Again"].value
        elif val == 3:
            return Move_Values["Move_From_Ulo"].value
        else:
            return Move_Values["End_Of_Turn"].value


def main_cli():
    # full_board = Board("mancala")
    full_board = Board("sungkala")
    full_board.move(2, True) # Move Again
    full_board.move(5, True) # End of Turn
    full_board.move(8, False) # Move Again
    full_board.move(7, False) # End of Turn
    full_board.move(1, True) # Move Again
    full_board.move(5, True) # Move Again
    full_board.move(2, True) # End of Turn
    full_board.move(12, False) # Move Again
    full_board.move(8, False) # End of Turn
    full_board.move(1, True) # Move Again
    full_board_dummy = type('dummy', (object,), {})
    full_board_attrs = {attr:getattr(full_board, attr) for attr in dir(full_board) if (not attr in dir(full_board_dummy))}
    B = type('B', (object,), full_board_attrs)
    a = 0

if __name__ == '__main__':
    main_cli()