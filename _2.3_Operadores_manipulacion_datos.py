#2.3.1 Python como una calculadora

print(2+2)
#4

#2.3.2 Operadores Básicos
#Un operador es un símbolo del lenguaje de programación, el cual es capaz de realizar operaciones con los valores.
# no todos los operadores de Python son tan simples como el signo de más, veamos algunos de los operadores disponibles en Python, las reglas que se deben seguir para emplearlos, y como interpretar las reglas que realizan.
#+
#-
#*
#/
#//
#%
#*

#Recuerda: Cuando los datos y operadores se unen, forman juntos expresiones. La expresión más sencilla es el literal.

#Exponenciación
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
#8
#8.0
#8.0
#8.0

#Cuando ambos ** argumentos son enteros, el resultado es entero, también;
#Cuando al menos un ** argumento es flotante, el resultado también es flotante.

#Multiplicación
#Un símbolo de * (asterisco) es un operador de multiplicación.
print(2 * 3)
#6

#División

#Un símbolo de / (diagonal) es un operador de división.
#El valor después de la diagonal es el dividendo, el valor antes de la diagonal es el divisor.
print(6 / 2)
#3.0
#El resultado producido por el operador de división siempre es flotante, sin importar si a primera vista el resultado es flotante: 1 / 2, o si parece ser completamente entero: 2 / 1.

#División entera
#Un símbolo de // (doble diagonal) es un operador de división entera. Difiere del operador estándar / en dos detalles:
#El resultado carece de la parte fraccionaria, está ausente (para los enteros), o siempre es igual a cero (para los flotantes); esto significa que los resultados siempre son redondeados;Se ajusta a la regla entero vs flotante.

print(6 // 2)
#3
print(7 // 2)
#3
print(7.0 // 2)
#3.0
#Como se puede observar, una división de entero entre entero da un resultado entero. Todos los demás casos producen flotantes.
#El resultado de la división entera siempre se redondea al valor entero inferior mas cercano del resultado de la división no redondeada. Esto es muy importante: el redondeo siempre va hacia abajo.
print(-6 // 4)
#-2
print(6. // -4)
#-2.0
#El resultado es un par de dos negativos. El resultado real (no redondeado) es -1.5 en ambo casos. Sin embargo, los resultados se redondean. El redondeo se hace hacia el valor inferior entero, dicho valor es -2, por lo tanto los resultados son: -2 y -2.0.
#La division entera también se le suele llamar en inglés floor division.

#Residuo (módulo)

#El siguiente operador es uno muy peculiar, porque no tiene un equivalente dentro de los operadores aritméticos tradicionales.
#Su representación gráfica en Python es el símbolo de % (porcentaje)
#El resultado de la operación es el residuo que queda de la división entera.

print(14 % 4)
#2

#Como no dividir
#Como probablemente sabes, la división entre cero no funciona.
#No intentes: Dividir entre cero;  Realizar una división entera entre cero; Encontrar el residuo de una división entre cero

#Suma

#El símbolo del operador de suma es el + (signo de más), el cual esta completamente alineado a los estándares matemáticos.
print(-4 + 4)
#0
print(-4. + 8)
#4.0

#El operador de resta, operadores unarios y binarios

#El símbolo del operador de resta es obviamente - (el signo de menos), sin embargo debes notar que este operador tiene otra función - puede cambiar el signo de un número.
#Esta es una gran oportunidad para mencionar una distinción muy importante entre operadores unarios y binarios.
#En aplicaciones de resta, el operador de resta espera dos argumentos: el izquierdo (un minuendo en términos aritméticos) y el derecho (un sustraendo).
print(-4 - 4)
#-8
print(4. - 8)
#-4.0
print(-1.1)
#-1.1

#2.3.3 Operadores y sus prioridades

#Python define la jerarquía de todos los operadores, y asume que los operadores de mayor jerarquía deben realizar sus operaciones antes que los de menor jerarquía. Entonces, si se sabe que la * tiene una mayor prioridad que la +, el resultado final debe de ser obvio.

#Operadores y sus enlaces

#El enlace de un operador determina el orden en que se computan las operaciones de los operadores con la misma prioridad, los cuales se encuentran dentro de una misma expresión.

print(9 % 6 % 2)
#1

#El operador de módulo tiene una prioridad más alta que el operador de suma, por lo tanto, el resultado de la operación 9 % 6 se computa primero, y el resultado es 3. Luego, el resultado de esta operación se utiliza como el primer argumento del segundo operador de módulo, y el resultado final es 1.

#Lista de prioridades

#1. Exponenciación (**)
#2. Negación, identidad y multiplicación unaria (+x, -x, ~x)
#3. Multiplicación, división, división entera y módulo (*, /, //, %)
#4. Suma y resta (+, -) 

#Operadores y paréntesis

#se permite hacer uso de paréntesis, lo cual cambiará el orden natural del cálculo de la operación. De acuerdo con las reglas aritméticas, las sub-expresiones dentro de los paréntesis siempre se calculan primero.

#2.3.4 RESUMEN DE SECCIÓN

# Una expresión es una combinación de valores (o variables, operadores, llamadas a funciones, aprenderás de ello pronto) las cuales son evaluadas y dan como resultado un valor, por ejemplo, 1 + 2.

#Los operadores son símbolos especiales o palabras clave que son capaces de operar en los valores y realizar operaciones matemáticas, por ejemplo, el * multiplica dos valores: x * y.

#Los operadores aritméticos en Python: + (suma), - (resta), * (multiplicación), / (división clásica: regresa un flotante siempre), % (módulo: divide el operando izquierdo entre el operando derecho y regresa el residuo de la operación, por ejemplo, 5 % 2 = 1), ** (exponenciación: el operando izquierdo se eleva a la potencia del operando derecho, por ejemplo, 2 ** 3 = 2 * 2 * 2 = 8), // (división entera: retorna el número resultado de la división, pero redondeado al número entero inferior más cercano, por ejemplo, 3 // 2.0 = 1.0)

#Un operador unario es un operador con solo un operando, por ejemplo, -1, o +3.

#Un operador binario es un operador con dos operandos, por ejemplo, 4 + 5, o 12 % 5.

#Algunos operadores actúan antes que otros, a esto se le llama - jerarquía de prioridades:

#El operador ** (exponencial) tiene la prioridad más alta; Posteriormente los operadores unarios + y - (nota: los operadores unarios a la derecha del operador exponencial enlazan con mayor fuerza, por ejemplo 4 ** -1 es igual a 0.25) Después *, /, //, y %, Finalmente, la prioridad más baja: los operadores binarios + y -.

#Las sub-expresiones dentro de paréntesis siempre se calculan primero, por ejemplo,  15 - 1 * ( 5 *( 1 + 2 ) ) = 0.

#Los operadores de exponenciación utilizan enlazado del lado derecho, por ejemplo, 2 ** 2 ** 3 = 256.


