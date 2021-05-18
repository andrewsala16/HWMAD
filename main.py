import pygame
import initdiamond
import initcross
import pygame_menu

pygame.init()
screen = pygame.display.set_mode((790, 790))


menu = pygame_menu.Menu(765, 765, 'Skip All But One Game', theme = pygame_menu.themes.THEME_SOLARIZED)

menu.add_label('Choose Which Board You Would Like To Play On')
menu.add_button('Diamond', initdiamond.run)
menu.add_button('Cross', initcross.run)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
