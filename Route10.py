######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
####################### Route program ########################
def Route10(): 
    
    PortView_Battery()

    leftArm.run_time(700, 900, then=Stop.BRAKE, wait=True) # Κατεβάζει τον καταπέλτη 
    while Button.RIGHT not in hub.buttons.pressed(): 
        wait(200) # Περιμένει να πατηθεί το δεξί κουμπί να φύγει το ρομπότ

    MoveSteering_Seconds(-80, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο

#### Απόχώρηση από τη Βάση #### 
    MoveStraight_Distance(400,700,760,True,True,Stop.BRAKE) # Ευθεία, φεύγει από τη Βάση
    PointTurn_Angle(300, 200, 91, True, Stop.BRAKE) # στροφή δεξιά 90 μοιρών
    MoveStraight_Distance(400,200,800,True,True,Stop.BRAKE) # ευθεία, διασχιζει όλη τη Βόρεια πλευρά
    
#### Σημαία ####
    PointTurn_Angle(65, 200, -57, True, Stop.BRAKE) # μικρή στροφή αριστερά, είναι έτοιμο να αφήσει τη Σημαία
    MoveStraight_Distance(400,700, -50,True,True,Stop.BRAKE) # όπισθεν, αφήνει τη Σημαία
    PointTurn_Angle(250, 200, 65 , True, Stop.BRAKE) # στροφή δεξιά
    
#### Forum ####
    MoveStraight_Distance(400,500,-465 ,True,True,Stop.BRAKE)# όπισθεν πορεία στο Forum

    MoveSteering_Seconds(-300, 100, 700) # όπισθεν γωνία, ισιώνει με Forum
    MoveStraight_Distance(400,500,120  ,True,True,Stop.BRAKE) # Ευθεία, είναι δίπλα στο Forum

    leftArm.run_time(-900,1000 , then=Stop.BRAKE, wait=True) # Σηκώνει τον καταπέλτη
    MoveStraight_Distance(400,500,100  ,True,True,Stop.BRAKE) # ευθεία μέσα μπαίνει στο Forum
    MoveSteering_Seconds(-500, -90, 750)
