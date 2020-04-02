from graph import *
from math import *

listOblacov = []

direction=[int(1)]

def main():
    draw_main_bacground()
    draw_sun(70,70,65,2,2)
    #draw_oblaco(70,70,40)
    listOblacov.append(draw_oblaco(350,70,30))
    listOblacov.append(draw_oblaco(600,70,40))
    listOblacov.append(draw_oblaco(850,70,30))
    draw_tree(100,400,20,200,37)
    draw_home(200,400,250,200,70,70)
    draw_tree(500,500,10,100,16)
    draw_home(550,500,130,100,35,35)
    draw_tree(750,550,5,50,8)
    draw_tree(900,550,5,50,8)
    draw_home(780,550,75,50,17.5,17.5)

    onTimer(dvigatel_oblacov,100)
    onKey(keyPressed)   
    run()
    return 0

def keyPressed(event):
    if event.keycode == VK_ESCAPE:
        close()

        
def draw_main_bacground():
    canvasSize(1000,700)
    width, height = canvasSize()
    windowSize(width,height)

    brushColor('#9de9f4')
    rectangle(0,0,width, height / 2.5)

    brushColor('#0e9325')
    rectangle(0, height / 2.5, width, height)

def draw_oblaco(x0, y0, r0):
    listOblac = []
    y = y0
    for i in range(2,6,2):
        if i == 2:
            x = x0 + r0
        else:
            x = x0
        for k in range(1,i+1):
            brushColor('white')
            listOblac.append(circle(x,y,r0))
            if i == 2:
                x = x0 + (r0 * 2)
            else:    
                x = x0 + (r0 * k)
        y = y0 + r0
    return listOblac

def draw_home(x0, y0, homeW, homeH, winW, winH):
    brushColor('#964b00')
    rectangle(x0,y0,x0 +homeW, y0 +homeH)
    x1 = x0 + ((homeW/2) - (winW/2))
    y1 = y0 + ((homeH/2) - (winH/2))
    brushColor('blue')
    rectangle(x1,y1,x1 + winW, y1 + winH)
    brushColor('#f80000')
    polygon([(x0,y0),(x0+homeW,y0),(x0+homeW/2,y0-homeH/2)])
    
def draw_tree(x0,y0, stvolW, stvolH, r0):
    popr0=r0 *0.2
    popr1=r0 *1.4
    popr2=r0 *1.7
    popr3=r0 *2.1
    popr4=r0 *0.5
    popr5=r0 *3.3
    popr6=r0 *1.8
    brushColor('#964b00')
    rectangle(x0,y0,x0 + stvolW, y0 + stvolH)
    for k in range(2):
        brushColor('#0f530e')
        circle((x0+popr1*k) - popr4,(y0-popr0),r0)
    circle(x0+popr0,(y0-popr5),r0)
    for k in range(2):
        brushColor('#0f530e')
        circle((x0 - popr4)+popr6*k,(y0 - popr3),r0)
    circle(x0+popr0,(y0 - (r0)),r0)


def draw_sun(x0,y0,r0,polygonW,polygonH):
    brushColor('#f9c2c2')
    r1=10/11*r0
    n = 5
    a=pi/180*(360/n/2)
    poligonList = []
    for c in range(0,n*2,2):
        x1=cos(a*c)*r0+x0
        x2=cos(a*(c+1))*r1+x0
        y1=sin(a*c)*r0+y0
        y2=sin(a*(c+1))*r1+y0
        poligonList.append((x1,y1))
        poligonList.append((x2,y2))
    polygon(poligonList)

def direction_get():
    return direction[0]

def direction_reverse():
    direction[0] = -1*direction_get()
    return
    
def dvigatel_oblacov():
    width, height = canvasSize()
    for c in listOblacov:
        if xCoord(c[5])+2*30 >= width: 
            direction_reverse()
            
        if xCoord(c[2]) <= 0:
            direction_reverse()
            
        for i in c:     
            moveObjectBy(i,5*direction_get(),0)    
        
main()

