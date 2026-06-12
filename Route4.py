######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from MyLibrary import *

  
######################## Route program ########################
def Route4():

   PortView_Battery()

### Αποχώρηση από Βάση ####
   MoveSteering_Seconds(-50, 0, 300) # Μικρή όπισθεν, κολλάει τοίχο

#### Μ10 "Αναποδογυρίστε τη ζυγαριά"  Δίσκος Ζύγισης #### 

   MoveStraight_Distance(800,700,80,True,True,Stop.BRAKE) # Ευθεία, φεύγει από τη Βάση
   PointTurn_Angle(700, 700, -49, True, Stop.BRAKE) # Στροφή αριστερα 48 μοίρες
   MoveStraight_Distance(700,700,370,True,True,Stop.BRAKE) # Το έμβολο είναι διπλα στον Δίσκο Ζύγισης
   MoveStraight_Distance(300,700,60,True,True,Stop.BRAKE) # Το έμβολο είναι κάτω από τον Δίσκο Ζύγισης

#### Επιστροφή στη Βάση ####
   MoveSteering_Seconds(-900, -70, 500) # Όπισθεν, γυρίζει στη Βάση
   MoveSteering_Seconds(-900, 110, 1400) # Όπισθεν, γυρίζει στη Βάση

   
