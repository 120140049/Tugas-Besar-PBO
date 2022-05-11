import pygame
import sys
import karakter
import assetModule
import pilihArena
import pilihKarakter
import pilihTingkatKesulitan
import menuUtama
import matchResult
from pygame import mixer
from objek import Lantai

pygame.init()
mixer.init()

FPS = 60
WINDOW = pygame.display.set_mode((896, 504))
pygame.display.set_caption("Dungeon Fighter")

grounds = pygame.sprite.Group()
clock = pygame.time.Clock()

game_over = False
onscreen_chara = [None, None]
consider = arena = None
heroes = heroes1 = monster = monster_hp = heroes_hp = None

your_turn = assetModule.get_font(15).render("Your Turn", True, "yellow")
monster_turn = assetModule.get_font(15).render("Enemy Turn", True, "yellow")

def selectCharacter(onscreen_chara):
    global heroes, monster, monster_hp, heroes_hp #heroes1
    # print("1. Alectrona\n2. Nipalto\n3. Salazar")
    # x = int(input("Masukkan Karakter yang diinginkan:"))
    if onscreen_chara[0] == 1:
        heroes = karakter.Alectrona()
    elif onscreen_chara[0] == 2:
        heroes = karakter.Nipalto()
    else:
        heroes = karakter.Salazar()
    # heroes = karakter.Alectrona()
    # heroes = karakter.Salazar()
    if onscreen_chara[1] == 1:
        monster = karakter.Aposteus()
    else:
        monster = karakter.Fenrir()
    # monster = karakter.Fenrir()

def createGrounds():
    for x in range(0, 930, 55):
        grounds.add(Lantai(x, 490, 'terrain1.png'))
        grounds.add(Lantai(x, 440, 'terrain1.png'))
        grounds.add(Lantai(x, 390, 'terrain2.png'))

def updateScreen(arena):
    # global your_turn, monster_turn
    WINDOW.blit(arena.bg_img, (0, 0))
    grounds.draw(WINDOW)
    heroes_act = heroes.animation[heroes.action][heroes.frame]
    #heroes1_act = heroes1.animation[heroes1.action][heroes1.frame]
    monster_act = monster.animation[monster.action][monster.frame]
    # WINDOW.blit(heroes1_act, (heroes1))
    # Heroes Health
    pygame.draw.rect(WINDOW, (255, 0, 0), (100, 30, 250, 20))
    pygame.draw.rect(WINDOW, (0, 255, 0), (100, 30, (heroes.hp/heroes_hp)*250, 20))
    # Monster Health
    pygame.draw.rect(WINDOW, (255, 0, 0), (575, 30, 250, 20))
    pygame.draw.rect(WINDOW, (0, 255, 0), (575, 30, (monster.hp/monster_hp)*250, 20))
    pygame.draw.rect(WINDOW, (76, 76 , 76), (100, 45, 250, 15))
    # Heroes Energy
    pygame.draw.rect(WINDOW, (44, 142, 212), (100, 45, 50*heroes.energi, 15))
    # Monster Buff Gauge
    pygame.draw.rect(WINDOW, (76, 76, 76), (575, 45, 250, 15))
    pygame.draw.rect(WINDOW, (237, 222, 62), (575, 45, 250/4*monster.buffmeter, 15))
    # pygame.draw.rect(WINDOW, (255, 0, 128), heroes, 2)
    # pygame.draw.rect(WINDOW, (255, 0, 128), monster, 2)
    if monster.finish:
        WINDOW.blit(monster_act, (monster))
        WINDOW.blit(heroes_act, (heroes))
        your_rect = your_turn.get_rect()
        your_rect.center = [458, 35]
    else:
        WINDOW.blit(heroes_act, (heroes))
        WINDOW.blit(monster_act, (monster))
        monster_rect = your_turn.get_rect()
        monster_rect.center = [458, 35]
    if monster.finish and not heroes.finish:
        WINDOW.blit(your_turn, your_rect)
    elif heroes.finish and not monster.finish:
        WINDOW.blit(monster_turn, monster_rect)


# Main Loop
def mainLoop(arena):
    global game_over
    createGrounds()
    mixer.music.load(arena.music)
    mixer.music.play(loops=-1)
    mixer.music.set_volume(0.3)
    heroes.floor_collision(grounds)
    monster.floor_collision(grounds)
    run = True
    while run:
        if (monster.hp <= 0 or heroes.hp <= 0) and \
            (monster.action == 0 and heroes.action == 0):
                run = False
                game_over = True
        clock.tick(FPS)
        updateScreen(arena)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if heroes.turn % 2 == 0 and monster.finish and heroes.action == 0 \
                and heroes.onground:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # highlight_btn(attack)
                        heroes.serang()
                    if event.key == pygame.K_1:
                        # highlight_btn(skill1)
                        heroes.skill1()
        if heroes.move_l or heroes.move_r:
            heroes.move(monster)
        if monster.move_l or monster.move_r:
            monster.move(heroes)
        if heroes.turn % 2 != 0 and heroes.finish:
            monster.serang(heroes)
        if monster.buffmeter == 4:
            monster.buff()
        if monster.buffed:
            if pygame.time.get_ticks() - monster.buff_time < 650:
                WINDOW.blit(monster.buff_alert, (575, 13))
            else:
                monster.buffed = False
                monster.finish = True
                heroes.finish = False

        heroes.update(monster)
        monster.update(heroes)
        pygame.display.flip()

def pilihKaraktermu(onscreen_chara):
    onscreen_chara[0] = pilihKarakter.pilihhero()
    if onscreen_chara[0] == 4:
        mainMenu()
    else:
        pilihLawan(onscreen_chara)

def pilihLawan(onscreen_chara):
    onscreen_chara[1] = pilihKarakter.pilihmonster()
    if onscreen_chara[1] != 3:
        selectDifficulty()
    else:
        pilihKaraktermu(onscreen_chara)

def selectDifficulty():
    global onscreen_chara, monster_hp, heroes_hp
    difficulty = pilihTingkatKesulitan.main()
    if difficulty != 'back' :
        selectCharacter(onscreen_chara)
        if difficulty == 'easy':
            pass
            #heroes.damage = heroes.damage * 1
        elif difficulty == 'medium' :
            monster.hp = monster.hp * 1.15 
            #heroes.damage = heroes.damage * 1.15
        elif difficulty == 'hard' :
            monster.hp = monster.hp * 1.25
            #heroes.damage = heroes.damage * 1.25
        monster_hp = monster.hp
        heroes_hp = heroes.hp
    else:
        pilihLawan(onscreen_chara)

def gameStart():
    global arena, consider, onscreen_chara
    pilihKaraktermu(onscreen_chara)
    arena = pilihArena.Arena()
    if arena.state == 'Back':
        selectDifficulty()
    mainLoop(arena)    
    if game_over:
        consider = matchResult.akhirpertandingan(arena.bg_img, grounds)
        if consider:
            mixer.music.stop()
            mainMenu()
        else:
            mixer.music.stop()
            gameStart()


def mainMenu():
    x = menuUtama.menuUtama()
    if x == 'Start':
        gameStart()
    else:
        sys.exit()

if __name__ == "__main__":
    mainMenu()
    