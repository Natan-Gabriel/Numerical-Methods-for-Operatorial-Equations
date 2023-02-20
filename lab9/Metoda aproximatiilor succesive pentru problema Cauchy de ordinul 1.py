from math import exp


def f(x, y):
    return x + y


def exact_solution(x):
    return 2 * exp(x) - x - 1


def compute_precision(n):
    return 10 ** (-n)


def compute_sum(x, y, m, i):
    result = 0
    for j in range(1, i + 1):
        result += f(x[j - 1], y[m][j - 1]) + f(x[j], y[m][j])
    return result


def compute_max(y, m, n):
    result = 0
    for i in range(1, n + 1):
        result = max(result, abs(y[m][i] - y[m - 1][i]))
    return result


def main():
    a = float(input("a = "))
    b = float(input("b = "))
    y_0 = float(input("y[0] = "))
    eps = int(input("eps = "))
    eps = compute_precision(eps)
    n = int(input("n = "))

    x = [a]
    h = (b - a) / n

    for i in range(1, n + 1):
        x.append(a + i * h)

    y = [[y_0 for _ in range(n + 1)]]

    y.append([0 for _ in range(n + 1)])
    y[1][0] = y_0
    for i in range(1, n + 1):
        y[1][i] = y_0 + (b - a) / (2 * n) * compute_sum(x, y, 0, i)

    m = 1
    while compute_max(y, m, n) >= eps:
        y[m][0] = y_0
        y.append([0 for _ in range(n + 1)])
        for i in range(1, n + 1):
            y[m + 1][i] = y_0 + (b - a) / (2 * n) * compute_sum(x, y, m, i)
        m += 1

    y[m][0] = y_0

    print('\n' + "Ultima iteratie este m =", m, '\n')
    for i in range(0, n + 1):
        print("y[" + str(m) + ", " + str(i) + "] =", y[m][i])
        print("exact_solution(" + str(x[i]) + ") =", exact_solution(x[i]))
        print("eroare =", abs(y[m][i] - exact_solution(x[i])), '\n')


# arguments: a = 0, b = 1, y[0] = 1, eps = 14, n = 10 OR n = 100 OR n = 1000;
# A part of the solution for n = 10: y[18, 5] = 1.798818827518609, exact_solution(0.5) = 1.7974425414002564, eroare = 0.0013762861183526098
main()
