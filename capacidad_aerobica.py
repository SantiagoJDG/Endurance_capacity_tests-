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
    return clasification(cap_aer, sexo, edad)

def clasification(cap_aer, sexo, edad):
    logger.info('Clasification for gender')

    if sexo == 1:
        clas_men(cap_aer, edad)
    else:
        clas_woman(cap_aer, edad)

def clas_men(cap_aer, edad):
    logger.info('Clasificatin for men for age')
    cap_aer = round(cap_aer)

    if edad <= 19:
        
        age_19 = { 
            'Muy pobre' : list(range(0, 35)),
            'Pobre' : list(range(35, 38)),
            'Promedio' : list(range(38, 45)), 
            'Bueno' : list(range(45, 50)),
            'Excelente' : list(range(51, 55)),
            'Superior' : list(range(56, 100))
        } 

        for categ, valor in age_19.items(): 
            for val in valor:
                if cap_aer == val:
                    print('La capacidad aerobica es: {}, especificamente de: {}'.format(categ, val))

    elif edad is list(range(20, 29)): 

        age_20_29 = {
            'Muy pobre' : list(range(0, 33)),
            'Pobre' : list(range(34, 36)),
            'Promedio' : list(range(37, 42)), 
            'Bueno' : list(range(43, 46)),
            'Excelente' : list(range(47, 52)),
            'Superior' : list(range(53, 100))
        } 

        for categ, valor in age_20_29.items(): 
            for val in valor:
                if cap_aer == val:
                    print('La capacidad aerobica es: {}, especificamente de: {}'.format(categ, val))
        
    elif edad is list(range(30, 39)):

        age_30_39 = {
            'Muy pobre' : list(range(0, 31)),
            'Pobre' : list(range(32, 35)),
            'Promedio' : list(range(36, 40)), 
            'Bueno' : list(range(41, 45)),
            'Excelente' : list(range(46, 50)),
            'Superior' : list(range(51, 100))
        } 

        for categ, valor in age_30_39.items(): 
            for val in valor:
                if cap_aer == val:
                    print('La capacidad aerobica es: {}, especificamente de: {}'.format(categ, val))
        
    elif edad is list(range(40, 49)):
        
        age_40_49 = {
            'Muy pobre' : list(range(0, 30)),
            'Pobre' : list(range(31, 34)),
            'Promedio' : list(range(34, 39)), 
            'Bueno' : list(range(40, 43)),
            'Excelente' : list(range(44, 47)),
            'Superior' : list(range(48, 100))
        } 

        for categ, valor in age_40_49.items(): 
            for val in valor:
                if cap_aer == val:
                    print('La capacidad aerobica es: {}, especificamente de: {}'.format(categ, val))
        
    elif edad is list(range(50, 59)):

        age_50_59 = {
            'Muy pobre' : list(range(0, 25)),
            'Pobre' : list(range(26, 31)),
            'Promedio' : list(range(32, 36)), 
            'Bueno' : list(range(36, 41)),
            'Excelente' : list(range(42, 45)),
            'Superior' : list(range(46, 100))
        } 

        for categ, valor in age_50_59.items(): 
            for val in valor:
                if cap_aer == val:
                    print('La capacidad aerobica es: {}, especificamente de: {}'.format(categ, val))

    else: 
        age_60 = {
            'Muy pobre' : list(range(0, 20)),
            'Pobre' : list(range(21, 25)),
            'Promedio' : list(range(26, 31)), 
            'Bueno' : list(range(32, 36)),
            'Excelente' : list(range(37, 44)),
            'Superior' : list(range(45, 100))
        } 

        for categ, valor in age_60.items(): 
            for val in valor:
                if cap_aer == val:
                    print('La capacidad aerobica es: {}, especificamente de: {}'.format(categ, val))
               
