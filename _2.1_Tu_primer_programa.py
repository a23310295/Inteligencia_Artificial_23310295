print("¡Hola, Mundo!")
#¿De dónde provienen las funciones?

#Pueden venir de Python mismo. La función print es una de este tipo; dicha función es un valor agregado de Python junto con su entorno (está integrada); no tienes que hacer nada especial (por ejemplo, pedirle a alguien algo) si quieres usarla;

#Pueden provenir de uno o varios de los módulos; de Python llamados complementos algunos de los módulos vienen con Python, otros pueden requerir una instalación por separado - cual sea el caso, todos deben estar conectados explícitamente con el código (te mostraremos cómo hacer esto pronto);

#Puedes escribirlas tú mismo, colocando tantas funciones como desees y necesites dentro de su programa para hacerlo más simple, claro y elegante.

# 2.1.3 Argumentos de funciones
# una función puede tener: Un efecto,resultado.

#Como puedes ver, la cadena está delimitada por comillas - de hecho, las comillas forman la cadena, recortan una parte del código y le asignan un significado diferente.

#Podemos imaginar que las comillas significan algo así: el texto entre nosotros no es un código. No está diseñado para ser ejecutado

#2.1.4 Invocación de funciones
#El nombre de la función (print en este caso) junto con los paréntesis y los argumento(s), forman la invocación de la función.
print("¡Hola, Mundo!")

#  LAB   Trabajando con la función print()

print("ROBERTO GAEL LOPEZ ANDRADE")

#2.1.6 La función print() y su efecto, argumentos, y valores retornados

 #¿Qué efecto tiene la función print()? todo lo que pongas en la función print() se aparecerá en tu pantalla.

 #¿Qué argumentos espera print()? Cualquiera. Puede operar con prácticamente todos los tipos de datos que ofrece Python. Cadenas, números, caracteres, valores lógicos, objetos 

# ¿Qué valor devuelve la función print()? Ninguno. La función print() no devuelve ningún valor, su efecto es suficiente 

#2.1.7 Instrucciones

#cualquier programa complejo generalmente contiene muchas más instrucciones que una. La pregunta es: ¿Cómo se acopla más de una instrucción en el código de Python? La sintaxis de Python es bastante específica en esta área. A diferencia de la mayoría de los lenguajes de programación, Python requiere que no haya más de una instrucción por línea.

print("La Witsi Witsi Araña subió a su telaraña.")
print("Vino la lluvia y se la llevó.")

#El programa invoca a la función print() dos veces, y puedes ver dos líneas separadas en la consola - esto significa que print() comienza su salida desde una nuevalínea cada vez que comienza su ejecución; puedes cambiar este comportamiento, pero también puedes usarlo a tu favor;

#Cada invocación de print() contiene una cadena diferente, como su argumento, y el contenido de la consola lo refleja - esto significa que las instrucciones en el código se ejecutan en el mismo orden en el que se han colocado en el archivo fuent

print("La Witsi Witsi Araña subió a su telaraña.")
print()
print("Vino la lluvia y se la llevó.")

#la invocación vacía de print() no está tan vacía como podrías haber esperado - genera una línea vacía o (esta interpretación también es correcta) genera una nuevalínea.

#2.1.8 Caracteres de escape y nueva línea en Python

#Se ven así: \n.

print("La Witsi Witsi Araña\nsubió a su telaraña.")
print()
print("Vino la lluvia\ny se la llevó.")

#La barra invertida (\) tiene un significado muy especial cuando se usa dentro de cadenas - se llama carácter de escape.
#La palabra escape debe entenderse específicamente - significa que la serie de caracteres en la cadena se escapa por un momento (un momento muy breve) para introducir una inclusión especial

#la letra n colocada después de la barra invertida proviene de la palabra newline.

#Tanto la barra invertida como n forman un símbolo especial llamado un carácter de nuevalínea, que insta a la consola a iniciar una nuevalínea de salida.

#2.1.9 Usando múltiples argumentos

print("La Witsi Witsi Araña" , "subió" , "a su telaraña.")

#Hay una invocación de la función print(), pero contiene tres argumentos. Todos ellos son cadenas.
#Los argumentos están separados por comas.
#La función print() invocada con más de un argumento los muestra todos en una sola línea.
#La función print() pone un espacio entre los argumentos de salida por iniciativa propia

