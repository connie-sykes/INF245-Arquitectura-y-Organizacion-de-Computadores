import random
from prettytable import PrettyTable

# ---------------------------------------MAPA --------------------------------
def crear_mapa(size,cantidad_naves):
    '''
    ***
    *size: int, es el tamaño del mapa (size*size)
    *cantidad_naves: int, cantidad de naves a derribar en el mapa
    ***
    La funcion crea una lista de listas que simula una tabla de tamaño de nx2n donde n es el input size y donde en cada sublista
    se agrega una letra X, Y o Z ,en posiciones aleatorias, x cantidad de veces donde x es el input cantidad-naves.
    '''
    listaposnaves = []
    lista = []
    for i in range(0,size*2):
        row = []
        for j in range(0,size):
            row.append('?')
        lista.append(row)

    for i in range(0,cantidad_naves):
        cordx = random.randint(0,2*size-1)
        cordy = random.randint(0,size-1)
        tipo = random.randint(0,2)
        tipos = 'XYZ'
        if lista[cordx][cordy] != '?':
            continue
        else:
            lista[cordx][cordy] = tipos[tipo]
            listaposnaves.append((cordx,cordy))

    return(lista,listaposnaves)

def visualizar_mapa(lista):
    '''
    ***
    *lista: Es una lista de listas donde la sublista contiene variables de tipo strings ya creada con anterioridad.
    ***
    la funcion utiliza funciones de la librearia "PrettyTable" para lograr una visualizacion mas comoda 
    en la terminal de una lista de listas creada anteriormente.
    '''
    tabla = PrettyTable()
    tabla.field_names = [''] + list(range(len(lista[0])))

    for numberfila, row in enumerate(lista):
        row_data = [numberfila] + row
        tabla.add_row(row_data)

    print(tabla)

# CONVERSIÓN DE COORDENADAS A BASE DECIMAL -----------------------------------------------------------
    
def bin2dec(input_x,input_y):
    '''
    ***
    *input_x: int, coordenada x a convertir
    *input_y: int, coordenada y a convertir
    ***
    Itera inversamente el string aplicando el algoritmo del polinomio caracteristico, es decir,
    va sumando acumulativamente el bit(1 o 0) multiplicado por base^posicion respectiva del bit
    '''
    x = 0
    y = 0
    for i in range(len(str(input_x))):
        bit = int(input_x[i])
        x += bit * (2 ** (len(str(input_x)) - 1 - i))

    for j in range(len(str(input_y))):
        bit = int(input_y[j])
        y += bit * (2 ** (len(str(input_y)) - 1 - j))
    
    return x, y

def oct2dec(input_x,input_y):
    '''
    ***
    *input_x: int, coordenada x a convertir
    *input_y: int, coordenada y a convertir
    ***
    Itera inversamente el string aplicando el algoritmo del polinomio caracteristico, es decir,
    va sumando acumulativamente el bit(numero entre 0-7) multiplicado por base^posicion respectiva del bit
    '''
    x = 0
    y = 0
    for i in range(len(str(input_x))):
        bit = int(input_x[i])
        x += bit * (8 ** (len(str(input_x)) - 1 - i))
        
    for j in range(len(str(input_y))):
        bit = int(input_y[j])
        y += bit * (8 ** (len(str(input_y)) - 1 - j))
    return x, y

