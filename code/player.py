#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.entity import Entity


class Player(Entity):
    def __init__(self, nome: str, position: tuple):
        super().__init__(nome, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top >0 :
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT :
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx+= ENTITY_SPEED[self.name]
        pass


