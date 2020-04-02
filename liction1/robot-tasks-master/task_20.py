#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
        for y in range(6):
            for x in range(27):
                move_right()
                fill_cell()
            move_down()
            for d in range(27):
                fill_cell()
                move_left()
            move_down()
        move_right()    



if __name__ == '__main__':
    run_tasks()
