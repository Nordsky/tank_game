import pygame
import setting as s

pygame.init()

# stats


# main

class Player():
    def __init__(self, x, y):
        self.speed = 0
        self.speed_mask = [2,0]
        self.speed_max = int(s.TANK[0])+s.SPEED_BUST
        self.amp = float(s.TANK[1])+s.AMPLITUDE_BUST # tank's amplitude
        self.body_rot_speed = float(s.TANK[2])+s.ROTATE_BUST
        self.reload_speed = 2+s.RELOAD_BUST
        self.bullet_speed = s.BULLET[1]
        self.bullet_count = s.BULLET[0]
        # image
        # main body
        self.body = pygame.image.load(s.TANK[4][:len(s.TANK[4])-1])
        self.body = pygame.transform.scale(self.body, \
            (self.body.get_width()//6, self.body.get_height()//6))
        # main rotated body
        self.body_rot = pygame.image.load(s.TANK[5][:len(s.TANK[5])-1])
        self.body_rot = pygame.transform.scale(self.body_rot, \
            (self.body_rot.get_width()//6, self.body_rot.get_height()//6))
        # rect
        self.body_r = self.body.get_rect(center=(x,y))
        self.body_rot_r = self.body_rot.get_rect(center=(x,y))
        # this body 
        self.this_body = self.body
        self.this_body_r = self.body_rot_r

    # stats bars
        # rotated
        self.rotate_complite = 0
        self.rb_height = 5
        # base
        self.rotate_bar = pygame.Rect((self.this_body_r.x,\
            self.this_body_r.y+130, 0, 0))
        self.rotate_bar_surf = pygame.Surface((s.FPS*3, self.rb_height))
        self.rotate_bar_surf.fill(s.BAR_BACK)
        # find
        self.rotate_bar_f = pygame.Rect((self.this_body_r.x,\
            self.this_body_r.y+130, 0, 0))
        self.rotate_bar_surf_f = pygame.Surface((self.rotate_complite, self.rb_height))
        self.rotate_bar_surf_f.fill(s.BAR_COMPL)

        # rotated
        self.reload_complite = 0
        # base
        self.reload_bar = pygame.Rect((self.this_body_r.x,\
            self.this_body_r.y+150, 0, 0))
        self.reload_bar_surf = pygame.Surface((s.FPS*3, self.rb_height))
        self.reload_bar_surf.fill(s.BAR_BACK)
        # find
        self.reload_bar_f = pygame.Rect((self.this_body_r.x,\
            self.this_body_r.y+150, 0, 0))
        self.reload_bar_surf_f = pygame.Surface((self.reload_complite, self.rb_height))
        self.reload_bar_surf_f.fill(s.BAR_COMPL_R)

    def bar_update(self):
        # rotate
        self.rotate_bar = pygame.Rect((self.this_body_r.x,\
            self.this_body_r.y+130, 0, 0))
        if s.ROTATING_NOW:
            #self.speed = 0
            self.rotate_complite+=self.body_rot_speed + s.ROTATE_BUST
            if self.rotate_complite >= s.FPS*3:
                s.ROTATING_NOW = False
                self.rotate_complite = 0
            self.rotate_bar_f = pygame.Rect((self.this_body_r.x,\
            self.this_body_r.y+130, 0, 0))
            self.rotate_bar_surf_f = pygame.Surface((self.rotate_complite, self.rb_height))
            self.rotate_bar_surf_f.fill(s.BAR_COMPL)
        # reload
        self.reload_bar = pygame.Rect((self.this_body_r.x,\
            self.this_body_r.y+150, 0, 0))
        if s.RELOAD_NOW and self.bullet_count > 0:
            self.reload_complite+=self.reload_speed + s.RELOAD_BUST
            if self.reload_complite >= s.FPS*3:
                s.RELOAD_NOW = False
                self.reload_complite = 0
                self.bullet_count -= 1
                s.BULLET[0] -= 1
            self.reload_bar_f = pygame.Rect((self.this_body_r.x,\
            self.this_body_r.y+150, 0, 0))
            self.reload_bar_surf_f = pygame.Surface((self.reload_complite, self.rb_height))
            self.reload_bar_surf_f.fill(s.BAR_COMPL_R)

    # body game transform and/or move
    def body_rotate(self):
        if s.ROTATED:
            if s.BASE_ROT == 0:
                self.this_body = self.body
                self.speed_mask = [2,0]
            elif s.BASE_ROT == 1 or s.BASE_ROT == -7:
                self.this_body = self.body_rot
                self.speed_mask = [1,1]
            elif s.BASE_ROT == 2 or s.BASE_ROT == -6:
                self.this_body = pygame.transform.rotate(self.body, -90)
                self.speed_mask = [0,2]
            elif s.BASE_ROT == 3 or s.BASE_ROT == -5:
                self.this_body = pygame.transform.rotate(self.body_rot, -90)
                self.speed_mask = [-1,1]
            elif s.BASE_ROT == 4 or s.BASE_ROT == -4:
                self.this_body = pygame.transform.flip(self.body, 1, 0)
                self.speed_mask = [-2,0]
            elif s.BASE_ROT == 5 or s.BASE_ROT == -3:
                self.this_body = pygame.transform.flip(self.body_rot, 1, 1)
                self.speed_mask = [-1,-1]
            elif s.BASE_ROT == 6 or s.BASE_ROT == -2:
                self.this_body = pygame.transform.rotate(self.body, 90)
                self.speed_mask = [0,-2]
            elif s.BASE_ROT == 7 or s.BASE_ROT == -1:
                self.this_body = pygame.transform.rotate(self.body_rot, 90)
                self.speed_mask = [1,-1]
            s.ROTATED = False   
    def speeded(self, pos):
        if pos == 1: # up
            if self.speed <= self.speed_max:
                self.speed += self.amp
        if pos == 2: # down
            if self.speed >= self.speed_max*(-1):
                self.speed -= self.amp
        if pos == 3: # stop
            if self.speed > 0:
                self.speed -= self.amp
            if self.speed < 0:
                self.speed += self.amp
            if self.speed < 0.1 and self.speed > -0.1:
                self.speed = 0
        #print(self.speed)
    def move(self):
        if s.UP:
            self.speeded(1)
        if s.DOWN:
            self.speeded(2)
        if s.STOP:
            self.speeded(3)
        s.SPEED_COUNT = self.speed
        self.this_body_r.x += self.speed_mask[0]*self.speed
        self.this_body_r.y += self.speed_mask[1]*self.speed
    def update(self, screen):
        #screen.blit(two, (0,0))
        screen.blit(self.this_body, self.this_body_r)
        if s.ROTATING_NOW:
            self.bar_update()
            screen.blit(self.rotate_bar_surf, self.rotate_bar)
            screen.blit(self.rotate_bar_surf_f, self.rotate_bar_f)
        if s.RELOAD_NOW and self.bullet_count > 0:
            self.bar_update()
            screen.blit(self.reload_bar_surf, self.reload_bar)
            screen.blit(self.reload_bar_surf_f, self.reload_bar_f)
        #pygame.display.update(BLANK)
        pygame.display.update()
    def pre_game_update(self):
        self.speed_max = int(s.TANK[0])+s.SPEED_BUST
        self.amp = float(s.TANK[1])+s.AMPLITUDE_BUST # tank's amplitude
        self.body_rot_speed = float(s.TANK[2])+s.ROTATE_BUST
        self.reload_speed = 2+s.RELOAD_BUST
        self.bullet_speed = s.BULLET[1]
        self.bullet_count = s.BULLET[0]







