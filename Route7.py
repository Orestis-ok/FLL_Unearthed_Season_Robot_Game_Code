######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
####################### Route program ########################
def Route7(): 

    PortView_Battery()

#### Mission 13 "Ανακατασκευή αγάλματος" ####

    MoveStraight_Distance(400,600, 20,True,True,Stop.COAST) # Λίγο μπροστά

    MoveSteering_Seconds(700, 4, 700) # Φεύγει από τη Βάση με ταχύτητα, σταματάει λίγο πριν το Πλοίο
    MoveSteering_Seconds(300, 6, 900) # Σπρώχνει το Πλοίο με μικρή ταχύτητα ώστε να Ανυψωθεί
    leftArm.run_time(-1000, 2000, then=Stop.BRAKE, wait=True) # περιστρέφεται ο μηχανισμός για να αναποδογυρίσει τη Ζυγαριά
    MoveStraight_Distance(400,600,-100,True,True,Stop.BRAKE) # Μικρή όπισθεν για να τραβήξει τον Μοχλό και να καθαρίσει την Άμμο

    MoveSteering_Seconds(-950, -5, 1200) # Επιστροφή στη Βάση 
    wait(200)         
    
