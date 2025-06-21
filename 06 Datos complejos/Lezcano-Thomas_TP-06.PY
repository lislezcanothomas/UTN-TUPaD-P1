# Programacion I - UTN - Tecnicatura Universitaria en Programación
# Trabajo Práctico N6: Estructuras de datos complejas
# Alumna: Lis Araceli  Lezcano Thomas
# =============================================================================

# -----------------------------------------------------------------------------
# Ejercicio 1: Añadir frutas al diccionario precios_frutas.
# -----------------------------------------------------------------------------
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# -----------------------------------------------------------------------------
# Ejercicio 2: Actualizar los precios de algunas frutas en precios_frutas.
# -----------------------------------------------------------------------------
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# -----------------------------------------------------------------------------
# Ejercicio 3: Crear una lista con solo los nombres de las frutas.
# -----------------------------------------------------------------------------
solo_frutas = list(precios_frutas.keys())
print(solo_frutas)


# -----------------------------------------------------------------------------
# Ejercicio 4: Agenda de contactos con 5 nombres y consulta por nombre.
# -----------------------------------------------------------------------------
agenda = {}
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input("Ingresá su número de teléfono: ")
    agenda[nombre] = numero

consulta = input("¿Qué contacto querés consultar?: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Contacto no encontrado.")


# -----------------------------------------------------------------------------
# Ejercicio 5: Contar palabras únicas y su frecuencia en una frase ingresada.
# -----------------------------------------------------------------------------
frase = input("Ingresá una frase: ")
palabras = frase.lower().split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Frecuencia de palabras:", contador)

# -----------------------------------------------------------------------------
# Ejercicio 6: Promedio de 3 notas para cada uno de 3 alumnos.
# -----------------------------------------------------------------------------
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingresá la nota {j+1} de {nombre}: ")) for j in range(3))
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")

# -----------------------------------------------------------------------------
# Ejercicio 7: Operaciones con sets de estudiantes que aprobaron dos parciales.
# -----------------------------------------------------------------------------
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# -----------------------------------------------------------------------------
# Ejercicio 8: Manejo de stock de productos con un diccionario.
# -----------------------------------------------------------------------------
stock = {'Yerba': 10, 'Azúcar': 5}

producto = input("¿Qué producto querés consultar?: ")
if producto in stock:
    print(f"Hay {stock[producto]} unidades de {producto}.")
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input(f"{producto} no existe. ¿Cuántas unidades querés agregar?: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# -----------------------------------------------------------------------------
# Ejercicio 9: Agenda de eventos donde las claves son tuplas (día, hora).
# -----------------------------------------------------------------------------
agenda = {("Lunes", "10:00"): "Reunión", ("Martes", "14:00"): "Gimnasio"}

dia = input("Ingresá el día: ")
hora = input("Ingresá la hora (hh:mm): ")
clave = (dia, hora)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividad registrada en ese horario.")

# -----------------------------------------------------------------------------
# Ejercicio 10: Invertir un diccionario de países y capitales.
# -----------------------------------------------------------------------------
paises = {'Argentina': 'Buenos Aires', 'Francia': 'París', 'Italia': 'Roma'}
capitales = {capital: pais for pais, capital in paises.items()}
print(capitales)
