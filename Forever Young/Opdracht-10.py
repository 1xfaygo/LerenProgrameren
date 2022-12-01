from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier
links = 9
for x in range(5):
    robotArm.grab()
    for z in range(links):
        robotArm.moveRight()
    robotArm.drop()
    links-=1
    for q in range(links):
        robotArm.moveLeft()
    links-=1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()