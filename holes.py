from typing import *
from enum import Enum

class Move_Pieces(Enum):
    No_Pieces = 0
    End_Of_Turn = 1
    Move_Again = 2
    Move_From_Ulo = 3

class Hole:
    def __init__(self, pieces: int):
        # have to actually link the right pieces count to the count of the right hole
        # Don't do this dingy shit below
        self.pieces = pieces
        self.right = pieces
        self.adjacent = pieces

    def inc_count(self):
        self.pieces += 1

    def dec_right(self):
        self.right -= 1

    def move_init(self):
        self.pieces = 0
        self.right += 1

    def move_reset_right(self):
        self.right = 0

    def move_end(self):
        self.pieces += 1

    def move(self):
        self.pieces += 1
        self.right += 1

class Holes:
    def __init__(self, num_of_holes: int, pieces: int):
        # + 2 for each sides ulo
        self.holes = [[]] * (num_of_holes + 2)
        self.holes[:] = [Hole(i) for i in [pieces] * (num_of_holes + 2)]
        self.holes[int(len(self.holes) / 2) - 1].pieces = 0
        self.holes[int(len(self.holes) / 2) - 1].adjacent = None
        self.holes[int(len(self.holes) / 2) - 2].right = 0
        self.holes[-1].pieces = 0
        self.holes[-1].adjacent = None
        self.holes[-2].right = 0

    # player 0 = [0:ulo_0], player 1 = [ulo_0: ulo_1]
    # side: False = player 0
    # side: True = player 1
    def ulo_count(self, side: bool) -> int:
        if side:
            return self.holes[-1].pieces
        else:
            return self.holes[int(len(self.holes) / 2) - 1].pieces

    def inc_count_ulo(self, side: bool):
        if side:
            self.holes[int(len(self.holes) / 2) - 1].inc_count()
        else:
            self.holes[len(self.holes) - 1].inc_count()

    def dec_right(self, hole: int):
        self.holes[hole].dec_right()

    def update_adjacent(self, hole: int):
        self.holes[len(self.holes) - 2 - hole].adjacent = self.holes[hole].pieces

    # for captured pieces
    def captured(self, hole: int, side: bool):
        pieces = self.holes[hole].adjacent + 1
        # update adjacent hole pieces to be 0
        self.holes[len(self.holes) - 2 - hole].pieces = 0
        # update right of hole left to adjacent hole to be 0
        self.holes[len(self.holes) - 3 - hole].right = 0
        # update adjacent to be 0 of current hole
        self.holes[hole].adjacent = 0
        # update right of hole left to current hole to be 0
        self.holes[hole - 1].right = 0

        for piece in range(1, pieces + 1):
            self.inc_count_ulo(side)

    def move_end(self, hole: int):
        self.holes[hole].move_end()

    def move_init(self, hole: int):
        self.holes[hole].move_init()
        self.holes[hole-1].move_reset_right()

    def _move(self, hole: int):
        self.holes[hole].move()

    def inner_move_check(self, hole: int, side: bool) -> Optional[int]:
        '''
        Really just a placeholder for the different types of games to overload
        '''
        return 0

    # player 0 = [0:ulo_0], player 1 = [ulo_0: ulo_1]
    # side: True = player 0
    # side: False = player 1
    def move(self, hole: int, side: bool) -> int:
        pieces = self.holes[hole].pieces
        # if there are no pieces in the hole, then ya done fucked up
        if pieces == 0:
            return Move_Pieces["No_Pieces"].value
        if hole == len(self.holes) - 1 or hole == int(len(self.holes) / 2) - 1:
            return Move_Pieces["Move_From_Ulo"]
        self.move_init(hole)
        self.update_adjacent(hole)
        # for hole_num in range(hole + 1, hole + 1 + pieces):
        hole_num = hole + 1
        val = None
        while hole_num < hole + 1 + pieces:
            actual_hole_num = hole_num % len(self.holes)
            # if player 0
            if side:
                # check to see if landing in other player's ulo
                if not (actual_hole_num == len(self.holes) - 1):
                    # if landing in ulo
                    if actual_hole_num == int((len(self.holes) / 2) - 1):
                        # if last piece is played
                        if hole_num == hole + pieces:
                            self.move_end(actual_hole_num)
                            return Move_Pieces["Move_Again"].value
                        # if last piece is not played
                        else:
                            self._move(actual_hole_num)
                    # if last piece is played
                    elif hole_num == hole + pieces:
                        val = self.inner_move_check(actual_hole_num, side)
                    # if last piece is not played
                    else:
                        self._move(actual_hole_num)
                        self.update_adjacent(actual_hole_num)
                else:
                    self.dec_right(actual_hole_num - 1)
                    pieces += 1
            # if player 1
            else:
                # skip opponent's ulo
                if not (actual_hole_num == int(len(self.holes) / 2) - 1):
                    # if piece placed in ulo
                    if actual_hole_num == int(len(self.holes) - 1):
                        self.inc_count_ulo(actual_hole_num)
                        if hole_num == hole + pieces:
                            self.move_end(actual_hole_num)
                            return Move_Pieces["Move_Again"].value
                        else:
                            self._move(actual_hole_num)
                    elif hole_num == hole + pieces:
                        val = self.inner_move_check(actual_hole_num, side)
                    else:
                        self._move(actual_hole_num)
                        self.update_adjacent(actual_hole_num)
                else:
                    self.dec_right(actual_hole_num - 1)
                    pieces += 1

            hole_num += 1

        if val:
            return val
        else:
            return Move_Pieces["End_Of_Turn"].value

