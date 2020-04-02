#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    c = 0
    if cell_is_filled() == True:
        c += 1
    while(c != 5):
        if cell_is_filled() == True:
            c += 1
        if(c < 5):
            move_right()

if __name__ == '__main__':
    run_tasks()
