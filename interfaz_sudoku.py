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
            if lista[i]["state"]!=DISABLED:
                lista[i]["state"] = DISABLED
                lista[i]["font"] = font.Font(weight="bold", slant="italic", size=9)
                lista[i].configure(bg="#88ff78")
            continue
        elif (cuadros[0])[i] != 0:
            print("Tienes un error en = fila 1, columna {0}".format(i + 1))
            lista[i].configure(bg="red")
        else:
            lista[i].configure(bg="#ffdb78")

    for i in range(9):
        if int(str(tablero.fila1[i])) == (cuadros[1])[i]:
            if lista[i+9]["state"] != DISABLED:
                lista[i+9]["state"] = DISABLED
                lista[i+9]["font"] = font.Font(weight="bold", slant="italic", size=9)
                lista[i+9].configure(bg="#88ff78")
            continue
        elif (cuadros[1])[i] != 0:
            print("Tienes un error en = fila 2, columna {0}".format(i + 1))
            lista[i+9].configure(bg="red")
        else:
            lista[i+9].configure(bg="#ffdb78")

    for i in range(9):
        if int(str(tablero.fila2[i])) == (cuadros[2])[i]:
            if lista[i+9*2]["state"] != DISABLED:
                lista[i+9*2]["state"] = DISABLED
                lista[i+9*2]["font"] = font.Font(weight="bold", slant="italic", size=9)
                lista[i+9*2].configure(bg="#88ff78")
            continue
        elif (cuadros[2])[i] != 0:
            print("Tienes un error en = fila 3, columna {0}".format(i + 1))
            lista[i + 9 * 2].configure(bg="red")
        else:
            lista[i + 9 * 2].configure(bg="#ffdb78")

    for i in range(9):
        if int(str(tablero.fila3[i])) == (cuadros[3])[i]:
            if lista[i+9*3]["state"] != DISABLED:
                lista[i+9*3]["state"] = DISABLED
                lista[i+9*3]["font"] = font.Font(weight="bold", slant="italic", size=9)
                lista[i+9*3].configure(bg="#88ff78")
            continue
        elif (cuadros[3])[i] != 0:
            print("Tienes un error en = fila 4, columna {0}".format(i + 1))
            lista[i + 9*3].configure(bg="red")
        else:
            lista[i + 9*3].configure(bg="#ffdb78")

    for i in range(9):
        if int(str(tablero.fila4[i])) == (cuadros[4])[i]:
            if lista[i+9*4]["state"] != DISABLED:
                lista[i+9*4]["state"] = DISABLED
                lista[i+9*4]["font"] = font.Font(weight="bold", slant="italic", size=9)
                lista[i+9*4].configure(bg="#88ff78")
            continue
        elif (cuadros[4])[i] != 0:
            print("Tienes un error en = fila 5, columna {0}".format(i + 1))
            lista[i + 9*4].configure(bg="red")
        else:
            lista[i + 9 * 4].configure(bg="#ffdb78")

    for i in range(9):
        if int(str(tablero.fila5[i])) == (cuadros[5])[i]:
            if lista[i+9*5]["state"] != DISABLED:
                lista[i+9*5]["state"] = DISABLED
                lista[i+9*5]["font"] = font.Font(weight="bold", slant="italic", size=9)
                lista[i+9*5].configure(bg="#88ff78")
            continue
        elif (cuadros[5])[i] != 0:
            print("Tienes un error en = fila 6, columna {0}".format(i + 1))
            lista[i + 9*5].configure(bg="red")
        else:
            lista[i + 9 * 5].configure(bg="#ffdb78")

    for i in range(9):
        if int(str(tablero.fila6[i])) == (cuadros[6])[i]:
            if lista[i+9*6]["state"] != DISABLED:
                lista[i+9*6]["state"] = DISABLED
                lista[i+9*6]["font"] = font.Font(weight="bold", slant="italic", size=9)
                lista[i+9*6].configure(bg="#88ff78")
            continue
        elif (cuadros[6])[i] != 0:
            print("Tienes un error en = fila 7, columna {0}".format(i + 1))
            lista[i + 9*6].configure(bg="red")
        else:
            lista[i + 9 * 6].configure(bg="#ffdb78")

    for i in range(9):
        if int(str(tablero.fila7[i])) == (cuadros[7])[i]:
            if lista[i+9*7]["state"] != DISABLED:
                lista[i+9*7]["state"] = DISABLED
                lista[i+9*7]["font"] = font.Font(weight="bold", slant="italic", size=9)
                lista[i+9*7].configure(bg="#88ff78")
            continue
        elif (cuadros[7])[i] != 0:
            print("Tienes un error en = fila 8, columna {0}".format(i + 1))
            lista[i + 9*7].configure(bg="red")
        else:
            lista[i + 9 * 7].configure(bg="#ffdb78")

    for i in range(9):
        if int(str(tablero.fila8[i])) == (cuadros[8])[i]:
            if lista[i+9*8]["state"] != DISABLED:
                lista[i+9*8]["state"] = DISABLED
                lista[i+9*8]["font"] = font.Font(weight="bold", slant="italic", size=9)
                lista[i+9*8].configure(bg="#88ff78")
            continue
        elif (cuadros[8])[i] != 0:
            print("Tienes un error en = fila 9, columna {0}".format(i + 1))
            lista[i + 9*8].configure(bg="red")
        else:
            lista[i + 9 * 8].configure(bg="#ffdb78")


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

