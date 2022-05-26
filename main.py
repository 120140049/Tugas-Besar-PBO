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
import guide
from assetModule import game_env, get_font, menu_bgm
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
heroes = heroes1 = monster  = heroes_hp = button = mouse_pos = None

your_turn = assetModule.get_font(15).render("Your Turn", True, "red")
monster_turn = assetModule.get_font(15).render("Enemy Turn", True, "red")
win_txt = assetModule.get_font(35).render("YOU WIN!", True, "yellow")
lose_txt = assetModule.get_font(35).render("YOU LOSE!", True, "red")
game_start = assetModule.get_font(40).render("Game Start", True, "red")
game_fight = assetModule.get_font(40).render("FIGHT!!!", True, "red")
over_rect = win_txt.get_rect(center=(440, 240))
turn_rect = your_turn.get_rect(center=(455, 35))

# Membuat karakter yang sudah dipilih
def makeCharacter(onscreen_chara, difficulty):
    global heroes, monster, heroes_hp
    if onscreen_chara[0] == 1:
        heroes = karakter.Alectrona()
    elif onscreen_chara[0] == 2:
        heroes = karakter.Nipalto()
    else:
        heroes = karakter.Salazar()
    if onscreen_chara[1] == 1:
        monster = karakter.Aposteus()
        if difficulty == 'easy':
            pass
        if difficulty == 'medium' :
            monster.heal = int(monster.hp * 0.05)
        if difficulty == 'hard' :
            monster.heal = int(monster.hp * 0.066)
        monster.buff_alert = get_font(15).render(f"HP +{monster.heal}", True, "green")
    else:
        monster = karakter.Fenrir()
        if difficulty == 'easy':
            pass
        if difficulty == 'medium' :
            monster.buff_dmg = 0.12
        if difficulty == 'hard' :
            monster.buff_dmg = 0.2

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
    pygame.draw.rect(WINDOW, (255, 0, 0), (80, 30, 250, 20))
    pygame.draw.rect(WINDOW, (0, 255, 0), (80, 30, (heroes.hp/heroes_hp)*250, 20))
    # Monster
    pygame.draw.rect(WINDOW, (255, 0, 0), (575, 30, 250, 20))
    pygame.draw.rect(WINDOW, (0, 255, 0), (575, 30, (monster.hp/monster.max_hp)*250, 20))
    # Energi Hero
    pygame.draw.rect(WINDOW, (76, 76 , 76), (80, 45, 250, 15))
    pygame.draw.rect(WINDOW, (44, 142, 212), (80, 45, 50*heroes.energi, 15))
    # BUff Gauge Monster
    pygame.draw.rect(WINDOW, (76, 76, 76), (575, 45, 250, 15))
    pygame.draw.rect(WINDOW, (237, 222, 62), (575, 45, 250/3*monster.buffmeter, 15))
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
        if heroes.nama == 'Alectrona':
            WINDOW.blit(heroes.skill_projectile[heroes.frame], (heroes.skill_rect))

# Update tombol aksi
def updateButton(button, x):
    for i in range(len(button)):
        if i == len(button) - 1:
            button[i].update(WINDOW)
        else:
            button[0].changeColor(x)
            button[0].update(WINDOW)
            button[1].changeColor(x)
            button[1].update(WINDOW)

