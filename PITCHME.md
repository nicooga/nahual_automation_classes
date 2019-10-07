# Python: diccionarios

---

El diccionario es una estructura de datos, que relaciona claves con valores (key/values).

También conocidos como:

- associative/relational arrays (arreglos relacionales)
- maps (mapas)
- hashes
- tables (tablas)

---

#### Características

- las claves son únicas, no se pueden repetir
- tanto claves como valores pueden ser cualquier tipo de dato
- mayormente se usan cadenas (strings) como claves para un diccionario

---

#### Operaciones. Que podemos hacer con un diccionario?

---

##### Creación

```python
# creamos un diccionario vacío
dict_a = {}

# creamos un diccionario con algunos valores
dict_b = { 'clave': 'valor', 1: 2, 'Argentina': 'Buenos Aires', 'Lima': 'Peru', 'Chile': 'Santiago de Chile' }
```

---

##### Seteo de valores

Para setear valores usanmos el operador especial `diccionario[...]=`

```python
# seteamos el valor de la clave '`otra_clave`' para que apunte al valor `True`
dict_b['otra_clave'] = True
```

---

##### Búsqueda de valores

Para buscar valores usanmos el operador especial `diccionario[...]`

```python
# le preguntamos al diccionario cual es el valor que le corresnde a la clave `'clave'`
dict_b['clave']
# => 'valor'
```

---

##### Iteración

Tal vez lo mas interesante y util de un diccionario: el hecho de que es una colección y podemos iterar sobre sus valores de forma sequencial.

```python
for key in dict_b:
  print(f'La clave "{key}" apunta al valor "{dict_b[key]}"')

## Imprime en la consola =>
# La clave "clave" apunta al valor "valor"
# La clave "1" apunta al valor "2"
# La clave "Argentina" apunta al valor "Buenos Aires"
# La clave "Lima" apunta al valor "Peru"
# La clave "Chile" apunta al valor "Santiago de Chile"
```

---

#### Casos de uso

Los diccionarios son colecciones, y constituyen un bloque de construcción básico con el que podemos contar a la hora de programar.

---

##### Memoizing

Un ejemplo claro y bastante común del uso de un diccionario en todos los lenguajes es el memoizing.

---


El memoizing consisite en recordar el resultado de una función según el valor del argumento, de forma que nos nos ahorremos volver a calcular el resultado de la función la segunda vez nos pidan un valor.

---

Por ejemplo tenemos una función `fibb(n)` que calcula el número #n de la serie de Fibbonacci usando recursión:

```python
def fibb(n):
  if n == 0 or n === 1:
    return n
  else:
    return fibb(n - 1) + fibb(n - 2)
```

---

Usando esta función podemos imprimir todos los números de la serie de Fibbonacci de forma sequencial:

```python
for n in range(1, 100):
  print(fibb(n))
```

Pero pasando el 30º (treintaavo) número se vuelve muy lenta la ejecución, porque la función tiene que calcular el valor de todos los números anteriores para poder calcular un solo número de la serie.

---

Con la ayuda de un diccionario podemos memorizar el resultado de `fibb(n)` para cada valor de `n`:

```python
cache = {} # Un diccionario donde vamos a almacenar los resultados

def fibb(n):
  # si el resultado no esta "cacheado",
  # lo calculamos y lo guardamos en el cache
  if not n in cache:
    if n == 0 or n === 1:
      cache[n] = n
    else:
      cache[n] = fibb(n - 1) + fibb(n - 2)

  # finalmente devolvemos el valor que si o si
  # va a estar cacheado para cuando se ejecute esta linea de código
  return cache[n]
```

---

De esta forma nuestra función se vuelve exponencialmente más rápida:

```python
for n in range(1, 100):
  print(fibb(n))
```

---

# Python: argumentos de linea de comando

---

Los argumentos de linea de comando permiten especificar parametros según los cuales va a correr nuestro programa,
de la misma forma en que una funcion puede opcionalmente tomar parámetros.

---

Ésta es una funcionalidad común a muchos lenguages de scripting, no solo Python.

---

Cuando ejecutamos nuestro programa usando el comando `python` desde linea de comando, podemos pasar adicionalmente cualquier número de parametros que queramos:

```bash
$ python programa.py argumento1 argumento2
```

---

Los argumentos se harán disponibles a nuestro programa a traves de `sys.argv`

```python
# programa.py
import sys
print('Los argumentos que me diste son:', sys.argv)
```

---

### Casos de uso

Los argumentos de linea de comando nos permiten facilmente proveer parametros a nuestro programa.

---

Por ejemplo, supongamos que escribimos un programa que calcula el area de un círculo:

```python
import sys
from math import pi

def circle_area(radius):
  return pi * radius ** 2

r = int(sys.argv[1])
print(f"El área de un círculo de {r} cm de radio es {circle_area(r)} cm^2" )
```

---

Ahora podemos facilmente saber el área de cualquier círculo:

```bash
$ python circle_area.py 1099
# El área de un círculo de 1099 cm radio es 3794418.7485984056 cm^2

$ python circle_area.py 10991923
# El área de un círculo de 10991923 cm radio es 379574673870376.44 cm^2
```

---

Otro ejemplo, volviendo a la serie de Fibbonacci:

```python
# Supongamos que importo la función `fibb` desde otro archivo..

import sys
import fibbonacci

# Otra vez, convierto la string a entero
max_number = int(sys.argv[1])

# Imprimo los primeros 100 números de la serie de Fibbonacci
for n in range(0, max_number):
    print(n, fibbonacci.memoized_fibb(n))
```

---

Ahora tengo un programa que me imprime los primeros `n` números de la serie de Fibbonacci:

```bash
$ python fibbonacci2.py 100
# Imprime:
# 0 0
# 1 1
# 2 1
# 3 2
# 4 3
# 5 5
# 6 8
# 7 13
# 8 21
# ...
```
