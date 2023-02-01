## Haga un programa que pida al usuario una cantidad de pesos, una tasa de interés y un número de años. 
##Muestre por pantalla en cuánto se habrá convertido el capital inicial transcurridos esos años si cada año se aplica la tasa de interés introducida. 
##Recuerde que un capital de C pesos a un interés del X por cien durante n años se convierte en:
##C (1+X/100)^n pesos. 
##Pruebe su programa sabiendo que una cantidad de 10.000 pesos al 4.5% de interés anual se convierte en 24.117.14 pesos al cabo de 20 años. 


cantidad_pesos = input("Ingrese la cantidad en pesos: ")
tasa_interes = input("Ingrese la tasa de interés: ")
años = input("Ingrese el número de años: ")

c = float (cantidad_pesos)
x = float (tasa_interes)
yr = int (años)


valor_futuro = c*(1+x/100)**yr
print ("El valor futuro del monto inicial es: " + str(valor_futuro) )  #Coloco el str porque si quiero concatenar toca así, si no lo pongo y uso el +, sale error. 

