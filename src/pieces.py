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
                    if board.pieces[pos[0]][pos[1]].team == board.turn:
                        continue
                moves.append(pos)
        return moves

    def explode(self, board):
        return

    def destroy_connected(self, board, originator=None):
        pass


class Bishop(Piece):

    filename_black = "bd.png"
    filename_white = "bl.png"

    def list_possible_moves(self, board):
        multiboard_pos = (self.pos[0], self.pos[1])
        diagonals = [(1,1), (-1,-1), (-1, 1), (1, -1)]
        moves = []
        for vector in diagonals:
            clcting = True
            i = 1
            while clcting:
                calculating_position = ((i*vector[0])+multiboard_pos[0], (i*vector[1])+multiboard_pos[1])
                if calculating_position[0]<-7 or calculating_position[0]>15 or calculating_position[1]<0 or calculating_position[1]>7:
                    clcting = False
                    continue
                if calculating_position[0]<0:
                    posx = [calculating_position[0]+8, calculating_position[1]]
                elif calculating_position[0]>7:
                    posx = [calculating_position[0] - 8, calculating_position[1]]
                else:
                    posx = [calculating_position[0], calculating_position[1]]
                if (that_piece:=board.pieces[posx[0]][posx[1]]):
                    if that_piece.team != self.team:
                       moves.append(posx)
                    clcting = False
                    continue
                moves.append(posx)
                i+=1
            print('--')

        return moves


class Knight(Piece):

    filename_black = "nd.png"
    filename_white = "nl.png"

    def is_legal_move(self, pos, board, get=False):
        try:
            if board.pieces[pos[0]][pos[1]] is not None:
                if board.pieces[pos[0]][pos[1]].team == board.turn:
                    return False
        except:
            pass
        move_vectors = [(2*i, 1*j) for j in [-1, 1] for i in [-1, 1]]
        move_vectors.extend((1*i, 2*j) for j in [-1, 1] for i in [-1, 1])
        for move_vector in move_vectors:
            if (x := (pos[0]+move_vector[0], pos[1]+move_vector[1])) == self.pos:
                posx = [pos[0], pos[1]]
                if pos[0]<0:
                    posx = [pos[0]+8, pos[1]]
                if pos[0]>7:
                    posx = [pos[0] - 8, pos[1]]
                if board.pieces[posx[0]][posx[1]] is not None:
                    if board.pieces[posx[0]][posx[1]].team == board.turn:
                        return False
                if get:
                    return pos
                return True
        return False


class Rook(Piece):

    filename_black = "rd.png"
    filename_white = "rl.png"

    def list_possible_moves(self, board):
        multiboard_pos = (self.pos[0], self.pos[1])
        lines = [(1,0), (-1,0), (0, 1), (0, -1)]
        moves = []
        for vector in lines:
            clcting = True
            i = 1
            while clcting:
                calculating_position = ((i*vector[0])+multiboard_pos[0], (i*vector[1])+multiboard_pos[1])
                if calculating_position[0]<-7 or calculating_position[0]>15 or calculating_position[1]<0 or calculating_position[1]>7:
                    clcting = False
                    continue
                if calculating_position[0]<0:
                    posx = [calculating_position[0]+8, calculating_position[1]]
                elif calculating_position[0]>7:
                    posx = [calculating_position[0] - 8, calculating_position[1]]
                else:
                    posx = [calculating_position[0], calculating_position[1]]
                if (that_piece:=board.pieces[posx[0]][posx[1]]):
                    if that_piece.team != self.team:
                        moves.append(posx)
                    clcting = False
                    continue
                moves.append(posx)
                i+=1
        return moves

class King(Piece):

    filename_black = "kd.png"
    filename_white = "kl.png"

    def list_possible_moves(self, board):
        multiboard_pos = (self.pos[0], self.pos[1])
        diagonals = [(1,1), (-1,-1), (-1, 1), (1, -1), (1,0), (-1,0), (0, 1), (0, -1)]
        moves = []
        for vector in diagonals:
            clcting = True
            i = 1
            while clcting:
                calculating_position = ((i*vector[0])+multiboard_pos[0], (i*vector[1])+multiboard_pos[1])
                if calculating_position[0]<-7 or calculating_position[0]>15 or calculating_position[1]<0 or calculating_position[1]>7:
                    clcting = False
                    continue
                if calculating_position[0]<0:
                    posx = [calculating_position[0]+8, calculating_position[1]]
                elif calculating_position[0]>7:
                    posx = [calculating_position[0] - 8, calculating_position[1]]
                else:
                    posx = [calculating_position[0], calculating_position[1]]
                if (that_piece:=board.pieces[posx[0]][posx[1]]):
                    if that_piece.team != self.team:
                        if i<2:
                            moves.append(posx)
                    clcting = False
                    continue
                if i<2:
                    moves.append(posx)
                i+=1
        return moves

