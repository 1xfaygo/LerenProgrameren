from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
# Jouw python instructies zet je vanaf hier:     
for x in range(1,11 -1):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for z in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for c in range(x -1 ):
            robotArm.moveLeft()   
    else:
        robotArm.drop()
        robotArm.moveRight()
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()