def clas_woman(cap_aer, edad):
    logger.info('Clasificatin for woman for age')
    cap_aer = round(cap_aer)

    if edad <= 19:
        
        age_19 = { 
            'Muy pobre' : list(range(0, 24)),
            'Pobre' : list(range(25, 31)),
            'Promedio' : list(range(32, 35)), 
            'Bueno' : list(range(35, 39)),
            'Excelente' : list(range(40, 56)),
            'Superior' : list(range(57, 100))
        } 

        for categ, valor in age_19.items(): 
            for val in valor:
                if cap_aer == val:
                    print('La capacidad aerobica es: {}, especificamente de: {}'.format(categ, val))

    elif edad is list(range(20, 29)): 

        age_20_29 = {
            'Muy pobre' : list(range(0, 23)),
            'Pobre' : list(range(24, 29)),
            'Promedio' : list(range(30, 33)), 
            'Bueno' : list(range(34, 37)),
            'Excelente' : list(range(38, 42)),
            'Superior' : list(range(43, 100))
        } 

        for categ, valor in age_20_29.items(): 
            for val in valor:
                if cap_aer == val:
                    print('La capacidad aerobica es: {}, especificamente de: {}'.format(categ, val))
        
    elif edad is list(range(30, 39)):

        age_30_39 = {
            'Muy pobre' : list(range(0, 22)),
            'Pobre' : list(range(23, 26)),
            'Promedio' : list(range(27, 31)), 
            'Bueno' : list(range(32, 34)),
            'Excelente' : list(range(35, 40)),
            'Superior' : list(range(41, 100))
        } 

        for categ, valor in age_30_39.items(): 
            for val in valor:
                if cap_aer == val:
                    print('La capacidad aerobica es: {}, especificamente de: {}'.format(categ, val))
        
    elif edad is list(range(40, 49)):
        
        age_40_49 = {
            'Muy pobre' : list(range(0, 20)),
            'Pobre' : list(range(21, 24)),
            'Promedio' : list(range(25, 29)), 
            'Bueno' : list(range(30, 33)),
            'Excelente' : list(range(34, 37)),
            'Superior' : list(range(38, 100))
        } 

        for categ, valor in age_40_49.items(): 
            for val in valor:
                if cap_aer == val:
                    print('La capacidad aerobica es: {}, especificamente de: {}'.format(categ, val))
        
    elif edad is list(range(50, 59)):

        age_50_59 = {
            'Muy pobre' : list(range(0, 20)),
            'Pobre' : list(range(21, 22)),
            'Promedio' : list(range(23, 26)), 
            'Bueno' : list(range(27, 30)),
            'Excelente' : list(range(31, 36)),
            'Superior' : list(range(37, 100))
        } 

        for categ, valor in age_50_59.items(): 
            for val in valor:
                if cap_aer == val:
                    print('La capacidad aerobica es: {}, especificamente de: {}'.format(categ, val))

    else: 
        age_60 = {
            'Muy pobre' : list(range(0, 17)),
            'Pobre' : list(range(18, 20)),
            'Promedio' : list(range(21, 24)), 
            'Bueno' : list(range(25, 30)),
            'Excelente' : list(range(31, 32)),
            'Superior' : list(range(33, 100))
        } 

        for categ, valor in age_60.items(): 
            for val in valor:
                if cap_aer == val:
                    print('La capacidad aerobica es: {}, especificamente de: {}'.format(categ, val))
        
        
          

if __name__ == "__main__":
            
    kg = int(input('Ingrese su peso: '))
    edad = int(input('Ingrese su edad: '))
    sexo = int(input('Siendo masculino = 1 y mujer = 0: '))
    segs =  int(input('Ingrese el tiempo de recorrido en segundos: '))
    mins = segs / 60
    fre_car_ps = float(input('Ingrese la frecuencia cardiaca por 10 s: '))
    fre_car_pm = fre_car_ps * 6
    
    cap_aero_calc(kg, edad, sexo, mins, fre_car_pm)
    
    



