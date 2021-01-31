import pygame
import math

pygame.init()

width = 1280
height = 960

win = pygame.display.set_mode((width, height))
bg = pygame.image.load('png/BG scaled.png')

planesprites = [pygame.image.load('png/plane/Fly 1-00.png'), pygame.image.load('png/plane/Fly 1-10.png'), pygame.image.load('png/plane/Fly 1-20.png'),
                pygame.image.load('png/plane/Fly 1-30.png'),pygame.image.load('png/plane/Fly 1-40.png'),pygame.image.load('png/plane/Fly 1-50.png'),
                pygame.image.load('png/plane/Fly 1-60.png'),pygame.image.load('png/plane/Fly 1-70.png'),pygame.image.load('png/plane/Fly 1-80.png'),
                pygame.image.load('png/plane/Fly 1-90.png'),pygame.image.load('png/plane/Fly 1-100.png'),pygame.image.load('png/plane/Fly 1-110.png'),
                pygame.image.load('png/plane/Fly 1-120.png'),pygame.image.load('png/plane/Fly 1-130.png'),pygame.image.load('png/plane/Fly 1-140.png'),
                pygame.image.load('png/plane/Fly 1-150.png'),pygame.image.load('png/plane/Fly 1-160.png'),pygame.image.load('png/plane/Fly 1-170.png'),
                pygame.image.load('png/plane/Fly 1-180.png'),pygame.image.load('png/plane/Fly 1-190.png'),pygame.image.load('png/plane/Fly 1-200.png'),
                pygame.image.load('png/plane/Fly 1-210.png'),pygame.image.load('png/plane/Fly 1-220.png'),pygame.image.load('png/plane/Fly 1-230.png'),
                pygame.image.load('png/plane/Fly 1-240.png'),pygame.image.load('png/plane/Fly 1-250.png'),pygame.image.load('png/plane/Fly 1-260.png'),
                pygame.image.load('png/plane/Fly 1-270.png'),pygame.image.load('png/plane/Fly 1-280.png'),pygame.image.load('png/plane/Fly 1-290.png'),
                pygame.image.load('png/plane/Fly 1-300.png'),pygame.image.load('png/plane/Fly 1-310.png'),pygame.image.load('png/plane/Fly 1-320.png'),
                pygame.image.load('png/plane/Fly 1-330.png'),pygame.image.load('png/plane/Fly 1-340.png'),pygame.image.load('png/plane/Fly 1-350.png'),
                pygame.image.load('png/plane/Fly 1-360.png')
                ]

plane2sprites = [pygame.image.load('png/plane2/Fly 1-00.png'), pygame.image.load('png/plane2/Fly 1-10.png'), pygame.image.load('png/plane2/Fly 1-20.png'),
                pygame.image.load('png/plane2/Fly 1-30.png'),pygame.image.load('png/plane2/Fly 1-40.png'),pygame.image.load('png/plane2/Fly 1-50.png'),
                pygame.image.load('png/plane2/Fly 1-60.png'),pygame.image.load('png/plane2/Fly 1-70.png'),pygame.image.load('png/plane2/Fly 1-80.png'),
                pygame.image.load('png/plane2/Fly 1-90.png'),pygame.image.load('png/plane2/Fly 1-100.png'),pygame.image.load('png/plane2/Fly 1-110.png'),
                pygame.image.load('png/plane2/Fly 1-120.png'),pygame.image.load('png/plane2/Fly 1-130.png'),pygame.image.load('png/plane2/Fly 1-140.png'),
                pygame.image.load('png/plane2/Fly 1-150.png'),pygame.image.load('png/plane2/Fly 1-160.png'),pygame.image.load('png/plane2/Fly 1-170.png'),
                pygame.image.load('png/plane2/Fly 1-180.png'),pygame.image.load('png/plane2/Fly 1-190.png'),pygame.image.load('png/plane2/Fly 1-200.png'),
                pygame.image.load('png/plane2/Fly 1-210.png'),pygame.image.load('png/plane2/Fly 1-220.png'),pygame.image.load('png/plane2/Fly 1-230.png'),
                pygame.image.load('png/plane2/Fly 1-240.png'),pygame.image.load('png/plane2/Fly 1-250.png'),pygame.image.load('png/plane2/Fly 1-260.png'),
                pygame.image.load('png/plane2/Fly 1-270.png'),pygame.image.load('png/plane2/Fly 1-280.png'),pygame.image.load('png/plane2/Fly 1-290.png'),
                pygame.image.load('png/plane2/Fly 1-300.png'),pygame.image.load('png/plane2/Fly 1-310.png'),pygame.image.load('png/plane2/Fly 1-320.png'),
                pygame.image.load('png/plane2/Fly 1-330.png'),pygame.image.load('png/plane2/Fly 1-340.png'),pygame.image.load('png/plane2/Fly 1-350.png'),
                pygame.image.load('png/plane2/Fly 1-360.png')
                ]


