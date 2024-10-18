# C
import pygame

COLOR_ORANGE = 255, 128, 0
COLOR_YELLOW = 255, 255, 0
COLOR_WHITE = 255, 255, 255
COLOR_GREEN = 0, 128, 0
COLOR_CYAN = 0, 128, 128

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
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
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
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,

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
    'Player1': 3,
    'Player1Shot': 1,
    'Player2': 3,
    'Player2Shot': 1,
    'Enemy1': 2,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 2,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 100,
    'Enemy2': 200,
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
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPE  RATIVE',
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

# S
SPAWN_TIME = 2000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 10000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
