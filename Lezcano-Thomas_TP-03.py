# Trabajo Práctico N°03 – Estructuras Secuenciales
# Tecnicatura Universitaria en Programación – UTN
# Alumna: Lis Araceli Lezcano Thomas
# Año: 2025

# Ejercicio 1 Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# Solicita su edad
edad = int(input("Ingrese su edad: "))
#  Evalua si es mayor de edad
if edad >= 18:
    print("Es mayor de edad")


# Ejercicio 2 Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

# Solicita su nota 
nota = int(input("Ingrese su nota: "))
# Evalúa si la nota esta aprobada o desaprobada
if nota >= 6:
    print("Aprobado")
else:
    print ("Desaprobado")

# Ejercicio 3 Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

#   Solicita numero
numero = int((input("Ingrese un número: ")))
# Evalúa si el numero es par o impar usando modulo
if numero % 2 == 0:
    print("Ingresaste un número par")
else:
    print("Por favor, ingrese un número par")

# Ejercicio 4 Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las categorías pertenece:

#   Solicita su edad
edad = int(input("Ingrese su edad: "))
#   Evalua a que categoria pertenece
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Ejercicio 5 Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

# Solicita su contraseña
contraseña = input("Ingrese su contraseña: ")
# Obtiene longitud
longitud = len(contraseña)
# Verifica si la contraseña 
if 8 <= longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#  Ejercicio 6 Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Importa las funciones
import random
from statistics import mode, median, mean
# Define la lista numeros_aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Calcula y guarda en variables
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
# Compara los valores 
if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")

# Ejercicio 7  Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Solicita una frase o palabra
frase = input("ingrese una frase o palabra")
# Define vocales 
vocales = "aeiouAEIOU"
# Verifica el ultimo caracter y si es vocal concatena "!"
if frase[-1] in vocales:
    frase += "!"
print(frase)

#Ejercicio 8 Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO., 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro., 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.

# Solicita su nombre y la opcion 
nombre = input("Ingrese su nombre")
opcion = input("Elige 1 (MAYÚSCULA), 2 (minúscula) o 3 (Título): ")
# Evalua las opciones
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida")


# Ejercicio 9 Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla

# Solicitud de la magnitud de un terremoro 

magnitud = float(input("Ingrese la magnitud de un terremoto"))

# Evalua la magnitud

if magnitud < 3:
    print("Muy leve")
elif magnitud >=3 and magnitud < 4:
    print("Leve")
elif magnitud >=4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")
else:
    print ("Extremo") 


# Ejercicio 10 Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# Solicita hemisferio, mes y día
hemisferio = input("¿Estás en el hemisferio Norte (N) o Sur (S)? ")
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día (1-31): "))

# Determina la estación
if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
    if hemisferio == "N":
        print("Invierno")
    else:
        print("Verano")
elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
    if hemisferio == "N":
        print("Primavera")
    else:
        print("Otoño")
elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
    if hemisferio == "N":
        print("Verano")
    else:
        print("Invierno")
elif (mes == 9 and dia >= 21) or (mes <= 12 and dia <= 20):
    if hemisferio == "N":
        print("Otoño")
    else:
        print("Primavera")
else:
    print("Fecha inválida")

