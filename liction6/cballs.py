import tkinter as tk
from random import randrange as rnd, choice
import math
from math import pi, sin, cos
import time


root = tk.Tk()
canv = tk.Canvas(root,bg='white')
counterOchkov = 0
label1 = tk.Label(text=counterOchkov, fg="#eee", bg="#333")
label1 = tk.Label(text=counterOchkov, fg="black")
CircleF = 2
RectF = 0.7
StarF = 0.3


'''
Свойства объекта:
form = Форма круг,  круг, звезда
color = Цвет случайный из списка
size = Размер диаметр(2R), a, диаметр(2R)
bonus = Бонус
f = Частота появления
v = скорость движения
a = угол поворота при столкновении 180-a
sprite = спрайт(сам объект)

Методы объекта:
target_constructor(form) метод создаёт объект заданной формой
target_destructor(targets,n)
target_clic_over(this,x,y)
tarrget_move_yourself(this)

sprite_draw(form,x,y,size,color0) возвращает ссылку на отрисованный объект
sprite_draw_circle(x,y,size,color0)
sprite_draw_rect(x,y,size,color0)
sprite_draw_star(x,y,size,color0)




'''
colors = ['red','orange','yellow','green','blue']
target = dict(form="circle",color="red",size=30,bonus=1,f=2,v=7,a=30,sprite='')
target_forms = ["circle","rect","star"]
targets = []



def main():
    global root, canv
    root.geometry('800x600')
    canv.pack(fill=tk.BOTH,expand=1)
    canv.bind('<Button-1>', click)
    #target_constructor("circle")
    ontimer_add_circle()
    ontimer_add_rect()
    ontimer_add_star()
    #draw_ball()
    #draw_rect()
    #draw_star()
    target_motion()
    #on_closing()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

def ontimer_add_circle():
    global root
    target_constructor("circle")
    time = int(1000/CircleF)
    root.after(time,ontimer_add_circle)
    
def ontimer_add_rect():
    global root
    target_constructor("rect")
    time = int(1000/RectF)
    root.after(time,ontimer_add_rect)
    
def ontimer_add_star():
    global root
    target_constructor("star")
    time = int(1000/StarF)
    root.after(time,ontimer_add_star)

def target_constructor(form):
    global root, canv, colors, target, targets
    this = target.copy()
    if form == "circle":
        x = rnd(100,700)
        y = rnd(100,500)
        r = rnd(30,50)
        create_obj_circle(this,r)
        this["sprite"] = sprite_draw('circle',r,this["color"],x,y)

    elif form == "rect":
        x = rnd(100,700)
        y = rnd(100,500)
        a = rnd(30,50)
        create_obj_rect(this, a)
        this["sprite"] = sprite_draw('rect',a,this["color"],x,y)

    elif form == "star":
        x = rnd(100,700)
        y = rnd(100,500)
        r = rnd(30,50)
        r1=6/7*r
        n = 15
        a=pi/180*(360/n/2)
        poligonList = []
        for c in range(0,n*2,2):
            x1=cos(a*c)*r+x
            x2=cos(a*(c+1))*r1+x
            y1=sin(a*c)*r+y
            y2=sin(a*(c+1))*r1+y
            poligonList.append((x1,y1))
            poligonList.append((x2,y2))
        create_obj_star(this,r)
        this["sprite"] = sprite_draw('star', r,this["color"],0,0,poligonList)
    targets.append(this)

def create_obj_circle(this,r):
    this["form"] = "circle"
    this["color"] = str(choice(colors))
    this["size"] = r*2
    this["bonus"] = 1
    this["f"] = 1
    this["v"] = rnd(1,20)
    this["a"] = rnd(3,87)

def create_obj_rect(this,a):
    this["form"] = "rect"
    this["color"] = str(choice(colors))
    this["size"] = a
    this["bonus"] = 3
    this["f"] = 0.5
    this["v"] = rnd(20,40)
    this["a"] = rnd(3,87)




    
