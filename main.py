import pygame
import sys
import os
import karakter
import pilihArena
import pilihKarakter
import pilihTingkatKesulitan
import menuUtama
import matchResult
import assetModule
import ButtonMatch
from assetModule import game_env
from pygame import mixer
from objek import Lantai

pygame.init()
mixer.init()

FPS = 60
WINDOW = pygame.display.set_mode((896, 504))
pygame.display.set_caption("Dungeon Fighter")

grounds = pygame.sprite.Group()
clock = pygame.time.Clock()

game_over = None
onscreen_chara = [None, None]
consider = arena = None
heroes = heroes1 = monster = monster_hp = heroes_hp = None

your_turn = assetModule.get_font(15).render("Your Turn", True, "yellow")
monster_turn = assetModule.get_font(15).render("Enemy Turn", True, "yellow")
win_txt = assetModule.get_font(35).render("YOU WIN!", True, "yellow")
lose_txt = assetModule.get_font(35).render("YOU LOSE!", True, "red")
game_start = assetModule.get_font(40).render("Game Start", True, "red")
game_fight = assetModule.get_font(40).render("FIGHT!!!", True, "red")
over_rect = win_txt.get_rect(center=(445, 257))
turn_rect = your_turn.get_rect(center=(458, 35))

# Membuat karakter yang sudah dipilih
def makeCharacter(onscreen_chara):
    global heroes, monster, monster_hp, heroes_hp
    if onscreen_chara[0] == 1:
        heroes = karakter.Alectrona()
    elif onscreen_chara[0] == 2:
        heroes = karakter.Nipalto()
    else:
        heroes = karakter.Salazar()
    if onscreen_chara[1] == 1:
        monster = karakter.Aposteus()
    else:
        monster = karakter.Fenrir()

# Membuat lantari
def createGrounds():
    for x in range(0, 930, 55):
        grounds.add(Lantai(x, 490, 'terrain1.png'))
        grounds.add(Lantai(x, 440, 'terrain1.png'))
        grounds.add(Lantai(x, 390, 'terrain2.png'))

# Menggambar objek ke layar
def updateScreen(arena):
    # Arena BG
    WINDOW.blit(arena.bg_img, (0, 0))
    grounds.draw(WINDOW)
    # Animasi monster dan hero
    heroes_act = heroes.animation[heroes.action][heroes.frame]
    monster_act = monster.animation[monster.action][monster.frame]
    # Hp Bar 
    # Hero
    pygame.draw.rect(WINDOW, (255, 0, 0), (100, 30, 250, 20))
    pygame.draw.rect(WINDOW, (0, 255, 0), (100, 30, (heroes.hp/heroes_hp)*250, 20))
    # Monster
    pygame.draw.rect(WINDOW, (255, 0, 0), (575, 30, 250, 20))
    pygame.draw.rect(WINDOW, (0, 255, 0), (575, 30, (monster.hp/monster_hp)*250, 20))
    # Energi Hero
    pygame.draw.rect(WINDOW, (76, 76 , 76), (100, 45, 250, 15))
    pygame.draw.rect(WINDOW, (44, 142, 212), (100, 45, 50*heroes.energi, 15))
    # BUff Gauge Monster
    pygame.draw.rect(WINDOW, (76, 76, 76), (575, 45, 250, 15))
    pygame.draw.rect(WINDOW, (237, 222, 62), (575, 45, 250/4*monster.buffmeter, 15))
    # Gambar monster dulu
    if monster.finish and not heroes.finish and not heroes.die:
        WINDOW.blit(monster_act, (monster))
        WINDOW.blit(heroes_act, (heroes))
    # Gambar hero dulu
    elif heroes.finish and not monster.finish and not heroes.die:
        WINDOW.blit(heroes_act, (heroes))
        WINDOW.blit(monster_act, (monster))
    # Gambar notif turn
    if not heroes.death and not monster.death and heroes.onfloor:
        if not heroes.finish:
            WINDOW.blit(your_turn, turn_rect)
        elif not monster.finish:
            WINDOW.blit(monster_turn, turn_rect)
    # Tampilan Window jika hero mati
    if monster.die or heroes.die:
        if heroes.die:
            WINDOW.blit(monster_act, (monster))
            if heroes.nama == 'Alectrona':
                WINDOW.blit(heroes.dead_img, (180, 165))
            elif heroes.nama == 'Nipalto':
                WINDOW.blit(heroes.dead_img, (180, 242))
    if heroes.skilled:
        WINDOW.blit(heroes.skill_projectile[heroes.frame], (heroes.skill_rect))

