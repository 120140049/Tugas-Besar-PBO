import pygame,sys
from pygame.locals import *
from assetModule import guide_img
pygame.init()

FPS=60
FramePerSec=pygame.time.Clock()
WINDOW = pygame.display.set_mode((896, 504))
pygame.display.set_caption("Game Guide")

class Background():
    def __init__(self):
        self.background=pygame.image.load(guide_img)
        self.rectBG=self.background.get_rect()
        
        self.bgY1=0
        self.bgX1=0

        self.bgY2=self.rectBG.height
        self.bgX2=0

        self.sensitivity=25

    def scrollDown(self):
        if self.bgY1<=-self.rectBG.height:
            self.bgY1-=0
        if self.bgY2<=-self.rectBG.height:
            self.bgY2-=0
        else:
            self.bgY1-=self.sensitivity
            self.bgY2-=self.sensitivity
        # while self.bgY1 > self.rectBG.height and self.bgY2 > self.rectBG.height:
        #     self.bgY1-=self.sensitivity
        #     self.bgY2-=self.sensitivity

        
    def scrollUp(self):
        if self.bgY1>=self.rectBG.height:
            self.bgY1+=0
        if self.bgY2>=self.rectBG.height:
            self.bgY2+=0
        else:
            self.bgY1+=self.sensitivity
            self.bgY2+=self.sensitivity
        # while self.bgY1 < self.rectBG.height and self.bgY2 < self.rectBG.height:
        #     self.bgY1+=self.sensitivity
        #     self.bgY2+=self.sensitivity

        
    def render(self):
        WINDOW.blit(self.background,(self.bgX1,self.bgY1))
        WINDOW.blit(self.background,(self.bgX2,self.bgY2))

bg=Background()


def main():
    while True:
        bg.render()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 4 :
                    bg.scrollUp()
                    bg.render()
                if event.button == 5 :
                    bg.scrollDown()
                    bg.render()

        
        pygame.display.update()
        FramePerSec.tick(FPS)

    