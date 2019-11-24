import pygame
import pygame.font
import time
import math
pygame.init()


class ball(object):
    def __init__(self,x,y,radius,color,surf):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.surf = surf
        

    def draw(self,surf):
        pygame.draw.circle(self.surf, (0,0,0), (int(self.x),int(self.y)), self.radius)


    @staticmethod
    def ballPath(startx, starty, power, ang, time,i):
        angle = ang
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = (velx) * time
        #distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)
        distY = (vely) * time

        newx = round(distX + startx)
        newy = round(starty - distY)


        return (newx, newy)


    def redrawWindow(self,surf,obj,line):
        obj.draw(self.surf)
        pygame.draw.line(self.surf, (255,255,255),line[0], line[1])
        pygame.display.update()

    def findAngle(self,pos,obj):
        sX = obj.x
        sY = obj.y
        try:
            angle = math.atan((sY - pos[1]) / (sX - pos[0]))
        except:
            angle = math.pi / 2

        if pos[1] < sY and pos[0] > sX:
            angle = abs(angle)
        elif pos[1] < sY and pos[0] < sX:
            angle = math.pi - angle
        elif pos[1] > sY and pos[0] < sX:
            angle = math.pi + abs(angle)
        elif pos[1] > sY and pos[0] > sX:
            angle = (math.pi * 2) - angle

        return angle
    def game_intro(self,surf):
        self.bg = pygame.image.load('Course2.png')
        #self.bg = pygame.image.load('mainscreen.jpg')
        run = True
        time = 0
        power = 0
        angle = 0
        shoot = False
        clock = pygame.time.Clock()
        i = 1
        while run:
            clock.tick(200)
            if shoot:
                #if golfBall.y < 500 - golfBall.radius:
                if (self.x == 400-self.radius and self.y == 99):
                    shoot = False
                    self.x = 118
                    self.y = 453
                    time = 0
                else:
                    time += 0.05
                    po = ball.ballPath(x, y, power, angle, time,i)
                    self.x = po[0] 
                    self.y = po[1]
            
                    if self.x<0+self.radius:
                        self.x = -self.x
                    if self.x>236-self.radius and self.y>=210:
                        self.x  = 2*(236 - self.radius) - self.x
                        #self.angle = - self.angle
                    if self.y<0+self.radius:
                        self.y = -self.y
                    if self.y<210 and self.x>499-self.radius:
                        self.x = 2*(499 - self.radius) - self.x
                    if self.y<0+self.radius:
                        self.y = -self.y
                    if (self.x>0 and self.x<= 236-self.radius) and self.y > 499-self.radius:
                        self.y = 2*(499 - self.radius) - self.y
                    if (self.x>=236 and self.x<= 499-self.radius) and self.y > 210-self.radius:
                        self.y = 2*(210 - self.radius) - self.y
                    if self.y > 499:
                        self.y = 2*(210 - self.radius) - self.y
                    if self.y<0+self.radius:
                        self.y = -self.y

            line = [(self.x, self.y), pygame.mouse.get_pos()]
            self.redrawWindow(surf,self,line)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not shoot:
                        x = self.x
                        y = self.y
                        pos =pygame.mouse.get_pos()
                        print(pos)
                        shoot = True
                        power = math.sqrt((line[1][1]-line[0][1])**2 +(line[1][0]-line[0][1])**2)/8
                        angle = self.findAngle(pos,self)
            
            self.surf.blit(self.bg,(0,0))
            pygame.display.update()



        pygame.quit()
        quit()


