import pygame
from code.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from code.Level import Level
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run() # recebe o retorno do menu
            
            # opções de escolha de nivel de jogo com diferentes modos de jogar
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return) # inicialização da classe nivel
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit() # fecha a janela
                quit() # encerra jogo
            else:
                pass
            