# Main Loop
def mainLoop(arena):
    mixer.music.stop()
    global game_over, game_start, game_fight, button, mouse_pos
    createGrounds()
    mixer.music.load(arena.music)
    mixer.music.play(loops=-1)
    times = pygame.time.get_ticks()
    run = True
    button = menuUtama.matchButton()
    while run:
        clock.tick(FPS)
        heroes.floor_collision(grounds)
        monster.floor_collision(grounds)
        updateScreen(arena)
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.rect(WINDOW, (36, 36, 36), button[2].rect)
        updateButton(button, mouse_pos)
        if not heroes.onfloor:
            if pygame.time.get_ticks() - times > 600:
                WINDOW.blit(game_fight, (340, 220))
            else:
                WINDOW.blit(game_start, (230, 220))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button[2].checkForInput(mouse_pos) and event.button == 1:
                    mixer.music.pause()
                    pause()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mixer.music.pause()
                    pause()
            if heroes.turn % 2 == 0 and monster.finish and heroes.onfloor and \
                heroes.action == 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        heroes.serang()
                    elif event.key == pygame.K_1 and heroes.energi >= 2:
                        heroes.skill()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button[0].checkForInput(mouse_pos) and event.button == 1:
                        heroes.serang()
                    elif button[1].checkForInput(mouse_pos) and event.button == 1\
                        and heroes.energi >= 2:
                        heroes.skill()
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
            if monster.buffmeter == 3:
                monster.buffed = True
                monster.done_buff = False
            if monster.buffed:
                if pygame.time.get_ticks() - monster.buff_time < 900:
                    WINDOW.blit(monster.buff_alert, (575, 13))
                else:
                    monster.buffed = False
        if heroes.nama == 'Salazar' and heroes.skip_turn:
            if pygame.time.get_ticks() - heroes.skip_time < 1500:
                WINDOW.blit(heroes.skip_alert, (300, 220))
            else:
                heroes.skip_turn = False
        if heroes.move_l or heroes.move_r:
            heroes.move(monster)
        if monster.move_l or monster.move_r:
            monster.move(heroes)
        if heroes.skilled and heroes.nama == 'Alectrona':
            heroes.projectileCollide(monster)

        heroes.update(monster, grounds=grounds)
        monster.update(heroes)
        pygame.display.flip()

# PIlih Hero
def pilihKaraktermu(onscreen_chara):
    onscreen_chara[0] = pilihKarakter.pilihhero()
    if onscreen_chara[0] == 4:
        mainMenu()
    else:
        pilihLawan(onscreen_chara)

# Pilih Monster
def pilihLawan(onscreen_chara):
    onscreen_chara[1] = pilihKarakter.pilihmonster()
    if onscreen_chara[1] != 3:
        selectDifficulty()
    else:
        pilihKaraktermu(onscreen_chara)

# Pilih tingkat kesulitan
def selectDifficulty():
    global onscreen_chara, heroes_hp
    difficulty = pilihTingkatKesulitan.main()
    if difficulty != 'back' :
        makeCharacter(onscreen_chara, difficulty)
        if difficulty == 'easy':
            monster.hp = monster.hp * 1
        if difficulty == 'medium' :
            monster.hp = monster.hp * 1.15 
        if difficulty == 'hard' :
            monster.hp = monster.hp * 1.25
        monster.max_hp = monster.hp
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

def pause():
    pause_screen = os.path.join(f"{game_env}", "game_pause.jpg")
    image = pygame.image.save(WINDOW, pause_screen)
    image = pygame.image.load(pause_screen)
    image.set_alpha(50)
    text_pause = get_font(35).render("Game Paused", True, "red")
    y = menuUtama.pauseMenu()
    pause = True
    while pause:
        WINDOW.fill((0, 0, 0))
        WINDOW.blit(image, (0, 0))
        WINDOW.blit(text_pause, (240, 90))
        mouse_pos = pygame.mouse.get_pos()
        updateButton(y, mouse_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
                    mixer.music.unpause()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    if y[0].checkForInput(mouse_pos) and event.button == 1:
                        pause = False
                        mixer.music.unpause()
                    if y[1].checkForInput(mouse_pos) and event.button == 1:
                        mixer.music.stop()
                        playBGM()
                        mainMenu()
        
        pygame.display.flip()

def playBGM():
    mixer.music.load(menu_bgm)
    mixer.music.play(loops=-1)

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
        mixer.music.stop()
        playBGM()
        if consider:
            mainMenu()
        else:
            gameStart()

def mainMenu():
    x = menuUtama.menuUtama()
    if x == 'Start':
        gameStart()
    elif x == 'Guide':
        if guide.main() == 'Back':
            mainMenu()
    else:
        sys.exit()

if __name__ == "__main__":
    playBGM()
    mainMenu()
