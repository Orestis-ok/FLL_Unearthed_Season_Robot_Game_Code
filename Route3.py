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
    MoveStraight_Distance(700,750,350,True,True,Stop.BRAKE) # Ευθεία είναι δίπλα στο Σιλό (Μ08)
    PointTurn_Angle(700, 700, -31, True, Stop.BRAKE) # Στροφή αριστερά 31 μοίρες
    MoveStraight_Distance(700,750,320,True,True,Stop.BRAKE) # Ευθεία είναι δίπλα από το Ποιος Έζησε Εδώ (Μ05)
    PointTurn_Angle(700, 700, -140, True, Stop.BRAKE) # Στροφή αριστερά 140 μοίρες, είναι μπροστά από το Τι Είναι Προς Πώληση (Μ09)

#### Μ09 "Τι είναι προς πώληση" ####
    MoveStraight_Distance(700,750,80,True,True,Stop.BRAKE) # Ευθεία, πλησιάζει το Τι Είναι Προς Πώληση (Μ09)
    MoveStraight_Distance(800,250,180,True,True,Stop.BRAKE) # Ευθεία σπρώχνει με το έμβολο και σηκώνει τη Σκεπή 
    MoveSteering_Seconds(300, 0, 300) # Ευθεία με steering seconds κάνει έξτρα ευθεία για μεγαλύτερη σιγουριά ότι έχει ανασηκωθεί η τέντα 
    MoveStraight_Distance(600,250,-100,True,True,Stop.BRAKE) # μικρή όπισθεν να βγει το έμβολο από τον Πάγκο της Αγοράς
    
#### Μ10 "Αναποδογυρίστε τη ζυγαριά" ####    
    rightArm.run_time(1000, 3500, then=Stop.BRAKE, wait=True) # περιστρέφεται ο μηχανισμός για να αναποδογυρίσει τη Ζυγαριά
    MoveStraight_Distance(600,250,-100,True,True,Stop.BRAKE) # μικρή όπισθεν, φεύγει από Ζυγαριά

#### Πορεία προς Μ09 "Εμπορεύματα"####
    PointTurn_Angle(700, 700, -40, True, Stop.BRAKE) # Στροφή αριστερά 40 μοίρες
    rightArm.run_time(1000, 3800, then=Stop.BRAKE, wait=False) # περιστρέφεται ο μηχανισμός για να κατεβάσει το έμβολο για τον Δίσκο Ζύγισης 
    MoveStraight_Distance(800,700,400,True,True,Stop.BRAKE) # Ευθεία, είναι δίπλα από το Ποιος Έζησε Εδώ (Μ05)
    PointTurn_Angle(700, 700, 50, True, Stop.BRAKE) # Στροφή δεξιά 50 μοίρες
    MoveStraight_Distance(800,700,340,True,True,Stop.BRAKE) # Ευθεία είναι μπροστά από Σιλό (Μ08)
    PointTurn_Angle(700, 700, 83, True, Stop.BRAKE) # Στροφή δεξιά 83 μοίρες

#### Μ09 "Εμπορεύματα"####
    
    MoveStraight_Distance(600,700,460,True,True,Stop.BRAKE) # Ευθεία, κατεβάζει τον μοχλό στα Εμπορεύματα
    MoveSteering_Seconds(-900, 110, 1400) # Όπισθεν, γυρίζει στη Βάση


    
