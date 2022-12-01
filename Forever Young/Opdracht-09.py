from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
# Jouw python instructies zet je vanaf hier:
for blok in range(10):
    robotArm.grab()
    for rechts in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for links in range(4):
        robotArm.moveLeft()
    if blok==1 or (blok>=3 and blok<5) or blok>=6:
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()