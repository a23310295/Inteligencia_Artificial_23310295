#Un parámetro es una variable, pero existen dos factores que hacen a un parámetro diferente:

#los parámetros solo existen dentro de las funciones en donde han sido definidos, y el único lugar donde un parámetro puede ser definido es entre los paréntesis después del nombre de la función, donde se encuentra la palabra clave reservada def;
#la asignación de un valor a un parámetro de una función se hace en el momento en que la función se manda llamar o se invoca, especificando el argumento correspondiente.

#los parámetros solo existen dentro de las funciones (este es su entorno natural)
#los argumentos existen fuera de las funciones, y son los que pasan los valores a los parámetros correspondientes.
def message(what, number):
    print("Ingresa", what, "número", number)

message("teléfono", 11)
message("precio", 5)
message("número", "number")

#4.2.2 Paso de parámetros posicionales
#La técnica que asigna cada argumento al parámetro correspondiente, es llamada paso de parámetros posicionales, los argumentos pasados de esta manera son llamados argumentos posicionales.


