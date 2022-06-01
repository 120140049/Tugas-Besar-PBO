import pygame
import os
import assetModule
from random import randint
from abc import ABC, abstractmethod


# Abstract class
class Makhluk(ABC):
    def __init__(self, nama):
        self.nama = nama
        self.action = self.prev_action = self.frame = 0
        self.update_time = pygame.time.get_ticks()
        self.onground = self.onfloor = self.death = self.die = False
        self.move_l = self.move_r = self.finish = self.attacking = False

    def obj_collision(self, enemy):
       collide = self.rect.colliderect(enemy.rect)
       return collide

    def floor_collision(self, grounds):
        collide = pygame.sprite.spritecollide(self, grounds, False)
        if collide:
            self.onground = True
            self.onfloor = True
            idx = len(collide) - 1
            self.rect.bottom = collide[idx].rect.top
        else:
            self.onground = False

    def update(self, enemy, grounds = None):
        if self.tipe == 'Hero':
            if self.skilled and self.nama == 'Alectrona':
                self.skill_rect.x += 10
            elif self.skilled and self.nama != 'Alectrona':
                self.floor_collision(grounds)
        if self.hp <= 0:
            self.death = True
        if enemy.hp <= 0:
            enemy.death = True
        if not self.onground and not self.attacking:
            self.rect.y += 6
        if self.prev_action != self.action:
            self.frame = 0
            self.prev_action = self.action
        if pygame.time.get_ticks() - self.update_time > 90:
            if self.tipe == 'Hero':
                if self.skilled and self.nama == 'Alectrona':
                    self.frame = (self.frame + 1) % len(self.skill_projectile)
                    if self.frame == len(self.skill_projectile) - 2:
                        self.action = 0
                else:
                    self.frame = (self.frame + 1) % \
                        len(self.animation[self.action])
            else:
                self.frame = (self.frame + 1) % len(self.animation[self.action])
            self.update_time = pygame.time.get_ticks()
            if self.attacking:
                if self.frame == len(self.animation[self.action]) - 1:
                    self.action = 2
                    self.attacking = False
                    self.move_l = True
                    self.frame = 0
                    if self.tipe == 'Hero':
                        self.rect.right = enemy.rect.left
                        if not self.skilled:
                            pass
                        else:
                            if self.nama != 'Alectrona':
                                if self.nama == 'Salazar':                                                    
                                    skip = randint(1, 10)
                                    if skip < 4:
                                        self.skip_time = pygame.time.get_ticks()
                                        self.skip_turn = True
                                        self.turn += 1
                                self.rect = self.animation[0][0].get_rect() 
                                self.rect.y = 504
                                self.rect.right = enemy.rect.left
                                self.floor_collision(grounds)
                                self.skilled = False
                            if self.nama == 'Alectrona':
                                enemy - (self.skill_dmg + enemy.hp * 0.1)
                            elif self.nama == 'Nipalto':
                                enemy - self.skill_dmg
                                enemy.damage = -(enemy.damage * 0.01)
                            elif self.nama == 'Salazar':
                                enemy - self.skill_dmg
                            return      
                    else:
                        if self.nama == 'Aposteus':
                            self.rect.y = enemy.rect.y
                        self.rect.left = enemy.rect.right
                    enemy - self.damage
                    self + 1
            if self.tipe == 'Hero' and self.action == 4:
                if self.frame == len(self.animation[self.action]) - 1:
                    self.action = 0
                    self.frame = 0
                    self.die = True

    def __sub__(self):
        self.__hp -= amount

    @abstractmethod
    def serang(self):
        pass

# Parent Class
class Hero(Makhluk):
    def __init__(self, nama, hp, damage, energi=2):
        super().__init__(nama)
        self.__hp = hp
        self.__damage = damage
        self.__energi = energi
        self.tipe = 'Hero'
        self.turn = 0
        self.dead_img = None
        self.skilled = False

    def move(self, enemy):
        if not self.death:
            if self.obj_collision(enemy):
                self.rect.x += 50
                self.move_r = False
                self.attacking = True
                if self.skilled and self.nama != 'Alectrona':
                    self.action = 5
                    temp_x = self.rect.x
                    self.rect = self.animation[5][0].get_rect()
                    self.rect.y = 480
                    self.rect.right = enemy.rect.left + 120
                else:
                    self.action = 3
            if self.rect.x <= 180 and self.move_l:
                self.move_l = False
                if self.nama == 'Salazar' and self.skip_turn:
                    self.finish = False
                    enemy.finish = True
                else:
                    enemy.finish = False
                    self.finish = True
                self.action = 0
            if self.move_r:
                self.rect.x += 4.5
            if self.move_l:
                self.rect.x -= 4.5
        else:
            self.action = 4        

    def serang(self):
        self.move_r = True
        self.action = 1
        self.turn += 1

    def skill(self):
        pass

    def projectileCollide(self, enemy):
        if self.skill_rect.x >= enemy.rect.x + 80:
            self.finish = True
            enemy.finish = False
            self.skilled = False
            self.skill_rect.x = 220
            enemy - (self.damage + self.damage * 1.30)

    # Damage Getter
    @property
    def damage(self):
        return self.__damage

    # HP Getter
    @property
    def hp(self):
        return self.__hp

    # Energi Getter
    @property
    def energi(self):
        return self.__energi

    @energi.setter
    def energi(self, cost):
        self.__energi -= cost

    def __add__(self, amount):
        if self.__energi < 5:
            self.__energi += amount


class Monster(Makhluk):
    def __init__(self, nama, hp, damage):
        super().__init__(nama)
        self.__hp = hp
        self.__damage = damage
        self.__buffmeter = 0
        self.finish = True
        self.tipe = 'Monster'
        self.buffed = False
        self.done_buff = True
        self.buff_time = 0
        self.max_hp = 0

    def move(self, enemy):
        if self.death:
            if enemy.action == 0:
                self.action = 2
            if self.rect.x >= 896:
                self.action = 0
                self.die = True
            elif enemy.action == 0:
                self.rect.x += 6
        else:
            if self.obj_collision(enemy):
                self.move_r = False
                self.attacking = True
                self.rect.x = 150
                if self.nama == 'Aposteus':
                    self.rect.y = 0
                self.action = 3
            if not self.done_buff:
                self.buff()
            if self.rect.x >= 520 and self.move_l:
                self.move_l = False
                self.action = 0
                self.finish = True
                enemy.finish = False
            if self.move_r:
                self.rect.x -= 6
            if self.move_l:
                self.rect.x += 6

    def serang(self, obj):
        self.move_r = True
        self.action = 1
        obj.turn += 1

    def buff(self):
        pass

    # HP Getter
    @property
    def hp(self):
        return self.__hp

    # Damage Getter
    @property
    def damage(self):
        return self.__damage

    @property
    def buffmeter(self):
        return self.__buffmeter

    @hp.setter
    def hp(self, amount):
        self.__hp = amount

    @damage.setter
    def damage(self, amount):
        self.__damage += amount

    @buffmeter.setter
    def buffmeter(self, amount):
        self.__buffmeter -= amount

    def __add__(self, amount):
        if self.__buffmeter < 3:
            self.__buffmeter += 1


class Lantai(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            assetModule.game_env, image)).convert()
        self.image = pygame.transform.scale(self.image, (64, 66))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
