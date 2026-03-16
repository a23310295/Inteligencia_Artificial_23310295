print("Ingresa un valor: ")
a = int(input())

print("Ingresa un valor: ")
b = int(input())

print("Ingresa un valor: ")
c = int(input())
#Se necesita definirla. Aquí, la palabra definir es significativa.
#Así es como se ve la definición más simple de una función:

#def function_name():
    #cuerpo de la función

#Siempre comienza con la palabra reservada def (que significa definir)
#después de def va el nombre de la función (las reglas para darle nombre a las funciones son las mismas que para las variables)
#después del nombre de la función, hay un espacio para un par de paréntesis (ahorita no contienen algo, pero eso cambiará pronto)
#la línea debe de terminar con dos puntos;
#la línea inmediatamente después de def marca el comienzo del cuerpo de la función - donde varias o (al menos una) instrucción anidada, será ejecutada cada vez que la función sea invocada; nota: la función termina donde el anidamiento termina, se debe ser cauteloso


def message():
    print("Ingresar valor: ")

print("Inicia aqui.")
message()
print("Termina aqui.")

