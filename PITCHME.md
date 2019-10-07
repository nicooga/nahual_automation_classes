# Python: diccionarios

```python
{}
```

---

### Python: diccionarios

El diccionario es una estructura de datos, que relaciona claves con valores (key/values).

También conocidos como:

- associative/relational arrays (arreglos relacionales)
- maps (mapas)
- hashes
- tables (tablas)

---

### Python: diccionarios
#### Características

- las claves son únicas, no se pueden repetir
- tanto claves como valores pueden ser cualquier tipo de dato
- mayormente se usan cadenas (strings) como claves para un diccionario

---

### Python: diccionarios
#### Operaciones. Que podemos hacer con un diccionario?

##### Creación

```python
dict_a = {} # creamos un diccionario vacío
dict_b = { 'clave': 'valor', 1: 2, 'Argentina': 'Buenos Aires', 'Lima': 'Peru', 'Chile': 'Santiago de Chile' } # creamos un diccionario con algunos valores
```

##### Seteo de valores

```python
dict_b['otra_clave'] = True # seteamos el valor de la clave '`otra_clave`' para que apunte al valor `True`
```

##### Búsqueda de valores

```python
dict_b['clave'] # le preguntamos al diccionario cual es el valor que le corresnde a la clave `'clave'`
# => 'valor'
```

##### Iteración

Tal vez lo mas interesante y util de un diccionario: el hecho de que es una colección y podemos iterar sobre sus valores de forma sequencial:

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

### Python: diccionarios
#### Casos de uso

Los diccionarios son colecciones, y constituyen un bloque de construcción básico con el que podemos contar a la hora de programar.

##### Memoizing

Un ejemplo claro y bastante común del uso de un diccionario en todos los lenguajes es el memoizing.
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

Usando esta función podemos imprimir todos los números de la serie de Fibbonacci de forma sequencial:

```python
for n in range(1, 100):
  print(fibb(n))
```

Pero pasando el 30º (treintaavo) número se vuelve muy lenta la ejecución, porque la función tiene que calcular el valor de todos los números anteriores para poder calcular un solo número de la serie.

---

Con la ayuda de un diccionario podemos memorizar el resultado de `fibb(n)` para cada valor de `n`:

```python
cache = {} # Un diccionario donde vamos a almacenar los 

def fibb(n):
  # si el resultado no esta "cacheado", lo calculamos y lo guardamos en el cache
  if not n in cache:
    if n == 0 or n === 1:
      cache[n] = n
    else:
      cache[n] = fibb(n - 1) + fibb(n - 2)

  # finalmente devolvemos el valor que si o si va a estar cacheado para cuando se ejecute esta linea de código
  return cache[n]
```

De esta forma nuestra función se vuelve exponencialmente más rápida:

```python
for n in range(1, 100):
  print(fibb(n))
```
