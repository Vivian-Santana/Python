from genericpath import getsize
from tkinter.font import Font
import pygame
import pygame.image
from code.Const import COLOR_ORANGE, COLOR_WHITE, COLOR_YELLOW, MENU_OPTION, WIN_WIDTH


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)# retangulo começa no canto superior esq
    
    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # desenha as imagens
            self.window.blit(source=self.surf, dest=self.rect) # faz a img aparecer no retangulo criado
            self.menu_text(text_size = 50, text="Mountain", text_color= COLOR_ORANGE, text_center_pos= ((WIN_WIDTH / 2), 70))
            self.menu_text(text_size = 50, text="Shooter", text_color= COLOR_ORANGE, text_center_pos= ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                 
                if i == menu_option:
                      self.menu_text(text_size = 20, text= MENU_OPTION[i], text_color= COLOR_YELLOW, text_center_pos= ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                      self.menu_text(text_size = 20, text= MENU_OPTION[i], text_color= COLOR_WHITE, text_center_pos= ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip() # atualiza na tela

            # checa todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # fecha a janela
                    quit() # encerra pygame
                if event.type == pygame.KEYDOWN:
                     # Navegar no menu - seta para baixo ⬇️
                     if event.key == pygame.K_DOWN: 
                        if menu_option < len(MENU_OPTION) -1: # enquanto opção do menu for menor q -1 (enquanto não chegar no fim do menu)
                               menu_option += 1    # itera as opções do menu
                        else:
                             menu_option = 0  # quando chega no fim do menu, da um reset e volta para o começo

                    # Navegar no menu - seta para cima ⬆️
                     if event.key == pygame.K_UP:
                        if menu_option > 0: # quando chegar no topo em 0 volta para a ultima opção
                               menu_option -= 1               
                        else:
                             menu_option = len(MENU_OPTION) -1 # retorna para o final do menu

                    # enter = selecionar uma opção ▶️
                     if event.key == pygame.K_RETURN:
                          return MENU_OPTION[menu_option]

    # mesmo processo de desenhar a img só q para texto
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
            text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)
