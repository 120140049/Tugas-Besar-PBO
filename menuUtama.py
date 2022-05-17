import pygame, sys
from assetModule import game_env, get_font
from button import Button

state = None
run = True

pygame.init()

def menuUtama():
    global run, state
    while run == True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Main Menu")
        BG = pygame.image.load(f"{game_env}/bg_pilihTingkatKesulitan.jpeg").convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(35).render("Dungeon Fighter", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_start= Button(image=pygame.image.load(f"{game_env}/button1.png"), 
                            pos=(450, 180), text_input="Start", font=get_font(20))
        Tombol_guide = Button(image=pygame.image.load(f"{game_env}/button1.png"),
                            pos=(450, 290), text_input="Guide", font=get_font(20))
        Tombol_exit = Button(image=pygame.image.load(f"{game_env}/button1.png"),
                            pos=(450, 400), text_input="Exit", font=get_font(20))                

        Display.blit(Text_Judul, Judul_Rect)

        for button in [Tombol_start, Tombol_exit, Tombol_guide]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_start.checkForInput(Posisi_Mouse) and event.button == 1:
                    state = 'Start'
                    return state
                    run = False
                elif Tombol_guide.checkForInput(Posisi_Mouse) and event.button == 1:
                    state = 'Guide'
                    return state
                    run = False
                elif Tombol_exit.checkForInput(Posisi_Mouse) and event.button == 1:
                    state = 'Exit'
                    return state
                    run = False

        pygame.display.flip()


def matchButton():
    Tombol_attack= Button(image=pygame.image.load(f"{game_env}/button1.png"),
        pos=(290, 430), text_input="attack", font=get_font(15))
    Tombol_skill = Button(image=pygame.image.load(f"{game_env}/button1.png"),
        pos=(620, 430), text_input="skill", font=get_font(15))
    gambar_pause = pygame.image.load(f"{game_env}/pause_btn.png")
    gambar_pause = pygame.transform.scale(gambar_pause, (42, 42))
    Tombol_pause = Button(image=gambar_pause, pos=(450, 90))

    return [Tombol_attack, Tombol_skill, Tombol_pause]

def pauseMenu():
    Tombol_resume= Button(image=pygame.image.load(f"{game_env}/button1.png"),
		pos=(450, 270), text_input="Resume", font=get_font(15))
    Tombol_menu = Button(image=pygame.image.load(f"{game_env}/button1.png"),
		pos=(450, 400), text_input="Back to Menu", font=get_font(11))

    return [Tombol_resume, Tombol_menu]