def create_obj_star(this,r):
    this["form"] = "star"
    this["color"] = str(choice(colors))
    this["size"] = r*2
    this["bonus"] = 7
    this["f"] = 0.3
    this["v"] = rnd(40,60)
    this["a"] = rnd(3,87)

    
    
    


def target_destructor(targets, n):
    global root, canv
    canv.delete(targets[n]['sprite'])
    del targets[n]


def target_clic_over(this,clicX,clicY, objX, objY):
    if this["form"] == "rect":
        a = abs(clicX-(objX+(this['size'])))
        b = abs(clicY-(objY+(this['size'])))
        
    elif this["form"] == "star":
        a = abs(clicX-(objX-(cos(0)*  this['size']/2)))
        b = abs(clicY-(objY-(cos(0)*  this['size']/2)))
        ##print(a,b)
        
    else:
        a = abs(clicX-(objX+(this['size']/2)))
        b = abs(clicY-(objY+(this['size']/2)))
        
    r1 = math.sqrt((a**2)+(b**2))
    if r1 <= this['size']:
        return this['bonus']

    return 0

def tarrget_move_yourself(this):
    pos = canv.coords(this['sprite'])
    objX = pos[0]
    objY = pos[1]
    if this['form'] == "rect":
        if (int(objX) + (this['size'])) + this['v'] >= 800:
            this['a'] = 180 - this['a']
        elif int(objX) - this['v'] <= 0:
            this['a'] = 180 - this['a']
        if (int(objY)  + (this['size'])) + this['v'] >= 600:
            #print("pol1:" + str(this['a']))
            this['a'] = 180 + this['a']
            #print("pol2:" + str(this['a']))
        elif int(objY) - this['v'] <= 0:
            this['a'] = 180 + this['a']
        x = cos(pi/180*this['a']) * this['v']
        #print(objY)
        #print(pos[3])
        y = sin(pi/180*this['a']) * this['v']
        
        #print(len(pos))
    elif this['form'] == "star":
        centerX = objX-this['size']/2
        centerY = objY-this['size']/2
        if (objX + this['size']/2) + this['v'] >= 800:
            this['a'] = 180 - this['a']
        elif (centerX - this['size']/2) - this['v'] <= 0:
            this['a'] = 180 - this['a']
        if (objY + this['size']/2) + this['v'] >= 600:
            #print("pol1:" + str(this['a']))
            this['a'] = 180 + this['a']
            #print("pol2:" + str(this['a']))
        elif (centerY - this['size']/2) - this['v'] <= 0:
            this['a'] = 180 + this['a']
        x = cos(pi/180*this['a']) * this['v']
        #print(objY)
        #print(pos[3])
        y = sin(pi/180*this['a']) * this['v']
        
        #print(len(pos))
    else:
        y = sin(pi/180*this['a']) * this['v']
        if (int(objX) + this['size']) + this['v'] >= 800:
            this['a'] = 180 - this['a']
        elif int(objX) - this['v'] <= 0:
            this['a'] = 180 - this['a']
        if (int(objY)  + this['size']) + this['v'] >= 600:
            #print("pol1:" + str(this['a']))
            this['a'] = 180 + this['a']
            #print("pol2:" + str(this['a']))
        elif int(objY) - this['v'] <= 0:
            this['a'] = 180 + this['a']
        x = cos(pi/180*this['a']) * this['v']
        #print(objY)
        #print(pos[3])
        
        #print(len(pos))
        y = sin(pi/180*this['a']) * this['v']
    #print(x)
    canv.move(this['sprite'],x,y)
    #print('ball moving')




def sprite_draw(form,size,color,x=0,y=0,poligonList = []):
    if form == "circle":
        return sprite_draw_circle(x,y,size,color)
    elif form == "rect":
        return sprite_draw_rect(x,y,size,color)
    elif form == "star":
        return sprite_draw_star(poligonList,color)

