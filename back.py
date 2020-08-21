import pygame
import setting as s

pygame.init()


# main
Y = 120
ICON = pygame.image.load("pic/icon/icon_1.png")
GOLD_ICO = pygame.image.load("pic/icon/game/coin_test.png")
HONOR_ICO = pygame.image.load("pic/icon/game/honor_test.png")

# answer
BACK_ANSWER = pygame.Surface((600,300))
BACK_ANSWER.fill((50,20,120))
BACK_ANSWER_R = BACK_ANSWER.get_rect(center=(s.X/2,s.Y/2))

YES_ANSWER = pygame.image.load("pic/button/answer_yes.png")
YES_ANSWER_R = YES_ANSWER.get_rect(center=(s.X/2+150, s.Y/2+80))

NO_ANSWER = pygame.image.load("pic/button/answer_no.png")
NO_ANSWER_R = NO_ANSWER.get_rect(center=(s.X/2-150, s.Y/2+80))

# menu
MENU_BACK = pygame.image.load("pic/fon/menu_fon.jpg")

START = pygame.image.load("pic/button/start_test.jpg")
START_R = START.get_rect(center=(s.X/2,s.Y/2-Y-30))

SHOP = pygame.image.load("pic/button/shop_test.jpg")
SHOP_R = SHOP.get_rect(center=(s.X/2,s.Y/2))

RECORD = pygame.image.load("pic/button/record_test.jpg")
RECORD_R = RECORD.get_rect(center=(s.X/2,s.Y/2+Y+30))

BACK_MENU = pygame.image.load("pic/button/back_test.jpg")
BACK_MENU_R = BACK_MENU.get_rect(center=(150,s.Y-50))

SAVED_BUTTON = pygame.image.load("pic/button/check_yes.jpg")
SAVED_BUTTON_R = SAVED_BUTTON.get_rect(center=(s.X-100,s.Y-100))

NOSAVED_BUTTON = pygame.image.load("pic/button/check_no.jpg")
NOSAVED_BUTTON_R = NOSAVED_BUTTON.get_rect(center=(s.X-100,s.Y-100))

THIS_BUTTON = SAVED_BUTTON
THIS_BUTTON_R = SAVED_BUTTON_R

# map
MAP_BACK = pygame.image.load("pic/fon/map_fon_2.jpg")

LOC_1 = pygame.image.load("pic/icon/map/razvilka.png")
LOC_1_R = LOC_1.get_rect(center=(850,200))

LOC_2 = pygame.image.load("pic/icon/map/pole.png")
LOC_2_R = LOC_2.get_rect(center=(500,700))

LOC_3 = pygame.image.load("pic/icon/map/snow.png")
LOC_3_R = LOC_3.get_rect(center=(1540,100))


#LOC_1_INFO = pygame.Surface((200,400))
#...

BACK_MAP = pygame.image.load("pic/button/back_test.jpg")
BACK_MAP_R = BACK_MAP.get_rect(center=(150,s.Y-50))

# shop
SHOP_BACK = pygame.image.load("pic/fon/shop_fon.jpg")

BACK_SHOP = pygame.image.load("pic/button/back_test.jpg")
BACK_SHOP_R = BACK_SHOP.get_rect(center=(150,s.Y-50))

# first pillar
SH_BULLET_COUNT = pygame.image.load("pic/button/bullet_count.jpg")
SH_BULLET_COUNT_R = SH_BULLET_COUNT.get_rect(center=(100,100))

SH_BULLET_SPEED = pygame.image.load("pic/button/bullet_speed.jpg")
SH_BULLET_SPEED_R = SH_BULLET_SPEED.get_rect(center=(100,250))

SH_BULLET_SIZE = pygame.image.load("pic/button/bullet_size.jpg")
SH_BULLET_SIZE_R = SH_BULLET_SIZE.get_rect(center=(100,400))

SH_BULLET_RELOAD = pygame.image.load("pic/button/bullet_reload.jpg")
SH_BULLET_RELOAD_R = SH_BULLET_RELOAD.get_rect(center=(100,550))

# second pillar
SH_ROTATE = pygame.image.load("pic/button/tank_rotate.jpg")
SH_ROTATE_R = SH_ROTATE.get_rect(center=(500,100))

SH_SPEED = pygame.image.load("pic/button/tank_speed.jpg")
SH_SPEED_R = SH_SPEED.get_rect(center=(500,250))

SH_AMPL = pygame.image.load("pic/button/tank_amplitude.jpg")
SH_AMPL_R = SH_AMPL.get_rect(center=(500,400))

SH_GOLD = pygame.image.load("pic/button/gold_bust.jpg")
SH_GOLD_R = SH_GOLD.get_rect(center=(500,550))



SH_BLANK = pygame.image.load("pic/button/rerere.jpg")
SH_BLANK_R = SH_BLANK.get_rect(center=(s.X-100,s.Y-50))


# record
REC_BACK = pygame.image.load("pic/fon/record_fon.jpg")

BACK_REC = pygame.image.load("pic/button/back_test.jpg")
BACK_REC_R = BACK_REC.get_rect(center=(150,s.Y-50))

REC_TEXT_BECK = pygame.Surface((200,600))
REC_TEXT_BECK.fill((50,50,50))

RE_BLANK = pygame.image.load("pic/button/rerere.jpg")
RE_BLANK_R = RE_BLANK.get_rect(center=(s.X-100,s.Y-50))

# load
LOC_BACK = None

# game
GAME_BACK = None

QUIT_GAME = pygame.image.load("pic/button/quit.png")
QUIT_GAME_R = QUIT_GAME.get_rect(center=(s.X-80,80))