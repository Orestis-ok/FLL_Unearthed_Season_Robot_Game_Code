######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
######################## Route program ########################
def Route3():

    PortView_Battery()

    rightArm.run_time(300, 300, then=Stop.BRAKE, wait=False) # Σηκώνεται ψηλά ο μοχλός
    MoveSteering_Seconds(-50, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο

    #### Αποχώρηση από τη Βάση ####
    MoveStraight_Distance(500,600,260,True,True,Stop.BRAKE) # Φεύγει από τη Βάση
    PointTurn_Angle(700, 700, -46, True, Stop.BRAKE) # Στροφή αριστερά 46 μοίρες
    MoveStraight_Distance(500,600,180,True,True,Stop.BRAKE) # Ευθεία, είναι μπροστά από το "Τι είναι προς Πώληση"

    ####  Μ09 "Τι είναι προς Πώληση" ####
    rightArm.run_angle(-1000, 260, then=Stop.BRAKE, wait=True) #κατεβαίνει μοχλός, κατεβαζει κόκκινο βραχίονα
    rightArm.run_angle(1000, 90, then=Stop.BRAKE, wait=True) # Επαναφορά μοχλού
    
    MoveStraight_Distance(300,600,50,True,True,Stop.BRAKE) # Λίγο Ευθεία, μπαίνει ο μοχλός εντός της Τέντας
    rightArm.run_time(-300, 800, then=Stop.BRAKE, wait=True) # Κατεβαίνει ο μοχλός και γαντζώνει την Τέντα
    leftArm.run_angle(-500, 200, then=Stop.BRAKE, wait=True) #κατεβαίνει μοχλός, κατεβαζει κόκκινο βραχίονα
    wait(200)
    leftArm.run_angle(500, 200, then=Stop.BRAKE, wait=True) #ανεβαίνει μοχλός επανερχεται στη θέση του

    MoveStraight_Distance(300,600,-70,True,True,Stop.BRAKE) # Όπισθεν να σηκώσει την Τέντα
    MoveStraight_Distance(300,600,30,True,True,Stop.BRAKE) # Λίγο μπροστά να ξεγαντζώσει ο μοχλό
    rightArm.run_angle(1000, 140, then=Stop.BRAKE, wait=True) # Σηκώνεται λίγο ο γάντζος, είναι στην ευθεία με την Τέντα
    MoveStraight_Distance(150,600,-130,True,True,Stop.BRAKE) # Όπισθεν, απομάκρυνση από Τέντα

    rightArm.run_angle(1000, 150, then=Stop.BRAKE, wait=False) # Σηκώνεται λίγο ο γάντζος, είναι στην ευθεία με την Τέντα

    MoveSteering_Seconds(-900, 50, 950) # Γυρνάει πίσω στη Βάση
