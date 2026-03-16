list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)
#crea una lista de un elemento llamada list_1;
#la asigna a una nueva lista llamada list_2;
#cambia el único elemento de list_1;
#imprime la list_2;

#el nombre de una variable ordinaria es el nombre de su contenido;
#el nombre de una lista es el nombre de una ubicación de memoria donde se almacena la lista.

#3.6.3 Rebanadas – índices negativos
#start es el índice del primer elemento incluido en la rebanada.
#end es el índice del primer elemento no incluido en la rebanada.

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

#Más sobre la instrucción del
#La instrucción del descrita anteriormente puede eliminar más de un elemento de la lista a la vez - también puede eliminar rebanadas
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

#3.6.4 Los operadores in y not in
#Python ofrece dos operadores muy poderosos, capaces de revisar la lista para verificar si un valor específico está almacenado dentro de la lista o no.
elem in my_list # type: ignore
elem not in my_list # type: ignore

#El primero de ellos (in) verifica si un elemento dado (el argumento izquierdo) está actualmente almacenado en algún lugar dentro de la lista (el argumento derecho) - el operador devuelve True en este caso.

#El segundo (not in) comprueba si un elemento dado (el argumento izquierdo) está ausente en una lista - el operador devuelve True en este caso
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)


# Elimina duplicados de una lista
original_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_list = []

for num in original_list:
    if num not in unique_list:
        unique_list.append(num)

print("Lista original:", original_list)
print("Lista sin duplicados:", unique_list)
