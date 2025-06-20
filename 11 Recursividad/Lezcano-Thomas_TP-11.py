# Programacion I - UTN - Tecnicatura Universitaria en Programación
# Trabajo Práctico N11: Recursividad
# Alumna: Lis Araceli  Lezcano Thomas
# =============================================================================

# ------------------------------------------------------------------------------
# Ejercicio 1: Función recursiva que calcule el factorial de un número.
# ------------------------------------------------------------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Programa principal
limite = int(input("Ingresá un número: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

# ------------------------------------------------------------------------------
# Ejercicio 2: Función recursiva que calcule el valor de Fibonacci en una posición.
# ------------------------------------------------------------------------------
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

# Programa principal
hasta = int(input("¿Hasta qué posición querés ver la serie de Fibonacci? "))
for i in range(hasta + 1):
    print(f"F({i}) = {fibonacci(i)}")

# ------------------------------------------------------------------------------
# Ejercicio 3: Función recursiva que calcule una potencia (n^m).
# ------------------------------------------------------------------------------
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Programa principal
base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

# ------------------------------------------------------------------------------
# Ejercicio 4: Función recursiva que convierte un número decimal a binario.
# ------------------------------------------------------------------------------
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Programa principal
numero = int(input("Ingresá un número entero positivo: "))
if numero == 0:
    print("0")
else:
    print(f"Binario: {decimal_a_binario(numero)}")

# ------------------------------------------------------------------------------
# Ejercicio 5: Función recursiva que determina si una palabra es un palíndromo.
# ------------------------------------------------------------------------------
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Programa principal
texto = input("Ingresá una palabra (sin espacios ni tildes): ").lower()
print("¿Es palíndromo?", es_palindromo(texto))

# ------------------------------------------------------------------------------
# Ejercicio 6: Función recursiva que suma los dígitos de un número.
# ------------------------------------------------------------------------------
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

# Programa principal
numero = int(input("Ingresá un número entero positivo: "))
print(f"Suma de los dígitos: {suma_digitos(numero)}")

# ------------------------------------------------------------------------------
# Ejercicio 7: Función recursiva que cuenta el total de bloques para una pirámide.
# ------------------------------------------------------------------------------
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Programa principal
niveles = int(input("Ingresá la cantidad de bloques en la base de la pirámide: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")

# ------------------------------------------------------------------------------
# Ejercicio 8: Función recursiva que cuenta cuántas veces aparece un dígito.
# ------------------------------------------------------------------------------
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)

# Programa principal
num = int(input("Ingresá un número entero positivo: "))
dig = int(input("Ingresá el dígito a buscar (0-9): "))
print(f"Aparece {contar_digito(num, dig)} veces.")
