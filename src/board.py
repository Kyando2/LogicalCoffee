import pygame

from pieces import Rook, Knight, Bishop, Queen, King, Pawn

import time

class Board:
    def __init__(self, display):
        self.pieces = {i: {j: None for j in range(8)} for i in range(8)} # ROW (10 ;; 0-9) : COLUMN (8 ;; 0-7)
        self.pieces_linear = []
        self.screen = display
        self.selected = None
        self.ys = pygame.transform.scale(pygame.image.load("../images/ys.png"), (60,60))
        self.background = pygame.transform.scale(pygame.image.load("../images/cb.png"), (800,800))
        self.initialize_position()
        self.to_blit = []
        self.turn = 1

    def initialize_position(self):
        # Creates pieces of specified type `cls` for both teams on the provided Iterator of tuples `st`
        def create_piece(st, cls):
            for coord in st:
                x, y = coord[0], coord[1] # Unpack coord
                self.pieces[x][y] = cls(1, (x, y))
                self.pieces_linear.append(self.pieces[x][y])
                self.pieces[x][(7-y)] = cls(2, (x, (7-y)))
                self.pieces_linear.append(self.pieces[x][(7-y)])
        # Create all the pieces
        create_piece(((0, 0), (7, 0)), Rook)
        create_piece(((1, 0), (6, 0)), Knight)
        create_piece(((2, 0), (5, 0)), Bishop)
        create_piece([(3, 0)], Queen)
        create_piece([(4, 0)], King)
        create_piece([(x, 1) for x in range(8)], Pawn)

    def update(self):
        self.screen.blit(self.background, (0,0))
        for piece in self.pieces_linear:
            # Blit the piece's image on the screen
            self.screen.blit(piece.surf, find_screen_location_from_position(piece))
        for item in self.to_blit:
            self.screen.blit(item[0], item[1])

    def get_piece_from_mouse_position(self, pos):
        pos = (int((str(pos[0])[0] if len(list(str(pos[0])))==3 else "0")), 7-int((str(pos[1])[0] if len(list(str(pos[1])))==3 else "0")))
        if (found_piece := self.pieces[pos[0]][pos[1]]) is not None:
            return found_piece
        return None

    def select(self, pos):
        self.to_blit.clear()
        selected_piece = self.get_piece_from_mouse_position(pos)
        print(selected_piece)
        if selected_piece:
            if selected_piece.team == self.turn:
                self.selected = selected_piece
                # Show possible moves
                for pos in selected_piece.list_possible_moves(board=self):
                    location = (find_screen_location_from_position(coords=pos)[0]+20, find_screen_location_from_position(coords=pos)[1]+20)
                    self.to_blit.append((self.ys, location))
        else:
            if self.selected:
                if self.selected.team == self.turn:
                    if self.selected.is_legal_move((int((str(pos[0])[0] if len(list(str(pos[0])))==3 else "0")), 7-int((str(pos[1])[0] if len(list(str(pos[1])))==3 else "0"))), self):
                        old_pos = self.selected.pos
                        self.selected.pos = self.selected.getis_legal_move((int((str(pos[0])[0] if len(list(str(pos[0])))==3 else "0")), 7-int((str(pos[1])[0] if len(list(str(pos[1])))==3 else "0"))), self)
                        self.pieces[old_pos[0]][old_pos[1]] = None
                        self.pieces[self.selected.pos[0]][self.selected.pos[1]] = self.selected
                        self.switch_turn()


    def switch_turn(self):
        self.turn = 3-self.turn


def find_screen_location_from_position(piece=None, coords=None):
    if piece is None:
        local_pos = coords
    else:
        local_pos = piece.pos
    pub_pos = (local_pos[0], 7-local_pos[1])
    return (pub_pos[0]*100, pub_pos[1]*100)