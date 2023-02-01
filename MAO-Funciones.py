# Hacer un programa que rote los valores de 3 variables enteras X1, X2 y X3 hacia la derecha de forma que al final:
#X2 tenga el valor inicial de X1, X3 el de X2 y X1 el de X3. 

X1 = int(input("Ingrese el valor de X1: "))
X2 = int(input("Ingrese el valor de X2: "))
X3 = int(input("Ingrese el valor de X3: "))

#Procedemos con la rotación.

temporal = X1
X1 = X3
X3 = X2
X2 = temporal

print (str(X1)+", "+str(X2)+", "+str(X3))


