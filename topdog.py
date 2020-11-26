import pygame

import math
'''
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(1)
    left(1)
    if abs(pos()) < 1:
        break
end_fill()
done()
'''

pygame.init() #no idea what this does

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


pygame.display.set_caption("Top Diggity Dog")

clock = pygame.time.Clock() # where is the next method

run = True

planeX = 1
planeY = 650




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

    def draw(self, win):
        #pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

        win.blit(planesprites[self.angle//10], (self.x, self.y))
        self.hitbox = (self.x, self.y + 20, self.width, self.height - 40)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2) #Hitboxes

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

    def hit(self):
        print('Hit')
        pass

    def draw(self, win):
        #pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

        win.blit(plane2sprites[self.angle//10], (self.x, self.y))
        self.hitbox = (self.x, self.y + 20, self.width, self.height - 40 )
        pygame.draw.rect(win, (255,0,0), self.hitbox,2) #Hitboxes

class projectile(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self. color = color

    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.radius)


planeOne = plane(1,650,100,100,0,12,white)
planeTwo = enemyplane(1180,650,100,100,0,12,white)
shootLoop = 0
bombs=[]

win.blit(bg, (0,0))


def redrawGameWindow():

    win.blit(bg, (0,0))
    #win.fill(black)

    planeOne.draw(win)
    planeTwo.draw(win)

    for bomb in bombs:
        bomb.draw(win)

    

    pygame.display.update()


liftcoefficient = {
    355:0,
    0:2,
    5:2.5,
    10:2.75,
    15:2.5,
    20:2,
    25:0,
    155:0,
    160:2,
    165:2.5,
    170:2.75,
    175:2.5,
    180:2,
    185:0,
}

'''
# L = liftCoefficient * velocity

c = 0
W = 6
F = 12




Newtonian Law

F #thrust
L #lift
W #weight
D #drag
c=0 #angle of climb/attack

W = planeWeight * gravity


F * math.sin(c) - D * math.sin(c) + L* math.cos(c) - W = MAv #Vertical Force = negative planeY ? 

F * math.cos(c) - D * math.cos(c) + L * math.sin(c) = MAh #horizontal Force = planeX ?


gravity = 9.82
lift acceleration = 15
drag acceleration 
thrust acceleration = 
'''


while run:

    # digits are in milliseconds

    if shootLoop > 0:  
        shootLoop += 1

    if shootLoop > 10:
        shootLoop = 0    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        planeOne.angle += 5

    if keys[pygame.K_d]:
        planeOne.angle -= 5

    if planeOne.angle == 360:
        planeOne.angle = 0

    if planeOne.angle == -5:
        planeOne.angle = 355

    if 0 <= planeOne.angle <= 25 or 155<= planeOne.angle <= 185 or planeOne.angle == 355:
        L = 2 #liftcoefficient[planeOne.angle]
    else:
        L = 2 #0



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



    bulletY = planeOne.y + 25
    bulletX = planeOne.x + 50


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
            bomb.x += (20 * math.cos(math.radians(planeOne.angle))) #after every redraw the angle of the plane might change, which inherently changes the position of the bullet
        else:
            bombs.pop(bombs.index(bomb))

        if 0 < bomb.y < height:
            bomb.y -= (20 * math.sin(math.radians(planeOne.angle))) #after every redraw the angle of the plane might change, which inherently changes the position of the bullet
        else:
            bombs.pop(bombs.index(bomb))


# copy over plane one details for enemy plane

    if keys[pygame.K_RIGHT]:
        planeTwo.angle += 5

    if keys[pygame.K_LEFT]:
        planeTwo.angle -= 5

    if planeTwo.angle == 360:
        planeTwo.angle = 0

    if planeTwo.angle == -5:
        planeTwo.angle = 355

    if 0 <= planeTwo.angle <= 25 or 155<= planeTwo.angle <= 185 or planeTwo.angle == 355:
        L = 2 #liftcoefficient[planeTwo.angle]
    else:
        L = 2 #0



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






    redrawGameWindow()
    clock.tick(60)

















#angle of attack == c
#arbitrary lift coefficient as c increase, coefficient follows normal distribution , between 0 and 2

#set up a dictionary?



#Bumping
#Top layer Knock down
#bullets can travel width width +.5?
#36 images, 10 degree variance
# plane class with negative values to go backwards