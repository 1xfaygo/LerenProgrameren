from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)
# Jouw python instructies zet je vanaf hier:
zit_er_iets = True
for x in range(7):
    zit_er_iets = robotArm.grab()
    for z in range(1 + x):
        robotArm.moveRight()
    robotArm.drop()
    for b in range(1 + x):
        robotArm.moveLeft()
    if not zit_er_iets:
        break

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()