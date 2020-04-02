#!/usr/bin/python3

from pyrob.api import *



def crossFiller(storona):
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
    if(storona == 'right'):
        move_right(1)
        move_right(3)
        move_up()
        move_right()
    if(storona == 'left'):
            move_left(2)
            move_up()
            move_left()   

@task(delay=0.001)
def task_2_4():
        move_right()
        for i in range(9):
            crossFiller('right')
            
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
        move_right(1)
        move_down(3)
        
        for i in range(9):
            crossFiller('left')
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
        move_right(1)
        move_down(3)
        
        
        for i in range(9):
            crossFiller('right')
            
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
        move_right(1)
        move_down(3)
        
        for i in range(9):
            crossFiller('left')
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
        move_right(1)
        move_down(3)
        
        for i in range(9):
            crossFiller('right')
        
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
        while(wall_is_on_the_left() != True):
            move_left()

        move_up()
'''
    if wall_is_on_the_right() != True:
        if(storona == 'right'):
            move_right(1)
            move_right(3)
            move_up()
            move_right()
        elif wall_is_on_the_right() == True:
            move_left(2)
            move_up()
    if wall_is_on_the_left() != True:
        if(storona == 'left'):
            move_left(1)
            move_left(3)
            move_up()
            move_left()
    elif wall_is_on_the_left() == True:
            move_left(2)
            move_up()
'''

if __name__ == '__main__':
    run_tasks()