colores=[]
def obtener_colores(lista):
    global colores
    colores=[]
    for i in lista:
        colores.append(i.cget("bg"))

def restaurar_colores(colores,lista):
    from time import sleep
    sleep(1)
    for i in range(81):
        lista[i].configure(bg=colores[i])

def boton_verificar(colores,lista,tablero,cuadro):
    intento()
    actualizar_intentos(canvas)
    verificar(tablero, cuadros)
    #restaurar_colores(colores,lista)


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

(lista[0]).configure(command = lambda: change_num(lista[0],cuadros,0,0))
(lista[1]).configure(command = lambda: change_num(lista[1],cuadros,0,1))
(lista[2]).configure(command = lambda: change_num(lista[2],cuadros,0,2))
(lista[3]).configure(command = lambda: change_num(lista[3],cuadros,0,3))
(lista[4]).configure(command = lambda: change_num(lista[4],cuadros,0,4))
(lista[5]).configure(command = lambda: change_num(lista[5],cuadros,0,5))
(lista[6]).configure(command = lambda: change_num(lista[6],cuadros,0,6))
(lista[7]).configure(command = lambda: change_num(lista[7],cuadros,0,7))
(lista[8]).configure(command = lambda: change_num(lista[8],cuadros,0,8))
(lista[9]).configure(command = lambda: change_num(lista[9],cuadros,1,0))
(lista[10]).configure(command = lambda: change_num(lista[10],cuadros,1,1))
(lista[11]).configure(command = lambda: change_num(lista[11],cuadros,1,2))
(lista[12]).configure(command = lambda: change_num(lista[12],cuadros,1,3))
(lista[13]).configure(command = lambda: change_num(lista[13],cuadros,1,4))
(lista[14]).configure(command = lambda: change_num(lista[14],cuadros,1,5))
(lista[15]).configure(command = lambda: change_num(lista[15],cuadros,1,6))
(lista[16]).configure(command = lambda: change_num(lista[16],cuadros,1,7))
(lista[17]).configure(command = lambda: change_num(lista[17],cuadros,1,8))
(lista[18]).configure(command = lambda: change_num(lista[18],cuadros,2,0))
(lista[19]).configure(command = lambda: change_num(lista[19],cuadros,2,1))
(lista[20]).configure(command = lambda: change_num(lista[20],cuadros,2,2))
(lista[21]).configure(command = lambda: change_num(lista[21],cuadros,2,3))
(lista[22]).configure(command = lambda: change_num(lista[22],cuadros,2,4))
(lista[23]).configure(command = lambda: change_num(lista[23],cuadros,2,5))
(lista[24]).configure(command = lambda: change_num(lista[24],cuadros,2,6))
(lista[25]).configure(command = lambda: change_num(lista[25],cuadros,2,7))
(lista[26]).configure(command = lambda: change_num(lista[26],cuadros,2,8))
(lista[27]).configure(command = lambda: change_num(lista[27],cuadros,3,0))
(lista[28]).configure(command = lambda: change_num(lista[28],cuadros,3,1))
(lista[29]).configure(command = lambda: change_num(lista[29],cuadros,3,2))
(lista[30]).configure(command = lambda: change_num(lista[30],cuadros,3,3))
(lista[31]).configure(command = lambda: change_num(lista[31],cuadros,3,4))
(lista[32]).configure(command = lambda: change_num(lista[32],cuadros,3,5))
(lista[33]).configure(command = lambda: change_num(lista[33],cuadros,3,6))
(lista[34]).configure(command = lambda: change_num(lista[34],cuadros,3,7))
(lista[35]).configure(command = lambda: change_num(lista[35],cuadros,3,8))
(lista[36]).configure(command = lambda: change_num(lista[36],cuadros,4,0))
(lista[37]).configure(command = lambda: change_num(lista[37],cuadros,4,1))
(lista[38]).configure(command = lambda: change_num(lista[38],cuadros,4,2))
(lista[39]).configure(command = lambda: change_num(lista[39],cuadros,4,3))
(lista[40]).configure(command = lambda: change_num(lista[40],cuadros,4,4))
(lista[41]).configure(command = lambda: change_num(lista[41],cuadros,4,5))
(lista[42]).configure(command = lambda: change_num(lista[42],cuadros,4,6))
(lista[43]).configure(command = lambda: change_num(lista[43],cuadros,4,7))
(lista[44]).configure(command = lambda: change_num(lista[44],cuadros,4,8))
(lista[45]).configure(command = lambda: change_num(lista[45],cuadros,5,0))
(lista[46]).configure(command = lambda: change_num(lista[46],cuadros,5,1))
(lista[47]).configure(command = lambda: change_num(lista[47],cuadros,5,2))
(lista[48]).configure(command = lambda: change_num(lista[48],cuadros,5,3))
(lista[49]).configure(command = lambda: change_num(lista[49],cuadros,5,4))
(lista[50]).configure(command = lambda: change_num(lista[50],cuadros,5,5))
(lista[51]).configure(command = lambda: change_num(lista[51],cuadros,5,6))
(lista[52]).configure(command = lambda: change_num(lista[52],cuadros,5,7))
(lista[53]).configure(command = lambda: change_num(lista[53],cuadros,5,8))
(lista[54]).configure(command = lambda: change_num(lista[54],cuadros,6,0))
(lista[55]).configure(command = lambda: change_num(lista[55],cuadros,6,1))
(lista[56]).configure(command = lambda: change_num(lista[56],cuadros,6,2))
(lista[57]).configure(command = lambda: change_num(lista[57],cuadros,6,3))
(lista[58]).configure(command = lambda: change_num(lista[58],cuadros,6,4))
(lista[59]).configure(command = lambda: change_num(lista[59],cuadros,6,5))
(lista[60]).configure(command = lambda: change_num(lista[60],cuadros,6,6))
(lista[61]).configure(command = lambda: change_num(lista[61],cuadros,6,7))
(lista[62]).configure(command = lambda: change_num(lista[62],cuadros,6,8))
(lista[63]).configure(command = lambda: change_num(lista[63],cuadros,7,0))
(lista[64]).configure(command = lambda: change_num(lista[64],cuadros,7,1))
(lista[65]).configure(command = lambda: change_num(lista[65],cuadros,7,2))
(lista[66]).configure(command = lambda: change_num(lista[66],cuadros,7,3))
(lista[67]).configure(command = lambda: change_num(lista[67],cuadros,7,4))
(lista[68]).configure(command = lambda: change_num(lista[68],cuadros,7,5))
(lista[69]).configure(command = lambda: change_num(lista[69],cuadros,7,6))
(lista[70]).configure(command = lambda: change_num(lista[70],cuadros,7,7))
(lista[71]).configure(command = lambda: change_num(lista[71],cuadros,7,8))
(lista[72]).configure(command = lambda: change_num(lista[72],cuadros,8,0))
(lista[73]).configure(command = lambda: change_num(lista[73],cuadros,8,1))
(lista[74]).configure(command = lambda: change_num(lista[74],cuadros,8,2))
(lista[75]).configure(command = lambda: change_num(lista[75],cuadros,8,3))
(lista[76]).configure(command = lambda: change_num(lista[76],cuadros,8,4))
(lista[77]).configure(command = lambda: change_num(lista[77],cuadros,8,5))
(lista[78]).configure(command = lambda: change_num(lista[78],cuadros,8,6))
(lista[79]).configure(command = lambda: change_num(lista[79],cuadros,8,7))
(lista[80]).configure(command = lambda: change_num(lista[80],cuadros,8,8))

c1 = 0
c2 = 0
for l in lista:
    if c2 == 9:
        c1 += 1
        c2 = 0
    l.grid(row=c1, column=c2)
    c2 += 1

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
verify.configure(command=lambda: [boton_verificar(obtener_colores(lista),lista,tablero,cuadros),verify.after(800, lambda :[restaurar_colores(colores,lista)])])


sudoku.mainloop()
