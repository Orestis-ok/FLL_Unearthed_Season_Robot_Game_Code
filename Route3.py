######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
######################## Route program ########################
def Route3():

    PortView_Battery()

### Αποχώρηση από Βάση ####
    MoveSteering_Seconds(-50, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο
    
    MoveStraight_Distance(500,600,700,True,True,Stop.BRAKE) # Φεύγει από τη Βάση
    PointTurn_Angle(700, 700, -58, True, Stop.BRAKE) # Στροφή αριστερά 58 μοίρες
    MoveStraight_Distance(500,750,340,True,True,Stop.BRAKE) # Ευθεία είναι δίπλα στο Σιλό (Μ08)
    PointTurn_Angle(700, 700, -31, True, Stop.BRAKE) # Στροφή αριστερά 31 μοίρες
    MoveStraight_Distance(500,750,320,True,True,Stop.BRAKE) # Ευθεία είναι δίπλα από το Ποιος Έζησε Εδώ (Μ05)
    PointTurn_Angle(800, 700, -138, True, Stop.BRAKE) # Στροφή αριστερά 140 μοίρες, είναι μπροστά από το Τι Είναι Προς Πώληση (Μ09)

#### Μ09 "Τι είναι προς πώληση" ####
    MoveStraight_Distance(500,750,150,True,True,Stop.BRAKE) # Ευθεία, πλησιάζει το Τι Είναι Προς Πώληση (Μ09)
    MoveStraight_Distance(400,250,140,True,True,Stop.COAST) # Ευθεία σπρώχνει με το έμβολο και σηκώνει τη Σκεπή 
    MoveSteering_Seconds(300, 0, 600) # Ευθεία με steering seconds κάνει έξτρα ευθεία για μεγαλύτερη σιγουριά ότι έχει ανασηκωθεί η τέντα 
    wait(150)
    MoveStraight_Distance(600,250,-100,True,True,Stop.BRAKE) # μικρή όπισθεν να βγει το έμβολο από τον Πάγκο της Αγοράς
    
## Μ10 "Αναποδογυρίστε τη ζυγαριά" ####    
    rightArm.run_time(1000, 4500, then=Stop.BRAKE, wait=True) # περιστρέφεται ο μηχανισμός για να αναποδογυρίσει τη Ζυγαριά
    
    rightArm.run_time(1000, 7000, then=Stop.BRAKE, wait=False) # περιστρέφεται ο μηχανισμός για να κατεβάσει το έμβολο για τον Δίσκο Ζύγισης 

    MoveStraight_Distance(600,250,-100,True,True,Stop.BRAKE) # μικρή όπισθεν, φεύγει από Ζυγαριά

#### Πορεία προς Μ09 "Εμπορεύματα"####
    PointTurn_Angle(700, 700, -40, True, Stop.BRAKE) # Στροφή αριστερά 40 μοίρες
    # rightArm.run_time(1000, 6900, then=Stop.BRAKE, wait=False) # περιστρέφεται ο μηχανισμός για να κατεβάσει το έμβολο για τον Δίσκο Ζύγισης 
    MoveStraight_Distance(800,700,420,True,True,Stop.BRAKE) # Ευθεία, είναι δίπλα από το Ποιος Έζησε Εδώ (Μ05)
    PointTurn_Angle(700, 700, 50, True, Stop.BRAKE) # Στροφή δεξιά 50 μοίρες
    MoveStraight_Distance(800,700,310,True,True,Stop.BRAKE) # Ευθεία είναι μπροστά από Σιλό (Μ08)
    PointTurn_Angle(700, 700, 82, True, Stop.BRAKE) # Στροφή δεξιά 83 μοίρες

#### Μ09 "Εμπορεύματα"####
    
    MoveStraight_Distance(600,700,460,True,True,Stop.BRAKE) # Ευθεία, κατεβάζει τον μοχλό στα Εμπορεύματα
    MoveSteering_Seconds(-900, 110, 1600) # Όπισθεν, γυρίζει στη Βάση


    
