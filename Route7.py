######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
####################### Route program ########################
def Route7(): 

               
    PortView_Battery()
    
    MoveSteering_Seconds(-50, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο
     
#### Μ01 "Βούρτσισμα Επιφάνειας" και Μ02 "Αποκάλυψη Χάρτη" ####
    MoveStraight_Distance(600,700,720,True,True,Stop.BRAKE) # Ευθεία, αποχωρεί από την Βάση, περνάει δίπλα από "Βούρτσισμα Επιφάνειας"
    PointTurn_Angle(300, 300, -45, True, Stop.BRAKE) # Στροφή αριστερά 45 μοιρών, είναι ΜΠΡΟΣΤΑ από "Αποκάλυψη Χάρτη"

    MoveStraight_Distance(300,500,170,True,True,Stop.BRAKE)
    rightArm.run_time(300,600 , then=Stop.BRAKE, wait=True) # Ανεβαίνει ο βραχίονας να σηκώσει το "Επιφανειακό χώμα" 

#### Επιστροφή στη Βάση #####
    MoveStraight_Distance(300,500,-150,True,True,Stop.BRAKE) # όπισθεν
    PointTurn_Angle(300, 300, 45, True, Stop.BRAKE) # Στροφή δεξιά 45 μοιρών
    MoveStraight_Distance(600,700,-60,True,True,Stop.BRAKE) # Επιστροφή προς την βάση και ανασήκωση του πινέλου
    leftArm.run_time(700,900 , then=Stop.BRAKE, wait=True) # Ανεβαίνει ο βραχίονας για να σηκώσει το πινέλο
    wait(500) # Περιμένει λίγο για να σιγουρευτούμε πως έχει πιάσει το πινέλο
    leftArm.run_time(-400,800 , then=Stop.BRAKE, wait=True) # Γυρίζει ο βραχίονας προς την άλλη πλευρά με το πινέλο 
    MoveStraight_Distance(600,700,-720,True,True,Stop.BRAKE) # Επιστροφή Βάση
