######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
######################## Route program ########################
def Route6():

    PortView_Battery()

#### Αποχώρηση από Βάση ####
    MoveSteering_Seconds(-50, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο


#### Mission 13 "Ανακατασκευή αγάλματος" ####

    MoveStraight_Distance(800,500,300,True,True,Stop.BRAKE) # Ευθεία, φεύγει από τη Βάση
    PointTurn_Angle(700, 700, -90, True, Stop.BRAKE) # Στροφή αριστερά 90 μοίρες
    
    MoveStraight_Distance(400,500,690,True,True,Stop.BRAKE) # Ευθεία, διασχίζει νότια πλευρά και πλησιάζει Άγαλμα
    PointTurn_Angle(700, 700, 54, True, Stop.BRAKE) # Στροφή δεξιά 55 μοίρες
    
    MoveStraight_Distance(200,200,165,True,True,Stop.BRAKE) # Ευθεία, ακουμπάει Άγαλμα
    rightArm.run_time(1000, 2500, then=Stop.BRAKE, wait=True)  # Περιστροφή βραχίονα
    MoveStraight_Distance(900,800,-80,True,True,Stop.BRAKE) # όπισθεν, απομακρύνεται από Άγαλμα

#### Πορεία προς Αριστερή Βάση #####

    PointTurn_Angle(700, 700, 108, True, Stop.BRAKE) # Στροφή αριστερά 90 μοίρες
    MoveStraight_Distance(1000,800,-800,True,True,Stop.BRAKE) # όπισθεν, απομακρύνεται από Άγαλμα



#### παλιό προσάρτημα ####


### Mission 13 "Ανακατασκευή αγάλματος" ####

    # wait(400) # μικρή αναμονή για να πατήσει κουμπί χώρις να μετακινηθεί το ρομπότ

    # MoveStraight_Distance(300,300,-330,True,True,Stop.BRAKE) # Φεύγει ανάποδα από τη Βάση
    # PointTurn_Angle(500, 500, 34, True, Stop.BRAKE) # Στροφή δεξιά 35 μοιρες
    # MoveStraight_Distance(300,300,-420,True,True,Stop.BRAKE) # Συνεχίζει ανάποδα, πλησιάζει το Άγαλμα

    # rightArm.run_time(1000, 1000, then=Stop.BRAKE, wait=True)  # Ρίχνει Βραχίονα για να χτυπήσει και να σηκώσει το Άγαλμα
    # MoveStraight_Distance(200,300,-120,True,True,Stop.BRAKE) # Συνεχίζει ανάποδα, πλησιάζει το Άγαλμα
    
    # PointTurn_Angle(700, 800, 18, True, Stop.BRAKE) # Στροφή δεξιά 12 μοιρες
    
    
    # rightArm.run_angle(800, -130, then=Stop.HOLD, wait=True)  # Ανεβάζει Βραχίονα
    # PointTurn_Angle(700, 800, 8, True, Stop.BRAKE) # Στροφή δεξιά 18 μοιρες
   
    # wait(200)
    # PointTurn_Angle(550, 200, -73, True, Stop.BRAKE) # Στροφή αριστερή 78 μοιρες

    # rightArm.run_time(-600, 800, then=Stop.BRAKE, wait=False)  # Ανεβάζει Βραχίονα
    # MoveStraight_Distance(400,700,-900,True,True,Stop.BRAKE) # Ευθεία μπροστά, απομακρύνεται από το Άγαλμα


###### Με κοχλία #####

## Mission 13 "Ανακατασκευή αγάλματος" ####

    # wait(400) # μικρή αναμονή για να πατήσει κουμπί χώρις να μετακινηθεί το ρομπότ
    # rightArm.run_time(1000, 5500, then=Stop.BRAKE, wait=False)  # Ρίχνει Βραχίονα για να χτυπήσει και να σηκώσει το Άγαλμα

    # MoveStraight_Distance(300,300,-340,True,True,Stop.BRAKE) # Φεύγει ανάποδα από τη Βάση
    # PointTurn_Angle(500, 500, 37, True, Stop.BRAKE) # Στροφή δεξιά 35 μοιρες
    # MoveStraight_Distance(300,300,-420,True,True,Stop.BRAKE) # Συνεχίζει ανάποδα, πλησιάζει το Άγαλμα

    # MoveStraight_Distance(200,300,-100,True,True,Stop.BRAKE) # Συνεχίζει ανάποδα, πλησιάζει το Άγαλμα
    
    # PointTurn_Angle(700, 800, 12, True, Stop.BRAKE) # Στροφή δεξιά 18 μοιρες
    # rightArm.run_time(-1000, 3000, then=Stop.BRAKE, wait=True)  # Ρίχνει Βραχίονα για να χτυπήσει και να σηκώσει το Άγαλμα



