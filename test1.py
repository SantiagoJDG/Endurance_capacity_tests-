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
        
        first = 132.6 - (0.17 * self.kg)
        return first

    def second_part(self, edad, sexo):
        logger.info('Inicialization second part of the ecuation')

        second = - (0.39 * self.edad) + (6.31 * self.sexo)
        return second 
    
    def third_part(self, mins, fre_car_pm):
        logger.info('Inicialization third part of the ecuation')

        third = - (3.27 * self.mins) - (0.156 * self.fre_car_pm)
        return third

def cap_aero_calc(kg, edad, sexo, mins, fre_car_pm):
    logger.info('Inicialization ecuation')
    
   
    eq_ejec = Capacidad_aerobica(kg, edad, sexo, mins, fre_car_pm)
    a = eq_ejec.first_part(kg)
    b = eq_ejec.second_part(edad, sexo)
    c = eq_ejec.third_part(mins, fre_car_pm)

    cap_aer = (a + b + c)
    return clasification(cap_aer, sexo)

def clasification(cap_aer, sexo):
    logger.info('Clasification for gender')

    if sexo == 1:
        clas_men(cap_aer)
    else:
        clas_woman(cap_aero_calc, edad)

def clas_men(cap_aer):
    logger.info('Clasification for men for age')

    cap_aer = round(cap_aer)
    dict_19 = { 
        'Muy pobre' : list(range(0, 35)),
        'Pobre' : list(range(35, 38)),
        'Promedio' : list(range(38, 45)), 
        'Bueno' : list(range(45, 50)),
        'Excelente' : list(range(51, 55)),
        'Superior' : list(range(56, 100))
    } 
    
    for categ, valor in dict_19.items(): 
        for val in valor:
            if cap_aer == val:
                print('La capacidad aerobica es: {}, especificamente de: {}'.format(categ, val))

def clas_woman(cap_aero_calc, edad):
    pass
        
          

if __name__ == "__main__":
    
    kg = int(input('Ingrese su peso: '))
    edad = int(input('Ingrese su edad: '))
    sexo = int(input('Siendo masculino = 1 y mujer = 0: '))
    segs =  int(input('Ingrese el tiempo de recorrido en segundos: '))
    mins = segs / 60
    fre_car_ps = float(input('Ingrese la frecuencia cardiaca por 10 s: '))
    fre_car_pm = fre_car_ps * 6

    cap_aero_calc(kg, edad, sexo, mins, fre_car_pm)



