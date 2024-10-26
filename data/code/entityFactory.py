#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from data.code.background import Background
from data.code.const import WIN_HEIGHT, WIN_WIDTH
from data.code.enemy import Enemy
from data.code.player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1_bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1_bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1_bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level2_bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level2_bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2_bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level3_bg':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'Level3_bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level3_bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT/2 -30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 +30))

            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40) ))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy3':
                return Enemy('Enemy3', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))



