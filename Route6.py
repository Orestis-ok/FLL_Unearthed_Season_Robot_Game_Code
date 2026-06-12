######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
######################## Route program ########################
def Route6():

    PortView_Battery()

#### Mission 13 "Ανακατασκευή αγάλματος" ####

    MoveSteering_Seconds(-50, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο

    MoveStraight_Distance(900,700,270,True,True,Stop.BRAKE) # Φεύγει από τη Βάση

    PointTurn_Angle(700, 700, -87, True, Stop.BRAKE) # Στροφή αριστερά 90 μοίρες
    MoveStraight_Distance(700,700,790,True,True,Stop.BRAKE) # Ευθεία από τη Βάση κατά μήκος του Νότιου τοίχου

    PointTurn_Angle(700, 700, 90, True, Stop.BRAKE) # Είναι αριστερά από τα Αντικείμενα Ψαράδων, στρίβει δεξιά 87 μοίρες
    MoveStraight_Distance(900,700,530,True,True,Stop.BRAKE) # Ευθεία ανάμεσα στο Άγαλμα και στη Ζυγαριά
    MoveSteering_Seconds(-100, 0, 550) # μικρή όπισθεν από τοίχο
    PointTurn_Angle(700, 700, 47, True, Stop.BRAKE) # Στροφή δεξιά 50 μοιρες, ευθυγραμμίζει με Άγαλμα
    MoveStraight_Distance(100,700,-170,True,True,Stop.BRAKE) # όπισθεν, είναι πίσω από το Άγαλμα
    MoveStraight_Distance(100,700,25,True,True,Stop.BRAKE) # λίγο μπροστά από το Άγαλμα

    rightArm.run_time(-1000, 1500, then=Stop.BRAKE, wait=True)  # Ρίχνει Βραχίονα για να χτυπήσει και να σηκώσει το Άγαλμα
    rightArm.run_time(500, 1300, then=Stop.BRAKE, wait=True) # Ο Βραχίονας σηκώνεται και επιστρέφει στη θέση του 

#### Πορεία προς Βάση ####

    MoveStraight_Distance(500,500,160,True,True,Stop.BRAKE) # Φεύγει από το Άγαλμα
    PointTurn_Angle(350, 200, -139, True, Stop.BRAKE) # Στροφή αριστερά 240 μοιρες, 
    MoveStraight_Distance(400,700,630,True,True,Stop.BRAKE) #Ευθεία σηκώνει τον Εξερευνητή
    PointTurn_Angle(350, 500, -68, True, Stop.BRAKE) # Στροφή αριστερά 60 μοιρες
    MoveSteering_Seconds(900, 0, 1800) # Ευθεία να μπει ΒΑΣΗ
