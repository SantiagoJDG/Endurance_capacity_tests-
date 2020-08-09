import numpy as np
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Cooper_test: 

    def __init__(self, sexo, miles, edad):
        self.sexo = sexo
        self.miles = miles
        self.edad = edad

    def ct_clas_gender(self):
        logger.info('Cooper Test clasification for gender')
        
        if self.sexo == 1:
            ct_men_age_clas(miles, edad)
        else:
            ct_woman_age_clas(miles, edad)

def ct_men_age_clas(miles, edad):
    logger.info('Cooper Test clasificatin for men age')
    miles = float('{:.2f}'.format(miles))


    if edad <= 19: 

        age_19 = {
            'Muy Pobre' : list(np.arange(0.00, 1.31, 0.01)),
            'Pobre' : list(np.arange(1.31, 1.38, 0.01)),
            'Promedio' : list(np.arange(1.38, 1.57, 0.01)),
            'Bueno' : list(np.arange(1.57, 1.73, 0.01)),
            'Excelente' : list(np.arange(1.73, 1.87, 0.01)),
            'Superior' : list(np.arange(1.86, 3.01, 0.01))         
        }

        for categ, valor in age_19.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if vals == miles:
                    print('Segun Cooper Test tu capacidad es: {}, especificamente de: {}'.format(categ, vals))
    
    elif edad is list(range(20, 29)):

        age_20_29 = {
            'Muy Pobre' : list(np.arange(0.00, 1.23, 0.01)),
            'Pobre' : list(np.arange(1.23, 1.31, 0.01)),
            'Promedio' : list(np.arange(1.32, 1.50, 0.01)),
            'Bueno' : list(np.arange(1.50, 1.65, 0.01)),
            'Excelente' : list(np.arange(1.65, 1.77, 0.01)),
            'Superior' : list(np.arange(1.77, 3.00, 0.01))         
        }

        for categ, valor in age_20_29.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if vals == miles:
                    print('Segun Cooper Test tu capacidad es: {}, especificamente de: {}'.format(categ, vals))
                      
    elif edad is list(range(30, 39)):

        age_30_39 = {
            'Muy Pobre' : list(np.arange(0.00, 1.19, 0.01)),
            'Pobre' : list(np.arange(1.19, 1.31, 0.01)),
            'Promedio' : list(np.arange(1.31, 1.46, 0.01)),
            'Bueno' : list(np.arange(1.46, 1.57, 0.01)),
            'Excelente' : list(np.arange(1.57, 1.70, 0.01)),
            'Superior' : list(np.arange(1.70, 3.00, 0.01))         
        }

        for categ, valor in age_30_39.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if miles == vals:
                    print('Segun Cooper Test tu capacidad es: {}, especificamente de: {}'.format(categ, vals))

    elif edad is list(range(40, 49)):

        age_40_49 = {
            'Muy Pobre' : list(np.arange(0.00, 1.15, 0.01)),
            'Pobre' : list(np.arange(1.15, 1.25, 0.01)),
            'Promedio' : list(np.arange(1.25, 1.40, 0.01)),
            'Bueno' : list(np.arange(1.40, 1.54, 0.01)),
            'Excelente' : list(np.arange(1.54, 1.66, 0.01)),
            'Superior' : list(np.arange(1.66, 3.00, 0.01))         
        }

        for categ, valor in age_40_49.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if miles == vals:
                    print('Segun Cooper Test tu capacidad es: {}, especificamente de: {}'.format(categ, vals))

    elif edad is list(range(50, 59)):

        age_50_59 = {
            'Muy Pobre' : list(np.arange(0.00, 1.04, 0.01)),
            'Pobre' : list(np.arange(1.04, 1.17, 0.01)),
            'Promedio' : list(np.arange(1.17, 1.31, 0.01)),
            'Bueno' : list(np.arange(1.31, 1.45, 0.01)),
            'Excelente' : list(np.arange(1.45, 1.59, 0.01)),
            'Superior' : list(np.arange(1.59, 3.00, 0.01))         
        }

        for categ, valor in age_50_59.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))           
                if miles == vals:
                    print('Segun Cooper Test tu capacidad es: {}, especificamente de: {}'.format(categ, vals))
        
    else: 

        age_60 = {
            'Muy Pobre' : list(np.arange(0.00, 0.87, 0.01)),
            'Pobre' : list(np.arange(0.87, 1.03, 0.01)),
            'Promedio' : list(np.arange(1.03, 1.21, 0.01)),
            'Bueno' : list(np.arange(1.21, 1.33, 0.01)),
            'Excelente' : list(np.arange(1.33, 1.56, 0.01)),
            'Superior' : list(np.arange(1.56, 3.00, 0.01))         
        }

        for categ, valor in age_60.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))       
                if miles == vals:
                    print('Segun Cooper Test tu capacidad es: {}, especificamente de: {}'.format(categ, vals))
        

