import pygame
import sys
import karakter
import assetModule
import pilihArena
import pilihKarakter
import pilihTingkatKesulitan
import menuUtama
from pygame import mixer
from objek import Lantai

pygame.init()
mixer.init()
WINDOW = pygame.display.set_mode((896, 504))
pygame.display.set_caption("Dungeon Fighter")
FPS = 60
clock = pygame.time.Clock()

grounds = pygame.sprite.Group()
heroes = heroes1 = monster = None

def selectCharacter():
    global heroes, monster #heroes1
    # print("1. Alectrona\n2. Nipalto\n3. Salazar")
    # x = int(input("Masukkan Karakter yang diinginkan:"))
    # if x % 1 == 0:
    heroes = karakter.Nipalto()
    # heroes = karakter.Alectrona()
    # heroes = karakter.Salazar()
    monster = karakter.Aposteus()
    # monster = karakter.Fenrir()

def createGrounds():
    for x in range(0, 930, 55):
        grounds.add(Lantai(x, 490, 'terrain1.png'))
        grounds.add(Lantai(x, 440, 'terrain1.png'))
        grounds.add(Lantai(x, 390, 'terrain2.png'))

def updateScreen(arena):
    WINDOW.blit(arena.bg_img, (0, 0))
    grounds.draw(WINDOW)
    heroes_act = heroes.animation[heroes.action][heroes.frame]
    #heroes1_act = heroes1.animation[heroes1.action][heroes1.frame]
    monster_act = monster.animation[monster.action][monster.frame]
    WINDOW.blit(monster_act, (monster))
    WINDOW.blit(heroes_act, (heroes))
    # WINDOW.blit(heroes1_act, (heroes1))
    # pygame.draw.rect(WINDOW, (255, 0, 128), heroes, 2)
    # pygame.draw.rect(WINDOW, (255, 0, 128), monster, 2)

# Main Loop
def mainLoop(arena):
    selectCharacter()
    createGrounds()
    mixer.music.load(arena.music)
    mixer.music.play(loops=-1)
    mixer.music.set_volume(0.3)
    music_duration = pygame.time.get_ticks()
    run = True
    while run:
        #clock.tick(FPS)
        heroes.floor_collision(grounds)
        #heroes1.floor_collision(grounds)
        monster.floor_collision(grounds)
        updateScreen(arena)
        if heroes.move_l or heroes.move_r:
            heroes.move(monster)
        if monster.move_l or monster.move_r:
            monster.move(heroes)
        if heroes.turn % 2 != 0 and heroes.finish:
            monster.serang(heroes)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if heroes.turn % 2 == 0 and monster.finish and heroes.action == 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # highlight_btn(attack)
                        heroes.serang(monster)
                    if event.key == pygame.K_1:
                        # highlight_btn(skill1)
                        heroes.skill1()
                    if event.key == pygame.K_2:
                        # highlight_btn(skill2)
                        heroes.skill2()
        heroes.update(monster)
        monster.update(heroes)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    # y = pilihKarakter.selectCharacter()
    x = menuUtama.menuUtama()
    if x == 'Start':
        arena = pilihArena.Arena()
    else:
        sys.exit()
    pilihKarakter.pilihKarakter()
    mainLoop(arena)