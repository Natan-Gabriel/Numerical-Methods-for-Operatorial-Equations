def f(x):
    return x ** 2 - 2

def ddf(x):
    return 2

def compute_precision(n):
    return 10 ** (-n)

def compute_next(x):
    return x - f(x) ** 2 / (f(x + f(x)) - f(x))

def main():
    a = float(input("a = "))
    b = float(input("b = "))
    eps = int(input("eps = "))
    eps = compute_precision(eps)
    # dda = float(input("dda = "))
    dda = ddf(a)

    x = [b]

    if f(a) * dda > 0:
        x[0] = a

    x.append(compute_next(x[0]))

    n = 1
    while abs(x[n] - x[n - 1]) >= eps:
        x.append(compute_next(x[n]))
        n += 1

    print("n =", n)
    print("x[n] =", x[n])


# arguments: a = 1, b = 2, eps = 4; expected solution: n = 5, x[n] = 1.4142135638571252
main()