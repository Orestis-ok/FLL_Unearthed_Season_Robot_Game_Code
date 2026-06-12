######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *


####################### Route program ########################
def Route8(): 

    PortView_Battery()
    

    MoveSteering_Seconds(-50, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο
    rightArm.run_time(-500,500 , then=Stop.BRAKE, wait=False) # Κατεβάζει δεξιό βραχίονα
    MoveStraight_Distance(450,500,730,True,True,Stop.BRAKE) # Ευθεία, αποχωρεί από την Βάση, περνάει δίπλα από "Βούρτσισμα Επιφάνειας"
    PointTurn_Angle(300, 300, -45, True, Stop.BRAKE) # Στροφή αριστερά 45 μοιρών, είναι ΜΠΡΟΣΤΑ από "Αποκάλυψη Χάρτη"

    MoveStraight_Distance(200,500,130,True,True,Stop.BRAKE) # Ευθεία μπροστά για να σπρώξει την "Αποκάλυψη Χάρτη"
    MoveStraight_Distance(40,500,20,True,True,Stop.BRAKE) # Λίγο μπροστά για να σιγουρέψει ότι έχει σπρώξει τελείως

    rightArm.run_time(800,800 , then=Stop.BRAKE, wait=True) # Ανεβαίνει ο δεξιός βραχίονας να σηκώσει το "Επιφανειακό χώμα" 
    MoveStraight_Distance(300,500,-150,True,True,Stop.BRAKE) # όπισθεν, φεύγει από "Βούρτσισμα Επιφάνειας"
    PointTurn_Angle(300, 300, 45, True, Stop.BRAKE) # Στροφή δεξιά 45 μοιρών
    MoveStraight_Distance(300,500,-130,True,True,Stop.BRAKE) # Όπισθεν, είναι δίπλα στο "Βούρτσισμα Επιφάνειας" για να πάρει τη Βούρτσα
    MoveStraight_Distance(300,500,90,True,True,Stop.BRAKE) # Λίγο μπροστά για να ευθυγραμμιστεί με τη Βούρτσα


    leftArm.run_time(-1000,1800 , then=Stop.BRAKE, wait=True) # Περιστροφή του μοχλού του αριστερού βραχίονα για να πιάσει τη Βούρτσα
    MoveSteering_Seconds(-900, 7, 1700) # Όπισθεν με μικρή κλίση δεξιά για να γυρίσει στη Βάση
