from tkinter import *
from tkinter import font

import tablero_sudoku


def change_num(new_button, cuadros, i, j):
    if new_button['text'] >= 0 and new_button['text'] < 9:
        new_button['text'] += 1
        (cuadros[i])[j] += 1

    else:
        new_button['text'] = 0
        (cuadros[i])[j] = 0


def verificar(tablero, cuadros):
    for i in range(9):
        if int(str(tablero.fila0[i])) == (cuadros[0])[i]:
            continue
        else:
            print("Tienes un error en = fila 1, columna {0}".format(i + 1))

    for i in range(9):
        if int(str(tablero.fila1[i])) == (cuadros[1])[i]:
            continue
        else:
            print("Tienes un error en = fila 2, columna {0}".format(i + 1))

    for i in range(9):
        if int(str(tablero.fila2[i])) == (cuadros[2])[i]:
            continue
        else:
            print("Tienes un error en = fila 3, columna {0}".format(i + 1))

    for i in range(9):
        if int(str(tablero.fila3[i])) == (cuadros[3])[i]:
            continue
        else:
            print("Tienes un error en = fila 4, columna {0}".format(i + 1))

    for i in range(9):
        if int(str(tablero.fila4[i])) == (cuadros[4])[i]:
            continue
        else:
            print("Tienes un error en = fila 5, columna {0}".format(i + 1))

    for i in range(9):
        if int(str(tablero.fila5[i])) == (cuadros[5])[i]:
            continue
        else:
            print("Tienes un error en = fila 6, columna {0}".format(i + 1))

    for i in range(9):
        if int(str(tablero.fila6[i])) == (cuadros[6])[i]:
            continue
        else:
            print("Tienes un error en = fila 7, columna {0}".format(i + 1))

    for i in range(9):
        if int(str(tablero.fila7[i])) == (cuadros[7])[i]:
            continue
        else:
            print("Tienes un error en = fila 8, columna {0}".format(i + 1))

    for i in range(9):
        if int(str(tablero.fila8[i])) == (cuadros[8])[i]:
            continue
        else:
            print("Tienes un error en = fila 9, columna {0}".format(i + 1))


def crear_juego(tablero, cuadros):
    import random
    numeros = []
    for i in range(9):
        numeros.append(i)
    for j in range(4):
        n = random.choice(numeros)
        (cuadros[0])[n] = int(str(tablero.fila0[n]))
        numeros.remove(n)

    numeros1 = []
    for i in range(9):
        numeros1.append(i)
    for j in range(4):
        n = random.choice(numeros1)
        (cuadros[1])[n] = int(str(tablero.fila1[n]))
        numeros1.remove(n)

    numeros2 = []
    for i in range(9):
        numeros2.append(i)
    for j in range(4):
        n = random.choice(numeros2)
        (cuadros[2])[n] = int(str(tablero.fila2[n]))
        numeros2.remove(n)

    numeros3 = []
    for i in range(9):
        numeros3.append(i)
    for j in range(4):
        n = random.choice(numeros3)
        (cuadros[3])[n] = int(str(tablero.fila3[n]))
        numeros3.remove(n)

    numeros4 = []
    for i in range(9):
        numeros4.append(i)
    for j in range(4):
        n = random.choice(numeros4)
        (cuadros[4])[n] = int(str(tablero.fila4[n]))
        numeros4.remove(n)

    numeros5 = []
    for i in range(9):
        numeros5.append(n)
    for j in range(4):
        n = random.choice(numeros5)
        (cuadros[5])[n] = int(str(tablero.fila5[n]))
        numeros5.remove(n)

    numeros6 = []
    for i in range(9):
        numeros6.append(i)
    for j in range(4):
        n = random.choice(numeros6)
        (cuadros[6])[n] = int(str(tablero.fila6[n]))
        numeros6.remove(n)

    numeros7 = []
    for i in range(9):
        numeros7.append(i)
    for j in range(4):
        n = random.choice(numeros7)
        (cuadros[7])[n] = int(str(tablero.fila7[n]))
        numeros7.remove(n)

    numeros8 = []
    for i in range(9):
        numeros8.append(i)
    for j in range(4):
        n = random.choice(numeros8)
        (cuadros[8])[n] = int(str(tablero.fila8[n]))
        numeros8.remove(n)

num_intentos=0
def intento():
    global num_intentos
    num_intentos+=1

def actualizar_intentos(canvas):
    global num_intentos
    canvas.delete('all')
    canvas.create_text(50, 25, text="Intentos: {0}".format(num_intentos), fill="black", font=('Helvetica 11 bold'))


cuadros = {}
for i in range(9):
    cuadros[i] = []
    for j in range(9):
        (cuadros[i]).append(0)

tablero = tablero_sudoku.Tablero()
tablero.crear_tablero()

crear_juego(tablero, cuadros)

sudoku = Tk()

lista = []
for i in range(9):
    for j in range(9):
        lista.append(Button(text=(cuadros[i])[j], default="active", height=3, width=6))

c1 = 0
c2 = 0
for l in lista:
    if c2 == 9:
        c1 += 1
        c2 = 0
    l.grid(row=c1, column=c2)
    c2 += 1

cont_cuadro=0
cont_valor=0
for i in range(81):
    (lista[i]).configure(command=lambda: change_num(lista[i], cuadros, cont_cuadro, cont_valor))
    cont_valor+=1
    if cont_valor==9:
        cont_cuadro+=1
        cont_valor=0

color = ("cyan", "white")
contadores = [0, 0, 0, 0]
cambia_color = lambda num_color: 1 if num_color == 0 else 0
for i in lista:
    if contadores[1] == 3:
        contadores[0] = cambia_color(contadores[0])
        contadores[1] = 0
        contadores[2] += 1

    if contadores[2] == 3:
        contadores[0] = cambia_color(contadores[0])
        contadores[2] = 0
        contadores[3] += 1

    if contadores[3] == 3:
        contadores[0] = cambia_color(contadores[0])
        contadores[3] = 0

    i.configure(bg=color[contadores[0]])

    contadores[1] += 1

for i in lista:
    if i['text'] != 0:
        i["state"] = DISABLED
        i["font"] = font.Font(weight="bold", slant="italic", size=9)

print(tablero)


canvas= Canvas(sudoku, width= 100, height= 50, bg="#F0F0F0")
canvas.create_text(50, 25, text="Intentos: {0}".format(num_intentos), fill="black", font=('Helvetica 11 bold'))
canvas.grid(row=2, column=11)

verify = Button(text="Verificar", default="active", width=14)
verify.grid(row=4, column=11)
verify.configure(command=lambda: [verificar(tablero, cuadros),intento(),actualizar_intentos(canvas)])

sudoku.mainloop()
