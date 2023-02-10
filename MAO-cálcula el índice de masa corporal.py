#Cree una función que pueda calcular el índice de masa corporal (BMI) de una persona.
#La fórmula para calcular el BMI es la siguiente: 
#BMI = peso/(altura^2)
#En esta fórmula el peso está en kilogramos y la altura en metros. 
#Tenga en cuenta que el peso y altura que reciban su función, van a estar en libras y pulgadas respectivamente,
# ya que su función será usada en los Estados Unidos.

#Recuerde que:
# 1 libra corresponde a 0.45kg.
# 1 pulgada corresponde a 0.025 metros.
# El valor de retorno debe estar redondeado a dos decimales. 

def calcular_BMI (peso_kg: float, altura_m: float):
    return (bmi_real)
peso_kg= float (input("Ingrese el peso en kilogramos: "))
altura_m= float (input("Ingrese la altura en metros: "))
bmi = (peso_kg)/(altura_m**2)
bmi_real = round (bmi,2)
print ("El indice de masa corporal es: ", bmi_real)

#Sistema ingles con resultados en kg/m2

def calcular_BMI_ingles (peso_lb: float, altura_inch: float):
    return (bmi_real_ingles)
peso_lb= float (input("Ingrese el peso en libras: "))
altura_inch= float (input("Ingrese la altura en pulgadas: ")) 
peso_lb=peso_lb/2.222
altura_inch=altura_inch/40
bmi_ingles = (peso_lb)/(altura_inch**2)
bmi_real_ingles = round (bmi_ingles,2)
print ("El indice de masa corporal es: ", bmi_real_ingles)

#Respuesta UniAndes-Coursera
def calcular_BMI (peso_lb: float, altura_inch: float):
    peso_lb= peso_lb/2.222
    altura_inch= altura_inch/40
    bmi = (peso_lb)/(altura_inch**2)
    bmi_real = round (bmi,2)
    return (bmi_real)


