######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
####################### Route program ########################
def Route10(): 
    
    PortView_Battery()

    leftArm.run_time(1000, 1000, then=Stop.BRAKE, wait=True) # Κατεβάζει τον καταπέλτη 
    while Button.LEFT not in hub.buttons.pressed():
        wait(300)  # Περιμένει να πατηθεί το αριστερό κουμπί # Περιμένει να πατηθεί το δεξί κουμπί να φύγει το ρομπότ

    MoveSteering_Seconds(-80, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο

# ### Απόχώρηση από τη Βάση #### 
    rightArm.run_time(-750, 700, then=Stop.BRAKE, wait=False) # Κατεβαίνει ο βραχίονας για το ΤΡΕΝΟ

    MoveStraight_Distance(400,700,745,True,True,Stop.BRAKE) # Ευθεία, φεύγει από τη Βάση
    PointTurn_Angle(60, 200, 90, True, Stop.BRAKE) # στροφή δεξιά 90 μοιρών
    MoveStraight_Distance(400,400,790,True,True,Stop.BRAKE) # ευθεία, διασχιζει όλη τη Βόρεια πλευρά
#### Σημαία + Τρενάκι ####
    
    PointTurn_Angle(40, 200, -52, True, Stop.BRAKE) # μικρή στροφή αριστερά, είναι έτοιμο να αφήσει τη Σημαία (-57 παλιό)
    MoveStraight_Distance(250,200, 55,True,True,Stop.BRAKE) # ευθεία αφήνει τη Σημαία (55 παλιό)
    rightArm.run_time(700, 650, then=Stop.BRAKE, wait=True) # Ανεβαίνει ο βραχίονας με το ΤΡΕΝΟ
    wait(300) # αναμονή να σταθεροποιηθεί το τρένο
    MoveStraight_Distance(250,800, -55,True,True,Stop.BRAKE) # όπισθεν, αφήνει τη Σημαία
    PointTurn_Angle(250, 200, 54 , True, Stop.BRAKE) # στροφή δεξιά
    
# # # #### Forum ####
    MoveStraight_Distance(400,500,-480 ,True,True,Stop.BRAKE)# όπισθεν πορεία στο Forum

    MoveSteering_Seconds(-300, 100, 650) # όπισθεν γωνία, ισιώνει με Forum
    wait (200)
    rightArm.run_time(-130, 1400, then=Stop.BRAKE, wait=True) # Κατεβάζει τον βραχίονα με το τρενάκι
    MoveStraight_Distance(250,700, 100,True,True,Stop.BRAKE)# Ευθεία με κατεύθυνση το forum
    rightArm.run_time(300, 700, then=Stop.BRAKE, wait=False) # Ανεβάζει τον βραχίονα χωρίς το τρενάκι
    leftArm.run_time(-1000,1000 , then=Stop.BRAKE, wait=True) # Σηκώνει τον καταπέλτη
    MoveStraight_Distance(400,500, 75,True,True,Stop.BRAKE) # Ευθεία μπαίνει στο forum (65 παλιό)


# # # # #### Τελευταία σημαία ####
    MoveStraight_Distance(1000,800, -60,True,True,Stop.BRAKE)
    PointTurn_Angle(600, 400, -55, True, Stop.BRAKE) # 
    MoveStraight_Distance(1000,800,-90,True,True,Stop.BRAKE) # Όπισθεν αφήνει την τελυταία σημαία
