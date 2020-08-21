import pygame
import setting as s

pygame.init()

class Target(pygame.sprite.Sprite):
    def __init__(self, xs, ys, scalex, scaley, points, group):
        pygame.sprite.Sprite.__init__(self)
        self.add(group)
        self.points = points
        self.image = pygame.Surface((scalex,scaley))
        self.image.fill(s.BAR_BACK)
        self.rect = self.image.get_rect(center=(xs,ys))
    
    def update(self):
        s.POINTS += self.points
        self.kill()
