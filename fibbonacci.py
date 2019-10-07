# Una funcion que calcula el numéro n en la sequencia de Fibbonacci
def fibb(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibb(n-1) + fibb(n-2)

# La misma función, pero optimizada mediante memorizar el resultado usando un diccionario
cache = {}
def memoized_fibb(n):
    if not n in cache:
        if n == 0 or n == 1:
            cache[n] = n
        else:
            cache[n] = memoized_fibb(n-1) + memoized_fibb(n-2)

    return cache[n]
