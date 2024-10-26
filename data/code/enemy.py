#!/usr/bin/python
# -*- coding: utf-8 -*-
from data.code.const import ENTITY_SPEED, WIN_HEIGHT, ENTITY_SHOT_DELAY
from data.code.enemyShot import EnemyShot
from data.code.entity import Entity


class Enemy(Entity):
    def __init__(self, nome: str, position: tuple):
        super().__init__(nome, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.direction = "subir"

    def move(self,  ):
        if self.name == "Enemy3":
            self.rect.centerx -= ENTITY_SPEED[self.name]

            if self.direction == "subir":
                self.rect.centery -= ENTITY_SPEED[self.name]
                if self.rect.centery <= 0: 
                    self.direction = "descer"  
            elif self.direction == "descer":
                self.rect.centery += ENTITY_SPEED[self.name] * 2
                if self.rect.centery >= WIN_HEIGHT:
                    self.direction = "subir"
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]       
    
    def shoot(self,):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))