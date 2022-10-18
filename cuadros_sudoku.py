from valores_sudoku import Valor_sudoku

class Cuadro_sudoku:
    def __init__(self): #Define un solo diccionario con los valores por defecto en 0
    
        '''Las celdas del sudoku equivalen a las claves del diccionario de la siguente manera:
            0 1 2
            3 4 5
            6 7 8
        '''
        
        self.dic={}
        
        for i in range(9):
            self.dic[i]=Valor_sudoku()
            
    def crear_cuadro_ini (self): #Genera un cuadro de sudoku cualquiera
        from random import randint
        
        cont=0
        cuadro_ok=False
        valores_usados=[]
        
        while not cuadro_ok:
            nuevo_num=randint(1, 9)
            if nuevo_num not in valores_usados:
                self.dic[cont].def_valor(nuevo_num)
                cont+=1
                valores_usados.append(nuevo_num)
                
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        #Reemplaza los valores asociados a las claves del diccionario con números del 1 al 9
            if cont == 9:
                cuadro_ok=True
        #Al llenar los 9 valores del diccionario, retorna el objeto cuadro
        return self
    
    def __getitem__(self,clave):
        #El método sobrecarga el objeto de tal forma que se pueda acceder a los elementos del diccionario con solo parentesis cuadradas
        if clave>8 or clave<0:
            msn="Valor debe estar entre 0 y 8" #Las casillas de sudoku solo pueden tomar valores del 1-9
            error=ValueError(msn)
            raise error
            
        valor=self.dic[clave]
        return valor
    
    def __str__(self):#Retorna los valores del diccionario del cuadro a forma de cuadricula
        cont=0
        msn=""
        for i in self.dic.values():
            msn+="{0}\t".format(i)
            cont+=1
            if cont==3 or cont==6:
                msn+="\n"
        return msn