from tablero_sudoku import Tablero

tablero=Tablero()
tablero.crear_tablero()
print(tablero)

'''
La idea del proyecto es tomar el tablero que genera este ejecutable
y esconder ciertos valores del sudoku al usuario en la interfaz que usaremos.

Despues el usuario puede ingresar sus propios valores y el programa los compara con los
que genero este ejecutable, y le informa si acerto o no, ya que los tableros que se generan
ya vienen todos solucionados.
'''