import pygame, sys
from assetModule import game_env, get_font

state = None
run = True

class Button():
    def __init__(self, image, pos, text_input=None, font=None, base_color="white", hovering_color="red", ):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        if font != None:
            self.font = font
        if text_input != None:
            self.base_color, self.hovering_color = base_color, hovering_color
            self.text_input = text_input
            self.text = self.font.render(self.text_input, True, self.base_color)
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        else:
            self.text = None
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.image, self.rect)
        if self.text != None:
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
                if Tombol_start.checkForInput(Posisi_Mouse):
                    state = 'Start'
                    return state
                    run = False
                if Tombol_guide.checkForInput(Posisi_Mouse):
                    state = 'Guide'
                    return state
                    run = False
                if Tombol_exit.checkForInput(Posisi_Mouse):
                    state = 'Exit'
                    return state
                    run = False

        pygame.display.update()


def matchButton():
    Tombol_attack= Button(image=pygame.image.load(f"{game_env}/button1.png"),
        pos=(290, 430), text_input="attack", font=get_font(15))
    Tombol_skill = Button(image=pygame.image.load(f"{game_env}/button1.png"),
        pos=(620, 430), text_input="skill", font=get_font(15))
    gambar_pause = pygame.image.load(f"{game_env}/pause_btn.png")
    gambar_pause = pygame.transform.scale(gambar_pause, (42, 42))
    Tombol_pause = Button(image=gambar_pause, pos=(450, 80))

    return [Tombol_attack, Tombol_skill, Tombol_pause]

def pauseMenu():
    Tombol_resume= Button(image=pygame.image.load(f"{game_env}/button1.png"),
		pos=(450, 270), text_input="Resume", font=get_font(15))
    Tombol_menu = Button(image=pygame.image.load(f"{game_env}/button1.png"),
		pos=(450, 400), text_input="Back to Menu", font=get_font(11))

    return [Tombol_resume, Tombol_menu]
