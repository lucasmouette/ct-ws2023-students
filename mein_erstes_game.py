import pygame # Modul importieren

x = 320
y = 240
breite = 50
hoehe = 100

pygame.init()
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption('Basic Pygame program')

while True:
    pygame.draw.rect(surface=screen, 
                     color=(255, 255, 0), 
                     rect=(x, y, breite, hoehe))
    pygame.display.update()