def hex2dec(input_x,input_y):
    '''
    ***
    *input_x: int, coordenada x a convertir
    *input_y: int, coordenada y a convertir
    ***
    Itera inversamente el string aplicando el algoritmo del polinomio caracteristico, es decir,
    va sumando acumulativamente el bit(numero entre 0-9) multiplicado por base^posicion respectiva del bit,
    pero para el caso de las letras (a-f) se convierten a su numero respectivo (a=10, b=11, etc.)
    '''
    x = 0
    y = 0
    
    for i in range(len(str(input_x))):
        multiplicador = 0
        if input_x[i].lower() == "a":
            multiplicador = 10
        elif input_x[i].lower() == "b":
            multiplicador = 11
        elif input_x[i].lower() == "c":
            multiplicador = 12
        elif input_x[i].lower() == "d":
            multiplicador = 13
        elif input_x[i].lower() == "e":
            multiplicador = 14
        elif input_x[i].lower() == "f":
            multiplicador = 15
        else:
            multiplicador = int(input_x[i])

        x += multiplicador * (16 ** (len(str(input_x)) - 1 - i))

    for j in range(len(str(input_y))):
        multiplicador = 0
        if input_y[j].lower() == "a":
            multiplicador = 10
        elif input_y[j].lower() == "b":
            multiplicador = 11
        elif input_y[j].lower() == "c":
            multiplicador = 12
        elif input_y[j].lower() == "d":
            multiplicador = 13
        elif input_y[j].lower() == "e":
            multiplicador = 14
        elif input_y[j].lower() == "f":
            multiplicador = 15
        else:
            multiplicador = int(input_y[j])

        y += multiplicador * (16 ** (len(str(input_y)) - 1 - j))
    return x, y
#--------------------------------------------------------------------------------------------------------

#///// CHECKEO SI CORRESPONDE A LA BASE //////
def check_bin(input):
    '''
    ***
    *input: string, numero a corroborar su base
    ***
    Verifica que el input este compuesto solamente de 0 y 1, en caso de ser asi retorna True, caso contrario
    retorna False
    '''
    binario = list(input)
    for num in binario:
        if not (num == "1" or num == "0") :
            return False
    return True

def check_hex(input):
    '''
    ***
    *input: string, numero a corroborar su base
    ***
    Verifica que el input este compuesto solamente de digitos [0-9] y/o letras [a-f].
    Si el string comenzaba con un '0x', es removido del string.
    En caso de que el string cumpla esas condiciones retorna True, caso contrario retorna False
    '''
    abc = "abcdefABCDEF"
    dig = "0123456789"
    hexadecimal = list(input)
    if (hexadecimal[0]=="0" and hexadecimal[1]=="x"):   #EVALUA EXISTENCIA 0X
            hexadecimal = hexadecimal[2:len(hexadecimal)]

    for i in hexadecimal:
        if (i not in abc) and (i not in dig):
            return False
    return True

def check_oct(input):
    '''
    ***
    *input: int, numero a corroborar su base
    ***
    Verifica que el input este compuesto solamente de digitos [0-7], 
    en caso de ser asi retorna True, caso contrario
    retorna False
    '''
    base_octal="01234567"
    octal = list(input)
    for num in octal:
        if num not in base_octal:
            return False
    return True

#//////////

def acierto(tupla,tipo,lista1,lista2):
    '''
    ***
    *tupla: Es una tupla de enteros. 
    *tipo: corresponde a un entero entre 1 y 3 que representa el tipo de eleccion tomada.
    *lista1: corresponde a una lista de listas de strings a comparar.
    *lista2: Es una lista de tuplas de tipo entero de que se utilizara de comparacion.
    ***
    Primero verifica el valor del tipo para saber a que letra corresponde, luego utiliza la tupla ingresada "tupla"
    para compararla con "lista2" para reconocer si existe la nave en esa posicion y de ser asi comparara la letra
    del tipo con la letra de la tabla para verificar que si sea un acierto es decir que ambos sean del mismo tipo.
    Finalmente retornara un entero dependiendo de la situacion en la que se encuentre.
    '''
    a="?"
    if tipo== 1:
        a="X"
    elif tipo== 2:
        a="Y"
    elif tipo== 3:
        a="Z"
    if tupla in lista2:
        if a == lista1[tupla[0]][tupla[1]]:           
            return(int(1))
        elif a != lista1[tupla[0]][tupla[1]]:
            return(int(2))
    else:
        return(int(3))

#------------------------------------JUEGO-----------------------------------------------------------

a=int(input("Ingrese el tamaño del CAMPO DE BATALLA"'\n'"->"))
b=int(input("Ingrese la cantidad de ENEMIGOS"'\n'"->"))
coordenada=(0,0)

juego,naves = crear_mapa(a,b)
visualizar_mapa(juego)

# ITERACIÓN PARA JUGAR

