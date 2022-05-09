import pygame, sys, pygame_widgets
from assetModule import game_env, game_chara, get_font

run = True

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color =  hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))


    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

pygame.init()

def pilihhero():
    global run
    while True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Display Pilih Hero")
        BG = pygame.image.load(f'{game_env}/bg_pilihTingkatKesulitan.jpeg').convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(40).render("Pilih Hero", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_alectrona= Button(image=pygame.image.load(f"{game_env}/button1.png"),
            pos=(200, 180), text_input="Alectrona", font=get_font(15),
            base_color="red", hovering_color="White")
        Tombol_nipalto = Button(image=pygame.image.load(f"{game_env}/button1.png"),
            pos=(200, 290), text_input="Nipalto", font=get_font(15),
            base_color="red", hovering_color="White")
        Tombol_salazar = Button(image=pygame.image.load(f"{game_env}/button1.png"),
            pos=(200, 400), text_input="Salazar", font=get_font(15),
            base_color="red", hovering_color="White")
        Tombol_back = Button(image=pygame.image.load(f"{game_env}/button2.png"),
            pos=(100, 50), text_input="Back", font=get_font(15), base_color="red",
            hovering_color="White")

        Display.blit(Text_Judul, Judul_Rect)

        image_base = pygame.image.load(f'{game_chara}/unknownchar.png')
        #image_base = image_info.get_rect(center = (530,82))


        #pos_info=(530,82)

        for button in [Tombol_alectrona, Tombol_nipalto, Tombol_salazar,Tombol_back]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_alectrona.checkForInput(Posisi_Mouse):
                    state = 'Alectrona'
                    return state
                    run = False
                if Tombol_nipalto.checkForInput(Posisi_Mouse):
                    state = 'Nipalto'
                    return state
                    run = False
                if Tombol_salazar.checkForInput(Posisi_Mouse):
                    state = 'Salazar'
                    return state
                    run = False
                if Tombol_back.checkForInput(Posisi_Mouse):
                    state = 'Back'
                    return state
                    run = False


        if Tombol_alectrona.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(f'{game_chara}/infoAlectrona.png')
            Display.blit(image_base,(450,130))
        if Tombol_nipalto.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(f'{game_chara}/infoNipalto.png')
            Display.blit(image_base,(450,130))
        if Tombol_salazar.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(f'{game_chara}/infoSalazar.png')
            Display.blit(image_base,(450,130))

        Display.blit(image_base,(450,130))
        pygame_widgets.update(event)

        pygame.display.update()

def pilihmonster():
    global run
    while True:
        events = pygame.event.get()
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Display Pilih Monster")
        BG = pygame.image.load(f"{game_env}/bg_pilihTingkatKesulitan.jpeg").convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(40).render("Pilih Monster", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_aposteus= Button(image=pygame.image.load(f"{game_env}/button1.png"),
            pos=(200, 180), text_input="aposteus", font=get_font(15),
            base_color="red", hovering_color="White")
        Tombol_fenrir = Button(image=pygame.image.load(f"{game_env}/button1.png"),
            pos=(200, 290), text_input="fenrir", font=get_font(15),
            base_color="red", hovering_color="White")
        Tombol_back = Button(image=pygame.image.load(f"{game_env}/button2.png"),
            pos=(100, 50), text_input="Back", font=get_font(15), base_color="red",
            hovering_color="White")

        Display.blit(Text_Judul, Judul_Rect)
        image_base = pygame.image.load(f'{game_chara}/unknownchar.png')
        #image_base = image_info.get_rect(center = (530,82))


        #pos_info=(530,82)

        for button in [Tombol_aposteus, Tombol_fenrir,Tombol_back]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_aposteus.checkForInput(Posisi_Mouse):
                    state = 'Aposteus'
                    return state
                    run = False
                if Tombol_fenrir.checkForInput(Posisi_Mouse):
                    state = 'Fenrir'
                    return state
                    run = False
                if Tombol_back.checkForInput(Posisi_Mouse):
                    state = 'Back'
                    return state
                    run = False

        if Tombol_aposteus.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(f'{game_chara}/infoAposteus.png')
            Display.blit(image_base,(450,130))
        if Tombol_fenrir.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(f'{game_chara}/infoFenrir.png')
            Display.blit(image_base,(450,130))

        Display.blit(image_base,(450,130))
        pygame_widgets.update(events)

        pygame.display.update()

def main():
    x = pilihhero()
    if x == 'Back':
        sys.exit()
    y = pilihmonster()
    if y == 'Back':
        main()

main()
