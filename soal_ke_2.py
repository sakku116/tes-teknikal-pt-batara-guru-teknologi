
def hitungPecahan(n):
    n = n

    print(f'uang = {n}')

    a = n // 100000
    n %= 100000

    b = n // 50000
    n %= 50000

    c = n // 20000
    n %= 20000

    d = n // 5000
    n %= 5000

    e = n // 1000
    n %= 1000

    f = n // 50
    n %= 50

    print('sisa = ', n)

    return {
        'uang 100 ribuan': a,
        'uang 50 ribuan': b,
        'uang 20 ribuan': c,
        'uang 5 ribuan': d,
        'uang 1 ribuan': e,
        'koin 50': f,
    }

print(hitungPecahan(1895250))