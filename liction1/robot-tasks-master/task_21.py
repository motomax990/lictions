#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    c = 13
    v = 13

    move_right()
    move_down()
    for k in range(13):
        if(wall_is_beneath() == True):
            for i in range(c):    
                move_up()
                fill_cell()
            move_right()
            move_down()
            
        else:    
            for i in range(c):    
                fill_cell()
                move_down()
            move_right()
        v = v - 1
        c = v
    move_left(13)
if __name__ == '__main__':
    run_tasks()
