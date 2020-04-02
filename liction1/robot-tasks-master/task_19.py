#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    while(wall_is_on_the_left() != True):
        move_left()
    if wall_is_above() != True:
        while(wall_is_above() != True):
            move_up()
        
        
        
        
    else:
        while(wall_is_on_the_right() != True):
            move_right()
        if wall_is_above() != True:
            while(wall_is_above() != True):
                move_up()
            while(wall_is_on_the_left() != True):
                move_left()
        
if __name__ == '__main__':
    run_tasks()
