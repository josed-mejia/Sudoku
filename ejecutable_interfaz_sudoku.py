import tkinter.font
from tkinter import *
from tkinter import font

import tablero_sudoku


def change_num(new_button, cuadros, i, j): #Esta función reemplaza el número base (0) cada vez que el jugador da click sobre el botón, así sucesivamente hasta que llegue a 9.
    if new_button['text'] >= 0 and new_button['text'] < 9:
        new_button['text'] += 1
        (cuadros[i])[j] += 1

    else:
        new_button['text'] = 0
        (cuadros[i])[j] = 0

tablero_resuelto=False
def verificar(tablero, cuadros): #En esta función, se revisa cada fila del sudoku que se está resolviendo y se compara con cada valor del tablero resuelto, si es diferente, sale error y el botón se pone en color rojo por tiempo. Si está bien, cambia a verde para que sepa que está bien.
    cont_errores=0
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
            cont_errores+=1
        else:
            lista[i].configure(bg="#ffdb78")
            cont_errores+=1

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
            cont_errores+=1
        else:
            lista[i+9].configure(bg="#ffdb78")
            cont_errores+=1

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
            cont_errores+=1
        else:
            lista[i + 9 * 2].configure(bg="#ffdb78")
            cont_errores+=1

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
            cont_errores+=1
        else:
            lista[i + 9*3].configure(bg="#ffdb78")
            cont_errores+=1

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
            cont_errores+=1
        else:
            lista[i + 9 * 4].configure(bg="#ffdb78")
            cont_errores+=1

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
            cont_errores+=1
        else:
            lista[i + 9 * 5].configure(bg="#ffdb78")
            cont_errores+=1
        if cont_errores==0:
            global tablero_resuelto
            tablero_resuelto=True

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
            cont_errores+=1
        else:
            lista[i + 9 * 6].configure(bg="#ffdb78")
            cont_errores+=1

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
            cont_errores+=1
        else:
            lista[i + 9 * 7].configure(bg="#ffdb78")
            cont_errores+=1

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
            cont_errores+=1
        else:
            lista[i + 9 * 8].configure(bg="#ffdb78")
            cont_errores+=1

    if cont_errores==0:
        tablero_resuelto=True

def crear_juego(tablero, cuadros): #Muestra 5 números aleatorios de cada fila en el tablero ya resuelto, para que el jugador halle las 4 incógnitas restantes.
    import random
    numeros = []
    for i in range(9):
        numeros.append(i)
    for j in range(5):
        n = random.choice(numeros)
        (cuadros[0])[n] = int(str(tablero.fila0[n]))
        numeros.remove(n)

    numeros1 = []
    for i in range(9):
        numeros1.append(i)
    for j in range(5):
        n = random.choice(numeros1)
        (cuadros[1])[n] = int(str(tablero.fila1[n]))
        numeros1.remove(n)

    numeros2 = []
    for i in range(9):
        numeros2.append(i)
    for j in range(5):
        n = random.choice(numeros2)
        (cuadros[2])[n] = int(str(tablero.fila2[n]))
        numeros2.remove(n)

    numeros3 = []
    for i in range(9):
        numeros3.append(i)
    for j in range(5):
        n = random.choice(numeros3)
        (cuadros[3])[n] = int(str(tablero.fila3[n]))
        numeros3.remove(n)

    numeros4 = []
    for i in range(9):
        numeros4.append(i)
    for j in range(5):
        n = random.choice(numeros4)
        (cuadros[4])[n] = int(str(tablero.fila4[n]))
        numeros4.remove(n)

    numeros5 = []
    for i in range(9):
        numeros5.append(i)
    for j in range(5):
        n = random.choice(numeros5)
        (cuadros[5])[n] = int(str(tablero.fila5[n]))
        numeros5.remove(n)

    numeros6 = []
    for i in range(9):
        numeros6.append(i)
    for j in range(5):
        n = random.choice(numeros6)
        (cuadros[6])[n] = int(str(tablero.fila6[n]))
        numeros6.remove(n)

    numeros7 = []
    for i in range(9):
        numeros7.append(i)
    for j in range(5):
        n = random.choice(numeros7)
        (cuadros[7])[n] = int(str(tablero.fila7[n]))
        numeros7.remove(n)

    numeros8 = []
    for i in range(9):
        numeros8.append(i)
    for j in range(5):
        n = random.choice(numeros8)
        (cuadros[8])[n] = int(str(tablero.fila8[n]))
        numeros8.remove(n)

num_intentos=0
def intento(): #Aumenta en 1 la variable global intentos.
    global num_intentos
    num_intentos+=1

