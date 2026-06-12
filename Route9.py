######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
####################### Route program ########################
def Route9(): 
    
    PortView_Battery()

    #### Αποχώρηση από Βάση ####
    MoveSteering_Seconds(-50, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο

    MoveStraight_Distance(500,700,820,True,True,Stop.BRAKE) # Ευθεία μέχρι τον Βόρειο τοίχο
    PointTurn_Angle(500, 300, 187, True, Stop.BRAKE) # Στροφή 187 μοιρών, ετοιμάζεται να βρει τοίχο
    MoveStraight_Distance(800,700,-290,True,True,Stop.BRAKE) # Πηγαίνει με όπισθεν μέχρι τον Βόρειο τοίχο
    MoveSteering_Seconds(-50, 0, 300) # Όπισθεν κολλάει τοίχο
      
    ##### Προσεκτική αποκατάσταση M04 #####

    MoveStraight_Distance(800,500,70,True,True,Stop.BRAKE) # Ευθεία φεύγει από τοίχο
    PointTurn_Angle(300, 300, -93, True, Stop.BRAKE) # Στροφή αριστερά ώστε να ευθυγραμμιστεί με το Αντικείμενο
    wait(200)
    MoveSteering_Seconds(100, -10, 1200) # ευθεία φτάνει δίπλα στο Αντικείμενο

    leftArm.run_time(-800,1200, then=Stop.BRAKE, wait=False) # Στρίβει ο βραχίονας να πιάσει το Αντικείμενο
    rightArm.run_time(60, 2200, then=Stop.BRAKE, wait=True) # Ανεβάζει τον δεξί μοχλό για να σηκώσει τη ράμπα
    wait(300)
    MoveStraight_Distance(100,500,-120,True,True,Stop.BRAKE) # όπισθεν, βγαίνει με το Αντικείμενο

    #### Επιστροφή στη Βάση ####
    PointTurn_Angle(300, 300, 100, True, Stop.BRAKE) # στροφή δεξιά, η Βάση είναι μπροστά
    rightArm.run_time(-200, 1000, then=Stop.BRAKE, wait=False)
    MoveSteering_Seconds(1000, 0, 2000) # Όπισθεν κολλάει τοίχο
