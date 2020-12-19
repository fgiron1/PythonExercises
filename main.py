def fib(n):
    a, b = 0, 1
    lista = []
    while a < n:
        lista.append(a)
        a, b = b, a+b
    return lista
