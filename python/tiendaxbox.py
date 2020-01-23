

"""Importancion de random"""
from random import random #Del Modulo random obtener la funcion random
from random import randint #Del Modulo random obtener la funcion randint

"""Declaracion de variables"""
t_i=8*3600 #Demuestra el segundo en el que se abre
t_f= (t_i + (10*3600))#Calculo hora de cierre del negocio
consolas = []
while (len(consolas) < 5  ):
    consola = {} # creando diccionario 
    consola["usp"] = 4 #El indice usp hace referencia a Usuarios maximos que pueden accerder por consola
    consola["juc"] = 0  #Inicializacion de jugadores utlizando la consola=0
    consola["cph"] = (2000 + randint(50, 500)) # Reconociendo Valor de costo por hora en una maquina
    consolas.append (consola)

cola_eventos = [] # A medida que se generar aleatorios se guardan los eventos ocurridos por consola
cont = 0
while ( t_i < t_f):
    if (len(cola_eventos) == 0 ):
        t_a = (t_i + randint(1,120) )
        cola_eventos.append (t_a)
        cont += 1
    else:
        if(t_i == cola_eventos[0]):






            t_a = (cola_eventos [len (cola_eventos) - 1 ] + randint(1,120))
            cola_eventos.append(t_a)
            del(cola_eventos[0])
            cont += 1
    t_i += 1 


print (cont)
#print ( cola_eventos )
print ( consolas )

