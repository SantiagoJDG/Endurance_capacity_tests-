import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
  

class Capacidad_aerobica: 

    def __init__(self, kg, edad, sexo, mins, fre_car_pm):

        self.kg = kg
        self.edad = edad
        self.sexo = sexo
        self.mins = mins
        self.fre_car_pm = fre_car_pm

    def first_part(self, kg):
        logger.info('Inicialization first part of the ecuation')
        
        first = 132.6 - 0.17 * self.kg
        print(first)
        return first

    def second_part(self, edad, sexo):
        logger.info('Inicialization second part of the ecuation')

        second = 0.39 * self.edad + 6.31 * self.sexo
        print(second)
        return second 
    
    def third_part(self, mins, fre_car_pm):
        logger.info('Inicialization third part of the ecuation')

        third = 3.27 * self.mins - 0.156 * self.fre_car_pm
        print(third)
        return third

def main():

    cap_aer = Capacidad_aerobica(50, 23, 1, 3, 110)
    a = cap_aer.first_part(50)
    b = cap_aer.second_part(23, 1)
    c = cap_aer.third_part(3, 110)

    return print(a - b - c)    
  

if __name__ == "__main__":
    
    main()



