#!/usr/bin/python3

from pyrob.api import *


def fill_up_down():
    if not wall_is_above():
        move_up()
        fill_cell()
        move_down()
    if not wall_is_beneath():
        move_down()
        fill_cell()
        move_up()
 
 
@task
def task_8_11():
    if not wall_is_on_the_left():
            move_left()
            
    fill_up_down()
    while not wall_is_on_the_right():
        if  (wall_is_above() == True) and (wall_is_beneath() == True):
            fill_cell()
            
        move_right()
        fill_up_down()
    if  (wall_is_above() == True) and (wall_is_beneath() == True):
        fill_cell()

if __name__ == '__main__':
    run_tasks()