while len(naves)!=0:
    
    check_input=False
    while not check_input:
        entrada = input('\n'"¿Que armamento ocuparas esta vez?"'\n'"(1) Binario" '\n'"(2) Octal"'\n'"(3) Hexadecimal"'\n'"->")
        calibre_arma=int(entrada)
        if calibre_arma not in [1,2,3]:
            print('\n'"De ese no me queda, pero hey ¿Has probado estas bellezas? ¡Son bastante eficaces!"'\n')
            visualizar_mapa(juego)
        else:   #Input correcto
            check_input=True

    if calibre_arma == 1:
        print('\n'"¡La vieja confiable! ahora digame... ¿Cuáles son las coordenadas, cap?")
        
        input_x=input('\n'"Ingrese la coordenada x (fila) en binario"'\n'"->")
        while check_bin(input_x)==False:
            print("Oops, esta coordenada no es binaria, intentalo de nuevo")
            input_x=input('\n'"Ingrese la coordenada x (fila) en binario"'\n'"->")

        input_y=input('\n'"Ingrese la coordenada y (columna) en binario"'\n'"->")
        while check_bin(input_y)==False:
            print("Oops, esta coordenada no es binaria, intentalo de nuevo")
            input_y=input('\n'"Ingrese la coordenada y (columna) en binario"'\n'"->")

        coordenada=bin2dec(input_x,input_y)

    elif calibre_arma == 2:
        print('\n'"Nunca entendí porqué el simbolo de infinito, a no espera... ¡¿ES UN 8?! ahora digame... ¿Cuáles son las coordenadas, cap?"'\n')
        input_x=input('\n'"Ingrese la coordenada x (fila) en Octal"'\n'"->")
        while check_oct(input_x)==False:
            print("Oops, esta coordenada no es octal, intentalo de nuevo")
            input_x=input('\n'"Ingrese la coordenada x (fila) en Octal"'\n'"->")
        
        input_y=input('\n'"Ingrese la coordenada y (columna) en Octal"'\n'"->")
        while check_oct(input_y)==False:
            print("Oops, esta coordenada no es octal, intentalo de nuevo")
            input_y=input('\n'"Ingrese la coordenada y (columna) en Octal"'\n'"->")
        
        coordenada=oct2dec(input_x,input_y)

    elif calibre_arma == 3:
        print("¡Genial! ahora digame... ¿Cuales son las coordenadas cap?")
        proceed = False
        while not proceed:

            input_x=input('\n'"Ingrese la coordenada x (fila) en Hexadecimal"'\n'"->")
            while check_hex(input_x)==False:
                print("Oops, esta coordenada no es hexadecimal, intentalo de nuevo")
                input_x=(input('\n'"Ingrese la coordenada x (fila) en Hexadecimal"'\n'"->"))
            xlist= list(input_x)
            if ("x" in input_x):    #Formateo el 0x
                input_x = "".join(xlist[2:len(input_x)])
            
            input_y=input('\n'"Ingrese la coordenada y (columna) en Hexadecimal"'\n'"->")
            while check_hex(input_y)==False:
                print("Oops, esta coordenada no es hexadecimal, intentalo de nuevo")
                input_y=(input('\n'"Ingrese la coordenada y (columna) en Hexadecimal"'\n'"->"))
            ylist= list(input_y)
            if ("x" in input_y):    #Formateo el 0x
                input_y = "".join(ylist[2:len(input_y)])
                            
            proceed == True
        coordenada=hex2dec(input_x,input_y)
    
    golpe=acierto(coordenada,calibre_arma,juego,naves)
    if golpe== 1:       #1 = golpe a barco & bases concuerdan
        print('\n'"Alli va uno menos"'\n')
        naves.remove(coordenada)
        juego[coordenada[0]][coordenada[1]]="?"
    
    elif golpe == 2:    #2 = golpe a barco & bases no concuerdan
        print('\n'"¡¿LO RESISTIO?! tal vez usar otra arma funcione..."'\n')
    
    elif golpe == 3:    #3= ni barco ni base
        print('\n'"¡BUENA TACTICA! definitivamente eso intimidara a los peces, ¿Aunque no estabamos atacando barcos?"'\n')
    
    visualizar_mapa(juego)

if len(naves)==0:
    print("FIN DEL JUEGO!!!")
