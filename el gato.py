# -*- coding: utf-8 -*-
#Autor: Juan Francisco Martinez Paredes
#Fecha: 22 de Noviembre del año 2015
#Descripción: este programa consiste en el "juego del gato", en donde dos jugadores compiten para ganar.
#Abstracción.

 #while(hayJugada and not hayGanador):
     #x=pedirFila()
     #y=pedirColumna()
     #JugadorJugando=turno%2
     #hayGanador=chequear(ganador)
     #turno=turno+1

#Crear Funcion: funcion que pide al jugador la posicion en la cual desea hacer una jugada.
def hacerJugada(gato,jugador): #Esta funcion se utiliza dentro de otra que entrega el jugador respectivo.
        i=int(input("Ingrese la fila: "))
        i=i-1
        if 0<=i<3:
            j=int(input("Ingrese la columna: "))
            j=j-1
            if 0<=j<3:
                j=j
            else:
                j=int(input("Ingrese un valor entero entre 1 y 3: "))
                while j!=1 and j!=2 and j!=3:
                    j=int(input("Vuelva a intentar (valor entero entre 1 y 3): "))
                j=j-1
        else:
            i=int(input("Ingrese un valor entero entre 1 y 3: "))
            while i!=1 and i!=2 and i!=3:
                i=int(input("Vuelva a intentar (valor entero entre 1 y 3): "))
            i=i-1
            j=int(input("Ingrese la columna: "))
            j=j-1
            if 0<=j<3:
                j=j
            else:
                j=int(input("Ingrese un valor entero entre 1 y 3: "))
                while j!=1 and j!=2 and j!=3:
                    j=int(input("Vuelva a intentar (valor entero entre 1 y 3): "))
                j=j-1
        if gato[i][j]!=0 and gato[i][j]!=1:
            print(f"Su posicion es: fila {str(i+1)} y columna {str(j+1)}")
            if jugador==1:
                gato[i][j]=1
                print("Se añadirá un 1 en la posicion seleccionada")
            else:
                if jugador==2:
                    gato[i][j]=0
                    print("Se añadirá un 0 en la posicion seleccionada")
        else:
            while gato[i][j]==0 or gato[i][j]==1:
                print("La posicion ya fue ocupada, intente con otra: ")
                i=int(input("Ingrese la fila: "))
                i=i-1
                if 0<=i<3:
                    j=int(input("Ingrese la columna: "))
                    j=j-1
                    if 0<=j<3:
                        j=j
                    else:
                        j=int(input("Ingrese un valor entero entre 1 y 3: "))
                        while j!=1 and j!=2 and j!=3:
                            j=int(input("Vuelva a intentar (valor entero entre 1 y 3): "))
                        j=j-1
                else:
                    i=int(input("Ingrese un valor entero entre 1 y 3: "))
                    while i!=1 and i!=2 and i!=3:
                        i=int(input("Vuelva a intentar (valor entero entre 1 y 3): "))
                    i=i-1
                    j=int(input("Ingrese la columna: "))
                    j=j-1
                    if 0<=j<3:
                        j=j
                    else:
                        j=int(input("Ingrese un valor entero entre 1 y 3: "))
                        while j!=1 and j!=2 and j!=3:
                            j=int(input("Vuelva a intentar (valor entero entre 1 y 3): "))
                        j=j-1
            if jugador==1:
                gato[i][j]=1
                print("Se añadirá un 1 en la posicion seleccionada")
            elif jugador==2:
                gato[i][j]=0
                print("Se añadirá un 0 en la posicion seleccionada")
        return(gato)

#Crear Funcion: funcion que imprime en pantalla la matriz en orden que se asemeja al juego.
def printGato(gato):
    i=0
    print("El tablero continua de la siguiente forma: ")
    while i<3:
        print(str(gato[i][0])+"|"+str(gato[i][1])+"|"+str(gato[i][2]))
        i=i+1

#Crear Funcion: funcion que imprime en pantalla, para el instructivo, la matriz en orden que se asemeja al juego.
gato=[['_','_','_'],['_','_','_'],[' ',' ',' ']]
def printGatoMuestra(gato):
    i=0
    while i<3:
        print(f"Fila {i+1}==>{str(gato[i][0])}|{str(gato[i][1])}|{str(gato[i][2])}")
        i=i+1

