from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
direction = 1


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.direction  = 1

        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )
    def delite_yorself(self):
        canv.delete(self.id)
    def move(self):
        global direction
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        if self.x < 800:
            self.direction = -self.direction
        if self.y < 600:  
            self.direction = -self.direction
        if self.x < 0 or self.y > 600:
            #print('del ball')
            canv.delete(self.id)
        self.x += self.vx * self.direction
        self.y -= self.vy * self.direction
        self.y += 5
    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        length = ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5
        return length <= self.r + obj.r


class gun():
    def __init__(self):
        self.id = canv.create_oval(0, 0, 0, 0, fill="black")
    f2_power = 10
    f2_on = 0
    an = 1

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        canv.delete(self.id)
        self.id =canv.create_line(event.x,event.y,event.x,event.y,width=7)
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
            

class target():
    points = 0
    live = 1
    vx = 5
    vy = 15
    # DONE: don't work!!! How to call this functions when object is created?
    # self.id = canv.create_oval(0,0,0,0)
    # self.id_points = canv.create_text(30,30,text = self.points,font = '28')
    # self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.direction = 1
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        self.id = canv.create_oval(x-r,y-r,x+r,y+r)
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def set_live(self,n):
        self.live = n
    def get_live(self):
        return self.live
    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        if hasattr(self, "id_points"):
            canv.delete(self.id_points)
        self.id_points = canv.create_text(30,30,text = '',font = '28')
        canv.itemconfig(self.id_points, text=self.points)

    def move(self):
        #print('move')
        #print(self.y)
        if self.y > 600:  
            self.direction = -self.direction
        if self.y < 0:
            self.direction = -self.direction
        self.y -= self.vy * self.direction
        #print(self.y)
        canv.delete(self.id)
        self.id = canv.create_oval(self.x - self.r,self.y - self.r,self.x + self.r,self.y + self.r, fill = "red")
        canv.coords(self.id, self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)
        canv.itemconfig(self.id, fill=self.color)
    def delite_yorself(self):
        canv.delete(self.id)
        
t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []

def mover(b):
    b.move()
    b.set_coords()
def target_move():
    if t1.get_live() == 1:
        t1.move()
    if t2.get_live() == 1:
        t2.move()
    root.after(50,target_move)
    
def new_game(event=''):
    global gun, t1, screen1, balls, bullet, root
    targets = []
    t1.new_target()
    t2.new_target()
    bullet = 0
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    t1.vy = 5
    t2.vy = 5
    z = 0.03
    t1.set_live(1)
    t2.set_live(1)
    target_move()
    while (t1.get_live() == 1 or t2.get_live() == 1) or len(balls) >0:
        for b in balls:
            mover(b)
            if (b.hittest(t1) and (t1.get_live() == 1)) or (b.hittest(t2) and (t2.get_live() == 1)):


                if (b.hittest(t1) and t2.get_live() == 0):
                    t1.set_live(0)
                    t1.hit()
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                    for i in balls:
                        i.delite_yorself()
                    balls = []
                elif (b.hittest(t2) and t1.get_live() == 0):
                    t2.set_live(0)
                    t2.hit()
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                    for i in balls:
                        i.delite_yorself()
                    balls = []
                        
                elif (b.hittest(t1) and t2.get_live() == 1):
                    t1.set_live(0)
                    t1.hit()
                      
                elif ( t1.get_live() == 1):
                    t2.set_live(0)
                    t2.hit()
                
                    
                    
                    
        #time.sleep(1)    
        canv.update()
        time.sleep(0.03)    
        #g1.targetting()
        g1.power_up()
    print("exit now")
    t1.delite_yorself()
    t2.delite_yorself()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750,new_game)

new_game()

root.mainloop()
