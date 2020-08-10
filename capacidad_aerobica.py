import numpy as np
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
    cap_aer = float("{:.2f}".format(cap_aer))

    if edad <= 19:
        
        age_19 = { 
            'Muy pobre' : list(np.arange(0.00, 35.10, 0.01)),
            'Pobre' : list(np.arange(35.10, 38.40, 0.01)),
            'Promedio' : list(np.arange(38.40, 45.20, 0.01)), 
            'Bueno' : list(np.arange(45.20, 51.00, 0.01)),
            'Excelente' : list(np.arange(51.00, 56.00, 0.01)),
            'Superior' : list(np.arange(56.00, 60.00, 0.01))
        } 

        for categ, valor in age_19.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if vals == cap_aer:
                    print('Su capacidad aerobica es: {}, especificamente de: {}'.format(categ, vals))

    elif edad in list(range(20, 29)): 

        age_20_29 = {
            'Muy pobre' : list(np.arange(0.00, 33.10, 0.01)),
            'Pobre' : list(np.arange(33.10, 36.50, 0.01)),
            'Promedio' : list(np.arange(36.50, 42.30, 0.01)), 
            'Bueno' : list(np.arange(42.30, 46.50, 0.01)),
            'Excelente' : list(np.arange(46.50, 52.50, 0.01)),
            'Superior' : list(np.arange(52.50, 60.00, 0.01))
        } 

        for categ, valor in age_20_29.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if vals == cap_aer:
                    print('Su capacidad aerobica es: {}, especificamente de: {}'.format(categ, vals))
        
    elif edad in list(range(30, 39)):

        age_30_39 = {
            'Muy pobre' : list(np.arange(0.00, 31.60, 0.01)),
            'Pobre' : list(np.arange(31.60, 35.50, 0.01)),
            'Promedio' : list(np.arange(35.50, 41.00, 0.01)), 
            'Bueno' : list(np.arange(41.00, 45.00, 0.01)),
            'Excelente' : list(np.arange(45.00, 49.50, 0.01)),
            'Superior' : list(np.arange(49.50, 60.00, 0.01))
        } 

        for categ, valor in age_30_39.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if vals == cap_aer:
                    print('Su capacidad aerobica es: {}, especificamente de: {}'.format(categ, vals))
        
    elif edad in list(range(40, 49)):
        
        age_40_49 = {
            'Muy pobre' : list(np.arange(0.00, 30.30, 0.01)),
            'Pobre' : list(np.arange(30.30, 33.60, 0.01)),
            'Promedio' : list(np.arange(33.60, 39.00, 0.01)), 
            'Bueno' : list(np.arange(39.00, 43.80, 0.01)),
            'Excelente' : list(np.arange(43.80, 48.10, 0.01)),
            'Superior' : list(np.arange(48.10, 60.00, 0.01))
        } 

        for categ, valor in age_40_49.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if vals == cap_aer:
                    print('Su capacidad aerobica es: {}, especificamente de: {}'.format(categ, vals))
        
    elif edad in list(range(50, 59)):

        age_50_59 = {
            'Muy pobre' : list(np.arange(0.00, 26.20, 0.01)),
            'Pobre' : list(np.arange(26.20, 31.00, 0.01)),
            'Promedio' : list(np.arange(31.00, 35.80, 0.01)), 
            'Bueno' : list(np.arange(35.80, 41.00, 0.01)),
            'Excelente' : list(np.arange(41.00, 45.40, 0.01)),
            'Superior' : list(np.arange(45.40, 60.00, 0.01))
        } 

        for categ, valor in age_50_59.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if vals == cap_aer:
                    print('Su capacidad aerobica es: {}, especificamente de: {}'.format(categ, vals))

    else: 
        age_60 = {
            'Muy pobre' : list(np.arange(0.00, 20.60, 0.01)),
            'Pobre' : list(np.arange(20.60, 26.10, 0.01)),
            'Promedio' : list(np.arange(26.10, 32.30, 0.01)), 
            'Bueno' : list(np.arange(32.30, 36.50, 0.01)),
            'Excelente' : list(np.arange(36.50, 44.30, 0.01)),
            'Superior' : list(np.arange(44.30, 60.00, 0.01))
        } 

        for categ, valor in age_60.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if vals == cap_aer:
                    print('Su capacidad aerobica es: {}, especificamente de: {}'.format(categ, vals))
               