#Crear Funcion: funcion que define si existe o no un ganador.
def hayGanador(gato):
    if ((gato[0][0]==1 and gato[0][1]==1 and gato[0][2]==1)or\
        (gato[1][0]==1 and gato[1][1]==1 and gato[1][2]==1)or\
        (gato[2][0]==1 and gato[2][1]==1 and gato[2][2]==1)or\
        (gato[0][0]==1 and gato[1][0]==1 and gato[2][0]==1)or\
        (gato[0][1]==1 and gato[1][1]==1 and gato[2][1]==1)or\
        (gato[0][2]==1 and gato[1][2]==1 and gato[2][2]==1)or\
        (gato[0][0]==1 and gato[1][1]==1 and gato[2][2]==1)or\
        (gato[0][2]==1 and gato[1][1]==1 and gato[2][0]==1)):
        ganador=1
    elif ((gato[0][0]==0 and gato[0][1]==0 and gato[0][2]==0)or\
          (gato[1][0]==0 and gato[1][1]==0 and gato[1][2]==0)or\
          (gato[2][0]==0 and gato[2][1]==0 and gato[2][2]==0)or\
          (gato[0][0]==0 and gato[1][0]==0 and gato[2][0]==0)or\
          (gato[0][1]==0 and gato[1][1]==0 and gato[2][1]==0)or\
          (gato[0][2]==0 and gato[1][2]==0 and gato[2][2]==0)or\
          (gato[0][0]==0 and gato[1][1]==0 and gato[2][2]==0)or\
          (gato[0][2]==0 and gato[1][1]==0 and gato[2][0]==0)):
        ganador=2
    else:
        ganador=0
    return(ganador)

#Crear Funcion: funcion que dicta el turno de jugador.
def turnar(turno):
    ganador=0
    while turno<10 and ganador==0:
        if turno%2==1:
            jugador=1
        else:
            jugador=2
        print(f"Es el turno del jugador {jugador}")
        hacerJugada(gato,jugador)
        printGato(gato)
        turno=turno+1
        ganador=hayGanador(gato)
    if ganador==1:
        print("El ganador es el jugador 1")
    elif ganador==2:
        print("El ganador es el jugador 2")
    else:
        print("Es un empate")

#Intructivo
print("Bienvenido al juego del GATO")
print("Creado por Franz Martinz Entertainment Company (MR)")
print("---INSTRUCCIONES---")
print("-El juego consiste en rellenar un tablero vacio con unos(1) para el jugador uno o ceros(0) para el jugador 2.")
print("-Debe presionar la tecla Enter despues de ingresar cada dato.")
print("-El jugador que logre completar una linea recta o diagonal dentro del tablero con sus signos... GANA.")
print("-Cada jugador solo debe rellenar con sus signos en los espacios vacios del tablero.")
print("-Las lineas horizontales, las llamaremos filas mientras que las verticales seran las columnas.")
print("Este es el tablero vacio: ")
printGatoMuestra(gato)
print("-Cada espacio esta separado por una barra(|) con el anterior.")
print("-Tanto filas como columnas se enumeran desde el 1 hasta el 3.")
print("Advertencia: Si en los valores ingresa un numero racional (por ejemplo: 3.14), solo se contara la parte entera (en este caso: 3).")
#Proceso, Input, Salida.
n=int(input("¿Desea jugar?(1 para Si, 2 para No): "))
while(n!=1 and n!=2):
    n=int(input("Ingrese una opcion valida: "))
while(n==1):
    gato=[['_','_','_'],['_','_','_'],[' ',' ',' ']]
    turno=1
    print("¡Buena Suerte!")
    jugar=turnar(turno)
    n=int(input("Desea volver a jugar?(1 para Si, 2 para No): "))
    if n==2:
        print("Gracias por jugar.")
    elif n!=1 and n!=2:
        n=input("Ingrese una opcion valida: ")
if n==2:
    print("Adios.")

#Fin.

    




        

