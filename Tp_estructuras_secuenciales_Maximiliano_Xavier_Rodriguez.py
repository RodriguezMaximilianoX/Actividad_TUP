#Práctico 1: Estructuras secuenciales 
## Actividades 
""" 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”."""
print("Hola Mundo!")

"""2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla."""
nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}!")

"""3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla."""
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

"""4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro."""
import math
radio = int(input("Ingrese el radio de un circulo para conocer su área y perímetro: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El area del circulo es: {area} y su perimetro es: {perimetro}")

"""5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale."""
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")


"""6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número."""
numero = int(input("Ingrese un número: "))
print(f"Tabla del {numero}:")
for i in range(1, 11):
  print(f"{numero} x {i} = {numero * i}")

"""7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos."""
num1 = int(input("Ingrese un primer numero distinto de 0: "))
num2 = int(input("Ingrese un segundo numero distinto de 0: "))
suma = num1 + num2 
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"El resultado de sumar {num1} + {num2} es: {suma}")
print(f"El resultado de restar {num1} - {num2} es: {resta}")
print(f"El resultado de multiplicar {num1} * {num2} es: {multiplicacion}")
print(f"El resultado de dividir {num1} / {num2} es: {division}")

"""8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:"""
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura**2)
print(f"Su indice de masa muscular es: {imc}")

"""9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:"""
tempCelsius = float(input("Ingrese una temperatura en grados Celsius: "))
tempFahrenheit = (9/5) * tempCelsius + 32
print(f"Si la temperatura en grados Celsius es de: {tempCelsius} en grados Fahrenheit es de: {tempFahrenheit}")

"""10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números."""
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio entre {num1}, {num2} y {num3} es de {promedio}")


