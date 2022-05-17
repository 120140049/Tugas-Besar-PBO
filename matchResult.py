import pygame, sys
from assetModule import game_env, get_font
from button import Button

pygame.init()

def akhirpertandingan(arena, grounds):
    while True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Dungeon Fighter")
        temp = arena
        temp.set_alpha(75)
        Display.blit(temp, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(35).render("Permainan Selesai", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_menu = Button(image=pygame.image.load(f"{game_env}/button1.png"),
                        pos=(450, 400), text_input="Back to Menu", font=get_font(11))
        Tombol_back = Button(image=pygame.image.load(f"{game_env}/button1.png"),
                        pos=(450, 270), text_input="Main lagi", font=get_font(16))                   

        Display.blit(Text_Judul, Judul_Rect)

        for button in [Tombol_menu,Tombol_back]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Ke pilih karakter
                if Tombol_menu.checkForInput(Posisi_Mouse) and event.button == 1:
                    return True
                # Ke menu Utama
                if Tombol_back.checkForInput(Posisi_Mouse) and event.button == 1:
                    return False

        pygame.display.flip()