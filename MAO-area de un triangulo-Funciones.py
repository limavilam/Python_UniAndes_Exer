#El área de un triángulo 
# Reto 1: Área de un triángulo
#El área de un triángulo puede ser calculada cuando se conoce la longitud de sus lados. 
#Teniendo en cuenta que s1, s2 y s3 son las longitudes de los lados del triángulo, se puede calcular el subperímetro 
#s = (s1+s2+s3)/2, y, con este valor, se puede calcular el área del triángulo de la siguiente 
#manera: area = √( s * (s-s1) * (s-s2) * (s-s3) ). 

import math

def area_triangulo (s1: float, s2: float, s3: float):
    return (area)
s1 = float (input("Digite el lado 1: "))
s2 = float (input("Digite el lado 2: "))
s3 = float (input("Digite el lado 3: "))
subperimetro= (s1+s2+s3)/2
area = math.sqrt( subperimetro * (subperimetro-s1) * (subperimetro-s2) * (subperimetro-s3))
area_real = round (area,1)
print ("El área del triángulo sin redondear es: ", area)
print ("El área del triangulo es:", area_real)



