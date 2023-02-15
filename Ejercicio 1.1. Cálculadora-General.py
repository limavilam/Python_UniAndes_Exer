"""Ejercicio 1.1: Armar una calculadora
Hacer una calculadora definiendo funciones de operación. En particular:
a. Hacer una función que sume números
b. Hacer una función que reste números
c. Hacer una función que multiplique números
d. Hacer una función que divida números
e. Hacer una función que calcule una potencia de un número
f. Hacer una función que calcule una raíz cuadrada de un número
g. Probar la calculadora y chequear qué tipo ("type") de resultado se obtuvo.
h. Imprimir un string en la pantalla que diga el resultado de los cálculos (usar la función str() para convertir los números en strings.)"""
def funcion_suma(num_1:float, num_2:float):
   return (num_1 + num_2)

num_1 = float(input("Ingresa tu primer número: "))
num_2 = float(input("Ingresa tu segundo número: "))
suma = funcion_suma (num_1,num_2)
print ("La suma de los digitos es: ", suma)
   
def funcion_resta(num_1:float, num_2:float):
   return (num_1 - num_2)

num_1 = float(input("Ingresa tu primer número: "))
num_2 = float(input("Ingresa tu segundo número: "))
resta = funcion_resta (num_1,num_2)
print ("La diferencia de los digitos es: ", resta)

def funcion_multiplicacion(num_1:float, num_2:float):
   return (num_1 * num_2)

num_1 = float(input("Ingresa tu primer número: "))
num_2 = float(input("Ingresa tu segundo número: "))
multiplicacion = funcion_multiplicacion (num_1,num_2)
print ("La multiplicación de los digitos es: ", multiplicacion)

def potencia(base, exponente):
    resultado = pow(base, exponente)
    return resultado
base = float (input("Ingrese la base: "))
exponente = float (input("Ingrese el exponente: "))
resultado = potencia(base, exponente)
print("La potencia del número es: ", resultado)  


#Otra calculadora 

def main():
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = int(input("Elija una opción: "))

    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    if opcion == 1:
        resultado = suma(a, b)
    elif opcion == 2:
        resultado = resta(a, b)
    elif opcion == 3:
        resultado = multiplicacion(a, b)
    elif opcion == 4:
        resultado = division(a, b)
    else:
        resultado = "Opción inválida"

    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