class Mancala_Holes(Holes):
    # player 0 = [0:ulo_0], player 1 = [ulo_0: ulo_1]
    # side: True = player 0
    # side: False = player 1
    def move(self, hole: int, side: bool) -> int:
        pieces = self.holes[hole].pieces
        # if there are no pieces in the hole, then ya done fucked up
        if pieces == 0:
            return Move_Pieces["No_Pieces"].value
        self.move_init(hole)
        self.update_adjacent(hole)
        # for hole_num in range(hole + 1, hole + 1 + pieces):
        hole_num = hole + 1
        val = None
        while hole_num < hole + 1 + pieces:
            actual_hole_num = hole_num % len(self.holes)
            # if player 0
            if side:
                # check to see if landing in other player's ulo
                if not (actual_hole_num == len(self.holes) - 1):
                    # if landing in ulo
                    if actual_hole_num == int((len(self.holes) / 2) - 1):
                        # if last piece is played
                        if hole_num == hole + pieces:
                            self.move_end(actual_hole_num)
                            return Move_Pieces["Move_Again"].value
                        # if last piece is not played
                        else:
                            self._move(actual_hole_num)
                    # if last piece is played
                    elif hole_num == hole + pieces:
                        if self.holes[actual_hole_num].pieces == 0 and self.holes[actual_hole_num].adjacent > 0:
                            self.captured(actual_hole_num, side)
                        else:
                            self.move_end(actual_hole_num)
                            self.update_adjacent(actual_hole_num)
                    # if last piece is not played
                    else:
                        self._move(actual_hole_num)
                        self.update_adjacent(actual_hole_num)
                else:
                    self.dec_right(actual_hole_num - 1)
                    pieces += 1
            # if player 1
            else:
                # skip opponent's ulo
                if not (actual_hole_num == int(len(self.holes) / 2) - 1):
                    # if piece placed in ulo
                    if actual_hole_num == int(len(self.holes) - 1):
                        self.inc_count_ulo(actual_hole_num)
                        if hole_num == hole + pieces:
                            self.move_end(actual_hole_num)
                            return Move_Pieces["Move_Again"].value
                        else:
                            self._move(actual_hole_num)
                    elif hole_num == hole + pieces:
                        if self.holes[actual_hole_num].pieces == 0 and self.holes[actual_hole_num].adjacent > 0:
                            self.captured(actual_hole_num, side)
                        else:
                            self.move_end(actual_hole_num)
                            self.update_adjacent(actual_hole_num)
                    else:
                        self._move(actual_hole_num)
                        self.update_adjacent(actual_hole_num)
                else:
                    self.dec_right(actual_hole_num - 1)
                    pieces += 1

            hole_num += 1

        if val:
            return val
        else:
            return Move_Pieces["End_Of_Turn"].value

