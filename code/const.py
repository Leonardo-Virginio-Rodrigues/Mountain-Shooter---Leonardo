#C
import pygame
COLOR_ORANGE = 255,128,0
COLOR_YELLOW = 255, 255, 0
COLOR_WHITE = 255,255,255

#E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_HEALTH={
    'level1_bg0': 999,
    'level1_bg1': 999,
    'level1_bg2': 999,
    'level1_bg3': 999,
    'level1_bg4': 999,
    'level1_b5': 999,
    'level1_b6': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 50,
    'Enemy2': 60,
}

ENTITY_SPEED= {
    'level1_bg0': 0,
    'level1_bg1': 1,
    'level1_bg2': 2,
    'level1_bg3': 3,
    'level1_bg4': 4,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1,
}


#M
MENU_OPTION= ('NEW GAME 1P',
              'NEW GAME 2P - COOPE  RATIVE',
              'NEW GAME 2P - COMPETITIVE',
              'SCORE',
              'EXIT')

#P
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



#W
WIN_WIDTH = 576
WIN_HEIGHT = 324
