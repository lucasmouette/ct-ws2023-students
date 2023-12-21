import pygame

WINDOW_SIZE = (640, 480) # Variablen, die als Konstanten gelten IMMER groß schreiben
TILE_SIZE = (32, 32)
walls = ((0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (9,0), (10,0),
         (0,1),                                                                (10,1),
         (0,2),
         (0,3),)
snake = [[10,10], [10,11], [10,12], ...]
apple = [[5,5], [3,3], ...]

''' 
Divide and Conquer

[x]   * Im Speicher abbilden: (damit der Rechner das versteht)
            - Spielfeld
            - Schlange
            - Äpfel
[ ]   * Level-Datei einlesen
[ ]   * Tastatureingaben (z.B. Pfeiltasten) verarbeiten
[ ]   * Anfangspunkt der Schlange ermitteln
[ ]   * Befehl um Schlanze zu vergrößern
[ ]   * Darstellung und zeichnen:
            - Äpfel
            - Schlange
            - Wände
[ ]   * Game Over bestimmen
[ ]   * Interaktion mit Wänden (Leben verlieren): Spezifikation unklar (stirbt direkt oder verliert Leben?)
[ ]   * Physik: Bewegung der Schlange (in Einheit px / s)
  
'''

def read_level(filename):
    with open(filename, 'r', encoding='utf8') as file_handler:
        level_string 

def to_pixels(x, y):
    x_in_pixels = x * TILE_SIZE[0]
    y_in_pixels = y * TILE_SIZE[1]
    return x_in_pixels, y_in_pixels

def draw_wall(screen, x, y):
    x_in_pixels, y_in_pixels = to_pixels(x, y)

    pygame.draw.rect(surface=screen,    
        color=(255, 0, 0),
        rect=(x_in_pixels, y_in_pixels, TILE_SIZE[0], TILE_SIZE[1]))

def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.clock
    pygame.display.set_caption('Awesome Snake')

    print('Welcome to my first Snake Game')
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # 1. Clear
        screen.fill('black')

        # 2. Move
        # pygame.draw.rect(surface=screen,    
        #          color=(255, 0, 0),
        #         rect=(20, 30, 60, 60))
        
        # 3. Draw
        for wall in walls:
            draw_wall(screen, wall[0], wall[1])

        # pygame.display.update()

        # 4. Update (double buffering)
        clock.tick(60)















    
if __name__ == '__main__':
    main()