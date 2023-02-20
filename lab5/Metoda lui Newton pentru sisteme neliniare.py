from math import sqrt


def f(x, y):
    return x ** 2 + y ** 2 - 10


def g(x, y):
    return sqrt(x + y) - 2


def dfdx(x, y):
    return 2 * x


def dfdy(x, y):
    return 2 * y


def dgdx(x, y):
    return 1 / (2 * sqrt(x + y))


def dgdy(x, y):
    return 1 / (2 * sqrt(x + y))


def compute_precision(n):
    return 10 ** (-n)


def j(x, y):
    return dfdx(x, y) * dgdy(x, y) - dfdy(x, y) * dgdx(x, y)


def compute_next_element_in_x(x, y, j_x_y):
    return x - (f(x, y) * dgdy(x, y) - g(x, y) * dfdy(x, y)) / j_x_y


def compute_next_element_in_y(x, y, j_x_y):
    return y - (dfdx(x, y) * g(x, y) - dgdx(x, y) * f(x, y)) / j_x_y


def main():
    x_0 = float(input("x[0] = "))
    y_0 = float(input("y[0] = "))
    eps = int(input("eps = "))
    eps = compute_precision(eps)

    j_x_y = j(x_0, y_0)
    x = [x_0, compute_next_element_in_x(x_0, y_0, j_x_y)]
    y = [y_0, compute_next_element_in_y(x_0, y_0, j_x_y)]

    n = 1
    while abs(x[n] - x[n - 1]) >= eps or abs(y[n] - y[n - 1]) >= eps:
        j_x_y = j(x[n], y[n])
        x.append(compute_next_element_in_x(x[n], y[n], j_x_y))
        y.append(compute_next_element_in_y(x[n], y[n], j_x_y))
        n += 1

    print("n =", n)
    print("x[n] =", x[n])
    print("y[n] =", y[n])


# arguments: x[0] = 0.9, y[0] = 3.1, eps = 4; solution: n = 3, x[n] = 0.9999999999471225, y[n] = 3.0000000000528777
main()
