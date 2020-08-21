import pygame
import setting as s
import back as b
import time

pygame.init()

# other
font = pygame.font.Font(None, 40)
rezult_font = pygame.font.Font(None, 70)
color = (50,50,50)
bullet_color = (0,50,200)
speed_color = (100,220,0)
rezult_color = (210, 210, 210)
record_color = (200,200,200)
bg = (0,0,0)

def answer_window(screen, vari):
    if vari == 1:
        base = font.render("Вы хотите обнулить ангар ?", True, record_color)
        screen.blit(base, (s.X/2-170, s.Y/2-100))
    if vari == 2:
        base = font.render("Вы хотите обнулить рекорды ?", True, record_color)
        screen.blit(base, (s.X/2-170, s.Y/2-100))

def shop_buy(posi):
    # firs pillar
    if b.SH_BULLET_COUNT_R.collidepoint(posi):
        if s.GOLD >= s.SHOP_V[0]:
            s.GOLD -= s.SHOP_V[0]
            s.BULLET_COUNT += 1
    if b.SH_BULLET_SPEED_R.collidepoint(posi):
        if s.GOLD >= s.SHOP_V[1]:
            s.GOLD -= s.SHOP_V[1]
            s.BULLET_SPEED += 1
    if b.SH_BULLET_SIZE_R.collidepoint(posi):
        if s.GOLD >= s.SHOP_V[2]:
            s.GOLD -= s.SHOP_V[2]
            s.BULLET_SIZE += 1
    if b.SH_BULLET_RELOAD_R.collidepoint(posi):
        if s.GOLD >= s.SHOP_V[3]:
            s.GOLD -= s.SHOP_V[3]
            s.RELOAD_BUST += 1
    if b.SH_ROTATE_R.collidepoint(posi):
        if s.GOLD >= s.SHOP_V[4]:
            s.GOLD -= s.SHOP_V[4]
            s.ROTATE_BUST += 1
    if b.SH_SPEED_R.collidepoint(posi):
        if s.GOLD >= s.SHOP_V[5]:
            s.GOLD -= s.SHOP_V[5]
            s.SPEED_BUST += 1
    if b.SH_AMPL_R.collidepoint(posi):
        if s.GOLD >= s.SHOP_V[6]:
            s.GOLD -= s.SHOP_V[6]
            s.AMPLITUDE_BUST += 0.1
            s.AMPLITUDE_BUST = round(s.AMPLITUDE_BUST, 1)
    if b.SH_GOLD_R.collidepoint(posi):
        if s.GOLD >= s.SHOP_V[7]:
            s.GOLD -= s.SHOP_V[7]
            s.GOLD_BUST += 5

def restore_record():
    s.HONOR_STAK = [0,0,0,0,0,0,0,0,0,0]

def restore_store():
    s.BULLET_COUNT = 0
    s.BULLET_SPEED = 0
    s.BULLET_SIZE = 0
    s.ROTATE_BUST = 0
    s.RELOAD_BUST = 0
    s.GOLD_BUST = 0
    s.SPEED_BUST = 0
    s.AMPLITUDE_BUST = 0.1

def shop_table(screen):
    gold = rezult_font.render(str(s.GOLD), True, rezult_color)
    screen.blit(gold, (s.X-200,30))
    shoppi = []
    shoppi.append(s.BULLET_COUNT)
    shoppi.append(s.BULLET_SPEED)
    shoppi.append(s.BULLET_SIZE)
    shoppi.append(s.RELOAD_BUST)
    shoppi.append(s.ROTATE_BUST)
    shoppi.append(s.SPEED_BUST)
    shoppi.append(s.AMPLITUDE_BUST)
    shoppi.append(s.GOLD_BUST)
    for i in range(4):
        sho = rezult_font.render(str(shoppi[i]), True, record_color)
        screen.blit(sho, (200,70+i*150))
        golded = rezult_font.render(str(s.SHOP_V[i])+"g", True, record_color)
        screen.blit(golded, (300, 70+i*150))
        name = font.render(str(s.SHOP_NAME[i]), True, record_color)
        screen.blit(name, (40,150+i*150))
    for i in range(4):
        sho = rezult_font.render(str(shoppi[i+4]), True, record_color)
        screen.blit(sho, (600,70+i*150))
        golded = rezult_font.render(str(s.SHOP_V[i+4])+"g", True, record_color)
        screen.blit(golded, (700, 70+i*150))
        name = font.render(str(s.SHOP_NAME[i+4]), True, record_color)
        screen.blit(name, (440,150+i*150))


def record_table(screen):
    for i in range(10):
        honored = rezult_font.render(str(i+1)+" : "+str(int(s.HONOR_STAK[i])), True, record_color)
        screen.blit(honored, (s.X/2-50, 100+i*50))
    s.HONOR = 0
    #print('now is', time.strftime("%Y%m%d%h%M%S"))

def timer_rezult(screen):
    rezult_second = s.TIMER/s.FPS
    rezult = rezult_font.render("Время (сек): "+str(int(rezult_second)), True, rezult_color)
    screen.blit(rezult, (int(s.X/2)-100, 200))
    point = rezult_font.render("Счёт: "+str(int(s.POINTS)), True, rezult_color)
    screen.blit(point, (int(s.X/2)-100, 250))
    gold = rezult_font.render("Монеты: "+str(int(s.POINTS/5)+s.GOLD_BUST), True, rezult_color)
    screen.blit(gold, (int(s.X/2)-100, 300))

def schet():
    s.GOLD += int(s.POINTS/5) + s.GOLD_BUST
    s.HONOR = int(s.POINTS)
    s.HONOR_STAK[9] = s.HONOR
    s.HONOR_STAK.sort(reverse=True)

def menu_stats(screen):
    gold = font.render(str(s.GOLD), True, color)
    honor = font.render(str(s.HONOR_STAK[0]), True, color)
    screen.blit(gold, (s.X-140,30))
    screen.blit(honor, (s.X-140,100))
    saved = rezult_font.render(str("Сохранение"), True, record_color)
    screen.blit(saved, (s.X-500,s.Y-120))

def game_stats(screen):
    bullet = font.render(str(s.BULLET[0]), True, bullet_color)
    screen.blit(bullet, (50,30))
    speed = font.render(str(round(s.SPEED_COUNT*10, 1)), True, speed_color)
    screen.blit(speed, (50,60))

def key_pressed(key, press):
    if press == 2:
        s.RELOAD_NOW = True
    if press == 1:
        s.STOP = False
        if key == pygame.K_w:
            s.UP = True
        if key == pygame.K_s:
            s.DOWN = True
        if key == pygame.K_d:
            s.ROTATING_NOW = True
            #s.RIGHT_B = True
            if s.ROTATED == False:
                s.BASE_ROT += 1
            s.ROTATED = True
            if s.BASE_ROT == 8:
                s.BASE_ROT = 0
        if key == pygame.K_a:
            s.ROTATING_NOW = True
            #s.LEFT_B = True
            if s.ROTATED == False:
                s.BASE_ROT -= 1
            s.ROTATED = True
            if s.BASE_ROT == -8:
                s.BASE_ROT = 0

    if press == 0:
        s.STOP = True
        if key == pygame.K_w:
            s.UP = False
        if key == pygame.K_s:
            s.DOWN = False