def actualizar_intentos(canvas_intentos): #Reemplaza el texto con el número de intentos que se llevan hasta el momento.
    global num_intentos
    canvas_intentos.delete('all')
    canvas_intentos.create_text(50, 25, text="Intentos: {0}".format(num_intentos), fill="black", font=('Helvetica 11 bold'))

colores=[]
def obtener_colores(lista): #Obtiene los colores de cada botón y los agrega a una lista.
    global colores
    colores=[]
    for i in lista:
        colores.append(i.cget("bg"))

def restaurar_colores(colores,lista): #Restaura todos los colores de los botones del tablero.
    for i in range(81):
        lista[i].configure(bg=colores[i])

def boton_verificar(colores,lista,tablero,cuadro): #Verifica que cada valor  en los cuadros del tablero sí corresponda a la solución, de no ser así, aumenta el número de intentos.
    intento()
    actualizar_intentos(canvas_intentos)
    verificar(tablero, lineas)

def deshabilitar(boton): #Deshabilita el botón.
    boton["state"] = DISABLED

def habilitar(boton): #Habilita el botón.
    boton["state"] = ACTIVE

def acabar_juego(canvas_record): #Revisa si el tablero está resuelto, luego, si lo está, crea otra ventana con un mensaje de felicitaciones al usuario. También, revisa si el usuario mejoró el récord y actualiza el documento de mejor juego.
    global tablero_resuelto
    global num_intentos
    if tablero_resuelto:

        ventana_acabar=Tk()
        ventana_acabar.title("Felicitaciones!!!!!!!!!")
        canvas_cerrar = Canvas(ventana_acabar, width=300, height=150, bg="#F0F0F0")
        canvas_cerrar.create_text(150, 75, text="Felicidades! ha resuelto el sudoku\nen {0} intento{1}\n\nPuede cerrar ambas ventantas".format(num_intentos,("s" if num_intentos!=1 else "")), fill="black", font=('Helvetica 11 bold'))
        canvas_cerrar.grid(row=1,column=1)

        archivo_mejor_juego=open("Mejor_juego.txt","r")
        record=int(archivo_mejor_juego.read())
        archivo_mejor_juego.close()


        if record>num_intentos or record==0:
            archivo_mejor_juego = open("Mejor_juego.txt", "w")
            archivo_mejor_juego.write(str(num_intentos))
            canvas_record.delete('all')
            canvas_record.create_text(50, 25, text="Mejor juego:\n{0} intento{1}".format((num_intentos),("s" if num_intentos!=1 else "")), font=('Helvetica 11 bold'),fill="black")
            archivo_mejor_juego.close()

        ventana_acabar.mainloop()



def borrar_intentos(canvas_record): #Borra lo que tenga el archivo de mejor juego y borra todos los intentos que se hayan hecho.
    archivo_mejor_juego = open("Mejor_juego.txt", "w")
    archivo_mejor_juego.write("0")
    canvas_record.delete('all')
    canvas_record.create_text(50, 25, text="Sin mejor\n    juego", fill="black", font=('Helvetica 11 bold'))
    archivo_mejor_juego.close()

lineas = {}
for i in range(9):
    lineas[i] = []
    for j in range(9):
        (lineas[i]).append(0)  #Aquí se acaba de crear un tablero en blanco, es decir, con todos los valores en cero, para después mostrar algunos valores con la función crear_juego

tablero = tablero_sudoku.Tablero()
tablero.crear_tablero() #Aquí se crea un objeto de la clase tablero para poder dar los valores y tener una solución para comparar.

crear_juego(tablero, lineas) #Aquí se agregan algunos de los valores del tablero resuelto al tablero vacío.

sudoku = Tk()
sudoku.title("Sudoku") #Aquí se crea la ventana y se le cambia el título

lista = []
for i in range(9):
    for j in range(9):
        lista.append(Button(text=(lineas[i])[j], default="active", height=3, width=6)) #Aquí se crea una lista con los 81 botones de los números

