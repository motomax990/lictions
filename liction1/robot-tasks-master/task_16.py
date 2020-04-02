#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    while(wall_is_above() != True):
        move_up()
    if wall_is_on_the_left() and wall_is_above():
        while(wall_is_on_the_right() != True):
            move_right()
    elif wall_is_on_the_right() and wall_is_above():
        while(wall_is_on_the_left() != True):
            move_left()

if __name__ == '__main__':
    run_tasks()
