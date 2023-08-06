Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py
Hola mundo
Nueva linea


5+5
10
3-2
1
num = 15
print num
SyntaxError: incomplete input
num
15
print (num)
15
num = 8
print (num)
8
num
8

num + 2
10
num - 20
-12
nn = num + 2
nn
10

======== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =======
Hola mundo
Nueva linea
Traceback (most recent call last):
  File "C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py", line 3, in <module>
    print (nn)
NameError: name 'nn' is not defined

======== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =======
Hola mundo
Nueva linea
Traceback (most recent call last):
  File "C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py", line 3, in <module>
    print (num)
NameError: name 'num' is not defined. Did you mean: 'sum'?

======== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =======
Hola mundo
Nueva linea
8
edad = 24
Edad = 70
EDAD = 15
print (edad+Edad+EDAD)
109

======== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =======
Hola mundo
Nueva linea
20
8
type (8)
<class 'int'>
type (8.3)
<class 'float'>
type (hola)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    type (hola)
NameError: name 'hola' is not defined
Type ("Hola")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    Type ("Hola")
NameError: name 'Type' is not defined. Did you mean: 'type'?
type (hola)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    type (hola)
NameError: name 'hola' is not defined
type (3.05)
<class 'float'>
type help
SyntaxError: incomplete input
type ("Hola")
<class 'str'>
type(4>2)
<class 'bool'>
type(3=2)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
type (3==2)
<class 'bool'>
type (True)
<class 'bool'>
type (False)
<class 'bool'>
type ("hola con todos")
<class 'str'>
type (4+2)
<class 'int'>
type (4+2.05)
<class 'float'>
type ('Hola')
<class 'str'>

======== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =======
Hola mundo
Nueva linea
20
8
Isidora

======== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =======
Hola mundo
Nueva linea
20
8
Isidora

======== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =======
Hola mundo
Nueva linea
20
8
Juanita

======== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =======
Hola mundo
Nueva linea
20
8
Juanita
28

======== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =======
Hola mundo
Nueva linea
20
8
Juanita
28
Traceback (most recent call last):
  File "C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py", line 10, in <module>
    print (nombre + edad)
TypeError: can only concatenate str (not "int") to str

======== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =======
Hola mundo
Nueva linea
20
8
Traceback (most recent call last):
  File "C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py", line 9, in <module>
    print (nombre)
NameError: name 'nombre' is not defined. Did you mean: 'nombre1'?

======== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =======
Hola mundo
Nueva linea
20
8
28
JuanitaLuisita

======== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =======
Hola mundo
Nueva linea
20
8
28
Juanita Luisita
len ("")
0
len ("nombre")
6
len (" nombre")
7
7
7
nombre [0]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    nombre [0]
NameError: name 'nombre' is not defined. Did you mean: 'nombre1'?
nombre[0]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    nombre[0]
NameError: name 'nombre' is not defined. Did you mean: 'nombre1'?
nombre = "Mariana"
nombre[0]
'M'
nombre[12]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    nombre[12]
IndexError: string index out of range
"Mariana"[0]
'M'
"Mariana"[0:3]
'Mar'
nomnbre = "Mariana"
nombre[3:6]
'ian'
len (nombre)
7
num = len(nombre)
num = len(nombre)
nombre[inicio:]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    nombre[inicio:]
NameError: name 'inicio' is not defined
nombre[:]
'Mariana'
nombre[:fin]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    nombre[:fin]
NameError: name 'fin' is not defined. Did you mean: 'bin'?
nombre[: fin]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    nombre[: fin]
NameError: name 'fin' is not defined. Did you mean: 'bin'?
nombre[3:7:2]
'in'
nombre[1:7:2]
'ain'
nombre[1:7:3]
'aa'
nombre[3:20:2]
'in'
nombre.center()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    nombre.center()
TypeError: center expected at least 1 argument, got 0
nombre.capitalize()
'Mariana'
nombre = "luchita
SyntaxError: incomplete input
nombre = "luchita"
nombre.capitalize()
'Luchita'
nombre.find("i")
4
nombre.isdigit("i")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    nombre.isdigit("i")
TypeError: str.isdigit() takes no arguments (1 given)
nombre.lower()
'luchita'
nombre.upper()
'LUCHITA'
input ()
5
'5'
num = input(ingrese un numero)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
num = input("ingrese un numero")
ingrese un numero5
num
'5'

= RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py
Ingrese su edad25
25

= RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py
Ingrese su edad
= RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py
Ingrese su edad 25
Traceback (most recent call last):
  File "C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py", line 2, in <module>
    print (nn+2)
TypeError: can only concatenate str (not "int") to str

= RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py
Ingrese su edad 25
25años

= RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py
Ingrese su edad 25
25 años

= RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py
Ingrese su edad : 25
25 años

= RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py
Ingrese su edad : 49
Despues de cuantos años quiere saber su nueva edad: 5
54
dentro de 5 años  tendras 49 años

= RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py
Ingrese su edad : 49
Despues de cuantos años quiere saber su nueva edad: 5
54
Traceback (most recent call last):
  File "C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py", line 6, in <module>
    print ("dentro de " + net + " años " + " tendras " + ne + " años")
TypeError: can only concatenate str (not "NoneType") to str

= RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py
Ingrese su edad : 49
Despues de cuantos años quiere saber su nueva edad: 5
Traceback (most recent call last):
  File "C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py", line 4, in <module>
    ne = print (ea + ne)
NameError: name 'ne' is not defined. Did you mean: 'net'?

= RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py
Ingrese su edad : 49
Despues de cuantos años quiere saber su nueva edad: 5
495
Traceback (most recent call last):
  File "C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py", line 5, in <module>
    print ("dentro de " + net + " años " + " tendras " + ne + " años")
NameError: name 'ne' is not defined. Did you mean: 'net'?

= RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py
Ingrese su edad : 49
Despues de cuantos años quiere saber su nueva edad: 5
dentro de 54 años  tendras 54 años

= RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py
Ingrese su edad : 49
Despues de cuantos años quiere saber su nueva edad: 5
dentro de 5 años  tendras 54 años
15 // 5
3
15 // 7
2
-15 // 4
-4
-15 / 4
-3.75
15 // 4
3
-15 // 4
-4
5 ** 3
125
5 ** 2
25
5 *** 2
SyntaxError: invalid syntax
16 ** 0.2
1.7411011265922482
53535353 ** 0
1
12 // 2
6
12 % 2
0
13 % 2
1
5454545455 % 2
1
16 % 4
0
2 + (5-1) -8
-2
3 ** 2 + 3
12
3 + 3 ** 2
12
(3 > 2) and ( 4 > 1)
True
3 > 2
True
3 == 3
True
3 = 3
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
not -3
False
not (3>2)
False
not true
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True
not + and + or
SyntaxError: invalid syntax
3>=2
True
3>=3
True
3>=5
False
 4!= 6
 
SyntaxError: unexpected indent
4!=
SyntaxError: incomplete input
8!=8
False
8 != 7
True
"Hola" == "Hola"
True
"A" < "B"
True
2 += 3
SyntaxError: 'literal' is an illegal expression for augmented assignment
edad = 56
edad += 3
edad
59
56 +- 3
53
56 +- 3
53
56 += 3
SyntaxError: 'literal' is an illegal expression for augmented assignment

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Frio

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Calor

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Traceback (most recent call last):
  File "C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py", line 1, in <module>
    temt = imput("Ingrese la temperatura en celsiur: ")
NameError: name 'imput' is not defined. Did you mean: 'input'?

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Ingrese la temperatura en celsiur: 15
Frio

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Ingrese la temperatura en celsiur: 
Traceback (most recent call last):
  File "C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py", line 2, in <module>
    temp = int (temt)
ValueError: invalid literal for int() with base 10: ''

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Ingrese la temperatura en celsiur: 40
calor
Frio

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Ingrese la temperatura en celsius: 10
frio

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Ingrese la temperatura en celsius: 18
moderado

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Ingrese la temperatura en celsius: 28
Calor

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Ingrese la temperatura en celsius: 20
No hace frio

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Ingrese la temperatura en celsius: 10
frio

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Ingrese la temperatura en celsius: -8
muy frio

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Ingrese la temperatura en celsius: 12
frio

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Ingrese la temperatura en celsius: 30
calor

== RESTART: C:\Users\pbalbuen\Documents\curso-python\hola-mundo.py =
Ingrese la temperatura en celsius: 10
frio
[1, 2, 3, 4]
[1, 2, 3, 4]
num = in[1, 2, 3, 4]
SyntaxError: invalid syntax
Ingrese la temperatura en celsius: 10
SyntaxError: invalid syntax
num = [1, 2, 3]
num[0]
1
num[1]
2
type (num)
<class 'list'>
num.append(5)
num
[1, 2, 3, 5]
num.remove(1)
num
[2, 3, 5]
num.insert(2,5)
num
[2, 3, 5, 5]
num.insert (5,7)
>>> num
[2, 3, 5, 5, 7]
>>> num.remove(4)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    num.remove(4)
ValueError: list.remove(x): x not in list
>>> num.remove(7)
>>> num
[2, 3, 5, 5]
>>> num.remove(5)
>>> num
[2, 3, 5]
>>> num.remove(5)
>>> num
[2, 3]
>>> 4 in num
False
>>> 3 in num
True
>>> .index(3)
SyntaxError: invalid syntax
>>> num.index(3)
1
>>> num.index(8)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    num.index(8)
ValueError: 8 is not in list
