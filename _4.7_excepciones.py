#4.7.3 La rama try-except


try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except:
    print('No se que hacer con', value)

#Dos excepciones después de un try
#Observa el código en el editor. Como puedes ver, acabamos de agregar un segundo except. Esta no es la única diferencia - toma en cuenta que ambos except tienen nombres de excepción específicos. En esta variante, cada una de las excepciones esperadas tiene su propia forma de manejar el error, pero debe enfatizarse en que solo una de todas puede interceptar el control - si se ejecuta una, todas las demás permanecen inactivas.

#4.7.11 print debugging (depuración)
#Esta forma de depuración, que se puede aplicar a tu código mediante cualquier tipo de depurador, a veces se denomina depuración interactiva. El significado del término se explica por sí mismo - el proceso necesita su interacción (la del desarrollador) para que se lleve a cabo.