def clas_woman(cap_aer, edad):
    logger.info('Clasificatin for woman for age')
    cap_aer = float("{:.2f}".format(cap_aer))

    if edad <= 19:
        logger.info('Clasificatin for woman less than 19 years')
        
        age_19 = { 
            'Muy pobre' : list(np.arange(0.00, 25.10, 0.01)),
            'Pobre' : list(np.arange(25.10, 31.00, 0.01)),
            'Promedio' : list(np.arange(31.00, 35.00, 0.01)), 
            'Bueno' : list(np.arange(35.00, 39.00, 0.01)),
            'Excelente' : list(np.arange(39.00, 42.00, 0.01)),
            'Superior' : list(np.arange(42.00, 60.00, 0.01))
        } 

        for categ, valor in age_19.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if vals == cap_aer:
                    print('Su capacidad aerobica es: {}, especificamente de: {}'.format(categ, vals))

    elif edad in list(range(20, 29)): 

        age_20_29 = {
            'Muy pobre' : list(np.arange(0.00, 23.70, 0.01)),
            'Pobre' : list(np.arange(23.70, 29.00, 0.01)),
            'Promedio' : list(np.arange(29.00, 33.00, 0.01)), 
            'Bueno' : list(np.arange(33.00, 37.00, 0.01)),
            'Excelente' : list(np.arange(37.00, 41.00, 0.01)),
            'Superior' : list(np.arange(41.00, 60.00, 0.01))
        } 

        for categ, valor in age_20_29.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if vals == cap_aer:
                    print('Su capacidad aerobica es: {}, especificamente de: {}'.format(categ, vals))
        
    elif edad in list(range(30, 39)):

        age_30_39 = {
            'Muy pobre' : list(np.arange(0.00, 22.90, 0.01)),
            'Pobre' : list(np.arange(22.90, 27.00, 0.01)),
            'Promedio' : list(np.arange(27.00, 31.50, 0.01)), 
            'Bueno' : list(np.arange(31.50, 35.70, 0.01)),
            'Excelente' : list(np.arange(35.70, 40.20, 0.01)),
            'Superior' : list(np.arange(40.20, 60.00, 0.01))
        } 

        for categ, valor in age_30_39.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if vals == cap_aer:
                    print('Su capacidad aerobica es: {}, especificamente de: {}'.format(categ, vals))
        
    elif edad in list(range(40, 49)):
        
        age_40_49 = {
            'Muy pobre' : list(np.arange(0.00, 21.10, 0.01)),
            'Pobre' : list(np.arange(21.10, 24.50, 0.01)),
            'Promedio' : list(np.arange(24.50, 29.00, 0.01)), 
            'Bueno' : list(np.arange(29.00, 32.90, 0.01)),
            'Excelente' : list(np.arange(32.90, 37.00, 0.01)),
            'Superior' : list(np.arange(37.00, 60.00, 0.01))
        } 

        for categ, valor in age_40_49.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if vals == cap_aer:
                    print('Su capacidad aerobica es: {}, especificamente de: {}'.format(categ, vals))
        
    elif edad in list(range(50, 59)):
        logger.info('Clasificatin for woman between 50-59')


        age_50_59 = {
            'Muy pobre' : list(np.arange(0.00, 20.30, 0.01)),
            'Pobre' : list(np.arange(20.30, 22.80, 0.01)),
            'Promedio' : list(np.arange(22.80, 27.00, 0.01)), 
            'Bueno' : list(np.arange(27.00, 31.50, 0.01)),
            'Excelente' : list(np.arange(31.50, 35.80, 0.01)),
            'Superior' : list(np.arange(35.80, 60.00, 0.01))
        } 

        for categ, valor in age_50_59.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                print(categ, vals)
                if vals == cap_aer:
                    print('Su capacidad aerobica es: {}, especificamente de: {}'.format(categ, vals))

    else: 
        age_60 = {
            'Muy pobre' : list(np.arange(0.00, 17.60, 0.01)),
            'Pobre' : list(np.arange(17.60, 20.20, 0.01)),
            'Promedio' : list(np.arange(20.20, 24.50, 0.01)), 
            'Bueno' : list(np.arange(24.50, 30.30, 0.01)),
            'Excelente' : list(np.arange(30.30, 31.50, 0.01)),
            'Superior' : list(np.arange(31.50, 60.00, 0.01))
        } 

        for categ, valor in age_60.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if vals == cap_aer:
                    print('Su capacidad aerobica es: {}, especificamente de: {}'.format(categ, vals))
        
        
          

if __name__ == "__main__":
            
    kg = int(input('Ingrese su peso: '))
    edad = int(input('Ingrese su edad: '))
    sexo = int(input('Siendo masculino = 1 y mujer = 0: '))
    segs =  int(input('Ingrese el tiempo de recorrido en segundos: '))
    mins = segs / 60
    fre_car_ps = float(input('Ingrese la frecuencia cardiaca por 10 s: '))
    fre_car_pm = fre_car_ps * 6
    
    cap_aero_calc(kg, edad, sexo, mins, fre_car_pm)
    
    



