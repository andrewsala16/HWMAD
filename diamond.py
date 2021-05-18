import pygame
import initdiamond

black = 0, 0, 0
orange = 255, 127, 0
white = 255, 255, 255
dark_green = 128, 128, 128
green = 89, 153, 78
font = None


class Cell:
    rect = pygame.Rect(0, 0, 94, 94)
    mhover = False
    driver = None
    sel = False

    def on_click(self):
        self.driver.on_cell(self)


class Board:
    cells = None
    rect = None

    def __init__(self):
        self.rect = pygame.Rect(20, 80, 700, 700)
        self.cells = []
        for i in range(7):
            self.cells.append([])
            for j in range(7):
                self.cells[i].append(None)

        num = 1
        at = (2, 0)
        while num < 26:
            if num == 2:
                at = (2, 1)
            elif num == 5:
                at = (1, 2)
            elif num == 10:
                at = (0, 3)
            elif num == 17:
                at = (1, 4)
            elif num == 22:
                at = (2, 5)
            elif num == 25:
                at = (3, 6)

            else:
                at = (at[0] + 1, at[1])
            cell = Cell()
            cell.num = num
            cell.at = at
            cell.empty = False
            cell.bruh = False
            cell.color = black
            cell.rect = cell.rect.move(100 * at[0] + self.rect.left + 3, 100 * at[1] + self.rect.top + 3)

            self.cells[at[0]][at[1]] = cell

            num += 1

    def draw(self, surf):
        for i in range(7):
            for j in range(7):
                if self.cells[i][j]:
                    self.cells[i][j].empty = False
                    rect = self.cells[i][j].rect
                    color = green if self.cells[i][j].mhover else dark_green
                    color = white if self.cells[i][j].sel else color
                    pygame.draw.rect(surf, color, rect)
                    self.cells[3][3].empty = True

                    if not self.cells[i][j].empty:
                        rect = pygame.Rect(rect.left + 22, rect.top + 22, 50, 50)
                        pygame.draw.rect(surf, orange, rect)


class MouseHandler:
    pmon = None
    objs = []

    def add(self, obj):
        self.objs.append(obj)

    def handle_motion(self):
        mpos = pygame.mouse.get_pos()
        mon = self.mouse_on(mpos)

        if mon:
            mon.mhover = True
        if self.pmon and self.pmon != mon:
            self.pmon.mhover = False

        self.pmon = mon

    def handle_click(self):
        mpos = pygame.mouse.get_pos()
        mon = self.mouse_on(mpos)
        if mon: mon.on_click()

    def mouse_on(self, mpos):
        for obj in self.objs:
            if obj.rect.collidepoint(mpos):
                return obj
        return None


class Driver:
    board = None
    reset = None
    c_sel = None
    done = False
    actionmoves = 0
    undo_q = []

    def __init__(self, board):
        self.board = board
        self.centerboy()
        self.end_it()

    def action(self, c1, c2):

        if c2.at == (c1.at[0] + 2, c1.at[1]):
            mcell = self.board.cells[c1.at[0] + 1][c1.at[1]]
            self.actionmoves += 1
        elif c2.at == (c1.at[0] - 2, c1.at[1]):
            mcell = self.board.cells[c1.at[0] - 1][c1.at[1]]
            self.actionmoves += 1
        elif c2.at == (c1.at[0], c1.at[1] + 2):
            mcell = self.board.cells[c1.at[0]][c1.at[1] + 1]
            self.actionmoves += 1
        elif c2.at == (c1.at[0], c1.at[1] - 2):
            mcell = self.board.cells[c1.at[0]][c1.at[1] - 1]
            self.actionmoves += 1
        else:
            return

        if mcell.empty:
            return


        while self.actionmoves > 21:
            self.end_it()

        mcell.empty = True
        c1.empty = True
        c2.empty = False

        self.undo_q.append((c1, mcell, c2))

    def end_it(self):
        non_empties = 0
        non_empties_nomoves = 0

        for i in range(7):
            for j in range(7):
                if ((j == 0 and i == 0) or (j == 0 and i == 1) or (j == 1 and i == 1) or (j == 1 and i == 0) or
                        (j == 5 and i == 0) or (j == 5 and i == 1) or (j == 6 and i == 0) or (j == 6 and i == 1) or
                        (j == 0 and i == 5) or (j == 0 and i == 6) or (j == 1 and i == 5) or (j == 1 and i == 6) or
                        (j == 5 and i == 5) or (j == 5 and i == 6) or (j == 6 and i == 5) or (j == 6 and i == 6)):
                    return

                else:
                    if self.board.cells[i][j] == (self.board.cells[i][j + 1] and self.board.cells[i + 1][j]):
                        non_empties += 1

        for i in range(7):
            for j in range(7):
                if not self.board.cells[i][j].empty:
                    if self.board.cells[i - 1][j].empty:
                        if self.board.cells[i + 1][j].empty:
                            if self.board.cells[i][j + 1].empty:
                                if self.board.cells[i][j - 1].empty:
                                    non_empties_nomoves += 1
                    else:
                        return

            if non_empties_nomoves == non_empties:
                initdiamond.run()

    def on_cell(self, cell):
        if self.c_sel:
            self.action(self.c_sel, cell)
            self.c_sel.sel = False
            self.c_sel = None
        else:
            if not cell.empty:
                self.c_sel = cell
                self.c_sel.sel = True

    def centerboy(self):
        self.board.cells[3][3].empty = True


class Heading:
    rect = pygame.Rect(0, 0, 720, 80)
    text = "Skip All But One"

    def draw(self, surf):
        text = font.render(self.text, True, white)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        surf.blit(text, text_rect)