class mainScreen():
    
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode((655, 383))
        self.bg = pygame.image.load('mainscreen.jpg')
        self.win.blit(self.bg,(0,0))
        pygame.display.set_caption("First Game")
        largeText = pygame.font.Font('Kardust TS Condensed Bold Italic.ttf',72)
        TextSurf, TextRect = self.text_objects("Mini Golf", largeText)
        TextRect.center = ((655/2),(70))
        self.win.blit(TextSurf, TextRect)
        
        
        
    def text_objects(self,text, font):
        black = [0,0,0]
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def buttons(self):
        self.mouse = pygame.mouse.get_pos()
        if 485+150 > self.mouse[0] > 485 and 200+30 > self.mouse[1] > 200:
            pygame.draw.rect(self.win,[200,200,200],(485,200,150,30))
        else:
            pygame.draw.rect(self.win, [255,255,255],(485,200,150,30))

        if 485+150 > self.mouse[0] > 485 and 250+30 > self.mouse[1] > 250:
            pygame.draw.rect(self.win, [200,200,200],(485,250,150,30))
        else:
            pygame.draw.rect(self.win, [255,255,255],(485,250,150,30))

        if 485+150 > self.mouse[0] > 485 and 300+30 > self.mouse[1] > 300:
            pygame.draw.rect(self.win, [200,200,200],(485,300,150,30))
        else:
            pygame.draw.rect(self.win, [255,255,255],(485,300,150,30))

        button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Single Player", button1)
        textRect.center = ( (485+(150/2)), (200+(30/2)) )
        self.win.blit(textSurf, textRect)

        button2 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("MultiPlayer", button2)
        textRect.center = ( (485+(150/2)), (250+(30/2)) )
        self.win.blit(textSurf, textRect)

        button3 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Instructions", button3)
        textRect.center = ( (485+(150/2)), (300+(30/2)) )
        self.win.blit(textSurf, textRect)

    def game_intro(self):
        intro = True
        

        while intro:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.buttons()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse = pygame.mouse.get_pos()
                if 485+150 > self.mouse[0] > 485 and 200+30 > self.mouse[1] > 200:
                    sg = SinglePlayer()
                    
            pygame.display.update()
            self.clock.tick(15)
class SinglePlayer():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode((655, 383))
        self.bg = pygame.image.load('mainscreen.jpg')
        self.win.blit(self.bg,(0,0))
        pygame.display.set_caption("Single Player")
        largeText = pygame.font.Font('Kardust TS Condensed Bold Italic.ttf',72)
        TextSurf, TextRect = self.text_objects("Single Player", largeText)
        TextRect.center = ((655/2),(70))
        self.win.blit(TextSurf, TextRect)
        self.game_intro()
        

    def text_objects(self,text, font):
        black = [0,0,0]
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
    def levels(self):
        self.mouse = pygame.mouse.get_pos()
        if 485+150 > self.mouse[0] > 485 and 200+30 > self.mouse[1] > 200:
            pygame.draw.rect(self.win,[200,200,200],(485,200,150,30))
        else:
            pygame.draw.rect(self.win, [255,255,255],(485,200,150,30))

        if 485+150 > self.mouse[0] > 485 and 250+30 > self.mouse[1] > 250:
            pygame.draw.rect(self.win, [200,200,200],(485,250,150,30))
        else:
            pygame.draw.rect(self.win, [255,255,255],(485,250,150,30))

        if 485+150 > self.mouse[0] > 485 and 300+30 > self.mouse[1] > 300:
            pygame.draw.rect(self.win, [200,200,200],(485,300,150,30))
        else:
            pygame.draw.rect(self.win, [255,255,255],(485,300,150,30))

        button1 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Level 1", button1)
        textRect.center = ( (485+(150/2)), (200+(30/2)) )
        self.win.blit(textSurf, textRect)

        button2 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Level 2", button2)
        textRect.center = ( (485+(150/2)), (250+(30/2)) )
        self.win.blit(textSurf, textRect)

        button3 = pygame.font.Font("Kardust TS Condensed Bold Italic.ttf",20)
        textSurf, textRect = self.text_objects("Level 3", button3)
        textRect.center = ( (485+(150/2)), (300+(30/2)) )
        self.win.blit(textSurf, textRect)

    def game_intro(self):
        intro = True
    

        while intro:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.levels()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse = pygame.mouse.get_pos()
                if 485+150 > self.mouse[0] > 485 and 200+30 > self.mouse[1] > 200:
                    win = pygame.display.set_mode((500, 500))
                    pygame.display.set_caption("First Game")
                    bg = pygame.image.load('Course2.png')
                    golfBall = ball(118,453,5,(255,255,255),win)
                    golfBall.game_intro(win)
            pygame.display.update()
            self.clock.tick(15)
        

sc = mainScreen()
sc.game_intro()



