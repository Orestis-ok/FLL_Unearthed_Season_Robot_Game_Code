######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *


####################### Route program ########################
def Route8(): 

    PortView_Battery()
    
    MoveSteering_Seconds(-50, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο
    leftArm.run_time(-200,500 , then=Stop.BRAKE, wait=False) # ανεβάζει αριστερό βραχίονα
    rightArm.run_time(-500,500 , then=Stop.BRAKE, wait=False) # Κατεβάζει δεξιό βραχίονα

#### Μ01 "Βούρτσισμα Επιφάνειας" και Μ02 "Αποκάλυψη Χάρτη" ####
    MoveStraight_Distance(450,500,730,True,True,Stop.BRAKE) # Ευθεία, αποχωρεί από την Βάση, περνάει δίπλα από "Βούρτσισμα Επιφάνειας"
    PointTurn_Angle(300, 300, -45, True, Stop.BRAKE) # Στροφή αριστερά 45 μοιρών, είναι ΜΠΡΟΣΤΑ από "Αποκάλυψη Χάρτη"

    MoveStraight_Distance(200,500,170,True,True,Stop.BRAKE)
    rightArm.run_time(800,800 , then=Stop.BRAKE, wait=False) # Ανεβαίνει ο δεξιός βραχίονας να σηκώσει το "Επιφανειακό χώμα" 
    leftArm.run_time(800,1000 , then=Stop.BRAKE, wait=False) # Κατεβαίνει ο αριστερός βραχίονας για να πιάσει το πινέλο
    wait(300) # Περιμένει λίγο για να σιγουρευτούμε πως έχει πιάσει το πινέλο
    leftArm.run_time(-300,1000 , then=Stop.BRAKE, wait=True)  # Ανεβαίνει ο αριστερός βραχίονας με το πινέλο 
    
#### Επιστροφή στη Βάση #####
    MoveStraight_Distance(300,500,-150,True,True,Stop.BRAKE) # όπισθεν
    PointTurn_Angle(300, 300, 42, True, Stop.BRAKE) # Στροφή δεξιά 45 μοιρών
    MoveSteering_Seconds(-900, 10, 1900)
    wait(300)
