######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
####################### Route program ########################
def Route10(): 
    
    PortView_Battery()

    # leftArm.run_time(700, 900, then=Stop.BRAKE, wait=True) # Κατεβάζει τον καταπέλτη 
    # while Button.RIGHT not in hub.buttons.pressed(): 
        # wait(200) # Περιμένει να πατηθεί το δεξί κουμπί να φύγει το ρομπότ

    MoveSteering_Seconds(-80, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο

#### Απόχώρηση από τη Βάση #### 
    MoveStraight_Distance(400,700,760,True,True,Stop.BRAKE) # Ευθεία, φεύγει από τη Βάση
    PointTurn_Angle(60, 200, 90, True, Stop.BRAKE) # στροφή δεξιά 90 μοιρών
    MoveStraight_Distance(400,600,800,True,True,Stop.BRAKE) # ευθεία, διασχιζει όλη τη Βόρεια πλευρά
    
#### Σημαία ####
    PointTurn_Angle(40, 200, -57, True, Stop.BRAKE) # μικρή στροφή αριστερά, είναι έτοιμο να αφήσει τη Σημαία
    
    MoveStraight_Distance(500,600, 65,True,True,Stop.BRAKE) # στροφή δεξιά, αφήνει τη Σημαία

    MoveStraight_Distance(250,700, -70,True,True,Stop.BRAKE) # όπισθεν, αφήνει τη Σημαία
    
    PointTurn_Angle(250, 200, 60 , True, Stop.BRAKE) # στροφή δεξιά
    
# #### Forum ####
    MoveStraight_Distance(400,500,-480 ,True,True,Stop.BRAKE)# όπισθεν πορεία στο Forum (-465 παλιό)

    MoveSteering_Seconds(-300, 100, 700) # όπισθεν γωνία, ισιώνει με Forum
    MoveStraight_Distance(250,700, 100,True,True,Stop.BRAKE)
    leftArm.run_time(-900,1000 , then=Stop.BRAKE, wait=True) # Σηκώνει τον καταπέλτη
    MoveStraight_Distance(400,500, 100,True,True,Stop.BRAKE)
    MoveStraight_Distance(400,500, -80,True,True,Stop.BRAKE)
    PointTurn_Angle(300, 400, -56, True, Stop.BRAKE)
    MoveStraight_Distance(800,500,-85,True,True,Stop.BRAKE)
