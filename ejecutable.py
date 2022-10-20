from tablero_sudoku import Tablero
from copy import copy


tablero=Tablero()
tablero.crear_tablero()
tablero.borrar_valores(64)

tab2=Tablero()

cont=0

for i in range(9):
    for j in range(9):
        tab2[i][j].valor=tablero.valores()[cont]
        cont+=1

tab2.resolver_tablero()
tablero.resolver_tablero()

print(tab2)
print(tablero)

'''
La idea del proyecto es tomar el tablero que genera este ejecutable
y esconder ciertos valores del sudoku al usuario en la interfaz que usaremos.

Despues el usuario puede ingresar sus propios valores y el programa los compara con los
que genero este ejecutable, y le informa si acerto o no, ya que los tableros que se generan
ya vienen todos solucionados.
'''
