import pygame


class Piece:

    filename_black = "Null"
    filename_white = "Null"

    def __init__(self, team, pos):
        self.team = team
        self.pos = pos
        self.surf = pygame.transform.scale(pygame.image.load("../images/"+(self.__class__.filename_white if team == 1 else self.__class__.filename_black)), (100, 100))

    def list_possible_moves(self, board):
        moves = []
        for posx in [(i, j) for i in range(24) for j in range(8)]:
            pos = [posx[0]-8, posx[1]]
            if self.is_legal_move(pos, board):
                if pos[0]<0:
                    pos = [pos[0]+8, pos[1]]
                if pos[0]>7:
                    pos = [pos[0] - 8, pos[1]]
                if board.pieces[pos[0]][pos[1]] is not None:
                    continue
                moves.append(pos)
        return moves


class Bishop(Piece):

    filename_black = "bd.png"
    filename_white = "bl.png"


class Knight(Piece):

    filename_black = "nd.png"
    filename_white = "nl.png"

    def is_legal_move(self, pos, board):
        try:
            if board.pieces[pos[0]][pos[1]] is not None:
                return False
        except:
            pass
        move_vectors = [(2*i, 1*j) for j in [-1, 1] for i in [-1, 1]]
        move_vectors.extend((1*i, 2*j) for j in [-1, 1] for i in [-1, 1])
        for move_vector in move_vectors:
            print(move_vector, pos, (pos[0]+move_vector[0], pos[1]+move_vector[1]), self.pos)
            if (x := (pos[0]+move_vector[0], pos[1]+move_vector[1])) == self.pos:
                return True
        return False

    def getis_legal_move(self, pos, board):
        try:
            if board.pieces[pos[0]][pos[1]] is not None:
                return False
        except:
            pass
        move_vectors = [(2*i, 1*j) for j in [-1, 1] for i in [-1, 1]]
        move_vectors.extend((1*i, 2*j) for j in [-1, 1] for i in [-1, 1])
        for move_vector in move_vectors:
            # print(move_vector, pos, (pos[0]+move_vector[0], pos[1]+move_vector[1]), self.pos)
            if (x := (pos[0]+move_vector[0], pos[1]+move_vector[1])) == self.pos:
                posx = [pos[0], pos[1]]
                if pos[0]<0:
                    posx = [pos[0]+8, pos[1]]
                if pos[0]>7:
                    posx = [pos[0] - 8, pos[1]]
                if board.pieces[posx[0]][posx[1]] is not None:
                    return False
                return pos
        return False


class Rook(Piece):

    filename_black = "rd.png"
    filename_white = "rl.png"


class King(Piece):

    filename_black = "kd.png"
    filename_white = "kl.png"


class Queen(Piece):

    filename_black = "qd.png"
    filename_white = "ql.png"


class Pawn(Piece):

    filename_black = "pd.png"
    filename_white = "pl.png"