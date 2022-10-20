from tablero_sudoku import Tablero

tablero=Tablero()
tablero.crear_tablero()
tablero.borrar_valores(64)

tab2=Tablero()
tab2.copy(tablero)

tab2.resolver_tablero()
tablero.resolver_tablero()

print(tab2.valores()==tablero.valores())

'''
La idea del proyecto es tomar el tablero que genera este ejecutable
y esconder ciertos valores del sudoku al usuario en la interfaz que usaremos.

Despues el usuario puede ingresar sus propios valores y el programa los compara con los
que genero este ejecutable, y le informa si acerto o no, ya que los tableros que se generan
ya vienen todos solucionados.
'''