class Sungka_Holes(Holes):
    # player 0 = [0:ulo_0], player 1 = [ulo_0: ulo_1]
    # side: True = player 0
    # side: False = player 1
    def move(self, hole: int, side: bool) -> int:
        pieces = self.holes[hole].pieces
        # if there are no pieces in the hole, then ya done fucked up
        if pieces == 0:
            return Move_Pieces["No_Pieces"].value
        self.move_init(hole)
        self.update_adjacent(hole)
        # for hole_num in range(hole + 1, hole + 1 + pieces):
        hole_num = hole + 1
        val = None
        while hole_num < hole + 1 + pieces:
            actual_hole_num = hole_num % len(self.holes)
            # if player 0
            if side:
                # check to see if landing in other player's ulo
                if not (actual_hole_num == len(self.holes) - 1):
                    # if landing in ulo
                    if actual_hole_num == int((len(self.holes) / 2) - 1):
                        # if last piece is played
                        if hole_num == hole + pieces:
                            self.move_end(actual_hole_num)
                            return Move_Pieces["Move_Again"].value
                        # if last piece is not played
                        else:
                            self._move(actual_hole_num)
                    # if last piece is played
                    elif hole_num == hole + pieces:
                        self.move_end(actual_hole_num)
                        self.update_adjacent(actual_hole_num)
                        if self.holes[actual_hole_num].pieces > 1 and (
                                (actual_hole_num >= 0) and (actual_hole_num < int(len(self.holes) / 2))):
                            val = self.move(actual_hole_num, side)
                    # if last piece is not played
                    else:
                        self._move(actual_hole_num)
                        self.update_adjacent(actual_hole_num)
                else:
                    self.dec_right(actual_hole_num - 1)
                    pieces += 1
            # if player 1
            else:
                # skip opponent's ulo
                if not (actual_hole_num == int(len(self.holes) / 2) - 1):
                    # if piece placed in ulo
                    if actual_hole_num == int(len(self.holes) - 1):
                        self.inc_count_ulo(actual_hole_num)
                        if hole_num == hole + pieces:
                            self.move_end(actual_hole_num)
                            return Move_Pieces["Move_Again"].value
                        else:
                            self._move(actual_hole_num)
                    elif hole_num == hole + pieces:
                        self.move_end(actual_hole_num)
                        self.update_adjacent(actual_hole_num)
                        if self.holes[actual_hole_num].pieces > 1 and (
                                (actual_hole_num > int(len(self.holes) / 2)) and (
                                actual_hole_num < len(self.holes))):
                            val = self.move(actual_hole_num, side)
                    else:
                        self._move(actual_hole_num)
                        self.update_adjacent(actual_hole_num)
                else:
                    self.dec_right(actual_hole_num - 1)
                    pieces += 1

            hole_num += 1

        if val:
            return val
        else:
            return Move_Pieces["End_Of_Turn"].value

