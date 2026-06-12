######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
####################### Route program ########################
def Route8(): 
    
    PortView_Battery()
    
    #### Αποχώρηση από τη Βάση με όπισθεν
    MoveStraight_Distance(800,700,-700,True,True,Stop.BRAKE)
    PointTurn_Angle(300, 300, 20, True, Stop.BRAKE)
    MoveStraight_Distance(800,900,-190,True,True,Stop.BRAKE)

    ##### Προσεκτική αποκατάσταση M04 ####
    leftArm.run_time(300,300, then=Stop.BRAKE, wait=False) # Κατεβαίνει ο βραχίονας να πιάσει Μυλόπετρα και περιστρέφεται ο 2ος βραχίονας να πέσουν τα 3 Μπλοκ Ορυκτών
    MoveSteering_Seconds(-50, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο
    
    MoveStraight_Distance(800,500,60,True,True,Stop.BRAKE) # Ευθεία
    PointTurn_Angle(300, 300, -90, True, Stop.BRAKE) # Στροφή δεξιά
    MoveSteering_Seconds(100, -10, 1200)

    leftArm.run_time(-800,1000, then=Stop.BRAKE, wait=True) # Στρίβει ο βραχίονας να πιάσει Μυλόπετρα και περιστρέφεται ο 2ος βραχίονας να πέσουν τα 3 Μπλοκ Ορυκτών
    wait (1000)
    
    MoveStraight_Distance(100,500,-120,True,True,Stop.BRAKE) # όπισθεν

    
