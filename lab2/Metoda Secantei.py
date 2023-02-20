def f(x):
    return x ** 3 - x - 1

def compute_precision(n):
    return 10 ** (-n)

def main():
    a = float(input("a = "))
    b = float(input("b = "))
    eps = int(input("eps = "))
    eps = compute_precision(eps)
    x_0 = float(input("x[0] = "))
    x_1 = float(input("x[1] = "))

    x = [x_0, x_1]

    n = 1
    while abs(x[n] - x[n - 1]) >= eps:
        x.append(x[n] - f(x[n]) * (x[n] - x[n - 1]) / (f(x[n]) - f(x[n - 1])))
        n += 1

    print("n =", n)
    print("x[n] =", x[n])


# arguments: a = 1, b = 2, eps = 4, x[0] = 2, x[1] = 1.5; expected solution: n = 6, x[n] = 1.3247179601803296
main()