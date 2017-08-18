'''Some classes learning'''

class Vehicle:
    '''Vehicle object docstring'''

    def __init__(self, color, doors, tires, vtype):
        '''Constructor docstring'''
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        '''Stop car'''
        return '%s braking' % self.vtype

    def drive(self):
        '''Drive car'''
        return '%s driving' % self.vtype

class Car(Vehicle):
    '''Car docstring'''

    def brake(self):
        '''Override Vehicle method'''
        return 'The car class is now braking'

if __name__ == '__main__':
    CAR = Car('blue', 5, 4, 'car')
    print(CAR.brake())
    print(CAR.drive())

    TRUCK = Vehicle('red', 3, 6, 'truck')
    print(TRUCK.drive())
    print(TRUCK.brake())
