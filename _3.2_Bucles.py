#3.2.1 Bucles en tu código con while
#while
   # instruction
#Si observas algunas similitudes con la instrucción if, está bien. De hecho, la diferencia sintáctica es solo una: usa la palabra while en lugar de la palabra if.
#La diferencia semántica es más importante: cuando se cumple la condición, if realiza sus sentencias sólo una vez; while repite la ejecución siempre que la condición se evalúe como True.
#Nota: todas las reglas relacionadas con sangría también se aplican aquí

#si deseas ejecutar más de una sentencia dentro de un while, debes (como con if) poner sangría a todas las instrucciones de la misma manera.
#una instrucción o conjunto de instrucciones ejecutadas dentro del while se llama el cuerpo del bucle.
#si la condición es False (igual a cero) tan pronto como se compruebe por primera vez, el cuerpo no se ejecuta ni una sola vez (ten en cuenta la analogía de no tener que hacer nada si no hay nada que hacer).
#el cuerpo debe poder cambiar el valor de la condición, porque si la condición es True al principio, el cuerpo podría funcionar continuamente hasta el infinito. Observa que hacer una cosa generalmente disminuye la cantidad de cosas por hacer.

#3.2.2 Un bucle infinito
#Un bucle infinito, también denominado bucle sin fin, es una secuencia de instrucciones en un programa que se repite indefinidamente (bucle sin fin)
while True:
    print("Estoy atrapado dentro de un bucle.")
#El programa anterior es un ejemplo de un bucle infinito. La condición del bucle es siempre True, lo que significa que el cuerpo del bucle se ejecutará una y otra vez sin detenerse. En este caso, el programa imprimirá "Estoy atrapado dentro de un bucle." repetidamente hasta que se interrumpa manualmente (por ejemplo, presionando Ctrl+C en la consola).

#3.2.3 El bucle while: más ejemplos
## Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)

#Ciertas expresiones se pueden simplificar sin cambiar el comportamiento del programa. Intenta recordar cómo Python interpreta la verdad de una condición y ten en cuenta que estas dos formas son equivalentes:
#while number != 0: y while number:.
#La condición que verifica si un número es impar también puede codificarse en estas formas equivalentes:
#if number % 2 == 1: y if number % 2:.

#Empleando una variable counter para salir del bucle

counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

#Este código está destinado a imprimir la cadena "Dentro del bucle." y el valor almacenado en la variable counter durante un bucle dado exactamente cinco veces. Una vez que la condición se haya cumplido (la variable counter ha alcanzado 0), se sale del bucle y aparece el mensaje "Fuera del bucle." así como tambien el valor almacenado en counter se imprime.
#Pero hay una cosa que se puede escribir de forma más compacta - la condición del bucle while.


#3.2.4   LAB   Adivina el número secreto

#3.2.5 Bucles en tu código con for

#Otro tipo de bucle disponible en Python proviene de la observación de que a veces es más importante contar los "giros o vueltas" del bucle que verificar las condiciones. Imagina que el cuerpo de un bucle debe ejecutarse exactamente cien veces. Si deseas utilizar el bucle while para hacerlo, puede tener este aspecto

i = 0
while i < 100:
    # do_something()
    i += 1
# el bucle for está diseñado para realizar tareas más complicadas, puede "explorar" grandes colecciones de datos elemento por elemento.

for i in range(100):
    # do_something()
    pass

#la palabra reservada for abre el bucle for; nota - No hay condición después de eso; no tienes que pensar en las condiciones, ya que se verifican internamente, sin ninguna intervención.
#cualquier variable después de la palabra reservada for es la variable de control del bucle; cuenta los giros del bucle y lo hace automáticamente.
#la palabra reservada in introduce un elemento de sintaxis que describe el rango de valores posibles que se asignan a la variable de control.
#la función range() (esta es una función muy especial) es responsable de generar todos los valores deseados de la variable de control; en nuestro ejemplo, la función creará (incluso podemos decir que alimentará el bucle con) valores subsiguientes del siguiente conjunto: 0, 1, 2 .. 97, 98, 99; nota: en este caso, la función range() comienza su trabajo desde 0 y lo finaliza un paso (un número entero) antes del valor de su argumento.
#nota la palabra clave pass dentro del cuerpo del bucle - no hace nada en absoluto; es una instrucción vacía - la colocamos aquí porque la sintaxis del bucle for exige al menos una instrucción dentro del cuerpo (por cierto - if, elif, else y while expresan lo mismo).

