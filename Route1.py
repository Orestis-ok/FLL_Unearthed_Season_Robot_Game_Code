######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
######################## Route program ########################
def Route1():
    
    PortView_Battery()
    
    MoveSteering_Seconds(-80, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο

### Μ06 "Σιδηρουργείο" ####
    MoveStraight_Distance(400,700,500,True,True,Stop.BRAKE) # Ευθεία φέυγει από την βάση
    PointTurn_Angle(300, 300, -35, True, Stop.BRAKE) # Στρίβει αριστερά - είναι μπροστά από το "Τι είναι προς πώληση"
    MoveStraight_Distance(400,700,132,True,True,Stop.BRAKE) # Συνεχίζει ευθεία   
    PointTurn_Angle(300, 300, 80, True, Stop.BRAKE) # Στρίβει δεξιά και ευθυγραμμίζεται με το Σιδηρουργείο
    MoveStraight_Distance(400,700,170,True,True,Stop.BRAKE) # Συνεχίζει ευθεία προς το Σιδηρουργείο
    leftArm.run_time(500,1100 , then=Stop.BRAKE, wait=True) # Κατεβαίνει ο βραχίονας να πιάσει Μυλόπετρα και περιστρέφεται ο 2ος βραχίονας να πέσουν τα 3 Μπλοκ Ορυκτών
    wait(500) 
    leftArm.run_time(-900,1000 , then=Stop.BRAKE, wait=True) # Σηκώνεται ο βραχίονας με τη Μυλόπετρα
    
# # ## Πορεία προς Μ05 "Ποιος έζησε εδώ" ####
    MoveStraight_Distance(400,400,-210,True,True,Stop.BRAKE) # μικρή όπισθεν, φεύγει από Σιδηρουργείο
    PointTurn_Angle(300, 300, -23, True, Stop.BRAKE) # Στροφή αριστερή για να ισιώσει με το "Ποιος έζησε εδώ"
    MoveStraight_Distance(400,400,190,True,True,Stop.BRAKE) # ευθεία, είναι δίπλα στο "Ποιος έζησε εδώ"
    PointTurn_Angle(300, 300, -30, True, Stop.BRAKE) # Στροφή αριστερα ωστε να ισιώσει το δάπεδο της δομής του "Ποιος έζησε εδώ"
    MoveStraight_Distance(400,400,-50,True,True,Stop.BRAKE) # ευθεία, είναι δίπλα στο "Ποιος έζησε εδώ"
    
# #### Επιστροφή στη Βάση ####
    MoveSteering_Seconds(-900, -10, 1900) # Γυρνάει πίσω στη Βάση
