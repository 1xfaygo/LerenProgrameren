from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 5
robotArm.moveRight()
for a in range(7):
    robotArm.grab()
    for a in range(8):
        robotArm.moveRight()
    for c in range(1):
        robotArm.drop()
    for l in range(8):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()