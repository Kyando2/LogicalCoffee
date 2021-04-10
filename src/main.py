import pygame

from board import Board

pygame.init()

dis = pygame.display.set_mode((820,820))
pygame.display.update()
pygame.display.set_caption("Telechess")

running = True

board = Board(dis)

while running:
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            board.select(pos)

        if event.type == pygame.QUIT:
            running = False

    board.update()
    pygame.display.update()