def ct_woman_age_clas(miles, edad):
    logger.info('Cooper Test clasificatin for woman age')
    miles = float('{:.2f}'.format(miles))

    if edad <= 19: 

        age_19 = {
            'Muy Pobre' : list(np.arange(0.00, 1.01, 0.01)),
            'Pobre' : list(np.arange(1.01, 1.19, 0.01)),
            'Promedio' : list(np.arange(1.19, 1.30, 0.01)),
            'Bueno' : list(np.arange(1.30, 1.44, 0.01)),
            'Excelente' : list(np.arange(1.44, 1.52, 0.01)),
            'Superior' : list(np.arange(1.52, 3.00, 0.01))         
        }

        for categ, valor in age_19.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if miles == vals:
                    print('Segun Cooper Test tu capacidad es: {}, especificamente de: {}'.format(categ, vals))
    
    elif edad is list(range(20, 29)):

        age_20_29 = {
            'Muy Pobre' : list(np.arange(0.00, 0.97, 0.01)),
            'Pobre' : list(np.arange(0.97, 1.12, 0.01)),
            'Promedio' : list(np.arange(1.12, 1.23, 0.01)),
            'Bueno' : list(np.arange(1.23, 1.35, 0.01)),
            'Excelente' : list(np.arange(1.35, 1.46, 0.01)),
            'Superior' : list(np.arange(1.46, 3.00, 0.01))        
        }

        for categ, valor in age_20_29.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if miles == vals:
                    print('Segun Cooper Test tu capacidad es: {}, especificamente de: {}'.format(categ, vals))
    
    elif edad is list(range(30, 39)):

        age_30_39 = {
            'Muy Pobre' : list(np.arange(0.00, 0.95, 0.01)),
            'Pobre' : list(np.arange(0.95, 1.06, 0.01)),
            'Promedio' : list(np.arange(1.06, 1.19, 0.01)),
            'Bueno' : list(np.arange(1.19, 1.30, 0.01)),
            'Excelente' : list(np.arange(1.30, 1.40, 0.01)),
            'Superior' : list(np.arange(1.40, 3.00, 0.01))         
        }

        for categ, valor in age_30_39.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if miles == vals:
                    print('Segun Cooper Test tu capacidad es: {}, especificamente de: {}'.format(categ, vals))

    elif edad is list(range(40, 49)):

        age_40_49 = {
            'Muy Pobre' : list(np.arange(0.00, 0.89, 0.01)),
            'Pobre' : list(np.arange(0.89, 0.99, 0.01)),
            'Promedio' : list(np.arange(0.99, 1.12, 0.01)),
            'Bueno' : list(np.arange(1.12, 1.25, 0.01)),
            'Excelente' : list(np.arange(1.25, 1.35, 0.01)),
            'Superior' : list(np.arange(1.35, 3.00, 0.01))         
        }

        for categ, valor in age_40_49.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if miles == vals:
                    print('Segun Cooper Test tu capacidad es: {}, especificamente de: {}'.format(categ, vals))

    elif edad is list(range(50, 59)):

        age_50_59 = {
            'Muy Pobre' : list(np.arange(0.00, 0.85, 0.01)),
            'Pobre' : list(np.arange(0.85, 0.94, 0.01)),
            'Promedio' : list(np.arange(0.94, 1.06, 0.01)),
            'Bueno' : list(np.arange(1.06, 1.19, 0.01)),
            'Excelente' : list(np.arange(1.19, 1.31, 0.01)),
            'Superior' : list(np.arange(1.31, 3.00, 0.01))         
        }

        for categ, valor in age_50_59.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if miles == vals:
                    print('Segun Cooper Test tu capacidad es: {}, especificamente de: {}'.format(categ, vals))
        
    else: 

        age_60 = {
            'Muy Pobre' : list(np.arange(0.00, 0.79, 0.01)),
            'Pobre' : list(np.arange(0.79, 0.87, 0.01)),
            'Promedio' : list(np.arange(0.87, 0.99, 0.01)),
            'Bueno' : list(np.arange(0.99, 1.10, 0.01)),
            'Excelente' : list(np.arange(1.10, 1.19, 0.01)),
            'Superior' : list(np.arange(1.19, 3.00, 0.01))         
        }

        for categ, valor in age_60.items(): 
            for val in valor:
                vals = float("{:.2f}".format(val))
                if miles == vals:
                    print('Segun Cooper Test tu capacidad es: {}, especificamente de: {}'.format(categ, vals))
        


if __name__ == "__main__":
    
    sexo = int(input('Siendo masculino = 1 y mujer = 0: '))
    edad = int(input('Ingrese su edad: '))
    km = float(input('Ingrese la distancia recorrida en 12 mins: '))
    miles = km * 0.62
    
    
    cooper_test = Cooper_test(sexo, miles, edad)
    cooper_test.ct_clas_gender()