#Ahora, se va a asignar la función change_num a cada botón para que esa sea la acción que realice cada vez que se haga click.
#No se podía en un ciclo for porque cuando se corre el programa sólo queda asignado para el último valor dado.
(lista[0]).configure(command = lambda: change_num(lista[0],lineas,0,0))
(lista[1]).configure(command = lambda: change_num(lista[1],lineas,0,1))
(lista[2]).configure(command = lambda: change_num(lista[2],lineas,0,2))
(lista[3]).configure(command = lambda: change_num(lista[3],lineas,0,3))
(lista[4]).configure(command = lambda: change_num(lista[4],lineas,0,4))
(lista[5]).configure(command = lambda: change_num(lista[5],lineas,0,5))
(lista[6]).configure(command = lambda: change_num(lista[6],lineas,0,6))
(lista[7]).configure(command = lambda: change_num(lista[7],lineas,0,7))
(lista[8]).configure(command = lambda: change_num(lista[8],lineas,0,8))
(lista[9]).configure(command = lambda: change_num(lista[9],lineas,1,0))
(lista[10]).configure(command = lambda: change_num(lista[10],lineas,1,1))
(lista[11]).configure(command = lambda: change_num(lista[11],lineas,1,2))
(lista[12]).configure(command = lambda: change_num(lista[12],lineas,1,3))
(lista[13]).configure(command = lambda: change_num(lista[13],lineas,1,4))
(lista[14]).configure(command = lambda: change_num(lista[14],lineas,1,5))
(lista[15]).configure(command = lambda: change_num(lista[15],lineas,1,6))
(lista[16]).configure(command = lambda: change_num(lista[16],lineas,1,7))
(lista[17]).configure(command = lambda: change_num(lista[17],lineas,1,8))
(lista[18]).configure(command = lambda: change_num(lista[18],lineas,2,0))
(lista[19]).configure(command = lambda: change_num(lista[19],lineas,2,1))
(lista[20]).configure(command = lambda: change_num(lista[20],lineas,2,2))
(lista[21]).configure(command = lambda: change_num(lista[21],lineas,2,3))
(lista[22]).configure(command = lambda: change_num(lista[22],lineas,2,4))
(lista[23]).configure(command = lambda: change_num(lista[23],lineas,2,5))
(lista[24]).configure(command = lambda: change_num(lista[24],lineas,2,6))
(lista[25]).configure(command = lambda: change_num(lista[25],lineas,2,7))
(lista[26]).configure(command = lambda: change_num(lista[26],lineas,2,8))
(lista[27]).configure(command = lambda: change_num(lista[27],lineas,3,0))
(lista[28]).configure(command = lambda: change_num(lista[28],lineas,3,1))
(lista[29]).configure(command = lambda: change_num(lista[29],lineas,3,2))
(lista[30]).configure(command = lambda: change_num(lista[30],lineas,3,3))
(lista[31]).configure(command = lambda: change_num(lista[31],lineas,3,4))
(lista[32]).configure(command = lambda: change_num(lista[32],lineas,3,5))
(lista[33]).configure(command = lambda: change_num(lista[33],lineas,3,6))
(lista[34]).configure(command = lambda: change_num(lista[34],lineas,3,7))
(lista[35]).configure(command = lambda: change_num(lista[35],lineas,3,8))
(lista[36]).configure(command = lambda: change_num(lista[36],lineas,4,0))
(lista[37]).configure(command = lambda: change_num(lista[37],lineas,4,1))
(lista[38]).configure(command = lambda: change_num(lista[38],lineas,4,2))
(lista[39]).configure(command = lambda: change_num(lista[39],lineas,4,3))
(lista[40]).configure(command = lambda: change_num(lista[40],lineas,4,4))
(lista[41]).configure(command = lambda: change_num(lista[41],lineas,4,5))
(lista[42]).configure(command = lambda: change_num(lista[42],lineas,4,6))
(lista[43]).configure(command = lambda: change_num(lista[43],lineas,4,7))
(lista[44]).configure(command = lambda: change_num(lista[44],lineas,4,8))
(lista[45]).configure(command = lambda: change_num(lista[45],lineas,5,0))
(lista[46]).configure(command = lambda: change_num(lista[46],lineas,5,1))
(lista[47]).configure(command = lambda: change_num(lista[47],lineas,5,2))
(lista[48]).configure(command = lambda: change_num(lista[48],lineas,5,3))
(lista[49]).configure(command = lambda: change_num(lista[49],lineas,5,4))
(lista[50]).configure(command = lambda: change_num(lista[50],lineas,5,5))
(lista[51]).configure(command = lambda: change_num(lista[51],lineas,5,6))
(lista[52]).configure(command = lambda: change_num(lista[52],lineas,5,7))
(lista[53]).configure(command = lambda: change_num(lista[53],lineas,5,8))
(lista[54]).configure(command = lambda: change_num(lista[54],lineas,6,0))
(lista[55]).configure(command = lambda: change_num(lista[55],lineas,6,1))
(lista[56]).configure(command = lambda: change_num(lista[56],lineas,6,2))
(lista[57]).configure(command = lambda: change_num(lista[57],lineas,6,3))
(lista[58]).configure(command = lambda: change_num(lista[58],lineas,6,4))
(lista[59]).configure(command = lambda: change_num(lista[59],lineas,6,5))
(lista[60]).configure(command = lambda: change_num(lista[60],lineas,6,6))
(lista[61]).configure(command = lambda: change_num(lista[61],lineas,6,7))
(lista[62]).configure(command = lambda: change_num(lista[62],lineas,6,8))
(lista[63]).configure(command = lambda: change_num(lista[63],lineas,7,0))
(lista[64]).configure(command = lambda: change_num(lista[64],lineas,7,1))
(lista[65]).configure(command = lambda: change_num(lista[65],lineas,7,2))
(lista[66]).configure(command = lambda: change_num(lista[66],lineas,7,3))
(lista[67]).configure(command = lambda: change_num(lista[67],lineas,7,4))
(lista[68]).configure(command = lambda: change_num(lista[68],lineas,7,5))
(lista[69]).configure(command = lambda: change_num(lista[69],lineas,7,6))
(lista[70]).configure(command = lambda: change_num(lista[70],lineas,7,7))
(lista[71]).configure(command = lambda: change_num(lista[71],lineas,7,8))
(lista[72]).configure(command = lambda: change_num(lista[72],lineas,8,0))
(lista[73]).configure(command = lambda: change_num(lista[73],lineas,8,1))
(lista[74]).configure(command = lambda: change_num(lista[74],lineas,8,2))
(lista[75]).configure(command = lambda: change_num(lista[75],lineas,8,3))
(lista[76]).configure(command = lambda: change_num(lista[76],lineas,8,4))
(lista[77]).configure(command = lambda: change_num(lista[77],lineas,8,5))
(lista[78]).configure(command = lambda: change_num(lista[78],lineas,8,6))
(lista[79]).configure(command = lambda: change_num(lista[79],lineas,8,7))
(lista[80]).configure(command = lambda: change_num(lista[80],lineas,8,8))

