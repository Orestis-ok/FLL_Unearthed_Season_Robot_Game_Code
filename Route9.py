######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
####################### Route program ########################
def Route9(): 
    
    PortView_Battery()
    
    MoveSteering_Seconds(-50, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο

    MoveStraight_Distance(750,700,550,True,True,Stop.BRAKE) # Ευθεία φεύγει από την βάση
    PointTurn_Angle(400, 400, 28, True, Stop.BRAKE) # Κάνει στροφή 28 μοίρες δεξιά και ευθυγραμμίζεται με την βάση για το σημαιάκι
    MoveStraight_Distance(750,700,-350,True,True,Stop.BRAKE) # Απομακρύνεται από την βάση με το σημαιάκι κάνοντας όπισθεν
    
    PointTurn_Angle(400, 400, 28, True, Stop.BRAKE) # Κάνει στροφή 28 μοίρες δεξιά και ευθυγραμμίζεται με το forum
    MoveStraight_Distance(750,700,200,False,True,Stop.BRAKE) # Ευθεία κατευθύνεται προς το forum
    leftArm.run_time(-600, 1000, then=Stop.BRAKE, wait=False) # Ανεβάζει με αρνητική τιμή τον μηχανισμό στο προσάρτημα ώστε να απελευθερωθούν τα αντικείμενα 
    MoveStraight_Distance(750,700,230,False,True,Stop.BRAKE) # Κάνει επιπλέον ευθεία όπου σε αυτήν απελευθερώνονται τα αντικείμενα στο forum για μεγαλύτερη σιγουριά
    wait (500) # Κάνει μικρή παύση για να σιγουρευτούμε πως είχε μπει σωστά
    
    
    MoveStraight_Distance(750,700,-500,True,True,Stop.BRAKE) # Επιστρέφει πίσω στην βάση με όπισθεν
