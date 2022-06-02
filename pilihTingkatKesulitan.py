import pygame, sys
from assetModule import game_env, get_font
from button import Button

pygame.init()

def tingkatKesulitan():
    while True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Dungeon Fighter")
        BG = pygame.image.load(f"{game_env}/bg_pilihTingkatKesulitan.jpeg").convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(30).render("Tingkat Kesulitan", True, "white")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_easy= Button(image=pygame.image.load(f"{game_env}/button1.png"), pos=(450, 180), 
                            text_input="Easy", font=get_font(15))
        Tombol_medium = Button(image=pygame.image.load(f"{game_env}/button1.png"), pos=(450, 290), 
                            text_input="Medium", font=get_font(15))
        Tombol_hard = Button(image=pygame.image.load(f"{game_env}/button1.png"), pos=(450, 400), 
                            text_input="Hard", font=get_font(15))
        Tombol_back = Button(image=pygame.image.load(f"{game_env}/button2.png"), pos=(100, 50), 
                            text_input="Back", font=get_font(15))                   

        Display.blit(Text_Judul, Judul_Rect)

        for button in [Tombol_easy, Tombol_medium, Tombol_hard,Tombol_back]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_easy.checkForInput(Posisi_Mouse) and event.button == 1:
                    return 1
                if Tombol_medium.checkForInput(Posisi_Mouse) and event.button == 1:
                    return 2
                if Tombol_hard.checkForInput(Posisi_Mouse) and event.button == 1:
                    return 3
                if Tombol_back.checkForInput(Posisi_Mouse) and event.button == 1:
                    return 4

        pygame.display.flip()

def main():
    state=tingkatKesulitan()
    if state == 1 :
        return 'easy'
    if state == 2 :
        return 'medium'
    if state == 3 :
        return 'hard'
    if state == 4 :
        return 'back'