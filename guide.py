import pygame,sys,pygame_widgets
from pygame.locals import *
from assetModule import guide_img
from button import Button
from assetModule import game_env, get_font
pygame.init()

FPS=60
FramePerSec=pygame.time.Clock()
WINDOW = pygame.display.set_mode((896, 504))
pygame.display.set_caption("Game Guide")
posisi_mouse=pygame.mouse.get_pos()

class Background():
    Tombol_back = Button(image=pygame.image.load(f"{game_env}/button2.png"),
                pos=(100, 50), text_input="Back", font=get_font(15), base_color="white",
                hovering_color="red")
    def __init__(self):
        self.background=pygame.image.load(guide_img)
        self.rectBG=self.background.get_rect()
        
        self.bgY1=0
        self.bgX1=0

        # self.bgY2=self.rectBG.height
        # self.bgX2=0

        self.sensitivity=35

    def scrollDown(self):
        if self.bgY1>=-2000:
            print(self.rectBG.height)
            print('down',self.bgY1)
            self.bgY1-=self.sensitivity
            #self.bgY1-=0
        # if self.bgY2<=-self.rectBG.height:
        #     self.bgY2-=0
        #else:
            #self.bgY1-=self.sensitivity
            # self.bgY2-=self.sensitivity
        # while self.bgY1 > self.rectBG.height and self.bgY2 > self.rectBG.height:
        #     self.bgY1-=self.sensitivity
        #     self.bgY2-=self.sensitivity

        
    def scrollUp(self):
        if self.bgY1<=0:
            print(self.rectBG.height)
            print('up',self.bgY1)
            self.bgY1+=self.sensitivity
            #self.bgY1+=0
        # if self.bgY2>=self.rectBG.height:
        #     self.bgY2+=0
        #else:
            #self.bgY1+=self.sensitivity
            # self.bgY2+=self.sensitivity
        # while self.bgY1 < self.rectBG.height and self.bgY2 < self.rectBG.height:
        #     self.bgY1+=self.sensitivity
        #     self.bgY2+=self.sensitivity

        
    def render(self):
        WINDOW.blit(self.background,(self.bgX1,self.bgY1))
        # WINDOW.blit(self.background,(self.bgX2,self.bgY2))
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
            if event.type == MOUSEBUTTONDOWN:
                if bg.Tombol_back.checkForInput(Posisi_Mouse):
                    print("tombol back")
                if event.button == 4 :
                    bg.scrollUp()
                    bg.render()
                if event.button == 5 :
                    bg.scrollDown()
                    bg.render()

        
        pygame.display.update()
        pygame_widgets.update(event)
        FramePerSec.tick(FPS)

main()

    