#!/usr/bin/python3

from pyrob.api import *


def crossFiller():
    fill_cell()
    move_down()
    fill_cell()
    move_down()
    fill_cell()
    move_up()
    move_right()
    fill_cell()
    move_left(2)
    fill_cell()
    move_right(2)
    if wall_is_on_the_right() != True:
        move_right(3)
        move_up()
        move_right
    else:
        move_left(2)
        move_up()
        
        
        
        
@task
def task_2_2():
    move_right(1)
    move_down()
    for i in range(5):
        crossFiller()


if __name__ == '__main__':
    run_tasks()
