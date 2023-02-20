def f(x):
    return x ** 3 - x - 1

def df(x):
    return 3 * x**2 - 1

def ddf(x):
    return 6 * x

def compute_precision(n):
    return 10 ** (-n)

def compute_next_element(x):
    return x - 2 * f(x) * df(x) / (2 * df(x) * df(x) - f(x) * ddf(x))

def main():
    a = float(input("a = "))
    b = float(input("b = "))
    eps = int(input("eps = "))
    eps = compute_precision(eps)

    x = [b]

    if f(a) * ddf(a) > 0:
        x[0] = a

    x.append(compute_next_element(x[0]))

    n = 1
    while abs(x[n] - x[n - 1]) >= eps:
        x.append(compute_next_element(x[n]))
        n += 1

    print("n =", n)
    print("x[n] =", x[n])


# arguments: a = 1, b = 2, eps = 4; expected solution: n = 4, x[n] = 1.324717957244746
main()
