######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
######################## Route program ########################
def Route2():
    
    PortView_Battery()
    
    MoveSteering_Seconds(-80, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο

#### Μ05 "Ποιος έζησε εδώ" ####
    MoveStraight_Distance(400,700,750,True,True,Stop.BRAKE) # Ευθεία φεύγει από την βάση
    PointTurn_Angle(300, 300, -60, True, Stop.BRAKE) # Αριστερή στροφή για να κάνει το "Ποιος έζησε εδώ"
    PointTurn_Angle(300, 300, 60, True, Stop.BRAKE) # Στροφή δεξιά 
    
#### Μ06 "Σιδηρουργείο & Μυλόπετρα" ####
    MoveStraight_Distance(400,700,-300,True,True,Stop.BRAKE) # Όπισθεν - απομακρύνεται από το "Ποιος έζησε εδώ"
    PointTurn_Angle(300, 300, -30, True, Stop.BRAKE) # Αριστερή στροφή είναι μπροστά από την τέντα
    MoveStraight_Distance(400,700,150,True,True,Stop.BRAKE) # Ευθεία προς το "Ποιος έζησε εδώ"
    PointTurn_Angle(300, 300, 75, True, Stop.BRAKE) # Στροφή δεξιά είναι μπροστά από το Σιδηρουργείο
    MoveStraight_Distance(400,700,135,True,True,Stop.BRAKE) # Ευθεία προς το Σιδηρουργείο
    leftArm.run_time(1000,1000 , then=Stop.BRAKE, wait=True) # Κατεβάζει τον βραχίονα 
    MoveStraight_Distance(400,700,30,True,True,Stop.BRAKE) # Πηγαίνει ευθεία για να πιάσει την μυλόπετρα
    leftArm.run_time(-300,1200 , then=Stop.BRAKE, wait=True) # Ανεβάζει τον βραχίονα με την μυλόπετρα
    
#### Πορεία προς την βάση ####
    MoveStraight_Distance(400,700,-200,True,True,Stop.BRAKE) # Όπισθεν προς την βάση
    PointTurn_Angle(300, 300, -75, True, Stop.BRAKE) # Αριστερή στροφή προς την βάση
    MoveStraight_Distance(400,700,-600,True,True,Stop.BRAKE) # Γυρνά πίσω στην βάση
