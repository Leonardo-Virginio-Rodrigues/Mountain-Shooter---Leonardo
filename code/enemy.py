#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SPEED, WIN_WIDTH
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, nome: str, position: tuple):
        super().__init__(nome, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

