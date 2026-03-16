#Una computadora ejecuta el programa y proporciona las respuestas. El programa debe ser capaz de reaccionar de acuerdo con las respuestas recibidas.
#si o no, verdadero o falso, 1 o 0, etc. Estas son las respuestas que se pueden recibir. El programa debe ser capaz de reaccionar a estas respuestas de una manera u otra. Esto se llama tomar decisiones.

#3.1.2 Comparación: operador de igualdad

# ¿son dos valores iguales?
#Para hacer esta pregunta, se utiliza el == (igual igual) operador.
#No olvides esta importante distinción:

#= es un operador de asignación, por ejemplo, a = b asigna a la varable a el valor de b;
#== es una pregunta ¿Son estos valores iguales? así que a == b compara a y b.
#Es un operador binario con enlazado del lado izquierdo. Necesita dos argumentos y verifica si son iguales.

#3.1.4 Operadores

#El operador == (igual a) compara los valores de dos operandos. Si son iguales, el resultado de la comparación es True. Si no son iguales, el resultado de la comparación es False
print(1 == 1)
#True   
print(1 == 2)
#False
var = 0  # Asignando 0 a var
print(var == 0)
#True
var = 1  # Asignando 1 a var
print(var == 0)
#False

#Desigualdad: el operador no es igual a (!=)
#El operador != (no es igual a) también compara los valores de dos operandos. Aquí está la diferencia: si son iguales, el resultado de la comparación es False. Si no son iguales, el resultado de la comparación es True
var = 0  # Asignando 0 a var
print(var != 0)
#False
var = 1  # Asignando 1 a var
print(var != 0)
#True

#Operadores de comparación: mayor que
#También se puede hacer una pregunta de comparación usando el operador > (mayor que).True lo confirma; False lo niega.
#black_sheep > white_sheep  # Mayor que

#Operadores de comparación: mayor o igual que
#El operador mayor que tiene otra variante especial, una variante no estricta, pero se denota de manera diferente que la notación aritmética clásica: >= (mayor o igual que).
#Hay dos signos subsecuentes, no uno.
#Ambos operadores (estrictos y no estrictos), así como los otros dos que se analizan en la siguiente sección, son operadores binarios con enlazado del lado izquierdo, y su prioridad es mayor que la mostrada por == y !=
#centigrade_outside >= 0.0  # Mayor o igual que

#Operadores de comparación: menor o igual que
#Como probablemente ya hayas adivinado, los operadores utilizados en este caso son: El operador < (menor que) y su hermano no estricto: <= (menor o igual que)
#current_velocity_mph < 85  # Menor que
#current_velocity_mph <= 85  # Menor o igual que

#3.1.5 Haciendo uso de las respuestas
#Existen al menos dos posibilidades: primero, puedes memorizarlo (almacenarlo en una variable) y utilizarlo más tarde
#La segunda posibilidad es más conveniente y mucho más común: puedes utilizar la respuesta que obtengas para tomar una decisión sobre el futuro del programa.
#tabla de prioridades
#+, -, *, /, //, %, **, >, >=, <, <=, ==, !=


#3.1.6   LAB   Variables ‒ Preguntas y Respuestas

n = int(input("Ingresa un número: "))
print(n >= 100)
#Si el número ingresado es mayor o igual a 100, el programa imprimirá True. Si el número es menor que 100, el programa imprimirá False.

#3.1.7 Condiciones y ejecución condicional

#Se debe tener un mecanismo que le permita hacer algo si se cumple una condición, y no hacerlo si no se cumple.
#Es como en la vida real: haces ciertas cosas o no cuando se cumple una condición específica, por ejemplo, sales a caminar si el clima es bueno, o te quedas en casa si está húmedo y frío
#Para tomar tales decisiones, Python ofrece una instrucción especial. Debido a su naturaleza y su aplicación, se denomina instrucción condicional (o sentencia condicional)

#if true_or_not:
    #do_this_if_true

#La palabra clave reservada if;
#Uno o más espacios en blanco;
#Una expresión (una pregunta o una respuesta) cuyo valor se interpretar únicamente en términos de True (cuando su valor no sea cero) y False (cuando sea igual a cero);
#Unos dos puntos seguidos de una nuevalínea;
#Una instrucción con sangría o un conjunto de instrucciones (se requiere absolutamente al menos una instrucción); la sangría se puede lograr de dos maneras: insertando un número particular de espacios (la recomendación es usar cuatro espacios de sangría), o usando el tabulador; nota: si hay mas de una instrucción en la parte con sangría, la sangría debe ser la misma en todas las líneas; aunque puede parecer lo mismo si se mezclan tabuladores con espacios, es importante que todas las sangrías sean exactamente iguales Python 3 no permite mezclar espacios y tabuladores para la sangría.

