from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:
i = 3

# Na jouw code wachten tot het sluiten van de window:

for i in range(10):
    robotArm.grab()
    robotArm.moveRight();
robotArm.drop()
for i in range(5):
    robotArm.moveLeft();
robotArm.grab()
for i in range(5):
    robotArm.moveRight();
robotArm.moveRight();
robotArm.drop()
for i in range(2):
    robotArm.moveLeft();
robotArm.grab()
for i in range(2):
    robotArm.moveRight();
robotArm.drop()