black = (  0,   0,   0)
white = (255, 255, 255)
red = (255,   0,   0)
green = (  0, 255,   0)
blue = (  0,   0, 255)

pygame.display.set_caption("Top Dog")

clock = pygame.time.Clock()

run = False

planeX = 1
planeY = 650
L = 2 #lift speed


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

class plane(object):
    def __init__(self, x, y, width, height, angle, thrust, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.thrust = thrust
        self.color = color
        self.weight = 2
        self.hitbox = (self.x, self.y + 20, self.width, self.height - 40)
        self.health = 250
    
    def hit(self):
        print('Hit')
        pass
        self.health-=25

    def draw(self, win):

        win.blit(planesprites[self.angle//10], (self.x, self.y))
        self.hitbox = (self.x, self.y + 20, self.width, self.height - 40)
        
        pygame.draw.rect(win, (200,255,200), (30, 10 , 250, 10),)

        if self.health > 125:
            pygame.draw.rect(win, (0,255,0), (30, 10 , self.health, 10))

        elif 50 < self.health <=125:
            pygame.draw.rect(win, (255,165,0), (30, 10 , self.health, 10))
        
        else:
            pygame.draw.rect(win, (255,0,0), (30, 10 , self.health, 10))

        pygame.draw.rect(win, (0,0,0), (30, 10 , 250, 10), 2)

class projectile(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self. color = color

    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.radius)



class enemyplane(object):
    def __init__(self, x, y, width, height, angle, thrust, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.thrust = thrust
        self.color = color
        self.weight = 2
        self.hitbox = (self.x, self.y + 20, self.width, self.height - 40)
        self.health = 250

    def hit(self):
        print('Hit')
        pass
        self.health-=25
        

    def draw(self, win):

        win.blit(plane2sprites[self.angle//10], (self.x, self.y))
        self.hitbox = (self.x, self.y + 20, self.width, self.height - 40)
        
        pygame.draw.rect(win, (200,200,255), (1000, 10 , 250, 10),)

        if self.health > 125:
            pygame.draw.rect(win, (0,0,255), (1000, 10 , self.health, 10))

        elif 50 < self.health <=125:
            pygame.draw.rect(win, (255,165,0), (1000, 10 , self.health, 10))
        
        else:
            pygame.draw.rect(win, (255,0,0), (1000, 10 , self.health, 10))
        
       
        pygame.draw.rect(win, (0,0,0), (1000, 10 , 250, 10), 2)





def redrawGameWindow():

    win.blit(bg, (0,0))

    planeOne.draw(win)
    planeTwo.draw(win)

    for bomb in bombs:
        bomb.draw(win)

    for bomb in enemybombs:
        bomb.draw(win)

    pygame.display.update()


intro = True

while intro:

    planeOne = plane(1,650,100,100,0,12,white)
    planeTwo = enemyplane(1180,650,100,100,0,12,white)
    shootLoop = 0
    shootLoopEnemy = 0
    bombs=[]
    enemybombs=[]

    win.blit(bg, (0,0))

    planeOne.health = 250
    planeTwo.health = 250

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            run = True

    
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("Top Dog", largeText)
    TextRect.center = ((width/2),(height/2))
    win.blit(TextSurf, TextRect)

    smallText = pygame.font.Font('freesansbold.ttf',30)
    instructionSurf, instructionRect = text_objects("press any key to play", smallText)
    instructionRect.center = ((width/2),(height*2/3))
    win.blit(instructionSurf, instructionRect)
    pygame.display.update()
    clock.tick(15)


    while run:


        if shootLoop > 0:  
            shootLoop += 1

        if shootLoop > 10:
            shootLoop = 0    
        
        if shootLoopEnemy > 0:  
            shootLoopEnemy += 1

        if shootLoopEnemy > 10:
            shootLoopEnemy = 0 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                intro = False

        keys = pygame.key.get_pressed()

#plane One
        if keys[pygame.K_a]:
            planeOne.angle += 5

        if keys[pygame.K_d]:
            planeOne.angle -= 5

        if planeOne.angle == 360:
            planeOne.angle = 0

        if planeOne.angle == -5:
            planeOne.angle = 355


        horizontalF = (planeOne.thrust * math.cos(math.radians(planeOne.angle))) + (L * math.sin(math.radians(planeOne.angle)))

        verticalF = (planeOne.thrust * math.sin(math.radians(planeOne.angle))) + (L * math.cos(math.radians(planeOne.angle))) - planeOne.weight



        planeOne.x += horizontalF

        if planeOne.x > width:
            planeOne.x = 1

        if planeOne.x < 1:
            planeOne.x = width



        planeOne.y-=verticalF

        if planeOne.y > height:
            planeOne.y = 1

        if planeOne.y < 1:
            planeOne.y = height


        if keys[pygame.K_LSHIFT] and shootLoop == 0:
            if len(bombs) < 3 :
                bombs.append(projectile(planeOne.x + 50, planeOne.y + 25, 10, black))
            
            shootLoop = 1

        for bomb in bombs:
            if bomb.y - bomb.radius < planeTwo.hitbox[1] + planeTwo.hitbox[3] and bomb.y + bomb.radius > planeTwo.hitbox[1]:
                if bomb.x + bomb.radius > planeTwo.hitbox[0] and bomb.x - bomb.radius < planeTwo.hitbox[0] + planeTwo.hitbox[2]:
                    planeTwo.hit() 
                    bombs.pop(bombs.index(bomb))

            if 0 < bomb.x < width:
                bomb.x += (20 * math.cos(math.radians(planeOne.angle)))
            else:
                bombs.pop(bombs.index(bomb))

            if 0 < bomb.y < height:
                bomb.y -= (20 * math.sin(math.radians(planeOne.angle))) 
            else:
                bombs.pop(bombs.index(bomb))


#planeTwo

        if keys[pygame.K_RIGHT]:
            planeTwo.angle += 5

        if keys[pygame.K_LEFT]:
            planeTwo.angle -= 5

        if planeTwo.angle == 360:
            planeTwo.angle = 0

        if planeTwo.angle == -5:
            planeTwo.angle = 355


        horizontalFtwo = (planeTwo.thrust * math.cos(math.radians(planeTwo.angle))) + (L * math.sin(math.radians(planeTwo.angle)))

        verticalFtwo = (planeTwo.thrust * math.sin(math.radians(planeTwo.angle))) + (L * math.cos(math.radians(planeTwo.angle))) - planeTwo.weight



        planeTwo.x -= horizontalFtwo

        if planeTwo.x > width:
            planeTwo.x = 1

        if planeTwo.x < 1:
            planeTwo.x = width



        planeTwo.y-=verticalFtwo

        if planeTwo.y > height:
            planeTwo.y = 1

        if planeTwo.y < 1:
            planeTwo.y = height


        if keys[pygame.K_RSHIFT] and shootLoopEnemy == 0:
            if len(enemybombs) < 3 :
                enemybombs.append(projectile(planeTwo.x + 50, planeTwo.y + 25, 10, black))
            
            shootLoopEnemy = 1
            
        for bomb in enemybombs:
            if bomb.y - bomb.radius < planeOne.hitbox[1] + planeOne.hitbox[3] and bomb.y + bomb.radius > planeOne.hitbox[1]:
                if bomb.x + bomb.radius > planeOne.hitbox[0] and bomb.x - bomb.radius < planeOne.hitbox[0] + planeOne.hitbox[2]:
                    planeOne.hit() 
                    enemybombs.pop(enemybombs.index(bomb))

            if 0 < bomb.x < width:
                bomb.x -= (20 * math.cos(math.radians(planeTwo.angle)))
            else:
                enemybombs.pop(enemybombs.index(bomb))

            if 0 < bomb.y < height:
                bomb.y -= (20 * math.sin(math.radians(planeTwo.angle)))
            else:
                enemybombs.pop(enemybombs.index(bomb))
            
        if planeOne.health == 0:

            largeText = pygame.font.Font('freesansbold.ttf',115)
            TextSurf, TextRect = text_objects("Blue Won!", largeText)
            TextRect.center = ((width/2),(height/2))
            win.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)
            run = False

        if planeTwo.health == 0:

            largeText = pygame.font.Font('freesansbold.ttf',115)
            TextSurf, TextRect = text_objects("Green Won!", largeText)
            TextRect.center = ((width/2),(height/2))
            win.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)
            run = False


        redrawGameWindow()
        clock.tick(60)
