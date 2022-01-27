#Arsen Djurdjev 2022, January


#import pygame and make window that lasts until closing
import pygame
import random
import math
import time
from pygame.locals import *

pygame.init()

scr_width = 720
scr_height = 1280

#class that draws rectangleclass Square:

#create slider class

#Takes rectangle's size, position and a point. Returns true if that
#point is inside the rectangle and false if it isnt.
def pointInRectanlge(px, py, rw, rh, rx, ry):
    if px > rx and px < rx  + rw:
        if py > ry and py < ry + rh:
            return True
    return False

#Blueprint to make sliders in the game
class Slider:
    def __init__(self, position:tuple, upperValue:int=scr_height-(scr_height/10), sliderWidth:int = 30, text:str="Noise density: ",
                 outlineSize:tuple=(300, 100))->None:
        self.position = position
        self.outlineSize = outlineSize
        self.text = text
        self.sliderWidth = sliderWidth
        self.upperValue = upperValue
        
    #returns the current value of the slider
    def getValue(self)->float:
        return self.sliderWidth / (self.outlineSize[0] / self.upperValue)

    #renders slider and the text showing the value of the slider
    def render(self, display:pygame.display)->None:
        #draw outline and slider rectangles
        pygame.draw.rect(display, (0, 0, 0), (self.position[0], self.position[1], 
                                              self.outlineSize[0], self.outlineSize[1]), 3)
        
        pygame.draw.rect(display, (0, 0, 0), (self.position[0], self.position[1], 
                                              self.sliderWidth, self.outlineSize[1] - 10))

        #determite size of font
        self.font = pygame.font.Font(pygame.font.get_default_font(), int((15/100)*self.outlineSize[1]))

        #create text surface with value
        valueSurf = self.font.render(f"{self.text}: {round(self.getValue())}", True, (255, 0, 0))
        
        #centre text
        textx = self.position[0] + (self.outlineSize[0]/2) - (valueSurf.get_rect().width/2)
        texty = self.position[1] + (self.outlineSize[1]/2) - (valueSurf.get_rect().height/2)

        display.blit(valueSurf, (textx, texty))

    #allows users to change value of the slider by dragging it.
    def changeValue(self)->None:
        #If mouse is pressed and mouse is inside the slider
        mousePos = pygame.mouse.get_pos()
        if pointInRectanlge(mousePos[0], mousePos[1]
                            , self.outlineSize[0], self.outlineSize[1], self.position[0], self.position[1]):
            if pygame.mouse.get_pressed()[0]:
                #the size of the slider
                self.sliderWidth = mousePos[0] - self.position[0]

                #limit the size of the slider
                if self.sliderWidth < 1:
                    self.sliderWidth = 0
                if self.sliderWidth > self.outlineSize[0]:
                    self.sliderWidth = self.outlineSize[0]




class Stanje:
    PrviProlazak = True
    PrviProlazak2 = True



class Rect:
    def __init__(self, x, y, size,size2, color,width):
        self.x = x
        self.y = y
        self.size = size
        self.size2 = size2
        self.color = color
        self.width = width
        
        
    def update(self):
        if(Stanje.PrviProlazak):
           screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
        if not (Stanje.PrviProlazak):
         screen.blit(pygame.transform.rotate(screen, 180), (0, 0))  
         pygame.display.update()
        else:
         pygame.display.update()
         screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
         
    def show(self):
        #print(self.color, self.x, self.y, self. size, self.size2, self.width)
        pygame.draw.rect(
            screen,
            self.color,
            (self.x,
             self.y,
             self.size,
             self.size2),self.width)
        #Rect.update(self)
        






def check_exit():
        
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
            quit()
         if event.type == KEYDOWN:
             if event.key == K_ESCAPE:
                 quit()
         if event.type == KEYDOWN:
             if event.key == pygame.K_SPACE:
                
                 a=3



def max(a):
 m = 0 
 for i in range(len(a)):
        if(a[i]>m):
            m = a[i]
 return m

def visina(scr_height,height,broj,a):
    t = 0
    i = 1
    x = 1.5
    if(max(a)>scr_height):
     t=broj*(height/(1.1))
    
    else:
      t = broj*height
      #print(t, " je t")
    
    
    return t


def generate(vis):
    arr = []
    for i in range(vis):
        arr.append(random.randint(500,4000))
    return arr
    

def rect_update(arr):
 g = 0
 recty = []
 for i in range (len(arr)):
    recty.append(Rect(g,0,rectwidth,visina(scr_height,rectheight,arr[i],arr),(0,0,255),1))
    g+=rectwidth

 return recty


def wait_slider(slider):
    flag = True
    while flag:

        for event in pygame.event.get():
            screen.fill((255, 255, 255))
            slider.render(screen)
            slider.changeValue()
            pygame.display.update()
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                return int(slider.getValue())
            
            
def wait():
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_RETURN:
                flag = False           
            



def key_listener(flg):
    
    for event in pygame.event.get():
     if event.type == KEYDOWN:
             if event.key == pygame.K_SPACE:
                 #print("ovde sam")
                 flg = False
                 return False
     elif flg == True:
         return True
    
    return flg


def sortiraj(arr,fl):
    for i in range (len(arr)):
        fl=key_listener(fl)
        for j in range (0,len(arr)-i-1):
            fl=key_listener(fl)
            if(arr[j]>arr[j+1]):
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                fl=key_listener(fl)
                if(fl): 
                    fl=key_listener(fl)
                    rect = rect_update(arr)
                    Rect.update(rect)
                    check_exit()
                    #if(fl):
                        #print("fl je ovde")
                    screen.fill((255,255,255))
                    for i in range (len(arr)):
                     rect[i].show()
                     fl=key_listener(fl)





pygame.display.set_caption("Visualization of Bubble Sorting method")

screen = pygame.display.set_mode((scr_height, scr_width))
clock = pygame.time.Clock()

pygame.font.init()
GAME_FONT = pygame.font.Font(pygame.font.get_default_font(), 36)


arr = []

rect = []

pr_prolaz = True
sortiran = False
flag = True
fl = True
br = 0

slider = Slider((scr_height/2-150, scr_width/2-50))




#close pygame window if X is pressed# MAIN LOOP
while True:
    if(flag):
       screen.fill((255, 255, 255))
       #pygame.display.update()
       br_elem = wait_slider(slider)
       arr = generate(br_elem)
       rectwidth = ((scr_height-1)/len(arr))
       rectheight = (scr_width)/max(arr)
       rect = rect_update(arr)
       screen.fill((255, 255, 255))
       screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
       #pygame.transform.flip(screen,0,0) 
       pygame.display.update()
       text_surface = GAME_FONT.render('Noise density: ' + ' ' +str(len(arr)), True, (0, 50, 255))
       screen.blit(text_surface, dest=(scr_width/2,14))
       screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
       
    flag = False 
    check_exit()
    
    if not sortiran:
     for i in range (len(arr)):
      check_exit()
      rect[i].show()
      if(pr_prolaz):
       Rect.update(rect[i])
       br+=1
       if(len(arr)-br == 1):
             pr_prolaz = False
             Stanje.PrviProlazak = False
             
    if not sortiran:
       wait()
    
    if not (pr_prolaz):
        if not sortiran:
         sortiraj(arr,fl)
         rect = rect_update(arr)
        sortiran = True
        
        
        Rect.update(rect)
        screen.fill((255, 255, 255))
        for i in range (len(arr)):
             rect[i].show()

        


