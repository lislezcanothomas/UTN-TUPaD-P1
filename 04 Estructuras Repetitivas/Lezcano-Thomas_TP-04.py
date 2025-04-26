# Trabajo Práctico N°04 – Estructuras Repetitivas
# Tecnicatura Universitaria en Programación – UTN
# Alumna: Lis Araceli Lezcano Thomas
# Año: 2025
# =============================================================================
# Ejercicio 1
print("\nEjercicio 1:")
# Imprimo los números del 0 al 100 inclusive
for i in range(0, 101):
    print(i)

# Ejercicio 2
print("\nEjercicio 2:")
# Solicito un número entero al usuario
numero = int(input("Ingrese un número entero: "))
# Imprimo la cantidad de dígitos del número ingresado
print("Cantidad de dígitos:", len(str(abs(numero))))

# Ejercicio 3
print("\nEjercicio 3:")
# Solicito el primer número al usuario
a = int(input("Ingrese el primer número: "))
# Solicito el segundo número al usuario
b = int(input("Ingrese el segundo número: "))

# Inicializo la suma en 0
suma = 0
# Sumo los números entre el menor y el mayor, excluyéndolos
for i in range(min(a, b) + 1, max(a, b)):
    suma += i
# Imprimo la suma calculada
print("La suma de los números comprendidos es:", suma)

# Ejercicio 4
print("\nEjercicio 4:")
# Inicializo el total acumulado en 0
total = 0
while True:
    # Solicito un número al usuario
    num = int(input("Ingrese un número (0 para terminar): "))
    # Verifico si el número ingresado es 0 para finalizar
    if num == 0:
        break
    # Sumo el número ingresado al total
    total += num
# Imprimo el total acumulado
print("Total acumulado:", total)

# Ejercicio 5
import random
print("\nEjercicio 5:")
# Genero un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)
# Inicializo el contador de intentos
intentos = 0

while True:
    # Solicito al usuario que adivine el número
    intento = int(input("Adivine el número (0-9): "))
    # Incremento el contador de intentos
    intentos += 1
    # Verifico si el usuario adivinó
    if intento == numero_secreto:
        # Imprimo mensaje de acierto e intentos
        print(f"Correcto! Acertó en {intentos} intentos.")
        break

# Ejercicio 6
print("\nEjercicio 6:")
# Imprimo todos los números pares desde 100 hasta 0 en orden decreciente
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# Ejercicio 7
print("\nEjercicio 7:")
# Solicito un número entero positivo
limite = int(input("Ingrese un número entero positivo: "))

# Inicializo la suma total en 0
suma_total = 0
# Sumo todos los números desde 0 hasta el límite inclusive
for i in range(0, limite + 1):
    suma_total += i
# Imprimo la suma total
print("La suma es:", suma_total)

# Ejercicio 8
print("\nEjercicio 8:")
# Defino la cantidad de números a ingresar
CANTIDAD = 100
# Inicializo contadores
pares = impares = positivos = negativos = 0

for _ in range(CANTIDAD):
    # Solicito un número al usuario
    numero = int(input("Ingrese un número entero: "))
    # Verifico si es par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    # Verifico si es positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Imprimo los resultados
print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

# Ejercicio 9
print("\nEjercicio 9:")
# Inicializo la suma de números
suma_numeros = 0

for _ in range(CANTIDAD):
    # Solicito un número al usuario
    numero = int(input("Ingrese un número entero: "))
    # Acumulo la suma de los números
    suma_numeros += numero

# Calculo la media
media = suma_numeros / CANTIDAD
# Imprimo la media
print("La media es:", media)

# Ejercicio 10
print("\nEjercicio 10:")
# Solicito un número entero al usuario
numero = int(input("Ingrese un número entero: "))
# Invierto los dígitos del número
numero_invertido = int(str(abs(numero))[::-1])
# Verifico si el número era negativo para conservar el signo
if numero < 0:
    numero_invertido = -numero_invertido
# Imprimo el número invertido
print("Número invertido:", numero_invertido)