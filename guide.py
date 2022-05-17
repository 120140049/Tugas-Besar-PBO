import pygame,sys
from assetModule import guide_img
from button import Button
from assetModule import game_env, get_font
from main import mainMenu
pygame.init()

FPS=60
FramePerSec=pygame.time.Clock()
WINDOW = pygame.display.set_mode((896, 504))
pygame.display.set_caption("Game Guide")
posisi_mouse=pygame.mouse.get_pos()

class Background():
    Tombol_back = Button(image=pygame.image.load(f"{game_env}/button2.png"),
                pos=(100, 50), text_input="Back", font=get_font(15))
    def __init__(self):
        self.background=pygame.image.load(guide_img)
        self.rectBG=self.background.get_rect()
        
        self.bgY1=0
        self.bgX1=0

        self.sensitivity=35

    def scrollDown(self):
        if self.bgY1>=-1930:
            self.bgY1-=self.sensitivity
        
    def scrollUp(self):
        if self.bgY1<=0:
            self.bgY1+=self.sensitivity
        
    def render(self):
        WINDOW.blit(self.background,(self.bgX1,self.bgY1))
        self.Tombol_back.update(WINDOW)

bg=Background()

def main():
    while True:
        bg.render()
        Posisi_Mouse = pygame.mouse.get_pos()
        bg.Tombol_back.changeColor(Posisi_Mouse)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bg.Tombol_back.checkForInput(Posisi_Mouse) and event.button == 1:
                    return mainMenu()
                if event.button == 4:
                    bg.scrollUp()
                    bg.render()
                if event.button == 5:
                    bg.scrollDown()
                    bg.render()

        pygame.display.flip()
        #pygame_widgets.update(event)
        FramePerSec.tick(FPS)   