# Programacion I - UTN - Tecnicatura Universitaria en Programación
# Trabajo Práctico N5: Listas
# Alumna: Lis Araceli  Lezcano Thomas
# =============================================================================

# -----------------------------------------------------------------------------
# Ejercicio 1
# Crea una lista con los números del 1 al 100 que sean múltiplos de 4
# -----------------------------------------------------------------------------

# Uso la función range para generar los múltiplos de 4 desde el 4 hasta el 100 inclusive.
# range(4, 101, 4) empieza en 4, termina en 100 y va de 4 en 4.
multiplos_de_4 = list(range(4, 101, 4))

# Muestro por pantalla la lista de múltiplos 
print(multiplos_de_4)

# -----------------------------------------------------------------------------
# Ejercicio 2
# Crear una lista con cinco elementos y mostrar el penúltimo
# -----------------------------------------------------------------------------

# Creo una lista con cinco cosas que me gustan (pueden ser lo que quiera)
cosas_que_me_gustan = ["música", "mate", "perros", "viajar", "fotografía"]

# Uso índice negativo [-2] para acceder al penúltimo elemento de la lista
penultimo_elemento = cosas_que_me_gustan[-2]

# Muestro por pantalla el penúltimo elemento
print(penultimo_elemento)

# -----------------------------------------------------------------------------
# Ejercicio 3
# Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante
# -----------------------------------------------------------------------------

# Empiezo creando una lista vacía con corchetes
lista_vacia = []

# Agrego palabras a la lista usando el método append
# Elijo palabras que me representen 
lista_vacia.append("arte")
lista_vacia.append("código")
lista_vacia.append("naturaleza")

# Muestro por pantalla la lista con las tres palabras que agregué
print(lista_vacia)

# -----------------------------------------------------------------------------
# Ejercicio 4
# Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”
# -----------------------------------------------------------------------------

# Lista original 
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazo el segundo valor (índice 1) por "loro"
animales[1] = "loro"

# Reemplazo el último valor usando índice negativo [-1] por "oso"
animales[-1] = "oso"

# Muestro por pantalla la lista modificada
print(animales)

# -----------------------------------------------------------------------------
# Ejercicio 5
# Analizar y explicar qué hace este programa
# -----------------------------------------------------------------------------

# Primero se crea una lista de números.
# Después, con max(numeros), busco el valor más grande dentro de la lista.
# Luego, con remove(), elimino ese número máximo de la lista.
# Finalmente, imprimo la lista sin ese valor.

# En este caso, el número más grande es 22, así que se elimina de la lista.
# El resultado por pantalla va a ser: [8, 15, 3, 7]

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# -----------------------------------------------------------------------------
# Ejercicio 6
# Crear una lista con números del 10 al 30 (incluido), haciendo saltos de 5 en 5
# y mostrar por pantalla los dos primeros elementos
# -----------------------------------------------------------------------------

# Uso range para generar una lista del 10 al 30, saltando de 5 en 5
numeros = list(range(10, 31, 5))

# Muestro los dos primeros elementos usando slicing [0:2]
print(numeros[0:2])

# -----------------------------------------------------------------------------
# Ejercicio 7
# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# -----------------------------------------------------------------------------

# Lista original 
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazo el segundo valor (índice 1) por "civic"
autos[1] = "civic"

# Reemplazo el tercer valor (índice 2) por "focus"
autos[2] = "focus"

# Muestro la lista modificada
print(autos)

# -----------------------------------------------------------------------------
# Ejercicio 8
# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# -----------------------------------------------------------------------------

# Empiezo creando la lista vacía
dobles = []

# Calculo el doble de cada número y lo agrego a la lista con append
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Muestro por pantalla la lista con los valores agregados
print(dobles)

# -----------------------------------------------------------------------------
# Ejercicio 9
# Manipular la lista de listas “compras”
# a) Agregar "jugo" al tercer cliente
# b) Reemplazar "fideos" por "tallarines" en el segundo cliente
# c) Eliminar "pan" del primer cliente
# d) Imprimir la lista resultante
# -----------------------------------------------------------------------------

# Creo la lista de compras con tres sublistas
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agrego "jugo" a la lista del tercer cliente 
compras[2].append("jugo")

# b) Reemplazo "fideos" por "tallarines" en la lista del segundo cliente
# "fideos" está en la posición 1 de esa sublista
compras[1][1] = "tallarines"

# c) Elimino "pan" de la lista del primer cliente
compras[0].remove("pan")

# d) Muestro por pantalla la lista completa después de los cambios
print(compras)

# -----------------------------------------------------------------------------
# Ejercicio 10
# Crear una lista anidada con los siguientes elementos en posiciones específicas
# -----------------------------------------------------------------------------

# Armo la lista anidada con los valores que indica la consigna

# lista_anidada[0] tiene que ser 15
# lista_anidada[1] tiene que ser True
# lista_anidada[2] tiene que ser otra lista con tres números flotantes: 25.5, 57.9, 30.6
# lista_anidada[3] tiene que ser False

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

# Muestro por pantalla la lista completa
print(lista_anidada)