import sys
import fibbonacci

# Otra vez, convierto la string a entero
max_number = int(sys.argv[1])

# Imprimo los primeros 100 números de la serie de Fibbonacci
for n in range(0, max_number):
    print(n, fibbonacci.memoized_fibb(n))