#Si la expresión true_or_not representa la verdad (es decir, su valor no es igual a cero), las sentencias con sangría se ejecutarán;
#Si la expresión true_or_not no representa la verdad (es decir, su valor es igual a cero), las sentencias con sangría se omitirán (ignorado), y la siguiente instrucción ejecutada será la siguiente al nivel de la sangría original.

#Ejecución condicional: la sentencia if

#if sheep_counter >= 120: # Evaluar una expresión condicional
    #sleep_and_dream() # Ejecutar si la expresión condicional es verdadera

#Puedes leerlo como sigue: si sheep_counter es mayor o igual que 120, entonces duerme y sueña (es decir, ejecuta la función sleep_and_dream).
#Hemos dicho que las sentencias condicionales deben tener sangría. Esto crea una estructura muy legible, demostrando claramente todas las rutas de ejecución posibles en el código.

#if sheep_counter >= 120:
    #make_a_bed()
    #take_a_shower()
    #sleep_and_dream()
    #feed_the_sheepdogs()

#Como puedes ver, tender la cama, tomar una ducha y dormir y soñar se ejecutan condicionalmente - cuando sheep_counter alcanza el límite deseado.
#Alimentar a los perros, sin embargo, siempre se hace (es decir, la función feed_the_sheepdogs() no tiene sangría y no pertenece al bloque if, lo que significa que siempre se ejecuta)

#Ejecución condicional: la sentencia if-else
#Comenzamos con una frase simple que decía: Si el clima es bueno, saldremos a caminar.
#Nota: no hay una palabra sobre lo que sucederá si el clima es malo. Solo sabemos que no saldremos al aire libre, pero no sabemos que podríamos hacer. Es posible que también queramos planificar algo en caso de mal tiempo.
#Ahora sabemos lo que haremos si se cumplen las condiciones, y sabemos lo que haremos si no todo sale como queremos. En otras palabras, tenemos un "Plan B".

#if true_or_false_condition:
    #perform_if_condition_true
#else:
    #perform_if_condition_false

#hay una nueva palabra: else - esta es una palabra clave reservada.
#La parte del código que comienza con else dice que hacer si no se cumple la condición especificada por el if (observa los dos puntos después de la palabra).
#La ejecución de if-else es la siguiente:
#Si la condición se evalúa como True (su valor no es igual a cero), la instrucción perform_if_condition_true se ejecuta, y la sentencia condicional llega a su fin;
#Si la condición se evalúa como False (es igual a cero), la instrucción perform_if_condition_false se ejecuta, y la sentencia condicional llega a su fin.

#La sentencia if-else: más sobre ejecución condicional
#if the_weather_is_good:
    #go_for_a_walk()
#else:
    #go_to_a_theater()
#have_lunch()

#Si el clima es bueno, entonces sal a caminar. De lo contrario, ve al teatro. Después de eso, almuerza (esta última acción no depende del clima, siempre se hace).
#Todo lo que hemos dicho sobre la sangría funciona de la misma manera dentro de la rama else:

#Sentencias if-else anidadas

#Primero, considera el caso donde la instrucción colocada después del if  es otro if.
#Lee lo que hemos planeado para este Domingo. Si hay buen clima, saldremos a caminar. Si encontramos un buen restaurante, almorzaremos allí. De lo contrario, vamos a comer un sandwich. Si hay mal clima, iremos al cine. Si no hay boletos, iremos de compras al centro comercial más cercano

#if the_weather_is_good:
#   if nice_restaurant_is_found:
#      have_lunch()
#   else:
#      eat_a_sandwich()
#else:
#   if tickets_are_available:
#     go_to_the_theater()
#  else:
#     go_shopping()

#Aquí hay dos puntos importantes:
#Este uso de la sentencia if se conoce como anidamiento; recuerda que cada else se refiere al if que se encuentra en el mismo nivel de sangría; se necesita saber esto para determinar cómo se relacionan los ifs y los else;
#Considera como la sangría mejora la legibilidad y hace que el código sea más fácil de entender y rastrea

#La sentencia elif

