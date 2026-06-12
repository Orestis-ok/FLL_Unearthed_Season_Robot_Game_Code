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
    MoveStraight_Distance(400,600, 20,True,True,Stop.BRAKE) # Λίγο μπροστά για να απελεθερωθεί από τον Μοχλό

    MoveSteering_Seconds(700, 4, 700) # Φεύγει από τη Βάση με ταχύτητα, σταματάει λίγο πριν το Πλοίο
    MoveSteering_Seconds(300, 6, 800) # Σπρώχνει το Πλοίο με μικρή ταχύτητα ώστε να Ανυψωθεί
    MoveStraight_Distance(250,600,-70,True,True,Stop.BRAKE) # Μικρή όπισθεν για να τραβήξει τον Μοχλό και να καθαρίσει την Άμμο
    wait(200) # μικρή αναμονή
    MoveStraight_Distance(300,600, 30,True,True,Stop.BRAKE) # Λίγο μπροστά για να απελεθερωθεί από τον Μοχλό
    
    MoveSteering_Seconds(-350, 5, 1500) # Επιστροφή στη Βάση
