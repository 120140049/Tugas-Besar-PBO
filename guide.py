import pygame,sys
from pygame.locals import *
import random, time
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

        self.sensitivity=10

    def scrolldown(self):
        self.bgY1-=self.sensitivity
        self.bgY2-=self.sensitivity

        if self.bgY1<=-self.rectBG.height:
            self.bgY1=self.rectBG.height
        if self.bgY2<=-self.rectBG.height:
            self.bgY2=self.rectBG.height
        
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
            if event.type == KEYDOWN:
                if event.key == pygame.K_DOWN :
                    bg.scrolldown()
                    bg.render()

        
        pygame.display.update()
        FramePerSec.tick(FPS)


main()
    