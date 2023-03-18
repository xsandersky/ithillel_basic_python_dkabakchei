class Vehicle:
    point_of_use = 'vehicle for planet Earth'

    def __init__(self, body_material):
        self.material = body_material
        self.nubmer_of_seats = 150
        self.propulsor = 'engine'


    def get_full_name_object(self):
        return f'We are talking about a {self.point_of_use}'
    
    def make_noise(self):
        return 'Brrrrrr '
        
    

class Train(Vehicle):
    number_of_wheels = 200
    point_of_use = 'land vehicle'
    
    def make_noise(self):
        result = super().make_noise() + 'when in standby'
        return result


class Airplane(Vehicle):
    number_of_wheels = 3
    point_of_use = 'air vehicle'
    
    def __init__(self, body_material):
        super().__init__(body_material)
        self.propulsor = 'turbine'
    
    def set_speed(self, speed):
        self.speed = speed

train = Train('steel')
airplane = Airplane('Cast iron')
airplane.set_speed(850)
print(f'{train.get_full_name_object()} with {train.material} material, {train.nubmer_of_seats} number of seats and {train.number_of_wheels} wheels. The propulsor of this vehicle is {train.propulsor}. This vehicle makes the following sound: {train.make_noise()}\n')

print(f'{airplane.get_full_name_object()} with {airplane.material} material, {airplane.nubmer_of_seats} number of seats and {airplane.number_of_wheels} wheels. The propulsor of this vehicle is {airplane.propulsor}. This vehicle makes the following sound: {airplane.make_noise()} and speed is: {airplane.speed}')