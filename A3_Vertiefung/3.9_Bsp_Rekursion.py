# Funktionen, die sich selbst aufrufen heißen rekursive Funktionen
# Beispiel: Berechnung der Fakultät

def faku(n):
    p = 1
    for i in range(n):
        p = p * (i + 1)
    return p


print(faku(5))


# 2.  Fakultät über Rekursion -> p = n * (n-1)
def faku2(n):
    print("n=", n)
    if n == 1:
        p = 1
    else: p = n * faku2(n - 1)
    return p


print(faku2(10))



# Fibonacci per rekursion
# fib(n) =fib(n-1)+fib(n-2) fib(2)= 2 fib(1)= 1
def fibo(k):
    if k == 1:
        p = 1
    elif k == 2:
        p = 2
    else:
        p = fibo(k - 1) + fibo(k - 2)
    return p
print(fibo(10))
