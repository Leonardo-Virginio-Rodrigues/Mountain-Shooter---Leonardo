# C
import pygame

COLOR_ORANGE = 255, 128, 0
COLOR_YELLOW = 255, 255, 0
COLOR_WHITE = 255, 255, 255
COLOR_GREEN = 0, 128, 0
COLOR_CYAN = 0, 128, 128
COLOR_RED = 255, 0, 0

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_DAMAGE = {
    'Level1_bg0': 0,
    'Level1_bg1': 0,
    'Level1_bg2': 0,
    'Level1_bg3': 0,
    'Level1_bg4': 0,
    'Level1_bg5': 0,
    'Level1_bg6': 0,
    'Level2_bg0': 0,
    'Level2_bg1': 0,
    'Level2_bg2': 0,
    'Level2_bg3': 0,
    'Level2_bg4': 0,
    'Level2_bg5': 0,
    'Level2_bg6': 0,
    'Level3_bg0': 0,
    'Level3_bg1': 0,
    'Level3_bg2': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 30,
    'Enemy2': 1,
    'Enemy2Shot': 30,
    'Enemy3': 2,
    'Enemy3Shot': 40,
}

ENTITY_HEALTH = {
    'Level1_bg0': 999,
    'Level1_bg1': 999,
    'Level1_bg2': 999,
    'Level1_bg3': 999,
    'Level1_bg4': 999,
    'Level1_b5': 999,
    'Level1_b6': 999,
    'Level2_bg0': 999,
    'Level2_bg1': 999,
    'Level2_bg2': 999,
    'Level2_bg3': 999,
    'Level2_bg4': 999,
    'Level2_bg5': 999,
    'Level2_bg6': 999,
    'Level3_bg0': 999,
    'Level3_bg1': 999,
    'Level3_bg2': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
    'Enemy3': 80,
    'Enemy3Shot': 1,
}


ENTITY_SPEED = {
    'Level1_bg0': 0,
    'Level1_bg1': 1,
    'Level1_bg2': 2,
    'Level1_bg3': 3,
    'Level1_bg4': 4,
    'Level2_bg0': 0,
    'Level2_bg1': 1,
    'Level2_bg2': 2,
    'Level2_bg3': 3,
    'Level2_bg4': 4,
    'Level2_bg5': 5,
    'Level2_bg6': 6,
    'Level3_bg0': 3,
    'Level3_bg1': 4,
    'Level3_bg2': 5,
    'Player1': 2,
    'Player1Shot': 5,
    'Player2': 2,
    'Player2Shot': 5,
    'Enemy1': 2,
    'Enemy1Shot': 10,
    'Enemy2': 1,
    'Enemy2Shot': 12,
    'Enemy3': 1,
    'Enemy3Shot': 8,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 100,
    'Enemy2': 125,
    'Enemy3': 75,
}

ENTITY_SCORE = {
    'Level1_bg0': 0,
    'Level1_bg1': 0,
    'Level1_bg2': 0,
    'Level1_bg3': 0,
    'Level1_bg4': 0,
    'Level1_bg5': 0,
    'LevLel1_bg6': 0,
    'Level2_bg0': 0,
    'Level2_bg1': 0,
    'Level2_bg2': 0,
    'Level2_bg3': 0,
    'Level2_bg4': 0,
    'Level2_bg5': 0,
    'Level2_bg6': 0,
    'Level3_bg0': 0,
    'Level3_bg1': 0,
    'Level3_bg2': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
    'Enemy3': 150,
    'Enemy3Shot': 0,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}

PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SPAWN_TIME = 2000
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
}

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = {
    'Level1' : 20000,
    'Level2' : 40000,
    'Level3' : 80000,
}




