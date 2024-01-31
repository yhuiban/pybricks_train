from pybricks.pupdevices import DCMotor
from pybricks.parameters import Port
from pybricks.tools import wait

motor = DCMotor(Port.A)
for i in range(1, 10):
    print('War raok ! - En avant !')
    motor.dc(50)
    wait(1000)
    
    print('Herzel ! - Arrêt !')
    motor.brake()
    wait(1000)
    
    print('War gil ! - En Arrière !')
    motor.dc(-50)
    wait(1000)

    print('Herzel ! - Arrêt !')
    motor.brake()
    wait(1000)
