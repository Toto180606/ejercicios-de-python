print ("hola mundo")#

variable = "hola mundo"
print (variable)

variablenumero = 3
print (variablenumero)

nprimero = 10
nsegundo = 10
resultado = nprimero + nsegundo
print (resultado)


primern = int (input("elija un numero del 1 al 10: "))
segundon = int (input("elija otro numero del 1 al 10 para sumarlo: "))

resultado = primern + segundon
print (resultado)

def solicitarentero ():
    usuario = int(input("eleji un numero entero para imprimir: "))
    print ( usuario )
solicitarentero()        

def operaciones():
    numero1 = int (input("elija un numero: "))   
    numero2 = int(input("elija otro numero: "))
    suma = numero1 + numero2
    resta = numero1 - numero2
    multuiplicacion = numero1 * numero2
    divicion = numero1 / numero2
    print (f"la suma es {suma}, la resta es {resta}, la multiplicacion es {multuiplicacion} y al divicion es {divicion}")    
operaciones()    

def parimpar ():
    numero = int(input("ingrese un numero y le dire si es par o impar: "))
    if numero % 2 == 0 :
        print (f"El numero {numero} es par")
    else :
        print (f"El numero {numero} es impar")
parimpar()        

def cuantosaños ():
    año_nac = int(input("ingrese el año en el que nacio: "))
    año_ran = int(input("ingrese un año rtandom y te dire que edad tenias es año: "))
    edad = año_ran - año_nac
    print (f"usted tenia {edad} en el año {año_ran}")
resultado_edad = cuantosaños()    

def promedio_numeros ():
    n1 = int(input("elija su primer numero:"))
    n2 = int(input("elija su segundo numero:"))
    n3 = int(input("elija su tercer numero:"))
    n4 = int(input("elija su cuarto numero:"))
    n5 = int(input("elija su quinto numero:"))
    suma_total = n1 + n2 + n3 + n4 + n5 
    prmedio = suma_total / 5 
    print (f"el promedio de los numeros es {prmedio}")
promedio_numeros()    

def n_ant_sig ():
    numero = int (input("elija un numero le dire el siguiente y el anterior: "))
    n_sig = numero + 1 
    n_ant = numero - 1 
    print (f"el numero elejio es {numero}, el siguiente es {n_sig} y el anterior es {n_ant}")
n_ant_sig   ()


def unir_string_ynumero():
    string = input("Ingrese un texto: ")
    numero = int(input("Ingrese un número para sumar al string: "))
    resultado = string + str(numero)  # Convertimos el número a string antes de concatenar
    print(resultado)

unir_string_ynumero()

def resto_cociente (n1, n2):
    cociente = n1 // n2
    resto = n1 % n2 
    print (cociente, resto)
resto_cociente (15, 3 )    

def apellido_nombre ():
    apellido = input ("diagame su apellido: ")
    nombre = input ( " ingrese su nombre: ")
    print (apellido + nombre )
apellido_nombre()    

def apellido_nombre ():
    apellido = input ("diagame su apellido: ")
    nombre = input ( " ingrese su nombre: ")
    print (f"{apellido}, {nombre}")
apellido_nombre()    

def cantidad_letras ():
    texto = str (input("ingrese un texto y te dire la cantidad de letras que tiene: "))
    total_de_caracteres = len (texto)
    print (f"la cantidad de letras que tiene tu texto son {total_de_caracteres}")
cantidad_letras()    

def slicear ():
    palabra = str(input("escriba una palabra solo apareceran 5 caracteres: "))
    palabra_cortada = slice (0, 5)
    print (palabra [palabra_cortada])
slicear()    

def sacar_a ():
    palabra = str(input("ingrese una palabra o texto y le saco todsa las a: "))
    nueva_palabra = palabra.replace ("a", "")
    print (f"su nuevo texto o palabra es {nueva_palabra}")
sacar_a()    



#aca empieza la guia 3


def booleans (a,b):
    if a > b :
        print ("a es mayor a b ")
    elif a == b :
        print ("a es igual a b")
    else :
        print ("a es menor a b ")
booleans (10, 10)       

# def vocales (palabra) :
#     if  len (palabra) == 1 and in "aeiou":
#         print ("es una vocal")
#     else :
#         print ("no es una vocal")  
# vocales ("g")               