# Main Loop
def mainLoop(arena):
    global game_over, game_start, game_fight
    # Membuat lantai
    createGrounds()
    mixer.music.load(arena.music)
    mixer.music.play(loops=-1)
    mixer.music.set_volume(0.3)
    times = pygame.time.get_ticks()
    print(times)
    run = True
    while run:
        clock.tick(FPS)
        heroes.floor_collision(grounds)
        monster.floor_collision(grounds)
        updateScreen(arena)
        if not heroes.onfloor:
            if pygame.time.get_ticks() - times > 800:
                WINDOW.blit(game_fight, (340, 220))
            else:
                WINDOW.blit(game_start, (230, 220))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if heroes.turn % 2 == 0 and monster.finish and heroes.onfloor:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        heroes.serang()
                    if event.key == pygame.K_1 and heroes.energi >= 2:
                        heroes.skill1()
        if heroes.death or monster.death:
            if heroes.death:
                heroes.move(monster)
                if heroes.die:
                    if monster.action == 0:
                        game_over = 'lose'
                        run = False
            elif monster.death:
                monster.move(heroes)
                if monster.die:
                    if monster.action == 0:
                        game_over = 'win'
                        run = False
        else:
            if heroes.turn % 2 != 0 and heroes.finish:
                monster.serang(heroes)
            if monster.buffmeter == 4:
                monster.buff()
            if monster.buffed:
                if pygame.time.get_ticks() - monster.buff_time < 800:
                    WINDOW.blit(monster.buff_alert, (575, 13))
                else:
                    monster.buffed = False
                    monster.finish = True
                    heroes.finish = False
        if heroes.move_l or heroes.move_r:
            heroes.move(monster)
        if monster.move_l or monster.move_r:
            monster.move(heroes)
        if heroes.skilled:
            heroes.projectileCollide(monster)
        ButtonMatch.matchButton(WINDOW,heroes,monster)
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

# Pilih tingkat kesulitan
def selectDifficulty():
    global onscreen_chara, monster_hp, heroes_hp
    difficulty = pilihTingkatKesulitan.main()
    if difficulty != 'back' :
        makeCharacter(onscreen_chara)
        if difficulty == 'easy':
            monster.hp = monster.hp * 1
        if difficulty == 'medium' :
            monster.hp = monster.hp * 1.15 
        if difficulty == 'hard' :
            monster.hp = monster.hp * 1.25
        monster_hp = monster.hp
        heroes_hp = heroes.hp
    else:
        pilihLawan(onscreen_chara)

# Permainan selesai
def gameOver(text, image, time):
    global over_rect
    while pygame.time.get_ticks() - time < 3000:
        WINDOW.blit(image, (0, 0))
        WINDOW.blit(text, over_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

# Mulai permainan
def gameStart():
    global arena, consider, onscreen_chara, win_txt, lose_txt, over_rect
    pilihKaraktermu(onscreen_chara)
    arena = pilihArena.Arena()
    if arena.state == 'Back':
        selectDifficulty()
    mainLoop(arena)    
    if game_over != None:
        time = pygame.time.get_ticks()
        over_screen = os.path.join(f"{game_env}", "game_over.jpg")
        image = pygame.image.save(WINDOW, over_screen)
        image = pygame.image.load(over_screen)
        if game_over == 'win':
            gameOver(win_txt, image, time)
        else:
            gameOver(lose_txt, image, time)
        consider = matchResult.akhirpertandingan(image, grounds)
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
    