import os
import pygame

CWD = os.getcwd()

assets_dir = os.path.join(CWD, 'Assets')

game_env = os.path.join(assets_dir, 'env')
game_bgm = os.path.join(assets_dir, 'bgm')

menu_bgm = os.path.join(game_bgm, 'bgmMenu2.mp3')

game_chara = os.path.join(assets_dir, 'pilihKarakter')
game_font = os.path.join(assets_dir, 'font', 'A Goblin Appears!.otf')

bg = os.path.join(game_env, 'map.png')

alectrona_dir = os.path.join(assets_dir, 'alectrona')
alectrona_img = os.path.join(alectrona_dir, 'img')

nipalto_dir = os.path.join(assets_dir, 'nipalto')
nipalto_img = os.path.join(nipalto_dir, 'img')

salazar_dir = os.path.join(assets_dir, 'salazar')
salazar_img = os.path.join(salazar_dir, 'img')

aposteus_dir = os.path.join(assets_dir, 'aposteus')
aposteus_img = os.path.join(aposteus_dir, 'img')

fenrir_dir = os.path.join(assets_dir, 'fenrir')
fenrir_img = os.path.join(fenrir_dir, 'img')

guide_dir=os.path.join(assets_dir,'guide')
guide_img=os.path.join(guide_dir,'GuideBG.png')

def get_font(size): 
    return pygame.font.Font(f"{game_font}", size)