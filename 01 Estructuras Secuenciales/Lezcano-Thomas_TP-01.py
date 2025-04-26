# Trabajo Practico Nº1: Teoría de conjuntos, números y sus tipos
# Tecnicatura Universitaria en Programación – UTN
# Alumna: Lis Araceli Lezcano Thomas
# Año: 2025
# =============================================================================

#Ejercicios Resueltos

#1.	Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print(f"Hola Mundo!")

#2.	Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input ("Ingrese su nombre: ")
print(f"Hola {nombre}!")


#3.	Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ")
residencia = input ("Ingrese su residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#4.	Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

pi = 3.14159
radio =float(input("Ingrese el radio del círculo: "))

perimetro = 2*pi+radio
area= pi*radio**2

print(f"El perimetro del círculo es {perimetro} y el area es {area}.")

#5.	Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Ingrese una cantidad de segundos superior a 3600: "))

horas = segundos/3600

print(f"{segundos} segundos equivale a {horas} horas.")

#6.	Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese un numero: "))
uno = numero*1
dos = numero*2
tres = numero*3
cuatro =  numero*4
cinco =  numero*5
seis =  numero*6
siete = numero*7
ocho = numero*8
nueve = numero*9
diez =  numero*10

print (f"La tabla de {numero} es: {numero}x1 = {uno}, {numero}x2 = {dos}, {numero}x3 = {tres}, {numero}x4 = {cuatro},  {numero}x5 = {cinco},  {numero}x6 = {seis},  {numero}x7 = {siete},  {numero}x8 = {ocho},  {numero}x9 = {nueve},  {numero}x10 = {diez}. ")5


#7.	Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numUno = int(input("Ingrese un numero entero distinto del 0: "))
numDos = int(input("Ingrese otro numero entero distinto del 0: "))

suma = numUno + numDos 
resta = numUno - numDos
division = numUno / numDos
multiplicacion = numUno * numDos

print(f"{numUno}+{numDos}={suma}, {numUno}-{numDos}={resta}, {numUno}/{numDos}={division}, {numUno}x{numDos}={multiplicacion}.")

#8.	Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)

print(f"Tu índice de masa corporal es: {imc}")

#9.	Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit

celsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = (celsius * 1.8) + 32
	
print(f"La temperatura en Fahrenheit es de {fahrenheit}")

#10.	Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números. 

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los números es: {promedio}")

