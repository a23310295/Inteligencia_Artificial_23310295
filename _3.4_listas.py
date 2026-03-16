#3.4.2 Indexación de listas
#Vamos a asignar un nuevo valor de 111 al primer elemento en la lista.
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.

numbers[0] = 111
print("Nuevo contenido de la lista: ", numbers)  # Contenido actual de la lista.
# ahora queremos copiar el valor del quinto elemento al segundo elemento
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.
 
numbers[0] = 111
print("\nPrevio contenido de la lista:", numbers)  # Imprimiendo contenido de la lista anterior.
 
numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.
#El valor dentro de los corchetes que selecciona un elemento de la lista se llama un índice, mientras que la operación de seleccionar un elemento de la lista se conoce como indexación.
#Vamos a utilizar la función print() para imprimir el contenido de la lista cada vez que realicemos los cambios. Esto nos ayudará a seguir cada paso con más cuidado y ver que sucede después de una modificación de la lista en particular.

#3.4.3 Acceso al contenido de las listas
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

#La función len()

#La longitud de una lista puede variar durante la ejecución. Se pueden agregar nuevos elementos a la lista, mientras que otros pueden eliminarse de ella. Esto significa que la lista es una entidad muy dinámica.

#Si deseas verificar la longitud actual de la lista, puedes usar una función llamada len() (su nombre proviene de length - longitud).

#La función toma el nombre de la lista como un argumento y devuelve el número de elementos almacenados actualmente dentro de la lista (en otras palabras - la longitud de la lista).

#3.4.4 Eliminando elementos de una lista
#Cualquier elemento de la lista puede ser eliminado en cualquier momento - esto se hace con una instrucción llamada del (eliminar). Nota: es una instrucción, no una función.
del numbers[1]
print(len(numbers))
print(numbers)
#No puedes acceder a un elemento que no existe - no puedes obtener su valor ni asignarle un valor. Ambas instrucciones causarán ahora errores de tiempo de ejecución:

print(numbers[4])
numbers[4] = 1

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

###

del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

###

#3.4.5 Los índices negativos son legales
#Un elemento con un índice igual a -1 es el último en la lista.
numbers = [111, 7, 2, 1]
print(numbers[-1])

#3.4.6   LAB   Los fundamentos de las listas

hat_list = [1, 2, 3, 4, 5] # Lista original

# Paso 1: Reemplazar el número central (el índice 2 es el centro de 5 elementos)
hat_list[2] = int(input("Ingresa un número entero para el centro: "))

# Paso 2: Eliminar el último elemento de la lista
del hat_list[-1]

# Paso 3: Imprimir la longitud de la lista existente
print(len(hat_list))

print(hat_list) # Para verificar el resultado final

#3.4.7 Funciones vs métodos

#Un método es un tipo específico de función - se comporta como una función y se parece a una función, pero difiere en la forma en que actúa y en su estilo de invocación.

#Una función no pertenece a ningún dato - obtiene datos, puede crear nuevos datos y (generalmente) produce un resultado.

#Un método hace todas estas cosas, pero también puede cambiar el estado de una entidad seleccionada.

#Un método es propiedad de los datos para los que trabaja, mientras que una función es propiedad de todo el código.

#3.4.8 Agregando elementos a una lista: append() y insert(
#list.append(value)
#Dicha operación se realiza mediante un método llamado append(). Toma el valor de su argumento y lo coloca al final de la lista que posee el método.
#La longitud de la lista aumenta en uno.
#El método insert() es un poco más inteligente - puede agregar un nuevo elemento en cualquier lugar de la lista, no solo al final.

#3.4.9 Haciendo uso de las listas
#El bucle for tiene una variante muy especial que puede procesar las listas de manera muy efectiva
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

#El segundo aspecto del bucle for
#Pero el bucle for puede hacer mucho más. Puede ocultar todas las acciones conectadas a la indexación de la lista y entregar todos los elementos de la lista de manera práctica.
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

#3.4.10 Listas en acción

variable_1 = 1
variable_2 = 2

variable_2 = variable_1
variable_1 = variable_2
#Si haces algo como esto, perderás el valor previamente almacenado en variable_2. Cambiar el orden de las tareas no ayudará. Necesitas una tercera variable que sirva como almacenamiento auxiliar.
variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)

#3.4.11   LAB   Los fundamentos de las listas: los Beatles
# paso 1: crea una lista vacía llamada beatles
beatles = []
print("Paso 1:", beatles)

# paso 2: emplea el método append() para agregar los miembros iniciales
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3: emplea un bucle for y append() para pedir nuevos miembros
for i in range(2):
    nuevo_miembro = input("Introduce el nombre del siguiente miembro (Stu Sutcliffe y luego Pete Best): ")
    beatles.append(nuevo_miembro)
print("Paso 3:", beatles)

# paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best
# Al eliminar el índice [3], Pete Best pasa a ser el nuevo índice [3]
del beatles[3]
del beatles[3]
print("Paso 4:", beatles)

# paso 5: usa el método insert() para agregar a Ringo Starr al principio (índice 0)
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)

# probando la longitud de la lista
print("Los Fav", len(beatles))

