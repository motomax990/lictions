#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_6_6():
    move_right()
    while(wall_is_on_the_right() != True):
        if(wall_is_above() != True):
            move_up()
            while(wall_is_above() != True):
                fill_cell()
                move_up()
            fill_cell()
            while(wall_is_beneath() != True):
                move_down()
        move_right()
    if(wall_is_on_the_right() == True and wall_is_above() != True):
        move_up()
        while(wall_is_above() != True):
            fill_cell()
            move_up()
        fill_cell()    
        while(wall_is_beneath() != True):
            move_down()

        
        
    while(wall_is_on_the_left() != True):
        move_left()
    move_right()   


if __name__ == '__main__':
    run_tasks()
