from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
# Jouw python instructies zet je vanaf hier:
for c in range(8): 
    robotArm.moveRight()
for z in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        for x in range(2): 
            robotArm.moveLeft()
        
    else:
        robotArm.drop()
        robotArm.moveLeft()
        


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()