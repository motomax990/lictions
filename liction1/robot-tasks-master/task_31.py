#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    while(wall_is_on_the_right() != True):
        if()


if __name__ == '__main__':
    run_tasks()
