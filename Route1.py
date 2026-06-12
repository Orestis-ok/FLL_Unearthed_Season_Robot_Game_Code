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

    while Button.RIGHT not in hub.buttons.pressed(): # Αναμονή να μετακινήσει ο τεχνικός το robot για να φύγει ξανά με πάτημα δεξιού κουμπιού
        wait(200)
    MoveSteering_Seconds(-80, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο

#### Μ06 "Σιδηρουργείο" ####

    MoveStraight_Distance(400,700,660,True,True,Stop.BRAKE) # ευθεία, είναι δίπλα στο "Ποιος έζησε εδώ"
    PointTurn_Angle(300, 300, 45, True, Stop.BRAKE) # Στροφή αριστερα ωστε να ισιώσει το δάπεδο της δομής του "Ποιος έζησε εδώ"
    MoveStraight_Distance(400,400,80,True,True,Stop.BRAKE) # ευθεία, είναι δίπλα στο "Ποιος έζησε εδώ"
    leftArm.run_time(400,700 , then=Stop.BRAKE, wait=True) # Κατεβαίνει ο βραχίονας να πιάσει Μυλόπετρα και περιστρέφεται ο 2ος βραχίονας να πέσουν τα 3 Μπλοκ Ορυκτών
    wait(500) 
    leftArm.run_time(-80,2100 , then=Stop.BRAKE, wait=True) # Σηκώνεται ο βραχίονας με τη Μυλόπετρα

## Πορεία προς Μ05 "Ποιος έζησε εδώ" ####

    MoveStraight_Distance(400,400,-210,True,True,Stop.BRAKE) # μικρή όπισθεν, φεύγει από Σιδηρουργείο
    PointTurn_Angle(300, 300, -27, True, Stop.BRAKE) # Στροφή αριστερή για να ισιώσει με το "Ποιος έζησε εδώ"
    MoveStraight_Distance(400,400,190,True,True,Stop.BRAKE) # ευθεία, είναι δίπλα στο "Ποιος έζησε εδώ"
    PointTurn_Angle(300, 300, -27, True, Stop.BRAKE) # Στροφή αριστερα ωστε να ισιώσει το δάπεδο της δομής του "Ποιος έζησε εδώ"
    PointTurn_Angle(300, 300, 20, True, Stop.BRAKE) # Στροφη δεξιά. Ξεκινάει η επιστροφή στη Βάση

#### Επιστροφή στη Βάση ####
    MoveSteering_Seconds(-900, -40, 1900) # Γυρνάει πίσω στη Βάση
