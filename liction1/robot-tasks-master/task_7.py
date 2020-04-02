#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while(wall_is_beneath() != True):
        move_down()
    while(wall_is_beneath() == True):
        move_right()
    move_down()
    
    while(wall_is_above() != True):
        move_left()
    while(wall_is_above() == True):
        if wall_is_on_the_left() == True:
            break
        move_left()
    
    
    

    
if __name__ == '__main__':
    run_tasks()
