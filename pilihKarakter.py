import pygame, sys, pygame_widgets
from assetModule import game_env, game_chara, get_font
from button import Button


pygame.init()
run = True

def pilihhero():
    global run
    while True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Dungeon Fighter")
        BG = pygame.image.load(f'{game_env}/bg_pilihTingkatKesulitan.jpeg').convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(40).render("Pilih Hero", True, "white")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_alectrona= Button(image=pygame.image.load(f"{game_env}/button1.png"),
            pos=(275, 180), text_input="Alectrona", font=get_font(15))
        Tombol_nipalto = Button(image=pygame.image.load(f"{game_env}/button1.png"),
            pos=(275, 290), text_input="Nipalto", font=get_font(15))
        Tombol_salazar = Button(image=pygame.image.load(f"{game_env}/button1.png"),
            pos=(275, 400), text_input="Salazar", font=get_font(15))
        Tombol_back = Button(image=pygame.image.load(f"{game_env}/button2.png"),
            pos=(100, 50), text_input="Back", font=get_font(15))

        Display.blit(Text_Judul, Judul_Rect)

        image_base = pygame.image.load(f'{game_chara}/unknownchar.png')
        image_base = pygame.transform.scale(image_base, (250, 300))
        Display.blit(image_base, (500, 140))

        for button in [Tombol_alectrona, Tombol_nipalto, Tombol_salazar,Tombol_back]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_alectrona.checkForInput(Posisi_Mouse) and event.button == 1:
                    state = 1
                    return state
                if Tombol_nipalto.checkForInput(Posisi_Mouse) and event.button == 1:
                    state = 2
                    return state
                if Tombol_salazar.checkForInput(Posisi_Mouse) and event.button == 1:
                    state = 3
                    return state
                if Tombol_back.checkForInput(Posisi_Mouse) and event.button == 1:
                    state = 4
                    return state

        if Tombol_alectrona.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(f'{game_chara}/infoAlectrona.png')
            image_base = pygame.transform.scale(image_base, (250, 300))
            Display.blit(image_base, (500, 140))
        if Tombol_nipalto.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(f'{game_chara}/infoNipalto.png')
            image_base = pygame.transform.scale(image_base, (250, 300))
            Display.blit(image_base, (500, 140))
        if Tombol_salazar.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(f'{game_chara}/infoSalazar.png')
            image_base = pygame.transform.scale(image_base, (250, 300))
            Display.blit(image_base, (500, 140))

        pygame_widgets.update(event)
        pygame.display.update()

def pilihmonster():
    global run
    while True:
        events = pygame.event.get()
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Dungeon Fighter")
        BG = pygame.image.load(f"{game_env}/bg_pilihTingkatKesulitan.jpeg").convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(40).render("Pilih Monster", True, "white")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_aposteus= Button(image=pygame.image.load(f"{game_env}/button1.png"),
            pos=(275, 180), text_input="aposteus", font=get_font(15))
        Tombol_fenrir = Button(image=pygame.image.load(f"{game_env}/button1.png"),
            pos=(275, 290), text_input="fenrir", font=get_font(15))
        Tombol_back = Button(image=pygame.image.load(f"{game_env}/button2.png"),
            pos=(100, 50), text_input="Back", font=get_font(15))

        Display.blit(Text_Judul, Judul_Rect)
        image_base = pygame.image.load(f'{game_chara}/unknownchar.png')
        image_base = pygame.transform.scale(image_base, (250, 300))
        Display.blit(image_base,(500,140))

        for button in [Tombol_aposteus, Tombol_fenrir,Tombol_back]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_aposteus.checkForInput(Posisi_Mouse) and event.button == 1:
                    state = 1
                    return state
                if Tombol_fenrir.checkForInput(Posisi_Mouse) and event.button == 1:
                    state = 2
                    return state
                if Tombol_back.checkForInput(Posisi_Mouse) and event.button == 1:
                    state = 3
                    return state

        if Tombol_aposteus.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(f'{game_chara}/infoAposteus.png')
            image_base = pygame.transform.scale(image_base, (250, 300))
            Display.blit(image_base,(500, 140))
        if Tombol_fenrir.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(f'{game_chara}/infoFenrir.png')
            image_base = pygame.transform.scale(image_base, (250, 300))
            Display.blit(image_base,(500, 140))

        pygame_widgets.update(events)
        pygame.display.flip()
