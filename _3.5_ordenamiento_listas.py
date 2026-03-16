#3.5.1 Ordenamiento Burbuja

#3.5.2 Ordenando una lista
my_list = [8, 10, 6, 2, 4]  # lista a ordenar

for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.
print(my_list)


#3.5.3 El ordenamiento burbuja – versión interactiva
my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)

#3.5.4 RESUMEN DE SECCIÓN
#Puedes usar el método sort() para ordenar los elementos de una lista
lst = [5, 3, 1, 2, 4]
print(lst)

lst.sort()
print(lst)  # output: [1, 2, 3, 4, 5]