class Sungkala_Holes(Holes):

    def inner_move_check(self, hole: int, side: bool) -> Optional[int]:
        if side:
            if ((self.holes[hole].pieces == 0) and (
                        (hole >= 0) and (hole < int(len(self.holes) / 2)))) and self.holes[hole].adjacent > 0:
                self.captured(hole, side)
            else:
                self.move_end(hole)
                self.update_adjacent(hole)
                if self.holes[hole].pieces > 1 and (
                        (hole >= 0) and (hole < int(len(self.holes) / 2))):
                    return self.move(hole, side)
        else:
            if ((self.holes[hole].pieces == 0) and (
                        (hole > int(len(self.holes) / 2)) and (hole < len(self.holes)))) and self.holes[hole].adjacent > 0:
                self.captured(hole, side)
            else:
                self.move_end(hole)
                self.update_adjacent(hole)
                if self.holes[hole].pieces > 1 and (
                        (hole > int(len(self.holes) / 2)) and (hole < len(self.holes))):
                    return self.move(hole, side)

        return None

    # # player 0 = [0:ulo_0], player 1 = [ulo_0: ulo_1]
    # # side: True = player 0
    # # side: False = player 1
    # def move(self, hole: int, side: bool) -> int:
    #     pieces = self.holes[hole].pieces
    #     # if there are no pieces in the hole, then ya done fucked up
    #     if pieces == 0:
    #         return Move_Pieces["No_Pieces"].value
    #     self.move_init(hole)
    #     self.update_adjacent(hole)
    #     # for hole_num in range(hole + 1, hole + 1 + pieces):
    #     hole_num = hole + 1
    #     val = None
    #     while hole_num < hole + 1 + pieces:
    #         actual_hole_num = hole_num % len(self.holes)
    #         # if player 0
    #         if side:
    #             # check to see if landing in other player's ulo
    #             if not (actual_hole_num == len(self.holes) - 1):
    #                 # if landing in ulo
    #                 if actual_hole_num == int((len(self.holes) / 2) - 1):
    #                     # if last piece is played
    #                     if hole_num == hole + pieces:
    #                         self.move_end(actual_hole_num)
    #                         return Move_Pieces["Move_Again"].value
    #                     # if last piece is not played
    #                     else:
    #                         self._move(actual_hole_num)
    #                 # if last piece is played
    #                 elif hole_num == hole + pieces:
    #                     if self.holes[actual_hole_num].pieces == 0 and self.holes[actual_hole_num].adjacent > 0:
    #                         self.captured(actual_hole_num, side)
    #                     else:
    #                         self.move_end(actual_hole_num)
    #                         self.update_adjacent(actual_hole_num)
    #                         if self.holes[actual_hole_num].pieces > 1 and ((actual_hole_num >= 0) and (actual_hole_num < int(len(self.holes) / 2))):
    #                             val = self.move(actual_hole_num, side)
    #                 # if last piece is not played
    #                 else:
    #                     self._move(actual_hole_num)
    #                     self.update_adjacent(actual_hole_num)
    #             else:
    #                 self.dec_right(actual_hole_num - 1)
    #                 pieces += 1
    #         # if player 1
    #         else:
    #             # skip opponent's ulo
    #             if not (actual_hole_num == int(len(self.holes) / 2) - 1):
    #                 # if piece placed in ulo
    #                 if actual_hole_num == int(len(self.holes) - 1):
    #                     self.inc_count_ulo(actual_hole_num)
    #                     if hole_num == hole + pieces:
    #                         self.move_end(actual_hole_num)
    #                         return Move_Pieces["Move_Again"].value
    #                     else:
    #                         self._move(actual_hole_num)
    #                 elif hole_num == hole + pieces:
    #                     if self.holes[actual_hole_num].pieces == 0 and self.holes[actual_hole_num].adjacent > 0:
    #                         self.captured(actual_hole_num, side)
    #                     else:
    #                         self.move_end(actual_hole_num)
    #                         self.update_adjacent(actual_hole_num)
    #                         if self.holes[actual_hole_num].pieces > 1 and ((actual_hole_num > int(len(self.holes) / 2)) and (actual_hole_num < len(self.holes))):
    #                             val = self.move(actual_hole_num, side)
    #                 else:
    #                     self._move(actual_hole_num)
    #                     self.update_adjacent(actual_hole_num)
    #             else:
    #                 self.dec_right(actual_hole_num - 1)
    #                 pieces += 1
    #
    #         hole_num += 1
    #
    #     if val:
    #         return val
    #     else:
    #         return Move_Pieces["End_Of_Turn"].value


def main_cli():
    board = Holes(12, 4)
    hello = board.move(2, False)
    a = 0


if __name__ == '__main__':
    main_cli()