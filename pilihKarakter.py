#baru bikin aja
#ntar ajala kerjainnya

import pygame
import sys

pygame.init()
layar = pygame.display.set_mode((896,504))
main_font=pygame.font.SysFont("Times",65)

class TombolPilihan():
    def __init__ (self, warna_bg, gambar_avatar, x_pos, y_pos, nama_karakter):
        self.warna_bg=warna_bg
        self.background=pygame.Surface([x_pos,y_pos])
        self.background.fill("green")
        self.rect=self.background.get_rect(center=(x_pos,y_pos))
        self.gambar_avatar=gambar_avatar
        self.gambar_avatar_rect=self.gambar_avatar
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.nama_karakter=nama_karakter
        self.teks=main_font.render(self.nama_karakter,True,"white")
        self.teks_rect=self.teks.get_rect(center=(x_pos,y_pos))
    
    def update(self):
        layar.blit(self.background,self.rect)
        layar.blit(self.teks,self.teks_rect)
        layar.blit(self.gambar_avatar,self.gambar_avatar_rect)
    def cekInput(self,posisi):
        if posisi[0] in range(self.rect.left,self.rect.right) and posisi[1] in range(self.rect.top, self.rect.bottom):
            print("ini nanti diisi summon hero, terus panggil SelectMonster, \nkemungkinan nambah parameter lagi ntah di class atau disini")
    def gantiWarna(self,posisi):
        if posisi[0] in range(self.rect.left,self.rect.right) and posisi[1] in range(self.rect.top, self.rect.bottom):
            self.background=pygame.draw.rect(layar,self.warna_bg,pygame.Rect(self.x_pos,self.y_pos,485,70))
        else:
            self.background=pygame.draw.rect(layar,"green",pygame.Rect(self.x_pos,self.y_pos,485,70))

#masih ngga jelas summonnya gimana
tombol_alectrona=TombolPilihan("yellow",None,12,18,"Alectrona")



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            tombol_alectrona.cekInput(pygame.mouse.get_pos())
    layar.fill("white")

    tombol_alectrona.update()
    tombol_alectrona.gantiWarna(pygame.mouse.get_pos())

    #taro paling bawah, ini buat update semua perubahan
    pygame.display.update()



