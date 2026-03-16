#4.3.1 Efectos y resultados: la instrucción return
#Para lograr que las funciones devuelvan un valor (pero no solo para ese propósito) se utiliza la instrucción return (regresar o retornar).

#Esta palabra nos da una idea completa de sus capacidades. Nota: es una palabra clave reservada de Python.

#La instrucción return tiene dos variantes diferentes - considerémoslas por separado.
def boring_function():
    print("'Modo aburrimiento' ON.")
    return 123

print("¡Esta lección es interesante!")
boring_function()
print("Esta lección es aburrida...")
#En este caso, la función hace exactamente lo que su nombre sugiere - imprime un mensaje y luego regresa el número 123. Sin embargo, el valor que regresa no se utiliza en ningún lugar, por lo que no tiene ningún efecto en el programa.

#4.3.2 Unas pocas palabras sobre None
#Permítenos presentarte un valor muy curioso (para ser honestos, un valor que es ninguno) llamado None.
#Sus datos no representan valor razonable alguno - en realidad, no es un valor en lo absoluto; por lo tanto, no debe participar en ninguna expresión.

print(None + 2)
#Solo existen dos tipos de circunstancias en las que None se puede usar de manera segura:
# #cuando se le asigna a una variable (o se devuelve como el resultado de una función)
#cuando se compara con una variable para diagnosticar su estado interno.
value = None
if value is None:
    print("Lo siento, no contienes ningún valor")

#4.3.4   LAB   Un año bisiesto: escribiendo tus propias funciones

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")

#4.3.5   LAB   Cuántos días: escribiendo y usando tus propias funciones
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

test_years = [1900, 2000, 2016, 1987]
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr,mo,"-> ",end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")

#4.3.6   LAB   Día del año: escribiendo y usando tus propias funciones

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

print(day_of_year(2000, 12, 31))

#4.3.7   LAB   Números primos - cómo encontrarlos

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

