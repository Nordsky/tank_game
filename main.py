import pygame
import setting as s
import filecontrol as f
import player as p
import bullet as bu
import target as ta
import back as b
import controled as c
import random as r

pygame.init()

screen = pygame.display.set_mode((s.X,s.Y))
pygame.display.set_caption(s.NAME+s.VER)
pygame.display.set_icon(b.ICON)
clock = pygame.time.Clock()

# support surface

# answer screen
def answer_label(vari):
    screen.blit(b.BACK_ANSWER, b.BACK_ANSWER_R)
    c.answer_window(screen, vari)
    screen.blit(b.YES_ANSWER, b.YES_ANSWER_R)
    screen.blit(b.NO_ANSWER, b.NO_ANSWER_R)

    while s.ANSWER:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
                s.MAIN = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if b.YES_ANSWER_R.collidepoint(e.pos):
                    s.ANSWER = False
                    s.BLANKED = False
                if b.NO_ANSWER_R.collidepoint(e.pos):
                    s.ANSWER = False
                    s.BLANKED = True
        
        pygame.display.update()



# map
def map():
    screen.blit(b.MAP_BACK, (0,0))
    screen.blit(b.LOC_1, b.LOC_1_R)
    screen.blit(b.LOC_2, b.LOC_2_R)
    screen.blit(b.LOC_3, b.LOC_3_R)
    screen.blit(b.BACK_MAP, b.BACK_MAP_R)
    pygame.display.update()
    while s.MAP:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
                s.MAIN = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if b.BACK_MAP_R.collidepoint(e.pos):
                    s.MAP = False
                    s.REPRINT = True
                if e.button == 1:
                    if b.LOC_1_R.collidepoint(e.pos):
                        s.LOC_ID = 0
                        s.MAP = False
                        s.MENU = False
                        s.LOAD = True
                    if b.LOC_2_R.collidepoint(e.pos):
                        s.LOC_ID = 1
                        s.MAP = False
                        s.MENU = False
                        s.LOAD = True
                    if b.LOC_3_R.collidepoint(e.pos):
                        s.LOC_ID = 2
                        s.MAP = False
                        s.MENU = False
                        s.LOAD = True
    
        pygame.display.update()

# shop
def shop():
    screen.blit(b.SHOP_BACK, (0,0))
    screen.blit(b.BACK_SHOP, b.BACK_SHOP_R)
    screen.blit(b.SH_BLANK, b.SH_BLANK_R)
    screen.blit(b.SH_BULLET_COUNT, b.SH_BULLET_COUNT_R)
    screen.blit(b.SH_BULLET_SPEED, b.SH_BULLET_SPEED_R)
    screen.blit(b.SH_BULLET_SIZE, b.SH_BULLET_SIZE_R)
    screen.blit(b.SH_BULLET_RELOAD, b.SH_BULLET_RELOAD_R)
    screen.blit(b.SH_ROTATE, b.SH_ROTATE_R)
    screen.blit(b.SH_SPEED, b.SH_SPEED_R)
    screen.blit(b.SH_AMPL, b.SH_AMPL_R)
    screen.blit(b.SH_GOLD, b.SH_GOLD_R)
    c.shop_table(screen)
    pygame.display.update()
    while s.SHOP:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
                s.MAIN = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if b.BACK_SHOP_R.collidepoint(e.pos):
                    s.SHOP = False
                    s.REPRINT = True
                if b.SH_BLANK_R.collidepoint(e.pos):
                    s.ANSWER = True
                    answer_label(1)
                    if not s.BLANKED:
                        c.restore_store()
                        screen.blit(b.SHOP_BACK, (0,0))
                        c.shop_table(screen)
                screen.blit(b.SHOP_BACK, (0,0))
                c.shop_buy(e.pos)
                c.shop_table(screen)
                screen.blit(b.BACK_SHOP, b.BACK_SHOP_R)
                screen.blit(b.SH_BLANK, b.SH_BLANK_R)
                screen.blit(b.SH_BULLET_COUNT, b.SH_BULLET_COUNT_R)
                screen.blit(b.SH_BULLET_SPEED, b.SH_BULLET_SPEED_R)
                screen.blit(b.SH_BULLET_SIZE, b.SH_BULLET_SIZE_R)
                screen.blit(b.SH_BULLET_RELOAD, b.SH_BULLET_RELOAD_R)
                screen.blit(b.SH_ROTATE, b.SH_ROTATE_R)
                screen.blit(b.SH_SPEED, b.SH_SPEED_R)
                screen.blit(b.SH_AMPL, b.SH_AMPL_R)
                screen.blit(b.SH_GOLD, b.SH_GOLD_R)
    
        pygame.display.update()

# record screen
def record():
    screen.blit(b.REC_BACK, (0,0))
    screen.blit(b.BACK_REC, b.BACK_REC_R)
    screen.blit(b.RE_BLANK, b.RE_BLANK_R)
    screen.blit(b.REC_TEXT_BECK, (int(s.X/2)-90, 60))
    c.record_table(screen)
    pygame.display.update()
    while s.RECORD:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
                s.MAIN = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if b.BACK_REC_R.collidepoint(e.pos):
                    s.RECORD = False
                    s.REPRINT = True
                if b.RE_BLANK_R.collidepoint(e.pos):
                    s.ANSWER = True
                    answer_label(2)
                    if not s.BLANKED:
                        c.restore_record()
    
            pygame.display.update()
            screen.blit(b.REC_BACK, (0,0))
            screen.blit(b.BACK_REC, b.BACK_REC_R)
            screen.blit(b.RE_BLANK, b.RE_BLANK_R)
            screen.blit(b.REC_TEXT_BECK, (int(s.X/2)-90, 60))
            c.record_table(screen)



