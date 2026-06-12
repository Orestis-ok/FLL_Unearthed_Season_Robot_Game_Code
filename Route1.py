######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

######################## Route parallel program ########################
def Route1():

    PortView_Battery()

#### Αποχώρηση από Βάση ####
    MoveSteering_Seconds(-50, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο


# #### Μ08 "Σιλό" ####

    MoveStraight_Distance(800,500,490,True,True,Stop.BRAKE) # Ευθεία, φεύγει από τη Βάση, είναι δίπλα στο Σιλό
    rightArm.run_time(-300, 620, then=Stop.BRAKE, wait=True)
    wait(300)
    rightArm.run_time(300, 620, then=Stop.BRAKE, wait=True)
    wait(300)
    rightArm.run_time(-300, 620, then=Stop.BRAKE, wait=True) # Συνεχόμενα χτυπήματα στον μοχλό, ΚΑΤΕΒΑΣΜΑ
    wait(150)
    rightArm.run_time(300, 620, then=Stop.BRAKE, wait=True) # Συνεχόμενα χτυπήματα στον μοχλό, ΑΝΕΒΑΣΜΑ
    wait(150)
    rightArm.run_time(-300, 620, then=Stop.BRAKE, wait=True)
    wait(150)
    rightArm.run_time(300, 620, then=Stop.BRAKE, wait=True)
    wait(150)
    rightArm.run_time(-300, 620, then=Stop.BRAKE, wait=True)
    wait(150)
    rightArm.run_time(300, 620, then=Stop.BRAKE, wait=True)
    MoveStraight_Distance(800,500,-430,True,True,Stop.BRAKE) # Όπισθεν, Επιστρέφει στη Βάση
