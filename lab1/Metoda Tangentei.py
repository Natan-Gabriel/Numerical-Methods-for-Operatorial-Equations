def f(x):
    return x**2 - 3

def df(x):
    return 2*x

def compute_precision(n):
    return 10 ** (-n)

def main():
    a = float(input("a = "))
    b = float(input("b = "))
    eps = int(input("eps = "))
    eps = compute_precision(eps)
    dda = float(input("dda = "))

    x = [b]

    if f(a) * dda > 0:
        x[0] = a

    x.append(x[0] - f(x[0])/df(x[0]))

    n = 1
    while abs(x[n] - x[n-1]) >= eps:
        x.append(x[n] - f(x[n])/df(x[n]))
        n += 1

    print("n = ", n)
    print("x[n] = ", x[n])


# arguments: a = 0, b = 2, eps = 3, dda = 2
main()