"""
Bucle for basico

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

La funcion range() 

Esta limita el numero de iteraciones hasta llegar a un rango especificado.

for i in range(stop):
    # Código a ejecutar

for i in range(5):
    print(i)

La funcion range() funciona con tres parametros: start, stop y step, en donde start es el valor inicial, stop es el valor final (no incluido) y step es el incremento entre cada iteracion.

# Números del 3 al 7
for i in range(3, 8):
    print(i, end=" ")  # 3 4 5 6 7

print()  # Salto de línea

# Números pares del 2 al 10
for i in range(2, 11, 2):
    print(i, end=" ")  # 2 4 6 8 10

print()  # Salto de línea

# Cuenta regresiva
for i in range(10, 0, -1):
    print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1

Iterando sobre indices

nombres = ["Ana", "Carlos", "Elena"]
for i in range(len(nombres)):
    print(f"Posición {i}: {nombres[i]}")

alternativa con enumerate()

nombres = ["Ana", "Carlos", "Elena"]
for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: {nombre}")

iterando sobre cadenas

mensaje = "Python"
for letra in mensaje:
    print(letra)

iterando sobre diccionarios

usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

# Iterando sobre claves
for clave in usuario:
    print(f"Clave: {clave}, Valor: {usuario[clave]}")

compresiones de listas
# Crear una lista con los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]

# Filtrar elementos usando una condición
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

bucles anidados

# Crear una matriz de multiplicación 3x3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}", end="\t")
    print()  # Salto de línea después de cada fila

casos practicos
calcular la suma de los primeros n números naturales
n = 10
suma = 0
for i in range(1, n+1):
    suma += i
print(f"La suma de los primeros {n} números es: {suma}")  # 55

encontrar numeros primos en un rango dado

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primos = []
for num in range(2, 20):
    if es_primo(num):
        primos.append(num)

print(f"Números primos entre 2 y 19: {primos}")  # [2, 3, 5, 7, 11, 13, 17, 19]

procesamiento de datos

temperaturas = [22, 19, 24, 25, 21, 23, 20]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Encontrar el día más caluroso
max_temp = max(temperaturas)
indice_max = temperaturas.index(max_temp)
print(f"El día más caluroso fue {dias[indice_max]} con {max_temp}°C")

# Calcular la temperatura promedio
promedio = sum(temperaturas) / len(temperaturas)
print(f"Temperatura promedio: {promedio:.1f}°C")

# Días con temperatura superior al promedio
for i in range(len(dias)):
    if temperaturas[i] > promedio:
        print(f"{dias[i]}: {temperaturas[i]}°C (por encima del promedio)")

bucle while

contador = 1
while contador <= 5:
    print(contador)
    contador += 1


entrada = ""
while not entrada.isdigit():
    entrada = input("Introduce un número: ")

print(f"Has introducido el número: {entrada}")

bucles controlados por eventos

Un uso comun de while es esperar a que ocurra un evento, como la entrada del usuario.

import random

objetivo = random.randint(1, 10)
intentos = 0
adivinado = False

while not adivinado and intentos < 3:
    intentos += 1
    numero = int(input(f"Intento {intentos}/3: Adivina un número del 1 al 10: "))

    if numero == objetivo:
        print(f"¡Correcto! Has adivinado en {intentos} intentos.")
        adivinado = True
    else:
        pista = "mayor" if numero < objetivo else "menor"
        print(f"Incorrecto. El número es {pista} que {numero}.")

if not adivinado:
    print(f"Se acabaron los intentos. El número era {objetivo}.")

o como parte de un bucle que se ejecute hasta que el usuario adivine un número correcto.

bucles con condicion de salida variable

saldo = 1000
while saldo > 0:
    print(f"Saldo actual: {saldo}€")
    gasto = float(input("Introduce la cantidad a gastar (0 para salir): "))

    if gasto == 0:
        break  # Salimos del bucle inmediatamente

    if gasto > saldo:
        print("No tienes suficiente saldo.")
        continue  # Volvemos al inicio del bucle

    saldo -= gasto

print(f"Saldo final: {saldo}€")

tambien se puede cambiar el valor de la condicion de salida dentro del bucle, lo que permite un control mas dinamico del flujo del programa.

bucles infinitos controlados

while True:
    respuesta = input("¿Quieres continuar? (s/n): ").lower()

    if respuesta == "n":
        print("Programa finalizado.")
        break

    if respuesta == "s":
        print("Continuando...")
    else:
        print("Respuesta no válida. Introduce 's' o 'n'.")

procesamiento de datos con while

def calcular_factorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado

numero = 5
print(f"El factorial de {numero} es {calcular_factorial(numero)}")  # 120

simulaciones y aproximaciones

def calcular_raiz_cuadrada(numero, precision=0.0001):
    aproximacion = numero / 2  # Valor inicial
    while abs(aproximacion**2 - numero) > precision:
        aproximacion = (aproximacion + numero/aproximacion) / 2
    return aproximacion

print(f"Raíz cuadrada de 25: {calcular_raiz_cuadrada(25):.6f}")  # 5.000000
print(f"Raíz cuadrada de 7: {calcular_raiz_cuadrada(7):.6f}")    # 2.645751

validacion de entrada con while

def obtener_numero_en_rango(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Error: El número debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: Debes introducir un número entero.")

edad = obtener_numero_en_rango("Introduce tu edad (0-120): ", 0, 120)
print(f"Edad registrada: {edad} años")

patrones con while

def imprimir_triangulo(altura):
    fila = 1
    while fila <= altura:
        print("*" * fila)
        fila += 1

imprimir_triangulo(5)

Precauciones al usar while:
1. Asegurarse de que la condición de salida se pueda alcanzar para evitar bucles infinitos.
2. que las variables de control se actualicen correctamente dentro del bucle.
3. que la condición de salida sea lógica y clara.

Break y continue
El uso de `break` y `continue` permite un control más fino del flujo de los bucles.
El comando `break` se utiliza para salir inmediatamente de un bucle, mientras que `continue` salta a la siguiente iteración del bucle.

Break
for numero in range(1, 11):
    if numero == 5:
        print("¡Encontrado el 5! Saliendo del bucle...")
        break
    print(f"Número actual: {numero}")

print("Bucle terminado")

casos practicos con break
busqueda eficiente: Detener la búsqueda una vez encontrado el elemento deseado.

def buscar_elemento(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice

    return -1  # Si llegamos aquí, el elemento no está en la lista

numeros = [4, 7, 2, 9, 1, 5]
posicion = buscar_elemento(numeros, 9)
print(f"El elemento se encuentra en la posición: {posicion}")

Validación de entrada con salida: Permitir al usuario salir de un proceso de entrada.

while True:
    entrada = input("Escribe algo (o 'salir' para terminar): ")

    if entrada.lower() == 'salir':
        print("Programa terminado.")
        break

    print(f"Has escrito: {entrada}")

Optimización de algoritmos: Evitar cálculos innecesarios.

def es_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # No es primo, salimos inmediatamente

    return True  # Si llegamos aquí, es primo

Continue

for numero in range(1, 11):
    if numero % 2 == 0:  # Si el número es par
        continue  # Saltamos a la siguiente iteración

    print(f"Número impar: {numero}")

usos practicos de continue

Filtrado de datos: Procesar solo los elementos que cumplen cierta condición.

temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]

print("Temperaturas positivas:")
for temp in temperaturas:
    if temp <= 0:
        continue

    print(f"{temp}°C")

Manejo de casos especiales: Evitar procesar casos que requieren tratamiento diferente.

numeros = [1, 2, 0, 4, 0, 6, 7]

for num in numeros:
    if num == 0:
        print("Omitiendo división por cero")
        continue

    resultado = 10 / num
    print(f"10 / {num} = {resultado}")

Validación de datos: Saltar entradas inválidas en un proceso de análisis.

datos = ["25", "error", "42", "texto", "17"]

suma = 0
for valor in datos:
    if not valor.isdigit():
        print(f"Valor no numérico ignorado: '{valor}'")
        continue

    suma += int(valor)

print(f"La suma de los valores válidos es: {suma}")

Combinación de break y continue

numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
limite = 50
suma = 0

for num in numeros:
    # Ignoramos múltiplos de 3
    if num % 3 == 0:
        print(f"Omitiendo {num} (múltiplo de 3)")
        continue

    # Sumamos el número
    suma += num
    print(f"Añadiendo {num}: suma = {suma}")

    # Si la suma supera el límite, terminamos
    if suma > limite:
        print(f"Límite de {limite} superado")
        break
        
Uso en bucles anidados

for i in range(1, 4):
    print(f"Grupo {i}:")

    for j in range(1, 6):
        if j == 3:
            print("  Saltando el elemento 3")
            continue  # Solo afecta al bucle interno

        print(f"  Elemento {j}")

    print("Fin del grupo\n")

Si necesitas salir de múltiples bucles anidados, puedes usar una bandera o variable de control:

encontrado = False

for i in range(5):
    for j in range(5):
        if i * j > 10:
            print(f"Valor encontrado: {i} * {j} = {i*j}")
            encontrado = True
            break  # Sale del bucle interno

    if encontrado:
        break  # Sale del bucle externo
        
precauciones al usar break y continue:

1. Evita bucles complejos: Si tu código tiene muchos break y continue, considera refactorizarlo en funciones más pequeñas.

# En lugar de:
for item in lista:
    if condicion1(item):
        continue
    if condicion2(item):
        break
    # Más código...

# Considera:
def procesar_item(item):
    if condicion1(item):
        return False
    if condicion2(item):
        return None
    # Procesar y devolver resultado
    return resultado

for item in lista:
    resultado = procesar_item(item)
    if resultado is None:
        break
    if resultado is False:
        continue
    # Usar resultado...

2. Rendimiento: Usar break puede mejorar significativamente el rendimiento al evitar iteraciones innecesarias.

# Versión ineficiente
encontrado = False
for elemento in lista_grande:
    if elemento == objetivo:
        encontrado = True
# Seguimos recorriendo toda la lista aunque ya encontramos el objetivo

# Versión eficiente
encontrado = False
for elemento in lista_grande:
    if elemento == objetivo:
        encontrado = True
        break  # Terminamos inmediatamente

Ejemplos practicos avanzados:
Ejemplo 1: Validación de contraseña

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
            continue  # Optimización: ya verificamos este requisito

        if caracter.islower():
            tiene_minuscula = True
            continue

        if caracter.isdigit():
            tiene_numero = True

    return tiene_mayuscula and tiene_minuscula and tiene_numero

# Probamos algunas contraseñas
contraseñas = ["abc123", "Password", "Password1", "pass123", "PASS123"]
for pwd in contraseñas:
    if validar_contraseña(pwd):
        print(f"'{pwd}' es válida")
    else:
        print(f"'{pwd}' NO es válida")

Ejemplo 2: Procesamiento de transacciones

transacciones = [
    {"id": 1, "monto": 1200, "estado": "completada"},
    {"id": 2, "monto": -50, "estado": "error"},
    {"id": 3, "monto": 800, "estado": "pendiente"},
    {"id": 4, "monto": 1500, "estado": "completada"},
    {"id": 5, "monto": 0, "estado": "cancelada"}
]

total_procesado = 0

for t in transacciones:
    # Ignoramos transacciones no completadas
    if t["estado"] != "completada":
        print(f"Transacción {t['id']}: {t['estado']} - ignorada")
        continue

    # Verificamos montos válidos
    if t["monto"] <= 0:
        print(f"Transacción {t['id']}: monto inválido ({t['monto']})")
        continue

    # Procesamos la transacción
    total_procesado += t["monto"]
    print(f"Transacción {t['id']}: {t['monto']}€ procesada")

print(f"Total procesado: {total_procesado}€")

Pass y else en bucles
El uso de `pass` en bucles es una forma de indicar que no se realiza ninguna acción en una iteración específica. Es útil cuando se requiere una estructura de control pero no se necesita ejecutar código en ese punto.
El uso de `else` en bucles permite ejecutar un bloque de código una vez que el bucle ha terminado su iteración sin interrupciones, es decir, sin que se haya encontrado un `break`.

pass

# Bucle que no hace nada para los números pares
for numero in range(1, 10):
    if numero % 2 == 0:
        pass  # No hacemos nada con los números pares
    else:
        print(f"Procesando número impar: {numero}")

def procesar_datos():
    # Función aún no implementada
    pass

# El programa puede seguir ejecutándose sin errores
procesar_datos()

modo_debug = False

for i in range(100):
    # En modo normal, no mostramos nada durante el procesamiento
    if not modo_debug:
        pass
    else:
        print(f"Procesando iteración {i}")

    # Código de procesamiento real aquí

else

for elemento in secuencia:
    # Cuerpo del bucle
else:
    # Código que se ejecuta si el bucle termina normalmente

while condicion:
    # Cuerpo del bucle
else:
    # Código que se ejecuta si el bucle termina normalmente

el bloque else se ejecuta solo si el bucle no se interrumpe con un break y si completa todas sus iteraciones, y tambien se ejecuta si el bucle no se ejecuta ni una sola vez.

# Buscar un número primo en una lista
numeros = [4, 6, 8, 9, 10, 12]

for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado un primo: {num}!")
        break
else:
    print("No se encontró ningún número primo en la lista")

numeros = [4, 6, 7, 8, 10]  # Ahora incluimos el 7

for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado un primo: {num}!")
        break
else:
    print("No se encontró ningún número primo en la lista")

casos de usos practicos

Validación con else: El patrón else en bucles es perfecto para validaciones donde queremos confirmar que todos los elementos cumplen cierta condición:

def validar_edades(lista_edades):
    for edad in lista_edades:
        if not isinstance(edad, int) or edad < 0:
            print(f"Edad inválida encontrada: {edad}")
            break
    else:
        print("Todas las edades son válidas")
        return True

    return False

# Probamos con diferentes listas
validar_edades([25, 17, 30, 42])  # Todas válidas
validar_edades([25, -3, 30, 42])  # Una inválida

Busqueda con else: Otro uso común es para búsquedas donde queremos realizar una acción específica si no encontramos lo que buscamos:

def buscar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            print(f"Usuario encontrado: {usuario}")
            return usuario
    else:
        print(f"Usuario '{nombre}' no encontrado, creando nuevo perfil...")
        nuevo_usuario = {"nombre": nombre, "nivel": 1}
        usuarios.append(nuevo_usuario)
        return nuevo_usuario

base_usuarios = [
    {"nombre": "Ana", "nivel": 5},
    {"nombre": "Carlos", "nivel": 3}
]

buscar_usuario(base_usuarios, "Ana")      # Existente
buscar_usuario(base_usuarios, "Roberto")  # Nuevo

Combinando pass y else

Podemos combinar ambas características para crear patrones de control de flujo más sofisticados:

def analizar_datos(valores, umbral):
    tiene_advertencias = False

    for valor in valores:
        if valor > umbral:
            tiene_advertencias = True
            print(f"Advertencia: valor {valor} excede el umbral {umbral}")
        else:
            pass  # Explícitamente no hacemos nada con valores normales
    else:
        if not tiene_advertencias:
            print("Análisis completo: todos los valores están dentro del rango normal")
            return "OK"

    return "ADVERTENCIA"

# Probamos con diferentes conjuntos de datos
analizar_datos([10, 15, 20, 25], 30)  # Todos dentro del umbral
analizar_datos([10, 35, 20, 25], 30)  # Uno excede el umbral

Uso en bucles while

def encontrar_raiz(numero, max_iteraciones=10):
    aproximacion = numero / 2
    iteracion = 0

    while abs(aproximacion**2 - numero) > 0.001 and iteracion < max_iteraciones:
        aproximacion = (aproximacion + numero/aproximacion) / 2
        iteracion += 1
        print(f"Iteración {iteracion}: {aproximacion:.6f}")
    else:
        if iteracion < max_iteraciones:
            print(f"Convergencia alcanzada en {iteracion} iteraciones")
            return aproximacion

    print("No se alcanzó convergencia en el número máximo de iteraciones")
    return aproximacion

encontrar_raiz(25)  # Debería converger rápidamente
encontrar_raiz(612, 5)  # Probablemente no converja en 5 iteraciones

precauciones al usar pass y else:
1. Usa pass cuando quieras indicar explícitamente que "no hacer nada" es intencional.
2. La cláusula else en bucles puede ser confusa para programadores que vienen de otros lenguajes, así que considera añadir un comentario explicativo
    para mejorar la legibilidad.
3. En equipos de desarrollo, asegúrate de que todos entiendan estas construcciones

# Versión más explícita con comentarios
for item in coleccion:
    if condicion(item):
        # Procesamiento normal
        procesar(item)
    else:
        pass  # Intencionalmente no hacemos nada con estos elementos
else:
    # Este bloque se ejecuta si el bucle termina normalmente (sin break)
    print("Procesamiento completado sin interrupciones")

#Ejemplo integrado

def validar_formulario(datos):
    campos_requeridos = ["nombre", "email", "edad"]
    errores = []

    # Verificar campos requeridos
    for campo in campos_requeridos:
        if campo not in datos:
            errores.append(f"Falta el campo requerido: {campo}")
            break
        elif not datos[campo]:  # Campo vacío
            errores.append(f"El campo {campo} no puede estar vacío")
            break
    else:
        # Solo llegamos aquí si todos los campos requeridos existen y no están vacíos
        # Ahora validamos el formato de cada campo

        # Validar email
        if "@" not in datos["email"]:
            errores.append("Email inválido")

        # Validar edad
        try:
            edad = int(datos["edad"])
            if edad < 18 or edad > 120:
                errores.append("La edad debe estar entre 18 y 120")
        except ValueError:
            errores.append("La edad debe ser un número")

    # Validaciones opcionales
    if "telefono" in datos:
        if not datos["telefono"].isdigit():
            errores.append("El teléfono debe contener solo dígitos")
    else:
        pass  # Explícitamente indicamos que es opcional

    # Resultado final
    if errores:
        return {"valido": False, "errores": errores}
    else:
        return {"valido": True}

# Probamos con diferentes formularios
formulario1 = {
    "nombre": "Ana García",
    "email": "ana@ejemplo.com",
    "edad": "28"
}

formulario2 = {
    "nombre": "Carlos López",
    "email": "carlosejemplo.com",  # Falta @
    "edad": "17"  # Menor de edad
}

print(validar_formulario(formulario1))
print(validar_formulario(formulario2))
"""