#Python ofrece "cajas" (o "contenedores") especiales para este propósito, estas cajas son llamadas variables ‒ el nombre mismo sugiere que el contenido de estos contenedores puede variar en casi cualquier forma.
#componenetes de una variable: Un nombre; Un valor (el contenido del contenedor)

#2.4.2 Nombres de Variables

#REGLAS
#El nombre de la variable debe de estar compuesto por MAYÚSCULAS, minúsculas, dígitos, y el carácter _ (guion bajo)
#El nombre de la variable debe comenzar con una letra;
#El carácter guion bajo es considerado una letra;
#Las mayúsculas y minúsculas se tratan de forma distinta (un poco diferente que en el mundo real - Alicia y ALICIA son el mismo nombre, pero en Python son dos nombres de variable distintos, subsecuentemente, son dos variables diferentes);
#El nombre de las variables no pueden ser igual a alguna de las palabras reservadas de Python

#palabras claves

#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#Son llamadas palabras clave o (mejor dicho) palabras clave reservadas. Son reservadas porque no se deben utilizar como nombres: ni para variables, ni para funciones, ni para cualquier otra cosa que se desee crear.

#2.4.3 Cómo crear una variable
#Se puede utilizar una variable para almacenar cualquier tipo de los valores que ya se han mencionado, y muchos mas de los cuales aun no se han explicado.
#Una variable se crea cuando se le asigna un valor. A diferencia de otros lenguajes de programación, no es necesario declararla
#Para crear una variable, se debe escribir un nombre de variable, seguido de un signo igual (=), seguido del valor que se desea almacenar en la variable. El signo igual es el operador de asignación, y su función es asignar el valor a la variable.

var = 1
print(var)
#1

#2.4.4 Cómo emplear una variabl

#Se puede utilizar print() para combinar texto con variables utilizando el operador + para mostrar cadenas con variables, por ejemplo:
var = "3.8.5"
print("Python version: " + var)
#Python version: 3.8.5

#2.4.5 Cómo asignar un nuevo valor a una variable ya existente

#El signo de igual es de hecho un operador de asignación. Aunque esto suene un poco extraño, el operador tiene una sintaxis simple y una interpretación clara y precisa.
#Asigna el valor del argumento de la derecha al de la izquierda, aún cuando el argumento de la derecha sea una expresión arbitraria compleja que involucre literales, operadores y variables definidas anteriormente.
var = 1
print(var)
var = var + 1
print(var)
#1
#2  

#2.4.6 Resolviendo problemas matemáticos simples
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
#c = 5.0

#2.4.7   LAB   Variables
juan = 3
mary =5
adan =6
print(juan, mary, adan, sep=',')
total = juan + mary + adan
print("el total de manzanas es ", total)

#2.4.8 Operadores Abreviados

#Muy seguido, se desea utilizar la misma variable al lado derecho y al lado izquierdo del operador = operator.
#x = x * 2
#Python tiene una forma abreviada de escribir esta operación, la cual es:
#x *= 2
#Esto es exactamente lo mismo que x = x * 2, pero es más corto y más fácil de escribir. De hecho, Python tiene una forma abreviada para cada uno de los operadores aritméticos, por ejemplo:
#x += 1 # x = x + 1

# 2.4.9   LAB   Variables: un convertidor simple

#la función round(). Su trabajo es redondear la salida del resultado al número de decimales especificados en el paréntesis, y regresar un valor flotante (dentro de la función round() se puede encontrar el nombre de la variable, el nombre, una coma, y el número de decimales que se desean mostrar)
kilometers = 12.25
miles = 7.38

miles_to_kilometers =   miles * 1.609344 
kilometers_to_miles =   kilometers / 1.609344

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
#7.38 millas son 11.88 kilómetros
#12.25 kilómetros son 7.61 millas

# 2.4.10   LAB   Operadores y expresiones
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)
#y = -1.0
x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)
#y = 3.0
x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)
#y = -7.0

#2.4.11 RESUMEN DE SECCIÓN

#una variable es una ubicación nombrada reservada para almacenar valores en la memoria. Una variable es creada o inicializada automáticamente cuando se le asigna un valor por primera vez. (2.1.4.1)

#Cada variable debe de tener un nombre único - un identificador. Un nombre válido debe ser aquel que no contiene espacios, debe comenzar con un guion bajo(_), o una letra, y no puede ser una palabra reservada de Python. El primer carácter puede estar seguido de guiones bajos, letras, y dígitos. Las variables en Python son sensibles a mayúsculas y minúsculas.

#Python es un lenguaje de tipo dinámico, lo que significa que no se necesita declarar variables en él. Para asignar valores a las variables, se utiliza simplemente el operador de asignación, es decir el signo de igual (=), por ejemplo, var = 1.

#También es posible utilizar operadores de asignación compuesta (operadores abreviados) para modificar los valores asignados a las variables, por ejemplo: var += 1, o var /= 5 * 2.

#Se les puede asignar valores nuevos a variables ya existentes utilizando el operador de asignación o un operador abreviado






