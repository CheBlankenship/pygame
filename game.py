import pygame
import random

class Hero(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.




class Monster(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5

    def update(self, width, height):
        self.x += self.speed_x
        # self.y += self.speed_y
        if self.x  >= width:
            self.x = 0
            rand_num = random.randrange(20,480)
            self.y = rand_num
        if self.y >= height:
            self.speed_y = -30
        if self.x  < 0:
            self.speed_x = 40
        if self.y  < 0:
            self.speed_y = 50

    def render(self, screen):
        monster = pygame.image.load('monster.png')
        screen.blit(monster, (self.x,self.y))






def main():
    # declare the size of the canvas
    width = 512
    height = 480
    # initialize the pygame framework
    pygame.init()
    # create screen
    screen = pygame.display.set_mode((width, height))
    # give a image
    image = pygame.image.load('background.png').convert_alpha()
    goblin = pygame.image.load('goblin.png').convert_alpha()
    hero = pygame.image.load('hero.png').convert_alpha()
    # set window caption
    pygame.display.set_caption('Simple Example')
    # create a clock
    clock = pygame.time.Clock()
    # hero = Hero(250,250)
    monster = Monster(50,50)
    change_dir_countdown = 120
    # game loop
    stop_game = False
    while not stop_game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True

        change_dir_countdown -= 1
        if change_dir_countdown == 0:
            change_dir_countdown =  change_dir_countdown + 120
            rand_num = random.randint(0,4)
            if rand_num == 0:
                monster.y = 0



        screen.blit(image, (0,0))
        monster.render(screen)
        monster.update(width,height)
        pygame.display.update()
        # tick the clock to enforce a max framerate
        clock.tick(60)

# quit pygame properly to clean up resources
pygame.quit()

if __name__ == '__main__':
    main()
