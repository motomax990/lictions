#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_5_10():
    while(wall_is_on_the_right() != True):
        while(wall_is_beneath() != True):
            fill_cell()
            move_down()
        move_right()
        while(wall_is_above() != True):
            fill_cell()
            move_up()
        fill_cell()  
    while(wall_is_beneath() != True):
        move_down()
    while(wall_is_on_the_left() != True):
        move_left()
    fill_cell()
        
if __name__ == '__main__':
    run_tasks()
