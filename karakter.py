import os
import pygame
import assetModule
import spritesheet
from objek import Hero, Monster, Melee, Ranged
from assetModule import get_font

class Alectrona(Hero, Ranged):
    def __init__(self, nama='Alectrona', hp=3200, damage=240):
        Hero.__init__(self, nama, hp, damage)
        Ranged.__init__(self)
        self.animation = [[]]
        self.skill_projectile = []
        self.setAnimation()
        self.rect = self.animation[0][0].get_rect()
        self.skill_rect = self.skill_projectile[0].get_rect()
        self.skill_rect.x = 200
        self.skill_rect.y = 220
        self.dead_img = self.animation[4][4]
        self.rect.x = 180
        self.rect.y = 0

    def setAnimation(self):
        idle = spritesheet.Spritesheet(os.path.join(
            assetModule.alectrona_img, 'Idle.png'))
        for i in range(8):
            rect = ((i*150, 0), (150, 100))
            image = idle.image_at(rect)
            image = pygame.transform.scale2x(image)
            image = image.subsurface((90, 35), (100, 165))
            image = pygame.transform.scale(image, (140, 200))
            self.animation[0].append(image)
        temp_list = []
        self.animation.append(temp_list)
        run = spritesheet.Spritesheet(os.path.join(
            assetModule.alectrona_img, 'Move.png'))
        for i in range(8):
            rect = ((i*150, 0), (150, 150))
            image = run.image_at(rect)
            image = pygame.transform.scale2x(image)
            image = image.subsurface((65, 35), (150, 200))
            image = pygame.transform.scale(image, (190, 240))
            self.animation[1].append(image)
        temp_list = []
        self.animation.append(temp_list)
        for i in range(8):
            image = pygame.transform.flip(self.animation[1][i], True, False)
            self.animation[2].append(image)
        temp_list = []
        self.animation.append(temp_list)
        atk = spritesheet.Spritesheet(os.path.join(
            assetModule.alectrona_img, 'Attack.png'))
        for i in range(8):
            rect = ((i*150, 0), (150, 150))
            image = atk.image_at(rect)
            image = pygame.transform.scale2x(image)
            image = image.subsurface((65, 42), (220, 220))
            image = pygame.transform.scale(image, (255, 265))
            self.animation[3].append(image)
        temp_list = []
        self.animation.append(temp_list)
        dead = spritesheet.Spritesheet(os.path.join(
            assetModule.alectrona_img, 'Death.png'))
        for i in range(5):
            rect = ((i*150, 0), (150, 80))
            image = dead.image_at(rect)
            image = pygame.transform.scale2x(image)
            image = image.subsurface((90, 0), (100, 160))
            image = pygame.transform.scale(image, (140, 200))
            self.animation[4].append(image)
        skill = spritesheet.Spritesheet(os.path.join(
            assetModule.alectrona_img, 'projectile.png'))
        for i in range(8):
            rect = ((i*96, 0), (96, 112))
            image = skill.image_at(rect)
            image = pygame.transform.flip(image, True, False)
            self.skill_projectile.append(image)

    def skill1(self):
        self.energi = 2
        self.action = 3
        self.skilled = True
        self.turn += 1