#3.2.6 Más acerca del bucle for y la función range() con tres argumentos
#La función range() también puede aceptar tres argumentos

for i in range(2, 8, 3):
    print("El valor de i es", i)

#3.2.7   LAB   Fundamentos del bucle for – contando lentamente (mississippily)

#3.2.8 Las sentencias break y continue

#Python proporciona dos instrucciones especiales para la implementación de estas dos tareas. Digamos por razones de precisión que su existencia en el lenguaje no es necesaria - un programador experimentado puede codificar cualquier algoritmo sin estas instrucciones. Tales adiciones, que no mejoran el poder expresivo del lenguaje, sino que solo simplifican el trabajo del desarrollador, a veces se denominan dulces sintácticos o azúcar sintáctica.

#Estas dos instrucciones son:

#break - sale del bucle inmediatamente, e incondicionalmente termina la operación del bucle; el programa comienza a ejecutar la instrucción más cercana después del cuerpo del bucle.
#continue - se comporta como si el programa hubiera llegado repentinamente al final del cuerpo; el siguiente turno se inicia y la expresión de condición se prueba de inmediato.
#Ambas palabras son palabras clave reservadas.

# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

#3.2.9   LAB   La sentencia break - atrapado en un bucle

#La instrucción break se implementa para salir/terminar un bucle. Sin embargo, a veces es posible que quieras salir de un bucle, pero no deseas terminarlo completamente. En su lugar, solo quieres omitir el resto del cuerpo del bucle para la iteración actual y pasar a la siguiente iteración. Para eso sirve la instrucción continue.
while True:
    palabra = input("Ingresa una palabra: ")
    if palabra == "chupacabra":
        break

print("Has dejado el bucle con éxito.")

#3.2.10   LAB   La sentencia continue – el Feo Devorador de Vocales

# Pedir palabra al usuario
user_word = input("Ingresa una palabra: ")

# Convertir a mayúsculas
user_word = user_word.upper()

# Bucle for para recorrer la palabra
for letter in user_word:
    # Condicional para identificar vocales
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue  # Si es vocal, salta a la siguiente iteración
    
    # Imprimir la letra si no fue devorada
    print(letter)

# 3.2.12 El bucle while y el bloque else#Ambos bucles while y for, tienen una característica interesante (y rara vez se usa). Te mostraremos como funciona - intenta juzgar por ti mismo si es utilizable. En otras palabras, trata de convencerte si la función es valiosa y útil, o solo es azúcar sintáctica. Echa un vistazo al fragmento en el editor. Hay algo extraño al final - la palabra reservada else.
#Como pudiste haber sospechado, los bucles también pueden tener la rama else, como los if.
#La rama else del bucle siempre se ejecuta una vez, independientemente de si el bucle ha entrado o no en su cuerpo.

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

#3.2.13 El bucle for y el bloque else

for i in range(5):
    print(i)
else:
    print("else:", i)
#El cuerpo del bucle no se ejecutará aquí en absoluto. Nota: hemos asignado la variable i antes del bucle. Ejecuta el programa y verifica su output. Cuando el cuerpo del bucle no se ejecuta, la variable de control conserva el valor que tenía antes del bucle. Nota: si la variable de control no existe antes de que comience el bucle, no existirá cuando la ejecución llegue a la rama else branch.

#3.2.16 RESUMEN DE SECCIÓN
#Existen dos tipos de bucles en Python: while y for:
#El bucle while ejecuta una sentencia o un conjunto de sentencias siempre que una condición booleana especificada sea verdadera,

## Ejemplo 1
while True:
    print("Atrapado en un bucle infinito.")
 
# Ejemplo 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1
 