# main surface

# menu
def menu():
    screen.blit(b.MENU_BACK, (0,0))
    screen.blit(b.START, b.START_R)
    screen.blit(b.SHOP, b.SHOP_R)
    screen.blit(b.RECORD, b.RECORD_R)
    screen.blit(b.BACK_MENU, b.BACK_MENU_R)
    screen.blit(b.THIS_BUTTON, b.THIS_BUTTON_R)
    screen.blit(b.GOLD_ICO, (s.X-200,20))
    screen.blit(b.HONOR_ICO, (s.X-200,90))
    c.menu_stats(screen)
    pygame.display.update()
    while s.MENU:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
                s.MAIN = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if b.START_R.collidepoint(e.pos):
                    s.MAP = True
                    map()
                if b.SHOP_R.collidepoint(e.pos):
                    s.SHOP = True
                    shop()
                if b.RECORD_R.collidepoint(e.pos):
                    s.RECORD = True
                    record()
                if b.BACK_MENU_R.collidepoint(e.pos):
                    s.MENU = False
                    s.MAIN = False
                if b.THIS_BUTTON_R.collidepoint(e.pos):
                    if s.SAVED:
                        s.SAVED = False
                        b.THIS_BUTTON = b.NOSAVED_BUTTON
                        b.THIS_BUTTON_R = b.NOSAVED_BUTTON_R
                    else:
                        s.SAVED = True
                        b.THIS_BUTTON = b.SAVED_BUTTON
                        b.THIS_BUTTON_R = b.SAVED_BUTTON_R
                    s.REPRINT = True
    
        if s.REPRINT:
            s.REPRINT = False
            screen.blit(b.MENU_BACK, (0,0))
            screen.blit(b.START, b.START_R)
            screen.blit(b.SHOP, b.SHOP_R)
            screen.blit(b.RECORD, b.RECORD_R)
            screen.blit(b.BACK_MENU, b.BACK_MENU_R)
            screen.blit(b.THIS_BUTTON, b.THIS_BUTTON_R)
            screen.blit(b.GOLD_ICO, (1400,20))
            screen.blit(b.HONOR_ICO, (1400,90))
            c.menu_stats(screen)

        pygame.display.update()

# load
def load():
    if s.LOAD:
        f.tank_load()
        b.LOC_BACK = pygame.image.load(s.LOADS[s.LOC_ID])
        screen.blit(b.LOC_BACK,(0,0))
        pygame.display.update()
    while s.LOAD:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
                s.MAIN = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                s.LOAD = False
                s.GAME = True
            if e.type == pygame.KEYDOWN:
                s.LOAD = False
                s.GAME = True

        pygame.display.update()

# game
def game():
    if s.GAME:
        s.TIMER = 0
        gamer = p.Player(300, 200)
        s.POINTS = 0
        bullets = pygame.sprite.Group()
        targets = pygame.sprite.Group()
        ta.Target(1000,700,50,20,11,targets)
        s.BULLET = [7+s.BULLET_COUNT, 20+s.BULLET_SPEED, 10+s.BULLET_SIZE]
        gamer.pre_game_update()
        b.GAME_BACK = pygame.image.load(s.GAMES[s.LOC_ID])
        screen.blit(b.GAME_BACK,(0,0))
        screen.blit(b.QUIT_GAME,b.QUIT_GAME_R)
        c.game_stats(screen)
        gamer.update(screen)
        pygame.display.update()
    while s.GAME:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
                s.MAIN = False
            if e.type == pygame.KEYDOWN:
                c.key_pressed(e.key, 1)
            if e.type == pygame.KEYUP:
                c.key_pressed(e.key, 0)
            if e.type == pygame.MOUSEBUTTONDOWN:
                if not s.RELOAD_NOW:
                    bu.Bullet(s.BULLET[2], gamer.this_body_r.x, gamer.this_body_r.y, e.pos[0], e.pos[1], s.BULLET[1], bullets)
                c.key_pressed(e.pos, 2)
                if b.QUIT_GAME_R.collidepoint(e.pos):
                    s.GAME = False
                    s.RECORD = True

        screen.blit(b.GAME_BACK,(0,0))
        screen.blit(b.QUIT_GAME,b.QUIT_GAME_R)
        #screen.blit(p.TRIG, p.BLANK)
        if not s.ROTATING_NOW:
            gamer.body_rotate()
        gamer.move()
        gamer.update(screen)
        bullets.update()
        bullets.draw(screen)
        hits = pygame.sprite.groupcollide(targets, bullets, False, True)
        if hits:
            targets.update()
            ta.Target(r.randint(30,s.X-30), r.randint(30,s.Y-30),r.randint(10,50),r.randint(10,50),\
                r.randint(5,20), targets)
        targets.draw(screen)
        c.game_stats(screen)
            
        pygame.display.update()
        clock.tick(s.FPS)
        s.TIMER += 1

# finish score
def score():
    if s.RECORD:
        screen.blit(b.LOC_BACK,(0,0))
        c.schet()
        pygame.display.update()
    while s.RECORD:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
                s.MAIN = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                s.RECORD = False
                s.MENU = True
            if e.type == pygame.KEYDOWN:
                s.RECORD = False
                s.MENU = True

        c.timer_rezult(screen)
        pygame.display.update()


# base cycle
f.check_path()
# start
f.record_load()
f.start()

# loop
while s.MAIN:
    menu()
    load()
    game()
    score()
# finish
if s.SAVED:
    f.finish()
    f.record_save()
