# Programacion I - UTN - Tecnicatura Universitaria en Programación
# Trabajo Práctico N6: Funciones
# Alumna: Lis Araceli  Lezcano Thomas
# =============================================================================

# -----------------------------------------------------------------------------
# Ejercicio 1: Crear una función que imprima “Hola Mundo!” y llamarla desde el programa principal.
# -----------------------------------------------------------------------------

def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

# -----------------------------------------------------------------------------
# Ejercicio 2: Crear una función que reciba un nombre y devuelva un saludo personalizado.
# ------------------------------------------------------------------------------

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
nombre_usuario = input("Ingresá tu nombre: ")
print(saludar_usuario(nombre_usuario))

# ------------------------------------------------------------------------------
# Ejercicio 3: Crear una función que reciba datos personales e imprima un mensaje.
# ------------------------------------------------------------------------------

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# ------------------------------------------------------------------------------
# Ejercicio 4: Crear dos funciones para calcular el área y el perímetro de un círculo.
# ------------------------------------------------------------------------------

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
radio = float(input("Ingresá el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

# ------------------------------------------------------------------------------
# Ejercicio 5: Crear una función que reciba segundos y devuelva la cantidad de horas.
# ------------------------------------------------------------------------------

def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos = int(input("Ingresá la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# ------------------------------------------------------------------------------
# Ejercicio 6: Crear una función que imprima la tabla de multiplicar de un número.
# ------------------------------------------------------------------------------

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
num = int(input("Ingresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)

# ------------------------------------------------------------------------------
# Ejercicio 7: Crear una función que reciba dos números y devuelva una tupla con
# la suma, resta, multiplicación y división.
# ------------------------------------------------------------------------------

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

# Programa principal
a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))

resultados = operaciones_basicas(a, b)
print("Suma:", resultados[0])
print("Resta:", resultados[1])
print("Multiplicación:", resultados[2])
print("División:", resultados[3])

# ------------------------------------------------------------------------------
# Ejercicio 8: Crear una función que calcule el Índice de Masa Corporal (IMC).
# ------------------------------------------------------------------------------

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

# ------------------------------------------------------------------------------
# Ejercicio 9: Crear una función que convierta grados Celsius a Fahrenheit.
# ------------------------------------------------------------------------------

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
celsius = float(input("Ingresá la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# ------------------------------------------------------------------------------
# Ejercicio 10: Crear una función que calcule el promedio de tres números.
# ------------------------------------------------------------------------------

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
n1 = float(input("Ingresá el primer número: "))
n2 = float(input("Ingresá el segundo número: "))
n3 = float(input("Ingresá el tercer número: "))

promedio = calcular_promedio(n1, n2, n3)
print(f"El promedio es: {promedio:.2f}")