def par_o_no (numero):
    if numero < 10 and numero % 2 == 0 :
        print ("el numero es par y menor a 10")
    elif numero < 10 and numero % 2 != 0 :
        print ("el numero es impar y menor a 10")
    elif numero > 10 :
        print ("el numero es mayor a 10, elija uno menor") 
    else:
        print("no es un numero")       
par_o_no(8)            

def valor_absoluto (numero):
    if numero > 0 :
        print (numero)
    elif numero < 0 :
            nuevo_numero = numero * -1 
            print (nuevo_numero)
valor_absoluto (4)        

#version mas eficiente  
def absoluto (numero):
    return abs(numero)
print (absoluto (-4))    

def juego_piedra_papel_tijera ():
    usuario = str(input("¡Juguemos! Ingresá piedra ( R), papel (P) o tijera (T): "))
    if usuario == "R" :
        print ("papel, te ganee asjdasjd")
    elif usuario == "P":
        print ("tijera, te gane jdasjdajsd muerto")
    elif usuario == "T":
        print ("piedra, te ganer JASDJASDJAasAJSFAJSDGS")
    else :
        print ("no valae poner cualquir cosa")
juego_piedra_papel_tijera ()                   

def suma_da_100 (n1, n2 ):
    suma = n1 + n2 
    if suma < 100 :
        suma_menor_a_100 = 100 - suma
        print (f"la cuenta es menor a 100, le falta {suma_menor_a_100}")
    elif suma == 100 :
        print ("la suma da 100 exacto ")
    else :
        print ("la suma da mas de 100")    
suma_da_100(40, 20)        

def suma_da_100 (n1, n2 ):
     suma = n1 + n2 
     limite_usuario = int (input ("ingrese un numero para que sea el limite: "))
     if suma < limite_usuario :
         suma_menor_a_usuario = limite_usuario - suma
         print (F"la cuenta es menor a {limite_usuario}, le falta {suma_menor_a_usuario} ")
     elif suma == limite_usuario :
        print (f"da justo {limite_usuario}")    
     else :
        print ("la suma supera tu limite")   
suma_da_100( 40, 20)        

def estaciones ():
    usuario = str (input("ingrese una estacion con su respectiva letra V, I , P , O : ")).upper()
    if usuario == "V":
        print ("elejiste verano , muy bueno ")
    elif usuario == "I":
        print ("elejiste invireno, mi favorita")
    elif usuario == "O":
        print ("elejite otoño, muy buena eleccion")
    elif usuario == "P":
        print ("elejiste primavera, hermosas las flores")
    else:
        print ("error")   
estaciones()     


def aprender_contar ():
    chicos = int(input("elija un numero y te ditre todos los anteriores: "))
    for i in range (chicos -1,0, -1):
            print(i)          
aprender_contar()            

def tablas (numero):
    for i in range (1,11) :
        print (f"{numero} * {i} = {numero * i }")
tablas (2)        

def feliz_cumpleaños ():
    entero = int (input("ingrese la cantidad de veces que quiere que le cantemos faliz cumple: "))
    nombre = str(input("cual es tu nombre campeon?: "))
    for i in range(0,entero,):
        print (f"feliz cumpleaños {nombre}")
feliz_cumpleaños()        

def pagar_deuda():
    deuda = float(input("Ingresá el monto de la deuda: "))
    while deuda > 0:  
        pago = float(input(f"Debés ${deuda:.2f}. Ingresá un pago: "))
        if pago > deuda:  
            print(f"Pago demasiado alto. Te sobraron ${pago - deuda:.2f}.")
            deuda = 0  
        elif pago <= 0:  
            print("El pago debe ser un número positivo.")
        else:
            deuda -= pago  
            print(f"Pago registrado. Deuda restante: ${deuda:.2f}")
    print("¡Felicidades! Pagaste toda la deuda.")
pagar_deuda()


def par_impar ():
    for i in range (0,21):
        if i % 2 == 0 :
            print (f"el numero {i} es par")
        else :
            print (f"el numero {i} es impar ")
par_impar()                


def juego_fichas (n_fichas):
    fichas_ingresadas = 0 
    while fichas_ingresadas < n_fichas :
        print (f"ingresa {n_fichas} para comenzar")
        letra = input ().upper()
        if letra == "F" :
            fichas_ingresadas += 1
    print ("a jugar")