class Nipalto(Hero, Melee):
    def __init__(self, nama='Nipalto', hp=3200, damage=240):
        Hero.__init__(self, nama, hp, damage)
        Ranged.__init__(self)
        self.animation = [[]]
        self.setAnimation()
        self.rect = self.animation[0][0].get_rect()
        self.dead_img = self.animation[4][6]
        self.rect.x = 180
        self.rect.y = -100

    def setAnimation(self):
        idle = spritesheet.Spritesheet(os.path.join(
            assetModule.nipalto_img, 'Idle.png'))
        for i in range(6):
            rect = ((i*231, 0), (150, 100))
            image = idle.image_at(rect)
            image = pygame.transform.scale2x(image)
            image = image.subsurface((150, 20), (150, 180))
            image = pygame.transform.scale(image, (90, 110))
            self.animation[0].append(image)
        temp_list = []
        self.animation.append(temp_list)
        run = spritesheet.Spritesheet(os.path.join(
            assetModule.nipalto_img, 'Run.png'))
        for i in range(8):
            rect = ((i*231, 0), (231, 150))
            image = run.image_at(rect)
            image = pygame.transform.scale2x(image)
            image = image.subsurface((150, 110), (180, 180))
            image = pygame.transform.scale(image, (120, 110))
            self.animation[1].append(image)
        temp_list = []
        self.animation.append(temp_list)
        for i in range(8):
            image = pygame.transform.flip(self.animation[1][i], True, False)
            self.animation[2].append(image)
        temp_list = []
        self.animation.append(temp_list)
        atk = spritesheet.Spritesheet(os.path.join(
            assetModule.nipalto_img, 'Attack.png'))
        for i in range(8):
            rect = ((i*232, 0), (232, 150))
            image = atk.image_at(rect)
            image = pygame.transform.scale2x(image)
            image = image.subsurface((150, 110), (240, 190))
            image = pygame.transform.scale(image, (160, 120))
            self.animation[3].append(image)
        temp_list = []
        self.animation.append(temp_list)
        dead = spritesheet.Spritesheet(os.path.join(
            assetModule.nipalto_img, 'Death.png'))
        for i in range(7):
            rect = ((i*231, 0), (231, 100))
            image = dead.image_at(rect)
            image = pygame.transform.scale2x(image)
            image = image.subsurface((150, 0), (240, 190))
            image = pygame.transform.scale(image, (160, 120))
            self.animation[4].append(image)

    def skill1(self):
        self.energi = 2

class Salazar(Hero, Melee):
    def __init__(self, nama='Salazar', hp=3200, damage=240):
        Hero.__init__(self, nama, hp, damage)
        Ranged.__init__(self)
        self.animation = [[]]
        self.setAnimation()
        self.rect = self.animation[0][0].get_rect()
        self.dead_img = self.animation[4][22]
        self.rect.x = 180
        self.rect.y = -100

    def setAnimation(self):
        idle = spritesheet.Spritesheet(os.path.join(
            assetModule.salazar_img, 'idle.png'))
        for i in range(9):
            rect = ((i*80+5, 0), (55, 53))
            image = idle.image_at(rect)
            image = pygame.transform.scale2x(image)
            image = image.subsurface((20, 0), (85, 100))
            image = pygame.transform.scale(image, (160, 200))
            self.animation[0].append(image)
        temp_list = []
        self.animation.append(temp_list)
        run = spritesheet.Spritesheet(os.path.join(
            assetModule.salazar_img, 'run.png'))
        for i in range(6):
            rect = ((i*80+5, 0), (55, 53))
            image = run.image_at(rect)
            image = pygame.transform.scale2x(image)
            image = image.subsurface((20, 0), (85, 100))
            image = pygame.transform.scale(image, (160, 200))
            self.animation[1].append(image)
        temp_list = []
        self.animation.append(temp_list)
        for i in range(6):
            image = pygame.transform.flip(self.animation[1][i], True, False)
            self.animation[2].append(image)
        temp_list = []
        self.animation.append(temp_list)
        atk = spritesheet.Spritesheet(os.path.join(
            assetModule.salazar_img, 'attack.png'))
        for i in range(12):
            rect = ((i*80, 0), (80, 72))
            image = atk.image_at(rect)
            image = pygame.transform.scale2x(image)
            image = image.subsurface((10, 14), (145, 130))
            image = pygame.transform.scale(image, (310, 230))
            self.animation[3].append(image)
        temp_list = []
        self.animation.append(temp_list)
        dead = spritesheet.Spritesheet(os.path.join(
            assetModule.salazar_img, 'death.png'))
        for i in range(23):
            rect = ((i*80, 0), (80, 69))
            image = dead.image_at(rect)
            image = pygame.transform.scale2x(image)
            image = image.subsurface((20, 0), (135, 138))
            image = pygame.transform.scale(image, (310, 240))
            self.animation[4].append(image)

    def skill1(self):
        self.energi = 2

