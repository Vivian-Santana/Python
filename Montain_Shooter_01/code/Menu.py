from genericpath import getsize
from tkinter.font import Font
import pygame
import pygame.image
from code.Const import WIN_WIDTH


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)# retangulo começa no canto superior esq
    
    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect) # faz a img aparecer no retangulo criado
            self.menu_text(text_size = 50, text="Mountain", text_color=(255, 128, 0), text_center_pos= ((WIN_WIDTH / 2), 70))
            
            pygame.display.flip() # atualiza na tela

            # checar todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # fecha a janela
                    quit() # encerra pygame

    # mesmo processo de desenhar a img só q para texto
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
            text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)
