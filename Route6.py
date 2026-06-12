######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
######################## Route program ########################
def Route6():

    PortView_Battery()

#### Mission 13 "Ανακατασκευή αγάλματος" ####

    wait(300)
    MoveSteering_Seconds(-50, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο

    MoveStraight_Distance(300,700,-340,True,True,Stop.BRAKE) # Φεύγει ανάποδα από τη Βάση
    PointTurn_Angle(350, 500, 34, True, Stop.BRAKE) # Στροφή δεξιά 38 μοιρες
    MoveStraight_Distance(300,700,-470,True,True,Stop.BRAKE) # Συνεχίζει ανάποδα, πλησιάζει το Άγαλμα

    rightArm.run_time(-1000, 1300, then=Stop.BRAKE, wait=True)  # Ρίχνει Βραχίονα για να χτυπήσει και να σηκώσει το Άγαλμα
    MoveStraight_Distance(200,700,-80,True,True,Stop.BRAKE) # Συνεχίζει ανάποδα, πλησιάζει το Άγαλμα

    rightArm.run_time(250, 600, then=Stop.BRAKE, wait=True)  # Ανεβάζει Βραχίονα
    MoveStraight_Distance(400,700,120,True,True,Stop.BRAKE) # Ευθεία μπροστά, απομακρύνεται από το Άγαλμα
    PointTurn_Angle(550, 200, -57, True, Stop.BRAKE) # Στροφή δεξιά 57 μοιρες
    MoveStraight_Distance(700,300,-1040,True,True,Stop.BRAKE) # Όπισθεν φουλ για ΒΑΣΗ
