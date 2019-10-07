import sys
from math import pi

def circle_area(radius):
  return pi * radius ** 2

# A tener en cuenta, los argumentos siempre vendran
# en forma de string. Para poder hacer operaciones
# matemáticas primero lo convertimos en un entero
r = int(sys.argv[1])

print(f"El área de un círculo de {r} cm de radio es {circle_area(r)} cm^2" )
