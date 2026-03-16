#4.6.1 Tipos de secuencia y mutabilidad
#Antes de comenzar a hablar acerca de tuplas y diccionarios, se deben introducir dos conceptos importantes: tipos de secuencia y mutabilidad.

#Un tipo de secuencia es un tipo de dato en Python el cual es capaz de almacenar más de un valor (o ninguno si la secuencia esta vacía), los cuales pueden ser secuencialmente (de ahí el nombre) examinados, elemento por elemento.

#Debido a que el bucle for es una herramienta especialmente diseñada para iterar a través de las secuencias, podemos definirlas de la siguiente manera: una secuencia es un tipo de dato que puede ser escaneado por el bucle for.

#Hasta ahora, has trabajado con una secuencia en Python - la lista. La lista es un clásico ejemplo de una secuencia de Python. Aunque existen otras secuencias dignas de mencionar, las cuales se presentaran a continuación.

#La segunda noción - la mutabilidad - es una propiedad de cualquier tipo de dato en Python que describe su disponibilidad para poder cambiar libremente durante la ejecución de un programa. Existen dos tipos de datos en Python: mutables e inmutables.

#Los datos mutables pueden ser actualizados libremente en cualquier momento - a esta operación se le denomina "in situ".

#In situ es una expresión en Latín que se traduce literalmente como en posición, en el lugar o momento. Por ejemplo, la siguiente instrucción modifica los datos "in situ":

#4.6.2 Tuplas
#Lo primero que distingue una lista de una tupla es la sintaxis empleada para crearlas - las tuplas utilizan paréntesis, mientras que las listas usan corchetes, aunque también es posible crear una tupla tan solo separando los valores por comas.
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)
 
#La segunda diferencia entre las tuplas y las listas es que las tuplas son inmutables, lo que significa que no pueden ser modificadas después de haber sido creadas. En otras palabras, no puedes cambiar el valor de un elemento de una tupla, ni agregar nuevos elementos a una tupla, ni eliminar elementos de una tupla.


#4.6.3 Diccionarios
#El diccionario es otro tipo de estructura de datos de Python. No es una secuencia (pero puede adaptarse fácilmente a un procesamiento secuencial) y además es mutable.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

#Agregando nuevas claves
#El agregar una nueva clave con su valor a un diccionario es tan simple como cambiar un valor. Solo se tiene que asignar un valor a una nueva clave que no haya existido antes.

#4.6.5 Las tuplas y los diccionarios pueden trabajar juntos
school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break
    
if name in school_class:
        school_class[name] += (score,)
else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

