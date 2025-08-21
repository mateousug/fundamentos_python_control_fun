""" 
Condicionales simples en python
edad = 20
if edad >= 18:
    print("Eres mayor de edad.") 

temperatura = 30
if temperatura > 25:
    print("Hace calor hoy.") 

operaciones de comparación
ademas se puede usar and, or, not

hora = 10
if hora >= 6 and hora < 12:
    print("Buenos días.")

declaracion if-else

edad = 17
if edad >= 18:
    print("Puedes votar en las elecciones.")
else:
    print("Aún no tienes edad para votar.")

contrasena = input("Introduce la contraseña: ")
if contrasena == "secreta123":
    print("Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")

numero = 15
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
con multiples instrucciones
saldo = 300
retiro = 500
if saldo >= retiro:
    saldo -= retiro
    print("Retiro exitoso.")
    print(f"Nuevo saldo: {saldo}")
else:
    print("Fondos insuficientes.")
    print(f"Saldo actual: {saldo}")

declaracion if-elif-else
numero = 0

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

nota = 87

if nota >= 90:
    print("Calificación: Sobresaliente")
elif nota >= 80:
    print("Calificación: Notable")
elif nota >= 70:
    print("Calificación: Aprobado")
else:
    print("Calificación: Suspenso")

Los condicionales se ejecutan en orden, por lo que si una condición se cumple, las siguientes no se evalúan.
edad = 45

if edad < 18:
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    print("Eres adulto.")
else:
    print("Eres mayor de 65 años.")

tambien se puede evitar usar else con los elif
color = "azul"

if color == "rojo":
    print("El color es rojo.")
elif color == "verde":
    print("El color es verde.")
elif color == "azul":
    print("El color es azul.")

expresion match case

fruta = input("Introduzca una fruta: ")

match fruta:
    case "manzana":
        print("La fruta es una manzana.")
    case "naranja":
        print("La fruta es una naranja.")
    case "plátano":
        print("La fruta es un plátano.")
    case _:
        print("Fruta desconocida.")

El match case es especialmente util para estructuras de datos complejas como diccionarios o listas, permitiendo una sintaxis más clara y concisa para la selección de casos.

punto = (0, 0)

match punto:
    case (0, 0):
        print("El punto está en el origen.")
    case (0, y):
        print(f"El punto está en el eje Y en y={y}.")
    case (x, 0):
        print(f"El punto está en el eje X en x={x}.")
    case (x, y):
        print(f"El punto está en coordenadas x={x}, y={y}.")


es posible agregar condiciones adicionales a los casos en match case utilizando guardas (guards).

edad = 20

match edad:
    case edad if edad < 18:
        print("Eres menor de edad.")
    case edad if edad >= 18 and edad < 65:
        print("Eres adulto.")
    case edad if edad >= 65:
        print("Eres adulto mayor.")

usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Marta", "rol": "moderador"}
]

for usuario in usuarios:
    match usuario:
        case {"rol": "admin"}:
            print(f"{usuario['nombre']} tiene permisos de administrador.")
        case {"rol": "moderador"}:
            print(f"{usuario['nombre']} puede moderar contenidos.")
        case {"rol": "usuario"}:
            print(f"{usuario['nombre']} es un usuario regular.")
        case _:
            print(f"Rol de {usuario['nombre']} desconocido.")

numeros = [1, 2, 3, 4]

match numeros:
    case []:
        print("La lista está vacía.")
    case [uno]:
        print(f"Un solo elemento: {uno}.")
    case [uno, dos]:
        print(f"Dos elementos: {uno} y {dos}.")
    case [uno, *resto]:
        print(f"Primer elemento: {uno}, resto de la lista: {resto}.")

operaciones logicos en condicionales

AND

edad = 25
ingresos = 30000

if edad >= 18 and ingresos >= 20000:
    print("Eres elegible para el crédito.")

OR

dia = "sábado"

if dia == "sábado" or dia == "domingo":
    print("Es fin de semana.")

NOT

llueve = False

if not llueve:
    print("Podemos salir al parque.")

Combinacion de operadores logicos

edad = 17
permiso_parental = True

if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")

precedencia de operadores logicos es not and or

si se desea cambiar el orden de precedencia, se pueden usar paréntesis

resultado = (a or b) and c
print(resultado) 

condicionalles complejas en operadores if

usuario = "admin"
contrasena = "1234"

if usuario == "admin":
    if contrasena == "1234":
        print("Acceso concedido.")

if usuario == "admin" and contrasena == "1234":
    print("Acceso concedido.")

condicionales anidados

edad = 16
permiso_padres = True

if edad >= 18:
    print('Puedes obtener la licencia de conducir.')
else:
    if edad >= 16:
        if permiso_padres:
            print('Puedes obtener la licencia con permiso de tus padres.')
        else:
            print('Necesitas el permiso de tus padres para obtener la licencia.')
    else:
        print('Eres demasiado joven para conducir.')

edad = 16
permiso_padres = True

if edad >= 18:
    print('Puedes obtener la licencia de conducir.')
elif edad >= 16 and permiso_padres:
    print('Puedes obtener la licencia con permiso de tus padres.')
elif edad >= 16 and not permiso_padres:
    print('Necesitas el permiso de tus padres para obtener la licencia.')
else:
    print('Eres demasiado joven para conducir.')

usuario = 'admin'
contrasena = '1234'

if usuario == 'admin':
    if contrasena == '1234':
        print('Acceso concedido.')
    else:
        print('Contraseña incorrecta.')
else:
    print('Usuario no reconocido.')

a = 5
b = 10
c = 15

if a > b:
    if a > c:
        print('a es el mayor.')
    else:
        if c > b:
            print('c es el mayor.')
        else:
            print('b es el mayor.')
else:
    if b > c:
        print('b es el mayor.')
    else:
        print('c es el mayor.')

(alternativa a una operacion mas sencilla)

mayor = a

if b > mayor:
    mayor = b

if c > mayor:
    mayor = c

print(f'El número mayor es {mayor}.')

condicionales ternarios

valor_si_verdadero if condición else valor_si_falso

edad = 17
mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad."
print(mensaje)

a = 1

b = 2

print("El máximo es:", a if a > b else b)

edad = 20
categoria = "Menor" if edad < 18 else ("Joven Adulto" if edad < 30 else "Adulto")
print(categoria)

numeros = [1, 2, 3, 4, 5]
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(paridad)  # Salida: ['impar', 'par', 'impar', 'par', 'impar']

dividendo = 10
divisor = 0
resultado = dividendo / divisor if divisor != 0 else "División por cero no permitida"
print(resultado)

Evaluacion de cortocircuito

if condicion_a and condicion_b:
    # Código a ejecutar si ambas condiciones son verdaderas

if condicion_a or condicion_b:
    # Código a ejecutar si al menos una condición es verdadera

Uso para prevenir errores

lista = []

if lista and lista[0] == 'Python':
    print("El primer elemento es 'Python'.")

dividendo = 10
divisor = 0

if divisor != 0 and dividendo / divisor > 1:
    print("El resultado de la división es mayor que 1.")
else:
    print("No es posible dividir entre cero.")

Optimizacion de rendimiento

if usuario_esta_autenticado and tiene_permiso_avanzado and realizar_operacion_cara():
    # Ejecutar operación

efectos secundarios

acceso_registrado = True

acceso_permitido = False

if acceso_permitido or acceso_registrado:
    print("Acceso concedido.")
    
En este caso, si acceso_permitido es verdadero, la variable acceso_registrado no se evaluará debido al cortocircuito del operador or. Si es necesario que acceso_registrado se evalue siempre, debemos reorganizar el código:
if acceso_permitido:
    print("Acceso concedido.")
else:
    if acceso_registrado:
        print("Acceso concedido."


if acceso_permitido or (acceso_registrado and True):
    print("Acceso concedido.")

evaluacion de expresiones condicionales
La evaluación de cortocircuito también se aplica en las expresiones condicionales y puede ser aprovechada para escribir código más seguro. Por ejemplo:

resultado = funcion_pesada() if condicion else valor_por_defecto

funcion con all() y any()

any() detiene una evaulacion si encuentra un valor verdadero

numeros = [0, 0, 1, 0]

if any(numeros):
    print("Al menos un número es no cero.")

all() detiene una evaulacion si encuentra un valor falso

condiciones = [True, True, False, True]

if all(condiciones):
    print("Todas las condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.")
"""