juego_fichas(3)             

def numeros_primos (numero):
    for n in range (2,numero + 1):
        es_primo = True
        for i in range (2, int(n**0.5)+1):
            if n % i == 0:
                es_primo = False 
                break
        if es_primo :
            print (n)
numero = int(input("ingresa un numero: "))
numeros_primos (numero)                




#aca empieza la semana 4 :)

list = (1,2,3,4,5,6,7,8,9,10)
print (list[4])

list = [1,2,3,4,5,6,7,8,9,10]
print (len(list))


list = [4,7,0,2,8,3,9,5,1,6]
print (min(list))
print (max(list))


list = [4,7,0,2,8,3,9,5,1,6]
list.sort()
print (list)

tuple = ("tomas", 18 )
print (tuple[1])

nombres = ["tomas","jazchu","santi","edu","suki"]
nombres.pop(-1)
nombres.append ("juan")
print (nombres)

#otra manera
nombres =  ["tomas","jazchu","santi","edu","suki"]
nombres[-1] = "juan"
print (nombres)

nombres =  ["tomas","jazchu","santi","edu","suki"]
print (nombres[-2])

nombres =  ["tomas","jazchu","santi","edu","suki"]
for i in nombres :
    print (i)

nombres =  ["tomas","jazchu","santi","edu","suki"]
nombres_3 = nombres * 3
print (nombres_3)

n_1 = ("tomas", 18)
n_2 = ("jazmin", 19)
n_3 = ("santi", 18)
n_4 = ("juan", 19)
n_5 = ("suki", 10)

n_uno = list (n_1)
n_dos = list (n_2)
n_trs = list (n_3)
n_cuatro = list (n_4)
n_cinto = list (n_5)

n_1 = ("tomas", 18)
n_2 = ("jazmin", 19)
n_3 = ("santi", 18)
n_4 = ("juan", 19)
n_5 = ("suki", 10)
personas = [n_1, n_2, n_3, n_4, n_5 ]
print (personas)


def paises_lista (paises) :
    for pais in paises :
        print(f"País: {pais[0]} / Capital: {pais[1]} / Continente: {pais[2]}")
pais_1 = ("Francia", "París", "Europa")
pais_2 = ("Argentina", "Buenos Aires", "América del Sur")
pais_3 = ("Japón", "Tokio", "Asia")
pais_4 = ("Alemania", "Berlín", "Europa")
pais_5 = ("Perú", "Lima", "América del Sur")
paises = [pais_1, pais_2, pais_3, pais_4, pais_5]
paises_lista(paises)

from collections import Counter

libros = ["El principito", "It", "Sherlock Holmes", "It", "El principito", "It"]

# Contamos los libros
conteo_libros = Counter(libros)

# Imprimimos la cantidad de ejemplares de cada libro
for libro, cantidad in conteo_libros.items():
    print(f'"{libro}": {cantidad} ejemplares')

list = [1,2,3,4,5,6,7,8,9,10]
numeros_cuadrado = []
for i in list :
    numeros_cuadrado.append (i**2)
print (numeros_cuadrado)

def unir_palabras_invertidas(lista):
    lista_invertida = lista[::-1]  # Invertimos la lista
    frase = " ".join(lista_invertida)  # Unimos las palabras con un espacio
    return frase
palabras = [
    "entender", "pueden", "humanos", "los", "que", "código",
    "escriben", "programadores", "buenos", "Los", "entiende.",
    "computadora", "una", "que", "código", "escribe", "tonto", "Cualquier"
]   

resultado = unir_palabras_invertidas(palabras)
print(resultado)

def materias_guardadas ():
    lista = []
    while True:
        usuario = str (input("ingrese la materia que quieres agregar: ")).upper ()
        if usuario.lower() != "x":
            lista.append (usuario)
            print (lista)   
        else :
            print (f"la lisa final es {lista}")
            break         
materias_guardadas()

def lista_compras ():
    compra_1 = ("cebolla", 100)
    compra_2 = ("preservativos", 1600)
    lista = [compra_1, compra_2]
    precio_total = lista [0][1] + lista [1][1]
    print (f"el precio de tu compra es {precio_total}")
lista_compras()    