def sprite_draw_circle(x,y,r,color):
    global canv
    return canv.create_oval(x-r,y-r,x+r,y+r,fill = color, width=0)

def sprite_draw_rect(x,y,a,color):
    global canv
    return canv.create_rectangle(x,y,x+a,y+a,fill = color, width=0)

def sprite_draw_star(poligonList,color):
    global canv
    return canv.create_polygon(poligonList,fill = color, width=0)












def draw_ball():
    global root, canv, colors, targets, target
    this = target.copy()
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    this["form"] = "circle"
    this["color"] = str(choice(colors))
    this["size"] = r*2
    this["bonus"] = 1
    this["f"] = 1
    this["v"] = rnd(3,20)
    this["a"] = rnd(3,87)
    this["sprite"] = canv.create_oval(x-r,y-r,x+r,y+r,fill = this["color"], width=0)
    time = int(1000/this["f"])
    root.after(time,draw_ball)
    targets.append(this)

    
    

def draw_rect(): 
    global root, canv, colors
    this = target.copy()
    x = rnd(100,700)
    y = rnd(100,500)
    a = rnd(30,50)*rnd(1,3)
    this["form"] = "rect"
    this["color"] = str(choice(colors))
    this["size"] = a
    this["bonus"] = 3
    this["f"] = 0.5
    this["v"] = rnd(3,20)
    this["a"] = rnd(3,87)
    this["sprite"] = canv.create_rectangle(x,y,x+a,y+a,fill = this["color"], width=0)
    #print("creatin rectangl")
    time = int(1000/this["f"])
    root.after(time,draw_rect)
    targets.append(this)


def draw_star():
    global root, canv, colors
    this = target.copy()
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    r1=6/7*r
    n = 15
    a=pi/180*(360/n/2)
    poligonList = []
    for c in range(0,n*2,2):
        x1=cos(a*c)*r+x
        x2=cos(a*(c+1))*r1+x
        y1=sin(a*c)*r+y
        y2=sin(a*(c+1))*r1+y
        poligonList.append((x1,y1))
        poligonList.append((x2,y2))
    this["form"] = "star"
    this["color"] = str(choice(colors))
    this["size"] = r*2
    this["bonus"] = 7
    this["f"] = 0.3
    this["v"] = rnd(3,20)
    this["a"] = rnd(3,87)
    this["sprite"] = canv.create_polygon(poligonList,fill = this["color"], width=0)
    time = int(1000/this["f"])
    root.after(time,draw_star)
    targets.append(this)

    '''
    brushColor('#f9c2c2')
    n = 22
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

    '''
    
    


    
def click(event):
    global counterOchkov , root, label1, canv
    for i in range(len(targets)):        
        pos = canv.coords(targets[i]['sprite'])

        bonus = target_clic_over(targets[i],event.x,event.y, pos[0], pos[1])
        if bonus > 0:
            counterOchkov += bonus
            target_destructor(targets,i)
            i = i-1
            label1['text'] = counterOchkov
            label1.pack()





def target_motion():
    global targets, canv, root
    for i in range(len(targets)):
        this = targets[i]

        tarrget_move_yourself(this)
    root.after(50,target_motion)


def on_closing():
    global root
    if counterOchkov == 0:
        root.destroy()
        exit()

    with open("records.txt", 'a') as file:
        file.write(str(counterOchkov)+'\n') 
        
        
    with open("records.txt") as file:
        lines = []
        for i in file:
            lines.append(int(i.replace('\n', '')))
        
        print(lines)

        for i in range(len(lines)-1):
            for j in range(len(lines)-i-1):
                if lines[j] < lines[j+1]:
                    lines[j], lines[j+1] = lines[j+1], lines[j]
        
        print(lines)
    with open("records.txt", 'w') as file:
        string = str(lines)
        string = string.replace('[','')
        string = string.replace(']','\n')
        string = string.replace(',','\n')
        string = string.replace(' ','')
        print(string)
        file.write(string)
    root.destroy()


main()

