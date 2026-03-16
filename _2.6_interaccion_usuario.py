#2.6.1 La función input()
# print() envía datos a la consola. Esta nueva función obtiene datos de ella.
#print() no tiene un resultado utilizable. La importancia de esta nueva función es que regresa un valor muy utilizable.
#La función se llama input(). El nombre de la función lo dice todo
#La función input() es capaz de leer datos que fueron introducidos por el usuario y pasar esos datos al programa en ejecución.
#El programa entonces puede manipular los datos, haciendo que el código sea verdaderamente interactivo.
#Todos los programas leen y procesan datos. Un programa que no obtiene datos de entrada del usuario es un programa sordo.
print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")


#2.6.2 La función input() con un argumento

#La función input() puede hacer otra cosa: puede avisar al usuario sin ninguna ayuda de print().

anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")

#2.6.3 El resultado de la función input()

#el resultado de la función input() es una cadena.Una cadena que contiene todos los caracteres que el usuario introduce desde el teclado. No es un entero ni un flotante.Esto significa que no se debe utilizar como un argumento para operaciones matemáticas, por ejemplo, no se pueden utilizar estos datos para elevarlos al cuadrado, para dividirlos entre algo o por algo.
anything = input("Ingresa un número:")
something = anything ** 2.0
print(anything, "al cuadrado es", something)
#TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float' 

#2.6.5 Conversión de tipos (conversiones de tipos)

#La función int() toma un argumento (por ejemplo, una cadena: int(string)) e intenta convertirlo a un valor entero; si llegase a fallar, el programa entero fallará también (existe una manera de solucionar esto, se explicará mas adelante);
#La función float() toma un argumento (por ejemplo, una cadena: float(string)) e intenta convertirlo a flotante (el resto es lo mismo).

#Esto es muy simple y muy efectivo. Sin embargo, estas funciones se pueden invocar directamente pasando el resultado de la función input() directamente. No hay necesidad de emplear variables como almacenamiento intermedio

#2.6.6 Más sobre input() y conversión de tipo

#2.6.7 Operadores cadena

#El signo de + (más), al ser aplicado a dos cadenas, se convierte en un operador de concatenación
#Simplemente concatena (junta) dos cadenas en una. Por supuesto, puede ser utilizado más de una vez en una misma expresión, y en tal contexto se comporta con enlazado del lado izquierdo.
#En contraste con el operador aritmético, el operador de concatenación no es conmutativo, por ejemplo, "ab" + "ba" no es lo mismo que "ba" + "ab".
#No olvides, si se desea que el signo + sea un concatenador, no un sumador, solo se debe asegurar que ambos argumentos sean cadenas.
print("Hola" + "Mundo")
#HolaMundo 

fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")
#el usar + para concatenar cadenas te permite construir la salida de una manera más precisa que con una función print() pura, incluso si está enriquecida con end= y sep= argumentos de palabras clave.

#Replicación
#El signo de * (asterisco), cuando es aplicado a una cadena y a un número (o a un número y cadena) se convierte en un operador de replicación:

print("Hola" * 5)
#HolaHolaHolaHolaHola

#2.6.8 Conversiones de tipos una vez más
#str()
#A estas alturas ya sabes como emplear las funciones int() y float() para convertir una cadena a un número.

#Este tipo de conversión no es en un solo sentido. También se puede convertir un numero a una cadena, lo cual es más fácil y seguro - esta operación es posible hacerla siempre.

#Una función capaz de hacer esto se llama str()
print(str(3.14))
#3.14  

#2.6.9   LAB   Entradas y salidas simples
a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("\n¡Eso es todo, amigos!")

#2.6.10   LAB   Operadores y expresiones

#El resultado debe de ser asignado a y. Se cauteloso, observa los operadores y priorízalos. Utiliza cuantos paréntesis sean necesarios. Puedes utilizar variables adicionales para acortar la expresión (sin embargo, no es muy necesario)

x = float(input("Ingresa el valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

#2.6.11   LAB   Operadores y expresiones – 2
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura # encuentra el número total de minutos
hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
print(hour, ":", mins, sep='')

#2.6.12 RESUMEN DE SECCIÓN

#La función print() envía datos a la consola, mientras que la función input() obtiene datos de la consola.

# La función input() viene con un parámetro opcional: la cadena de mensaje. Te permite escribir un mensaje antes de que el usuario ingrese algo

# Cuando la función input() es llamada o invocada, el flujo del programa se detiene, el símbolo del cursor se mantiene parpadeando (le está indicando al usuario que tome acción ya que la consola está en modo de entrada) hasta que el usuario haya ingresado un dato y/o haya presionado la tecla Enter.

# El resultado de la función input() es una cadena. Se pueden unir cadenas unas con otras a través del operador de concatenación (+).

#También se pueden multiplicar (* - replicación) cadenas





