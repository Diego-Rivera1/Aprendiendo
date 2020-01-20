"""
Batalla entre dos individuos
Version de Python 3.5.2

Importacion de funciones del lenjuage necesarias para la batalla
"""
from random import random #Del Modulo random obtener la funcion random
from random import randint #Del Modulo random obtener la funcion randint

"""
Declaracion de variables
    @var integer p1_v (Puntos de vida del primer individuo)
    @var integer p1_a (Puntos de ataque del primer individuo)
    @var integer p2_v (Puntos de vida del segundo individuo)
    @var integer p2_a (Puntos de ataque del segundo individuo)

+---------------------------------------------------------------+
|Asignacion del valor por defecto o predeterminado de p1_v, p2_v|
+---------------------------------------------------------------+
    Segun un aleatorio entre 50 a 100
"""
p1_v = 50 + int(random() * 50)
p2_v = 50 + int(random() * 50) 

"""
Para el calculo del Ataque de cada individuo se tiene como base 5 puntos de ataque mas un numero entero este 
se obtendra con el 25% como constante y una porcion aleatorio de la vida incial del oponente
+----------------------------------------------------------------+
|Asignacion del valor por defecto o predeterminado de p1_v, p2_v |
+----------------------------------------------------------------+
"""
p1_a = 5 + int( (random() * p2_v) * 0.25 ) 
p2_a = 5 + int( (random() * p1_v) * 0.25 )

#El combate empiaza y continua unicamente si ambos participantes estan con  vida
while(p1_v > 0 and p2_v > 0):
    turno = random() #Asignar el aleatorio [0, 1]
    print(turno)
    if(turno > 0.5):
        #Ataca el primer individuo al segundo
        p2_v -= p1_a 
    else:
        #Ataca el segundo individuo al primero
        p1_v -= p2_a

#Visualizar al ganador
if(p1_v <= 0):
    print("Gano el segundo individuo")
else:
    print("Gano el primer individuo")