#El segundo caso especial presenta otra nueva palabra clave de Python: elif. Como probablemente sospechas, es una forma más corta de else if
#elif se usa para verificar más de una condición, y para detener cuando se encuentra la primera sentencia verdadera.
#Nuestro siguiente ejemplo se parece a la anidación, pero las similitudes son muy leves. Nuevamente, cambiaremos nuestros planes y los expresaremos de la siguiente manera: si hay buen clima, saldremos a caminar, de lo contrario, si obtenemos entradas, iremos al cine, de lo contrario, si hay mesas libres en el restaurante, vamos a almorzar; si todo falla, regresaremos a casa y jugaremos ajedrez.

#if the_weather_is_good:
#go_for_a_walk() 
#elif tickets_are_available:
#go_to_the_theater()
#elif table_is_available:
#go_for_lunch()
#else:
#play_chess_at_home()

#La forma de ensamblar las siguientes sentencias if-elif-else a veces se denomina cascada.
#Observa de nuevo como la sangría mejora la legibilidad del código.
# #Se debe prestar atención adicional a este caso:
#No debes usar else sin un if precedente;
#else siempre es la última rama de la cascada, independientemente de si has usado elif o no;
#else es una parte opcional de la cascada, y puede omitirse;
#Si hay una rama else en la cascada, solo se ejecuta una de todas las ramas;
#Si no hay una rama else, es posible que no se ejecute ninguna de las opciones disponibles.

#3.1.8 Análisis de muestras de código

#ejemplo1
# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)

#ejemplo2
# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2: larger_number = number1
else: larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)

#ejemplo3
# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1

# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2

# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3

# Imprime el resultado.
print("El número más grande es:", largest_number)

#3.1.9 Pseudocódigo e introducción a los bucles

#Por ahora ignoraremos los requisitos de la sintaxis de Python e intentaremos analizar el problema sin pensar en la programación real. En otras palabras, intentaremos escribir el algoritmo, y cuando estemos contentos con él, lo implementaremos.
#En este caso, utilizaremos un tipo de notación que no es un lenguaje de programación real (no se puede compilar ni ejecutar), pero está formalizado, es conciso y se puede leer. Se llama pseudocódigo

#largest_number = -999999999
#number = int(input())
#if number == -1:
# print(largest_number)
#exit()
#if number > largest_number:
#largest_number = number
# Ir a la línea 02

#Python a menudo viene con muchas funciones integradas que harán el trabajo por ti. Por ejemplo, para encontrar el número más grande de todos, puede usar una función incorporada de Python llamada max(). Puedes usarlo con múltiples argumentos. Analiza el código de abajo:

# Se leen tres números.
#number1 = int(input("Ingresa el primer número: "))
#number2 = int(input("Ingresa el segundo número: "))
#number3 = int(input("Ingresa el tercer número: "))

# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number.

#largest_number = max(number1, number2, number3)

# Imprime el resultado.
#print("El número más grande es:", largest_number)

#3.1.10   LAB   Operadores de comparación y ejecución condicional

#magina que tu programa de computadora ama estas plantas. Cada vez que recibe una entrada en forma de la palabra Espatifilo, grite involuntariamente a la consola la siguiente cadena: "¡Espatifilo es la mejor planta de todas!"

#Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

#imprima el enunciado "Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!" en la pantalla si la cadena ingresada es "ESPATIFILIO" (mayúsculas)
#imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo" (minúsculas)
#imprima "¡Espatifilo!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.

name = input("Introduce el nombre de la flor: ")

if name == "ESPATIFILIO":
    print("Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!")
elif name == "espatifilo":
    print("No, ¡quiero un gran ESPATIFILIO!")
else:
    print("¡ESPATIFILIO!, ¡No", name + "!")

#3.1.11   LAB   Fundamentos de la sentencia if-else

income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")


#3.1.12   LAB   Fundamentos de la sentencia if-elif-else

#El código debe mostrar uno de los dos mensajes posibles, que son Año Bisiesto o Año Común, según el valor ingresado.
#Sería bueno verificar si el año ingresado cae en la era Gregoriana y emitir una advertencia de lo contrario: No dentro del período del calendario Gregoriano. Consejo: utiliza los operadores != y %.
year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if year % 4 != 0:
		print("Año Común")
	elif year % 100 != 0:
		print("Año Bisiesto")
	elif year % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")
#3.1.13 RESUMEN DE SECCIÓN
#Los operadores de comparación (o también denominados operadores relacionales) se utilizan para comparar valores. La siguiente tabla ilustra cómo funcionan los operadores de comparación, asumiendo que x = 0, y = 1, y z = 0

#2. Cuando deseas ejecutar algún código solo si se cumple una determinada condición, puedes usar una sentencia condicional

#








