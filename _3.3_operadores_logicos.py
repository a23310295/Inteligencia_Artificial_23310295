#3.3.1 Lógica de computadoras
#Hemos utilizado la conjunción and (y), lo que significa que salir a caminar depende del cumplimiento simultáneo de estas dos condiciones. En el lenguaje de la lógica, tal conexión de condiciones se denomina conjunción. Y ahora otro ejemplo:Si tu estás en el centro comercial o yo estoy en el centro comercial, uno de nosotros le comprará un regalo a mamá. La aparición de la palabra or (o) significa que la compra depende de al menos una de estas condiciones. En lógica, este compuesto se llama una disyunción. Está claro que Python debe tener operadores para construir conjunciones y disyunciones. Sin ellos, el poder expresivo del lenguaje se debilitaría sustancialmente. Se llaman operadores lógicos.

#El operador and

#Un operador de conjunción lógica en Python es la palabra and. Es un operador binario con una prioridad inferior a la expresada por los operadores de comparación. Nos permite codificar condiciones complejas sin el uso de paréntesis como este:
counter > 0 and value == 100
#El resultado proporcionado por el operador and se puede determinar sobre la base de la tabla de verdad.
#Si consideramos la conjunción de A and B, el conjunto de valores posibles de argumentos y los valores correspondientes de conjunción se ve de la siguiente manera
#A	B	A and B
#False	False	False
# False	True	False
# True	False	False
# True	True	True

# El operador or   

# Un operador de disyunción es la palabra or. Es un operador binario con una prioridad más baja que and (al igual que + en comparación con *). Su tabla de verdad es la siguiente
#A	B	A or B
#False	False	False
# False	True	True
# True	False	True
# True	True	True

#El operador not
#Además, hay otro operador que se puede aplicar para condiciones de construcción. Es un operador unario que realiza una negación lógica. Su funcionamiento es simple: convierte la verdad en falso y lo falso en verdad.

#Este operador se escribe como la palabra not, y su prioridad es muy alta: igual que el unario + y -. Su tabla de verdad es simple:
#A	not A
#False	True
#True	False

#3.3.2 Expresiones lógicas
#Creemos una variable llamada var y asignémosle 1. Las siguientes condiciones son equivalentes a pares:
# Ejemplo 1:
print(var > 0)
print(not (var <= 0))

# Ejemplo 2:
print(var != 0)
print(not (var == 0))

#3.3.3 Valores lógicos vs bits individuales

#Los operadores lógicos toman sus argumentos como un todo, independientemente de cuantos bits contengan. Los operadores solo conocen el valor: cero (cuando todos los bits se restablecen) significa False; no cero (cuando se establece al menos un bit) significa True.
#El resultado de sus operaciones es uno de estos valores: False o True. Esto significa que este fragmento de código asignará el valor True a la variable j si i no es cero; de lo contrario, será False.

#3.3.4 Operadores bit a bit
#Sin embargo, hay cuatro operadores que le permiten manipular bits de datos individuales. Se denominan operadores bit a bit.
#Cubren todas las operaciones que mencionamos anteriormente en el contexto lógico, y un operador adicional. Este es el operador xor (significa o exclusivo ), y se denota como ^ (signo de intercalación).
#Aquí están todos ellos:

#& (ampersand) ‒ conjunción a nivel de bits;
#| (barra vertical) - disyunción a nivel de bits;
#~ (tilde) - negación a nivel de bits;
#^ (signo de intercalación) - o exclusivo a nivel de bits (xor).

#& requieres exactamente dos 1 s para proporcionar 1 como resultado;
#| requiere al menos un 1 para proporcionar 1 como resultado;
#^ requiere exactamente un 1 para proporcionar 1 como resultado.

#Agreguemos un comentario importante: los argumentos de estos operadores deben ser enteros; no debemos usar flotantes aquí.
#La diferencia en el funcionamiento de los operadores lógicos y de bits es importante: los operadores lógicos no penetran en el nivel de bits de su argumento. Solo les interesa el valor entero final.
#Los operadores bit a bit son más estrictos: tratan con cada bit por separado

#3.3.5 ¿Cómo tratar con bits individuales?

#La variable almacena la información sobre varios aspectos de la operación del sistema. Cada bit de la variable almacena un valor de si/no.
x & 1 = x # type: ignore
x & 0 = 0
#Si se desea verificar el valor del bit más bajo, se puede usar la operación x & 1. El resultado de esta operación es igual a x si el bit más bajo de x es 1, y es igual a 0 si el bit más bajo de x es 0.

#3.3.6 Desplazamiento binario a la izquierda y desplazamiento binario a la derecha

#ython ofrece otra operación relacionada con los bits individuales: shifting. Esto se aplica solo a los valores de número entero, y no debe usar flotantes como argumentos para ello. El desplazamiento a la izquierda se denota como <<, y el desplazamiento a la derecha se denota como >>. El número de posiciones para desplazar se especifica después del operador.

var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)
#17 68 8

#17 >> 1 → 17 // 2 (17 dividido entre 2 a la potencia de 1) → 8 (desplazarse hacia la derecha en un bit equivale a la división entera entre dos)
#17 << 2 → 17 * 4 (17 multiplicado por 2 a la potencia de 2) → 68 (desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro)

#3.3.7 RESUMEN DE SECCIÓN

#Python es compatible con los siguientes operadores lógicos:
#and → si ambos operandos son verdaderos, la condición es verdadera, por ejemplo, (True and True) es True.
#or → si alguno de los operandos es verdadero, la condición es verdadera, por ejemplo, (True or False) es True.
#not → devuelve False si el resultado es verdadero y devuelve True si es falso, por ejemplo, not True es False.

#Puedes utilizar operadores bit a bit para manipular bits de datos individuales. Los siguientes datos de muestra:

#x = 15, el cual es 0000 1111 en binario,
#y = 16, el cual es 0001 0000 en binario.
#Se utilizarán para ilustrar el significado de operadores bit a bit en Python. Analiza los ejemplos a continuación:

#& hace un bit a bit and (y), por ejemplo, x & y = 0, el cual es 0000 0000 en binario,
#| hace un bit a bit or (o), por ejemplo, x | y = 31, el cual es 0001 1111 en binario,
#˜ hace un bit a bit not (no), por ejemplo, ˜ x = 240*, el cual es 1111 0000 en binario,
#^ hace un bit a bit xor, por ejemplo, x ^ y = 31, el cual es 0001 1111 en binario,
#>> hace un desplazamiento bit a bit a la derecha, por ejemplo, y >> 1 = 8, el cual es 0000 1000 en binario,
#<< hace un desplazamiento bit a bit a la izquierda, por ejemplo, y << 3 = 128, el cual es 1000 0000 en binario.
