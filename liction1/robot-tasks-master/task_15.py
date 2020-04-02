#!/usr/bin/python3

from pyrob.api import *






@task
def task_8_21():
    if wall_is_on_the_left() and wall_is_above():
        move_right(9)
        move_down(9)
    elif wall_is_on_the_right() and wall_is_above():
        move_down(9)
        move_left(9)
    elif wall_is_on_the_right() and wall_is_beneath():
        move_left(9)
        move_up(9)
    elif wall_is_on_the_left() and wall_is_beneath():    
        move_right(9)
        move_up(9)
        


if __name__ == '__main__':
    run_tasks()
