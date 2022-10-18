class Valor_sudoku:        
    def __init__(self): #Crea un valor para una casilla de sudoku, asigna un valor 0 por defecto
        self.valor=0
        
    def def_valor(self,valor): #Asigna un numero al atributo valor
        if valor>9 or valor<1:
            msn="Valor debe estar entre 1 y 9" #Las casillas de sudoku solo pueden tomar valores del 1-9
            error=ValueError(msn)
            raise error
        else:
            self.valor=valor
    
    def __str__(self): #Retorna el valor asignado al objeto
        msn="{0}".format(self.valor)
            
        return msn