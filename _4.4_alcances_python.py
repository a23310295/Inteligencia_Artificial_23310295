#4.4.1 Funciones y alcances
#Comencemos con una definición:

#El alcance de un nombre (por ejemplo, el nombre de una variable) es la parte del código donde el nombre es reconocido correctamente.
def scope_test():
    x = 123


scope_test()
print(x) # type: ignore

#4.4.2 Funciones y alcances: la palabra clave global
#La palabra clave global se puede usar para declarar que un nombre dentro de una función es global (es decir, que se refiere a un nombre definido en el nivel superior del programa).

global name
global name1


#4.4.4 RESUMEN DE SECCIÓN

var = 2


def mult_by_var(x):
    return x * var


print(mult_by_var(7)) # salida: 14



