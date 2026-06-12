######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
####################### Route program ########################
def Route9(): 
    
    PortView_Battery()

    ##### Αποχώρηση από τη Βάση με όπισθεν #####
    MoveStraight_Distance(800,700,-670,True,True,Stop.BRAKE) # Πηγαίνει με όπισθεν μέχρι τον Βόρειο τοίχο
    PointTurn_Angle(300, 300, 12, True, Stop.BRAKE) # μικρή στροφή, ετοιμάζεται να βρει τοίχο
    MoveSteering_Seconds(-600, 0, 1100) # Όπισθεν κολλάει τοίχο
    leftArm.run_time(300,300, then=Stop.BRAKE, wait=True) # μικρή περιστροφή του άξονα ώστε να πάρει τη σωστή θέση

    ##### Προσεκτική αποκατάσταση M04 #####

    MoveStraight_Distance(800,500,60,True,True,Stop.BRAKE) # Ευθεία φεύγει από τοίχο
    PointTurn_Angle(300, 300, -90, True, Stop.BRAKE) # Στροφή αριστερά ώστε να ευθυγραμμιστεί με το Αντικείμενο
    MoveSteering_Seconds(100, -10, 1200) # ευθεία φτάνει δίπλα στο Αντικείμενο

    leftArm.run_time(-800,1000, then=Stop.BRAKE, wait=True) # Στρίβει ο βραχίονας να πιάσει το Αντικείμενο
    wait (1000)

    MoveStraight_Distance(100,500,-120,True,True,Stop.BRAKE) # όπισθεν, βγαίνει με το Αντικείμενο

    #### Επιστροφή στη Βάση ####
    PointTurn_Angle(300, 300, 105, True, Stop.BRAKE) # στροφή δεξιά, η Βάση είναι μπροστά
    MoveSteering_Seconds(900, 0, 2000) # Όπισθεν κολλάει τοίχο
