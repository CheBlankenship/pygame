import pygame

class Ball(object):
    def __init__(self,x,y,shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.speed_x = 10
        self.speed_y = 100
        self.radius = 50


    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x  + self.radius >= width:
            self.speed_x = -1
        if self.y + self.radius >= height:
            self.speed_y = -1
        if self.x -self.radius < 0:
            self.speed_x = 1
        if self.y - self.radius < 0:
            self.speed_y = 1


    def render(self, screen):
        if self.shape == 'circle':
            pygame.draw.circle(screen,(255,0,0),(self.x, self.y),self.radius)
        elif self.shape == 'rect':
            pygame.draw.rect(screen,(0,25,100),(self.x,self.y,50,50),0)
        elif self.shape == 'ellipse':
            pygame.draw.ellipse(screen,(100,100,100),(self.x, self.y,70,100),0)





def main():
    # declare the size of the canvas
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    ball_list = [
        Ball(5,500,'circle'),
        Ball(100,500,'rect'),
        Ball(50,10,'ellipse'),
        Ball(30,30,'circle'),
        Ball(200,30,'ellipse'),
        Ball(300,400,'rect')
    ]





    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################

    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.MOUSEBUTTONDOWN:
                print 'Click at coordinate %d, %d' % event.pos
                ball_list.append(Ball(50,50))
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        for ball in ball_list:
            ball.update(width, height)


        # fill background color
        screen.fill((25,100,20))

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        for ball in ball_list:
            ball.render(screen)


        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
