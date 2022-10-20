from cuadros_sudoku import Cuadro_sudoku

class Tablero:    
    def __init__(self): #Define un solo diccionario con los cuadros del tablero
    
        '''Las celdas del sudoku equivalen a las claves del diccionario de la siguente manera:
            0 1 2
            3 4 5
            6 7 8
        '''
        
        self.dic_tablero={}
        
        for i in range(9):
            self.dic_tablero[i]=Cuadro_sudoku()
            
        self.fila0=[]
        self.fila1=[]
        self.fila2=[]
        self.fila3=[]
        self.fila4=[]
        self.fila5=[]
        self.fila6=[]
        self.fila7=[]
        self.fila8=[]
        
        #Los ciclos for siguientes sirven para adjuntar todos los objetos Valor_Sudoku a sus filas correspondientes en el tablero, en forma de lista
        
        num_cuadro=0
        num_fila=0
        for _ in range(9):
            self.fila0.append(self.dic_tablero[num_cuadro][num_fila])
            num_fila+=1
            if num_fila==3:
                num_fila=0
                num_cuadro+=1
        
        num_cuadro=0
        num_fila=3
        for _ in range(9):
            self.fila1.append(self.dic_tablero[num_cuadro][num_fila])
            num_fila+=1
            if num_fila==6:
                num_fila=3
                num_cuadro+=1
        
        num_cuadro=0
        num_fila=6
        for _ in range(9):
            self.fila2.append(self.dic_tablero[num_cuadro][num_fila])
            num_fila+=1
            if num_fila==9:
                num_fila=6
                num_cuadro+=1
        
        num_cuadro=3
        num_fila=0
        for _ in range(9):
            self.fila3.append(self.dic_tablero[num_cuadro][num_fila])
            num_fila+=1
            if num_fila==3:
                num_fila=0
                num_cuadro+=1
        
        num_cuadro=3
        num_fila=3
        for _ in range(9):
            self.fila4.append(self.dic_tablero[num_cuadro][num_fila])
            num_fila+=1
            if num_fila==6:
                num_fila=3
                num_cuadro+=1
        
        num_cuadro=3
        num_fila=6
        for _ in range(9):
            self.fila5.append(self.dic_tablero[num_cuadro][num_fila])
            num_fila+=1
            if num_fila==9:
                num_fila=6
                num_cuadro+=1
        
        num_cuadro=6
        num_fila=0
        for _ in range(9):
            self.fila6.append(self.dic_tablero[num_cuadro][num_fila])
            num_fila+=1
            if num_fila==3:
                num_fila=0
                num_cuadro+=1
        
        num_cuadro=6
        num_fila=3
        for _ in range(9):
            self.fila7.append(self.dic_tablero[num_cuadro][num_fila])
            num_fila+=1
            if num_fila==6:
                num_fila=3
                num_cuadro+=1
        
        num_cuadro=6
        num_fila=6
        for _ in range(9):
            self.fila8.append(self.dic_tablero[num_cuadro][num_fila])
            num_fila+=1
            if num_fila==9:
                num_fila=6
                num_cuadro+=1
                
        self.columna0=[]        
        self.columna1=[]        
        self.columna2=[]        
        self.columna3=[]        
        self.columna4=[]        
        self.columna5=[]        
        self.columna6=[]        
        self.columna7=[]        
        self.columna8=[]
        
        #Los ciclos for siguientes sirven para adjuntar todos los objetos Valor_Sudoku a sus columnas correspondientes en el tablero, en forma de lista
        
        num_cuadro=0
        num_columna=0
        for _ in range(9):
            self.columna0.append(self.dic_tablero[num_cuadro][num_columna])
            num_columna+=3
            if num_columna==9:
                num_columna=0
                num_cuadro+=3
        
        num_cuadro=0
        num_columna=1
        for _ in range(9):
            self.columna1.append(self.dic_tablero[num_cuadro][num_columna])
            num_columna+=3
            if num_columna==10:
                num_columna=1
                num_cuadro+=3
        
        num_cuadro=0
        num_columna=2
        for _ in range(9):
            self.columna2.append(self.dic_tablero[num_cuadro][num_columna])
            num_columna+=3
            if num_columna==11:
                num_columna=2
                num_cuadro+=3
        
        num_cuadro=1
        num_columna=0
        for _ in range(9):
            self.columna3.append(self.dic_tablero[num_cuadro][num_columna])
            num_columna+=3
            if num_columna==9:
                num_columna=0
                num_cuadro+=3
        
        num_cuadro=1
        num_columna=1
        for _ in range(9):
            self.columna4.append(self.dic_tablero[num_cuadro][num_columna])
            num_columna+=3
            if num_columna==10:
                num_columna=1
                num_cuadro+=3
        
        num_cuadro=1
        num_columna=2
        for _ in range(9):
            self.columna5.append(self.dic_tablero[num_cuadro][num_columna])
            num_columna+=3
            if num_columna==11:
                num_columna=2
                num_cuadro+=3
        
        num_cuadro=2
        num_columna=0
        for _ in range(9):
            self.columna6.append(self.dic_tablero[num_cuadro][num_columna])
            num_columna+=3
            if num_columna==9:
                num_columna=0
                num_cuadro+=3
        
        num_cuadro=2
        num_columna=1
        for _ in range(9):
            self.columna7.append(self.dic_tablero[num_cuadro][num_columna])
            num_columna+=3
            if num_columna==10:
                num_columna=1
                num_cuadro+=3
        
        num_cuadro=2
        num_columna=2
        for _ in range(9):
            self.columna8.append(self.dic_tablero[num_cuadro][num_columna])
            num_columna+=3
            if num_columna==11:
                num_columna=2
                num_cuadro+=3
        
    def __getitem__(self,clave):
        #El método sobrecarga el objeto de tal forma que se pueda acceder a los elementos del diccionario con solo parentesis cuadradas
        valor=self.dic_tablero[clave]
        return valor
    
    def crear_cuadros_ini(self):
        for i in (0,4,8):
            self[i].crear_cuadro_ini() #Llena los valores de los cuadros 0,4 y 8
            
    def encontrar_vacio(self):#Encuentra las cooredenadas de un cuadro no resuelto
        filas=[self.fila0,self.fila1,self.fila2,self.fila3,self.fila4,self.fila5,self.fila6,self.fila7,self.fila8]
        columnas=[self.columna0,self.columna1,self.columna2,self.columna3,self.columna4,self.columna5,self.columna6,self.columna7,self.columna8]
    
        coordenadas=[]
        vacio=False
    
        for i in range(9):
            for j in range(9):
                if self[i][j].valor==0:
                    #Si el numero asignado a un valor es 0, significa que esta vacio
                    vacio=True
                if vacio:#Al encontrar un espacio vacio encuentra la fila y la columna relacionados a este
                    for l in filas:
                        if self[i][j] in l:
                            coordenadas.append(l)
                    for l in columnas:
                        if self[i][j] in l:
                            coordenadas.append(l)
                    #Se retornan tanto la fila como la columna en una lista coordenadas  
                    return coordenadas
        #Si ya no hay espacios vacios, no hay coordenadas para retornar, por lo tanto el metodo retorna None
        return None
    
    def valido(self,num,coordenadas):
        for i in range(9):
            for j in coordenadas[0]:
                if j in coordenadas[1]:
                    #Identifica el objeto valor correspondiente a las coordenadas y lo asigna a una variable para trabajar
                    valor=j
                    
            for j in range(9):
                if num==coordenadas[0][j].valor:
                    #Revisa si el valor esta repetido en la fila, que esta definida como lista en el primer valor de la lista coordenadas
                    return False
                
            for j in range(9):
                if num==coordenadas[1][j].valor:
                    #Revisa si el valor esta repetido en la columna, que esta definida como lista en el segundo valor de la lista coordenadas
                    return False
            
            for p in range(9):
                if valor in self[p].dic.values():#Busca el cuadro donde el valor está ubicado
                    cuadro=self[p]
                    
            for j in range(9):
                if num==cuadro[j].valor:#Si el valor esta repetido, lo descarta
                    return False
                        
            return True
            
    def resolver_valor(self):#Resuelve el valor que la funcion self.encontrar_vacio encuentre
        coordenadas=self.encontrar_vacio()
        
        if coordenadas==None:#Si no retorna coordenadas quiere decir que ya esta resuelto el tablero
            return True
        
        fila=coordenadas[0]
        columna=coordenadas[1]
    
        for i in range(1,10):
            if self.valido(i,(coordenadas)):#Revisa si el valor que toma i es valido dentro del tablero
                for j in fila:
                    if j in columna:
                        j.valor=i#Si es valido, lo asigna
                
                if self.resolver_valor():#Se devuelve a revisar si el valor cambia el estado del tablero
                    return True
                
                for j in fila:
                    if j in columna:#Si la funcion en el bloque anterior no retorna True, deja el espacio vacio para resolver luego
                        j.valor=0
                

        return False
    
    def resolver_tablero(self):#Resuelve cada cuadro hasta que no tenga más cuadros para resolver
        while not self.resolver_valor():
            pass
        
    def crear_tablero(self):#Crea un tablero resuelto totalmente aleatorio
    #La idea es esconder varios valores para que el usuario pueda resolverlos por su cuenta en la interfaz
        self.crear_cuadros_ini()
        self.resolver_tablero()
        
    def borrar_valores(self,num_valores):#Borra valores al azar
        if num_valores>64 or num_valores<1:
            msn="Valor debe estar entre 1 y 64" #A lo sumo se pueden borrar 64 valores para que tenga solucion
            error=ValueError(msn)
            raise error    
    
        for i in range(9):
            for j in range(9):
                if self[i][j].valor==0:
                    msn="El tablero no esta lleno" #Si encuentra un tablero no lleno, salta un error
                    error=ValueError(msn)
                    raise error
    
        from random import randint
        
        
        for i in range(num_valores):
            valor_borrado=False
            
            while not valor_borrado:
                num_cuadro=randint(0, 8)
                num_valor=randint(0, 8)
                if self[num_cuadro][num_valor].valor==0:
                    continue
                else:
                    self[num_cuadro][num_valor].valor=0
                    valor_borrado=True
                
    def valores(self):#Retorna los valores de todo en tablero en una lista
        valores={}
        cont=0
        
        for i in range(81):
            valores[i]=0
    
        for i in range(9):
            for j in range(9):
                valores[cont]=self[i][j].valor
                cont+=1
                
        return valores
    
    def copy(self,tab2):
        cont=0

        for i in range(9):
            for j in range(9):
                self[i][j].valor=tab2.valores()[cont]
                cont+=1
    
    def __str__(self):#Retorna los 9 cuadros del tablero en un string
    #Su propósito es revisar los cuadros mientras programamos
        cont=0
        msn=""
        for j in (self.fila0,self.fila1,self.fila2):
            for i in (j[cont],j[cont+1],j[cont+2]):
                msn+="{0}\t".format(i.valor)
            msn+="|"
            cont+=3
            for i in (j[cont],j[cont+1],j[cont+2]):
                msn+="{0}\t".format(i.valor)
            msn+="|"
            cont+=3
            for i in (j[cont],j[cont+1],j[cont+2]):
                msn+="{0}\t".format(i.valor)
            msn+="\n"
            cont=0
        msn+="------------------------------------------------------------------\n"
        
        for j in (self.fila3,self.fila4,self.fila5):
            for i in (j[cont],j[cont+1],j[cont+2]):
                msn+="{0}\t".format(i.valor)
            msn+="|"
            cont+=3
            for i in (j[cont],j[cont+1],j[cont+2]):
                msn+="{0}\t".format(i.valor)
            msn+="|"
            cont+=3
            for i in (j[cont],j[cont+1],j[cont+2]):
                msn+="{0}\t".format(i.valor)
            msn+="\n"
            cont=0
        msn+="------------------------------------------------------------------\n"
        
        for j in (self.fila6,self.fila7,self.fila8):
            for i in (j[cont],j[cont+1],j[cont+2]):
                msn+="{0}\t".format(i.valor)
            msn+="|"
            cont+=3
            for i in (j[cont],j[cont+1],j[cont+2]):
                msn+="{0}\t".format(i.valor)
            msn+="|"
            cont+=3
            for i in (j[cont],j[cont+1],j[cont+2]):
                msn+="{0}\t".format(i.valor)
            msn+="\n"
            cont=0
            
        return msn