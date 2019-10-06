import pygame
import time
import random



pygame.init()

#Screen size
display_width = 800
display_height =600

#color
black = (0,0,0)
white = (255, 255, 255)


#object width
car_width = 89

gameDisplay=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Racing Game')
clock = pygame.time.Clock()

gameExit = False

carImg = pygame.image.load('/home/nelsonfrank/Documents/code-room/python/pygame/images/top-car.png')

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_Object(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText =pygame.font.Font('/home/nelsonfrank/Documents/code-room/python/pygame/fonts/SourceCodePro-Regular.ttf', 80)
    TextSurf, TextRect = text_Object(text, largeText)
    TextRect =(display_width*0.3, display_height*0.35)

    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_main_loop()

def crashed():
    message_display("You Crashed!")


def game_main_loop():
    x = (display_width*0.45)
    y =(display_height*0.8)

    thing_startx= random.randrange(0, display_width)
    thing_starty= -600
    thing_width =100
    thing_height = 100
    thing_speed = 7

    #change position of object
    x_change= 0



    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            
            print(event)
            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.type == pygame.K_LEFT or pygame.K_RIGHT:
                    x_change = 0

        
        x+=x_change

        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color):
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty+=thing_speed

        car(x,y)

        if x > display_width-car_width or x<0:
            crashed()

        if thing_starty > display_height:
            thing_starty = 0- display_height
            thing_startx = random.randrange(0, display_width)


        if y < thing_starty+thing_height:
            print("y crossover")
            if x >thing_startx and x< thing_startx+thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width:
                print("x crossover")
                crashed()
            
        pygame.display.update()

        clock.tick(60) #set frame per second of the game

    pygame.quit()
    quit()

if __name__=="__main__":
    #call game_main_loop function
    game_main_loop()