def parte_b ():
    compra_1 = ("cebolla", 100)
    compra_2 = ("preservativos", 1600)
    lista_1 = [compra_1, compra_2]
    compra_3 = ("comida", 900)
    compra_4 = ("toallitas", 200)
    lista_2 = [compra_3, compra_4]
    precio_total = lista_1 [0][1] + lista_1 [1][1] + lista_2 [0][1] + lista_2 [1][1]
    print (precio_total)
parte_b()    

def vocales_solo (string):
    vocales = "aeiouAEIOU"
    resultado = ""
    for letra in string:
        if letra and letra not in vocales:
            resultado += letra
    print (resultado)       
vocales_solo ("hola como estas")  

def invertir_string (string):
    print (string [::-1])
invertir_string ("caca")    


def sub_string (string): #campeones del mundo-2022
    sub_str = string[:20]
    print (sub_str)
sub_string ("campeones del mundo-2022")   

lista_ingredientes = ["queso", "oregano", "huevo", "carne"]

while True:
    usuario = str(input("Ingrese el ingrediente que quieres agregar (o 'x' para salir): "))
    
    if usuario == "x":  # Si el usuario ingresa 'x', se termina el bucle
        break
    elif usuario not in lista_ingredientes:  # Si el ingrediente no está en la lista
        lista_ingredientes.append(usuario)
        print(f"La lista queda: {lista_ingredientes}")
    else:  # Si el ingrediente ya está en la lista
        print(f"Eso ya está, la lista queda: {lista_ingredientes}")


def instertar_entero (cartas):
    usuario = int (input ("ingrese la carta que quiera agregar al maso: "))
    cartas.append(usuario)
    cartas.sort ()
    print(f"el maso de cartas te queda {cartas}") 
instertar_entero ([1,2,3,4,5,6,9])

empanadas = ["carne", "JYQ", "choclo", "verdura y queso", "burger"]
print (F"tenes {len (empanadas)} para elejir, las opcioens son {empanadas}")

def tareas_pares (numeros):
    nueva_lista = []
    for i in numeros :
        if i % 2 == 0 :
            nueva_lista.append (i)
    print (nueva_lista)
tareas_pares([1,2,3,4,5,6,7,8,9,10])                



invitados_persona1 = ("Juan", "María", "Carlos", "Lucía")
invitados_persona2 = ("Pedro", "Lucía", "Ana", "María")

# Unimos las tuplas en una sola lista final (con posibles duplicados)
lista_invitados = invitados_persona1 + invitados_persona2
def eliminar_tuplas (tupla_invitados, nombre):
    
    lista_invitados = list(tupla_invitados)
    if nombre in lista_invitados:
        lista_invitados.remove (nombre)
        print(f"{nombre} canceló su asistencia.")
    else:
        print(f"{nombre} no estaba en la lista.")
    nueva_tupla = tuple(lista_invitados)
    return nueva_tupla   
lista_invitados = invitados_persona1 + invitados_persona2
lista_invitados = eliminar_tuplas(lista_invitados, "Juan")

print(f"Lista final de invitados: {lista_invitados}") 


def conmina (impar,par):
    for i in range (len(par)):
        impar.insert(i*2+1,par[i])
    return (impar)
impar = [1,3,5]
par =[2,4,6]
total = conmina (impar,par)
print (total)    

def caca (par):
    for i in range (len(par)):
        print (i)
caca ([1,2,3,4,5,6])        


def palabras ():
    letra = str(input("ingrese una letra: ")).lower()
    if letra in "A" or "a" or "B" or "b":
        print ("es vocal")
    else :
        print ("no es vocal")
palabras ()            


def convierte(t):
    term='able'
    return (t[:len(t)-1]+term).upper()


verbos=['lamento','RAZONO','SELecciona','almaCENA']
adjetivos=list(map(convierte,verbos))
print(adjetivos)

for vueltas in range (14,7,-2):
    print (vueltas)


def cobrar():
    monto = float(input("Ingrese su monto: "))
    acumulado = 0  # Variable para acumular los pagos
    while acumulado < monto:
        pago = float(input("Ingrese un monto a pagar: "))
        if pago <= 0:
            print("Ingresa un monto válido.")
        else:
            acumulado += pago
            if acumulado >= monto:
                resto = acumulado - monto
                print(f"¡Felicidades, pagaste! Tu vuelto es {resto}")
            else:
                falta = monto - acumulado
                print(f"Falta pagar {falta}")

cobrar()
