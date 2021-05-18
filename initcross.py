import pygame
import cross

def run():
    pygame.init()
    screen = pygame.display.set_mode((790, 790))
    done = False
    cross.font = pygame.font.SysFont('arial', 32)

    board = cross.Board()
    head = cross.Heading()
    mhandler = cross.MouseHandler()
    driver = cross.Driver(board)


    for i in range(7):
        for j in range(7):
            if board.cells[i][j]:
                board.cells[i][j].driver = driver
                mhandler.add(board.cells[i][j])


    while not driver.done and not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mhandler.handle_motion()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mhandler.handle_click()
        screen.fill(cross.black)
        board.draw(screen)
        head.draw(screen)
        pygame.display.flip()



    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            screen.fill(cross.black)
            pygame.display.flip()
            head.draw(screen)