class Aposteus(Monster, Ranged):
    def __init__(self, nama='Aposteus', hp=5000, damage=78):
        Monster.__init__(self, nama, hp, damage)
        Ranged.__init__(self)
        self.animation = [[]]
        self.setAnimation()
        self.rect.x = 520
        self.rect.y = -100
        self.buff_alert = get_font(15).render("HP +100", True, "green")

    def setAnimation(self):
        idle = spritesheet.Spritesheet(os.path.join(
            assetModule.aposteus_img, 'idle.png'))
        for i in range(6):
            rect = ((i*160, 0), (160, 144))
            image = idle.image_at(rect, (0, 0, 0))
            image = pygame.transform.scale2x(image)
            image = image.subsurface((0, 0), (320, 268))
            self.animation[0].append(image)
        self.rect = self.animation[0][0].get_rect()
        temp_list = []
        self.animation.append(temp_list)
        for i in range(len(self.animation[0])):
            self.animation[1].append(self.animation[0][i])
        temp_list = []
        self.animation.append(temp_list)
        for i in range(len(self.animation[0])):
            x = pygame.transform.flip(self.animation[0][i], True, False)
            self.animation[2].append(x)
        temp_list = []
        self.animation.append(temp_list)
        atk = spritesheet.Spritesheet(os.path.join(
            assetModule.aposteus_img, 'attack.png'))
        for i in range(11):
            rect = ((i*240, 0), (240, 192))
            image = atk.image_at(rect)
            image = pygame.transform.scale2x(image)
            self.animation[3].append(image)

    def buff(self):
        self.buff_time = pygame.time.get_ticks()
        print(self.buff_time)
        self.hp = 100
        self.buffmeter = 0
        self.buffed = True

class Fenrir(Monster, Melee):
    def __init__(self, nama='Fenrir', hp=5000, damage=82):
        Monster.__init__(self, nama, hp, damage)
        Ranged.__init__(self)
        self.animation = [[]]
        self.setAnimation()
        self.rect.x = 520
        self.rect.y = -100
        self.buff_alert = get_font(15).render("Damage +1000", True, "red")

    def setAnimation(self):
        for i in range(6):
            image = pygame.image.load(os.path.join(assetModule.fenrir_img, 
                'idle', f'demon_idle_{i+1}.png' ))
            image = pygame.transform.scale2x(image)
            image = image.subsurface((180, 70), (240, 250))
            self.animation[0].append(image)
        self.rect = self.animation[0][0].get_rect()
        temp_list = []
        self.animation.append(temp_list)
        for i in range(6):
            image = pygame.image.load(os.path.join(assetModule.fenrir_img, 
                'walk', f'demon_walk_{i+1}.png' ))
            image = pygame.transform.scale2x(image)
            image = image.subsurface((180, 70), (240, 250))
            self.animation[1].append(image)
        temp_list = []
        self.animation.append(temp_list)
        for i in range(6):
            image = pygame.transform.flip(self.animation[1][i], True, False)
            self.animation[2].append(image)
        temp_list = []
        self.animation.append(temp_list)
        for i in range(15):
            image = pygame.image.load(os.path.join(assetModule.fenrir_img, 
                'attack', f'demon_cleave_{i+1}.png' ))
            image = pygame.transform.scale2x(image)
            image = image.subsurface((10, 70), (546, 250))
            self.animation[3].append(image)

    def buff(self):
        self.buff_time = pygame.time.get_ticks()
        print(self.buff_time)
        self.damage = self.damage * 0.2
        self.buffmeter = 0
        self.buffed = True