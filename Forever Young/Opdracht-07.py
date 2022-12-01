from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier
robotArm.speed = 4 
for z in range(5):    
    for x in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for c in range(2):
        robotArm.moveRight()
    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()