#2.1.10 Argumentos posicionales
print("Mi nombre es", "Python.")
print("Monty Python.")

#La forma en que estamos pasando los argumentos a la función print() es la más común en Python, y se llama la forma posicional. Este nombre proviene del hecho de que el significado del argumento está dictado por su posición

#2.1.11 Argumentos de palabra clave

#Python ofrece otro mecanismo para el paso de argumentos, que puede ser útil cuando deseas convencer a la función print() para que cambie un poco su comportamiento.
#El mecanismo se llama argumentos de palabras clave. La función print() tiene dos argumentos de palabra clave que puedes usar para tus propósitos. El primero se llama end.
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")
#Mi nombre es Python. Monty Python.

# reglas: Un argumento de palabra clave consta de tres elementos: una palabra clave se identifica el argumento (end aquí); un signo de igual (=); y un valor asignado a ese argumento;
#cualquier argumento de palabra clave debe colocarse después del último argumento posicional (esto es muy importante)

#el argumento de palabra clave end determina los caracteres que la función print() envía a la salida una vez que llega al final de sus argumentos posicionales
#El comportamiento predeterminado refleja la situación en la que el argumento de palabra clave end se usa implícitamente de la siguiente manera: end="\n"

print("Mi nombre es ", end="")
print("Monty Python.")
#Mi nombre es Monty Python.

#Como el argumento end se ha establecido a nada, la función print() tampoco genera nada, una vez que se han agotado sus argumentos posicionales.
#La cadena asignada al argumento de palabra clave end puede ser de cualquier longitud. Experimenta con él si quieres.
#Dijimos anteriormente que la función print() separa sus argumentos de salida con espacios. Este comportamiento también se puede cambiar.
#El argumento de palabra clave que puede hacer esto se denomina sep (como en separador)

print("Mi", "nombre", "es", "Monty", "Python.", sep="-")
#Mi-nombre-es-Monty-Python.

#La función print() ahora usa un guión, en lugar de un espacio, para separar los argumentos de salida.
#el valor del argumento sep también puede ser una cadena vacía. Pruébalo tu mismo.
#Ambos argumentos de palabra clave pueden mezclarse en una invocación

print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
#Mi_nombre_es*Monty*Python.*

#2.1.12   LAB   La función print() y sus argumentos

print("Programming","Essentials","in", sep="***", end="...")
print("Python")
#Programming***Essentials***in...Python
#RECUERDA: Los argumentos de palabras clave deben pasarse después de cualquier argumento posicional requerido.

#2.1.13   LAB   Dando formato a la salida

#2.1.14 RESUMEN DE SECCIÓN
#La función print() es una función integrada imprime/envía un mensaje específico a la pantalla/ventana de consola.

#Para llamar a una función (invocación de función), debe utilizarse el nombre de la función seguido de un paréntesis. Puedes pasar argumentos a una función colocándolos dentro de los paréntesis. Se deben separar los argumentos con una coma, por ejemplo, print("¡Hola,", "Mundo!"). Una función print() "vacía" imprime una línea vacía a la pantalla.

#Las cadenas de Python están delimitadas por comillas, por ejemplo, "Soy una cadena" (comillas dobles), o 'Yo soy una cadena, también' (comillas simples).

#En las cadenas de Python la barra diagonal inversa (\) es un carácter especial que anuncia que el siguiente carácter tiene un significado diferente, por ejemplo, \n (el carácter de nuevalínea) comienza una nuevalínea de salida.

#Los argumentos posicionales son aquellos cuyo significado viene dictado por su posición, por ejemplo, el segundo argumento se emite después del primero, el tercero se emite después del segundo, etc.

#Los argumentos de palabra clave son aquellos cuyo significado no está dictado por su ubicación, sino por una palabra especial (palabra clave) que se utiliza para identificarlos.

#Los parámetros end y sep se pueden usar para dar formato la salida de la función print(). El parámetro sep especifica el separador entre los argumentos emitidos. Por ejemplo, print("H", "E", "L", "L", "O", sep="-"), mientras que el parámetro end especifica que imprimir al final de la declaración de impresión.
print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
#print('"Greg's book."') la linea 5 tiene error por que python lee la comilla simple como su funcion normal, el escape le dice que la interprete como una comilla de adorno y no como  una comilla de cierre de la cadena 


