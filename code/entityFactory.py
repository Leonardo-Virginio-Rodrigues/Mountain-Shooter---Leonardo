#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.background import Background
from code.const import WIN_HEIGHT, WIN_WIDTH
from code.enemy import Enemy
from code.player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1_bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'level1_bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1_bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT/2 -30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 +30))

            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40) ))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))



