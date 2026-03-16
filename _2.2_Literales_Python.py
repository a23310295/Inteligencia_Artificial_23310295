#2.2.1 Literales - los datos en sí mismos

#Un literal se refiere a datos cuyos valores están determinados por el literal mismo.

#Se utilizan literales para codificar datos y ponerlos dentro del código.

print("2")
print(2)
#2
#2

#encuentras dos tipos diferentes de literales: Una cadena, la cual ya conoces y un número entero, algo completamente nuevo.

#La función print() los muestra exactamente de la misma manera - Sin embargo, internamente, la memoria de la computadora los almacena de dos maneras completamente diferentes - La cadena existe como eso solo una cadena - una serie de letras.

#El número es convertido a una representación máquina (una serie de bits). La función print() es capaz de mostrar ambos en una forma legible para humanos.

#2.2.2 Enteros

#se puede afirmar que todos los números manejados por las computadoras modernas son de dos tipos:enteros, es decir, aquellos que no tienen una parte fraccionaria, y números punto-flotantes (o simplemente flotantes), los cuales contienen (o son capaces de contener) una parte fraccionaría.

#Tomemos por ejemplo, el número once millones ciento once mil ciento once. Si tomaras ahorita un lápiz en tu mano, escribirías el siguiente número: 11,111,111, o así: 11.111.111, incluso de esta manera: 11 111 111. Es claro que la separación hace que sea más fácil de leer, especialmente cuando el número tiene demasiados dígitos. Sin embargo, Python no acepta estas cosas, está prohibido. ¿Qué es lo que Python permite?. El uso de guion bajo en los literales numéricos.*
print(11_111_111) 
print(11111111)
# a partir de 3.6, Python permite el uso de guion bajo en los literales numéricos para mejorar su legibilidad. El guion bajo es completamente opcional y no afecta el valor del número. Es simplemente una herramienta para hacer que los números grandes sean más fáciles de leer.
print(-42)

#Números octales y hexadecimales
#Si un número entero esta precedido por un código 0O o 0o (cero-o), el número será tratado como un valor octal. Esto significa que el número debe contener dígitos en el rango del [0..7] únicamente. 0o123 es un número octal con un valor (decimal) igual a 83. La función print() realiza la conversión automáticamente
print(0o123)
#83
#La segunda convención nos permite utilizar números en hexadecimal. Dichos números deben ser precedidos por el prefijo 0x o 0X (cero-x). 0x123 es un número hexadecimal con un valor (decimal) igual a 291. La función print() puede manejar estos valores también. Intenta esto:
print(0x123)
#291

#2.2.3 Flotantes
#tienen una parte decimal no vacía.
print(3.14)
#3.14

# no hay que olvidar esta sencilla regla - se puede omitir el cero cuando es el único dígito antes del punto decimal.
print(.14)
#0.14  
 
#4 y 4.0 Se puede pensar que son idénticos, pero Python los ve de una manera completamente distinta.4 es un número entero mientras que 4.0 es un número punto-flotante.El punto decimal es lo que determina si es flotante.
#Se puede utilizar la letra e minuscula o mayuscula Cuando se desea utilizar números que son muy pequeños o muy grandes, se puede implementar la notación científica.
print(3E8)
#300000000.0

#El exponente (el valor después de la E) debe ser un valor entero;
#La base (el valor antes de la E) puede ser un valor entero o flotante.

#codificando flotantes

#Python siempre elige la presentación más corta del número, y esto se debe de tomar en consideración al crear literales.
print(0.0000000000000000000001)
#1e-22

#2.2.4 Cadenas

#Las cadenas se emplean cuando se requiere procesar texto, las cadenas requieren comillas así como los flotantes necesitan punto decimal.
print("Me gusta \"Monty Python\"")
#En este caso, las comillas dentro de la cadena se escapan utilizando el carácter de escape \, lo que permite incluir comillas dentro de la cadena sin finalizarla prematuramente. El resultado de esta línea de código sería: Me gusta "Monty Python".
#La segunda solución puede ser un poco sorprendente. Python puede utilizar una apóstrofe en lugar de una comilla
print('Me gusta "Monty Python"')

#2.2.5 Valores Booleanos

#Para concluir con los literales de Python, existen dos más.No son tan obvios como los anteriores y se emplean para representar un valor muy abstracto - la veracidad.
#Cada vez que se le pregunta a Python si un número es más grande que otro, el resultado es la creación de un tipo de dato muy específico - un valor booleano.
#las cuales definen el Álgebra Booleana - una parte del álgebra que hace uso de dos valores: True y False, denotados como 1 y 0.
#Estos dos valores booleanos tienen denotaciones estrictas en Python: True, False
print(True > False)
print(True < False)

#2.2.6   LAB   Literales de Python - Cadenas

print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")
#"Estoy"
#""aprendiendo""
#"""Python"""

#2.2.7 RESUMEN DE SECCIÓN
# Los literales son notaciones para representar valores fijos en el código. Python tiene varios tipos de literales - es decir, un literal puede ser un número por ejemplo, 123), o una cadena (por ejemplo, "Yo soy un literal.").

#El sistema binario es un sistema numérico que emplea 2 como su base. Por lo tanto, un número binario está compuesto por 0s y 1s únicamente, por ejemplo, 1010 es 10 en decimal.

#Los sistemas de numeración Octales y Hexadecimales son similares pues emplean 8 y 16 como sus bases respectivamente. El sistema hexadecimal utiliza los números decimales más seis letras adicionales.
#Los enteros (o simplemente int) son uno de los tipos numéricos que soporta Python. Son números que no tienen una parte fraccionaria, por ejemplo, 256, o -1 (enteros negativos).

#Los números punto-flotante (o simplemente flotantes) son otro tipo numérico que soporta Python. Son números que contienen (o son capaces de contener) una parte fraccionaria, por ejemplo, 1.27.

# Para codificar un apóstrofe o una comilla dentro de una cadena se puede utilizar el carácter de escape, por ejemplo, 'I\'m happy.', o abrir y cerrar la cadena utilizando un conjunto de símbolos distintos al símbolo que se desea codificar, por ejemplo, "I'm happy." para codificar un apóstrofe, y 'El dijo "Python", no "typhoon"' para codificar comillas.

#Los valores booleanos son dos objetos constantes True y False empleados para representar valores de verdad (en contextos numéricos 1 es True, mientras que 0 es False.

#Existe un literal especial más utilizado en Python: el literal None. Este literal es llamado un objeto de NoneType, y puede ser utilizado para representar la ausencia de un valor



