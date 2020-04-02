#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    print(wall_is_above())
    if wall_is_above() != True:
        move_up(1)
    elif wall_is_on_the_right() != True:
        move_right(1)    
    elif wall_is_beneath() != True:
        move_down(1)
    elif wall_is_on_the_left() != True:
        move_left(1)    

if __name__ == '__main__':
    run_tasks()
