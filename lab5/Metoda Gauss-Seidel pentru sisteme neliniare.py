from math import sqrt, log


def f1(x, y, z):
    return sqrt(0.5 * (y * z + 5 * x - 1))


def f2(x, y, z):
    return sqrt(2 * x + log(z))


def f3(x, y, z):
    return sqrt(x * y + 2 * z + 8)


def compute_precision(n):
    return 10 ** (-n)


def main():
    x_0 = float(input("x[0] = "))
    y_0 = float(input("y[0] = "))
    z_0 = float(input("z[0] = "))
    eps = int(input("eps = "))
    eps = compute_precision(eps)

    x = [x_0, f1(x_0, y_0, z_0)]
    y = [y_0, f2(x_0, y_0, z_0)]
    z = [z_0, f3(x_0, y_0, z_0)]

    n = 1
    while abs(x[n] - x[n - 1]) >= eps or abs(y[n] - y[n - 1]) >= eps or abs(z[n] - z[n - 1]) >= eps:
        x.append(f1(x[n], y[n], z[n]))
        y.append(f2(x[n + 1], y[n], z[n]))
        z.append(f3(x[n + 1], y[n + 1], z[n]))
        n += 1

    print("n =", n)
    print("x[n] =", x[n])
    print("y[n] =", y[n])
    print("z[n] =", z[n])


# arguments: x[0] = 10, y[0] = 10, z[0] = 10, eps = 4; solution: n = 17, x[n] = 4.529414513683486, y[n] = 3.291201619677754, z[n] = 5.88950849033705
main()
