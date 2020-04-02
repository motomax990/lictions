import tkinter as tk
from tkinter import messagebox

from random import randrange as rnd, choice
import math
import time




ball_list=[]
root = tk.Tk()
colors = ['red','orange','yellow','green','blue']
canv = tk.Canvas(root,bg='white')
counterOchkov = 0
label1 = tk.Label(text=counterOchkov, fg="black")
ball_direction = -1
def main():
    global root, colors, canv
    root.geometry('1000x700')
    canv.pack(fill=tk.BOTH,expand=1)
    new_ball()
    ball_motion()
    canv.bind('<Button-1>', click)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
 




def new_ball():
    global root, colors, canv, ball_list
    coord_list = []
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    coord_list.append(x)
    coord_list.append(y)
    coord_list.append(r)
    coord_list.append(canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0))
    ball_list.append(coord_list)
    root.after(500,new_ball)





    
def ball_motion():
    global ball_direction, canv, root
    for i in range(len(ball_list)-1):
        pos = canv.coords(ball_list[i][3])
        if (pos[0] + ball_list[i][2] *2) + 7 >= 1000:
            #print('change ball_direction')
            
            ball_direction = -1
        elif pos[0]  - 7 <= 0:
            ball_direction = 1
        if (pos[1]  + ball_list[i][2] *2) + 7 == 700:
            ball_direction = -1
        elif pos[1] - 7 == 0:
            ball_direction = 1
        rnd_num = 7
        canv.move(ball_list[i][3],rnd_num*ball_direction,0)
        canv.move(ball_list[i][3],0,rnd_num*ball_direction)
        #print('ball moving')
    root.after(50,ball_motion)

        
        
        
    
    




def click(event):
    global counterOchkov , root, label1, canv
    for i in range(len(ball_list)-1):        
        pos = canv.coords(ball_list[i][3])
        a = abs(event.x-(pos[0]+ball_list[i][2]))
        b = abs(event.y-(pos[1]+ball_list[i][2]))
        r1 = math.sqrt((a**2)+(b**2))
        if r1 <= ball_list[i][2]:
            counterOchkov += 1
            canv.delete(ball_list[i][3])
            del ball_list[i]
    label1['text'] = counterOchkov
    label1.pack()

def on_closing():
    global root
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        
 
main()