c1 = 0 #Contador de fila para la cuadrícula
c2 = 0 #Contador de columna para la cuadrícula
for l in lista:
    if c2 == 9:
        c1 += 1
        c2 = 0
    l.grid(row=c1, column=c2)
    c2 += 1 #Aquí se organizan los botones en una cuadrícula para que se vean ordenados

color = ("sky blue", "snow") #Estos son los los colores que tendrán los botones para que se puedan diferenciar los cuadros
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

    contadores[1] += 1  #En lo anterior, se le asignaron los colores a los botones para que el usuario pueda diferenciar los cuadros del sudoku

for i in lista:
    if i['text'] != 0:
        i["state"] = DISABLED
        i["font"] = font.Font(weight="bold", slant="italic", size=9) #Aquí deshabilita todos los botones que tengan valores ya resueltos

print(tablero)

archivo_mejor_juego=open("Mejor_juego.txt","r")
mejor_juego=int(archivo_mejor_juego.read()) #Aquí se lee el record que hay de intentos

canvas_record= Canvas(sudoku, width= 100, height= 50, bg="#F0F0F0")
canvas_record.create_text(50, 25, text="{0}".format("Mejor juego:\n{0} intento{1}".format((mejor_juego),("s" if mejor_juego!=1 else "")), fill="black", font=('Helvetica 11 bold')) if mejor_juego!=0 else "Sin mejor\n    juego", fill="black", font=('Helvetica 11 bold'))
canvas_record.grid(row=5, column=11) #Aquí se agrega un label a la ventana, este mostrará el mejor resultado que se tenga registrado

archivo_mejor_juego.close()

reset = Button(text="Borrar mejor\njuego", default="active", width=14)
reset.grid(row=7, column=11)
reset.configure(command=lambda: [borrar_intentos(canvas_record)]) #Aquí se crea un botón que borrará el registro de juegos anteriores


canvas_intentos= Canvas(sudoku, width= 100, height= 50, bg="#F0F0F0")
canvas_intentos.create_text(50, 25, text="Intentos: {0}".format(num_intentos), fill="black", font=('Helvetica 11 bold'))
canvas_intentos.grid(row=1, column=11) #Aquí se crea un label que muestra el número de intentos que lleva el usuario

verify = Button(text="Verificar", default="active", width=14)
verify.grid(row=3, column=11)
verify.configure(command=lambda: [deshabilitar(verify),boton_verificar(obtener_colores(lista),lista,tablero,lineas),verify.after(1800, lambda :[restaurar_colores(colores,lista),habilitar(verify)]),acabar_juego(canvas_record)])
#Aquí se crea el boton verificar que muestra si hay errores, si no hay, creará la nueva ventana de felicitaciones al usuario.


sudoku.mainloop()
