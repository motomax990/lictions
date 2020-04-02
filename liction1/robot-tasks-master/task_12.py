#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
        while((wall_is_above() == True) or (wall_is_beneath() == True) or (wall_is_above() != True) or (wall_is_beneath() != True)):
            if cell_is_filled() == True:
                fill_cell()
            if (wall_is_above() == True or wall_is_beneath() == True):
                while((wall_is_above() == True) or (wall_is_beneath() == True)):

                        if(wall_is_beneath() == True) and (wall_is_above() != True):

                            fill_cell()
                        if wall_is_on_the_right() == True:
                            break
                        move_right()
                
            elif(wall_is_above() != True and wall_is_beneath() != True):
                while(wall_is_above() != True and wall_is_beneath() != True):

                        if wall_is_on_the_right() == True:
                            break    
                        
                        move_right()
            if wall_is_on_the_right() == True:
                break


if __name__ == '__main__':
    run_tasks()