class Queen(Piece):

    filename_black = "qd.png"
    filename_white = "ql.png"

    def list_possible_moves(self, board):
        multiboard_pos = (self.pos[0], self.pos[1])
        diagonals = [(1,1), (-1,-1), (-1, 1), (1, -1), (1,0), (-1,0), (0, 1), (0, -1)]
        moves = []
        for vector in diagonals:
            clcting = True
            i = 1
            while clcting:
                calculating_position = ((i*vector[0])+multiboard_pos[0], (i*vector[1])+multiboard_pos[1])
                if calculating_position[0]<-7 or calculating_position[0]>15 or calculating_position[1]<0 or calculating_position[1]>7:
                    clcting = False
                    continue
                if calculating_position[0]<0:
                    posx = [calculating_position[0]+8, calculating_position[1]]
                elif calculating_position[0]>7:
                    posx = [calculating_position[0] - 8, calculating_position[1]]
                else:
                    posx = [calculating_position[0], calculating_position[1]]
                if (that_piece := board.pieces[posx[0]][posx[1]]):
                    if that_piece.team != self.team:
                        moves.append(posx)
                    clcting = False
                    continue
                moves.append(posx)
                i+=1
        return moves

class Pawn(Piece):

    filename_black = "pd.png"
    filename_white = "pl.png"

    def is_legal_move(self, pos, board, get=False):
        capture = False
        # forward = -1 if self.team == 2 else 1
        try:
            if board.pieces[pos[0]][pos[1]] is not None:
                if board.pieces[pos[0]][pos[1]].team == board.turn:
                    return False
                else:
                    capture = True
        except:
            pass
        posx = [pos[0], pos[1]]
        if pos[0]<0:
            posx = [pos[0]+8, pos[1]]
        if pos[0]>7:
            posx = [pos[0] - 8, pos[1]]
        if board.pieces[posx[0]][posx[1]] is not None:
            if board.pieces[posx[0]][posx[1]].team == board.turn:
                return False
            else:
                capture = True

        x, y = pos[0], pos[1]
        my_x, my_y = self.pos[0], self.pos[1]
        diff_x, diff_y = x-my_x, (y-my_y)
        if self.team == 1:
            if diff_y < 1: return False
            if diff_x != 0 and capture==False: return False
            if diff_y>1 and capture==True: return False
            if diff_x > 1 or diff_x < -1: return False
            if diff_y>2: return False
            if diff_y>1 and my_y != 1: return False
        elif self.team == 2:
            if diff_y > -1: return False
            if diff_x != 0 and capture==False: return False
            if diff_x > 1 or diff_x < -1: return False
            if diff_y<-1 and capture==True: return False
            if diff_y<-2: return False
            if diff_y<-1 and my_y != 6: return False

        if diff_x == 0:
            if self.team == 1:
                if board.pieces[(self.pos[0])][self.pos[1]+1] is not None or (board.pieces[(self.pos[0])][self.pos[1]+2] is not None and diff_y>1):
                    return False

            if self.team == 2:
                if board.pieces[(self.pos[0])][self.pos[1]-1] is not None or (board.pieces[(self.pos[0])][self.pos[1]-2] is not None and diff_y<-1):
                    return False

        posx = [x, y]
        if pos[0]<0:
            posx = [pos[0]+8, pos[1]]
        if pos[0]>7:
            posx = [pos[0] - 8, pos[1]]
        if board.pieces[posx[0]][posx[1]] is not None:
            if board.pieces[posx[0]][posx[1]].team == board.turn:
                return False
        return True

    def spawn_doppleganger(self, pos, board):
        x, y = pos[0], pos[1]
        my_x, my_y = self.pos[0], self.pos[1]
        diff_x, diff_y = x-my_x, (y-my_y)
        if diff_x == 0:
            if diff_y == 2 or diff_y == -2:
                board.pieces[x][y+(-1 if diff_y == 2 else 1)] = Doppleganger(self.team, self, (x, y+(-1 if diff_y == 2 else 1)))
                board.dopplegangers.append(board.pieces[x][y+(-1 if diff_y == 2 else 1)])



class Doppleganger:
    def __init__(self, team, connected: Piece, pos):
        self.team = team
        self.pos = pos
        self.connected = connected

    def explode(self, board):
        board.pieces[self.pos[0]][self.pos[1]] = None

    def destroy_connected(self, board, originator):
        if originator.__class__ == Pawn:
            board.pieces[self.connected.pos[0]][self.connected.pos[1]] = None
            board.pieces_linear.remove(self.connected)