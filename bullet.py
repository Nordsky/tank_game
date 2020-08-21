import pygame
import setting as s

pygame.init()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, size, xs, ys, xf, yf, speed, group):
        pygame.sprite.Sprite.__init__(self)
        self.add(group)
        self.line = int((abs(xf-xs)**2+abs(yf-ys)**2)**0.5)
        self.cell = int(self.line/speed)
        self.speed_x = (xf-xs)/self.cell
        self.speed_y = (yf-ys)/self.cell
        self.image = pygame.Surface((size,size))
        self.image.fill(s.FIRE)
        self.rect = self.image.get_rect(center=(xs,ys))
    
    def update(self):
        if self.rect.x < s.X and self.rect.x > 0\
            and self.rect.y < s.Y and self.rect.y > 0:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        else:
            self.kill()


