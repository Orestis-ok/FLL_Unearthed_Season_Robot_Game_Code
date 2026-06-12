######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
######################## Route program ########################
def Route5():

    PortView_Battery()

#### Mission 11 "Αντικείμενα Ψαράδων" ####
    MoveSteering_Seconds(400, -10, 900)
    leftArm.run_time(500, 1700, then=Stop.BRAKE, wait=False) # Φεύγει από τη Βάση περιστρέφοντας τον τροχό
    MoveSteering_Seconds(100, -5, 2000)
   
    leftArm.run_time(900, 1600, then=Stop.BRAKE, wait=False) # Περιστροφή του τροχού για να σηκωθούν τα Αντικείμενα
    MoveSteering_Seconds(30, 0, 1600)

    leftArm.run_time(-500, 1800, then=Stop.BRAKE, wait=False) # Φεύγει από Αντικείμενα Ψαράδων περιστρέφοντας τον τροχό
    MoveStraight_Distance(100,300,-200,True,True,Stop.BRAKE) # Αποχώρηση με μικρή ταχύτητα για να μη βρει ο τροχός πάνω στα Αντικείμενα
    MoveStraight_Distance(900,900,-290,True,True,Stop.BRAKE) # Επιστροφή στη Βάση 
