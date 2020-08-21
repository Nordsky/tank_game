# constans
X = 1600
Y = 900
NAME = "Tanks "
VER = "v 1.1.7"

MAIN = True
FPS = 30

MENU = True
MAP = False
SHOP = False
RECORD = False
LOAD = False
GAME = False
ANSWER = False

REPRINT = False
BLANKED = False
SAVED = True

# files param
BULLET_COUNT = 0
BULLET_SPEED = 0
BULLET_SIZE = 0
ROTATE_BUST = 0
RELOAD_BUST = 0
GOLD_BUST = 0
SPEED_BUST = 0
AMPLITUDE_BUST = 0
GOLD = 500
HONOR = 0

HONOR_STAK = [0,0,0,0,0,0,0,0,0,0]

# base var
BASE_PATH = "files/obj/t_34.txt"
TANK = []
BULLET = [7+BULLET_COUNT, 20+BULLET_SPEED, 10+BULLET_SIZE]
SPEED_COUNT = 0
POINTS = 0

# game var
LOC_ID = 0
TIMER = 0

STOP = True
UP = False
DOWN = False
ROTATED = False
LEFT_T = False
RIGHT_T = False

BASE_ROT = 0
ROT_STAT = [0,-90, 180, -90]

SHOP_V = [100,120,100,200,50,100,130,700]
SHOP_NAME = ["Количество снарядов", "Скорость снарядов", "Размер снарядов","Перезарядка снарядов",\
    "Скорость поворота танка","Скорость танка","Амплитуда танка","Бонус к ресурсам"]

# bar static
ROTATING_NOW = False
RELOAD_NOW = False

# game maps
LOADS = ["pic/fon/location/razvilka_screen.jpg","pic/fon/location/pole_screen.jpg","pic/fon/location/snow_screen.jpg"]
GAMES = ["pic/fon/location/razvilka.jpg","pic/fon/location/pole.jpg","pic/fon/location/snow.jpg"]

#color
BAR_BACK = (30,30,30)
BAR_COMPL = (0,200,0)
BAR_COMPL_R = (200,150,0)
FIRE = (150,0,0)

# function
