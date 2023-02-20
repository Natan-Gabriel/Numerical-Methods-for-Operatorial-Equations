from math import exp


def f(x, y):
    return 2 / 3 * exp(x) + 1 / 3 * y


def exact_solution(x):
    return exp(x)


def compute_precision(n):
    return 10 ** (-n)


def compute_max(y, m, n):
    result = 0
    for i in range(1, n + 1):
        result = max(result, abs(y[m][i] - y[m - 1][i]))
    return result


def compute_sum(x, y, m, i):
    result = 0
    for j in range(1, i + 1):
        result += (x[i] - x[j - 1]) * f(x[j - 1], y[m - 1][j - 1]) + (x[i] - x[j]) * f(x[j], y[m - 1][j])
    return result


def main():
    a = float(input("a = "))
    b = float(input("b = "))
    y_0 = float(input("y_0 = "))
    y_0_derived = float(input("y_0' = "))
    eps = int(input("eps = "))
    eps = compute_precision(eps)
    n = int(input("n = "))

    h = (b - a) / n
    x = [(a + i * h) for i in range(0, n + 1)]

    y = [[0 for _ in range(0, n + 1)]]
    for i in range(0, n + 1):
        y[0][i] = y_0 + (x[i] - x[0]) * y_0_derived

    m = 0
    while True:
        m += 1
        y.append([0 for _ in range(0, n + 1)])
        y[m][0] = y_0
        for i in range(1, n + 1):
            y[m][i] = y[0][i] + h / 2 * compute_sum(x, y, m, i)
        if compute_max(y, m, n) < eps:
            break

    print("\n" + "m =", m, '\n')
    for i in range(0, n + 1):
        print("y[" + str(m) + ", " + str(i) + "] =", y[m][i])
        print("exact_solution(" + str(x[i]) + ") =", exact_solution(x[i]))
        print("eroare =", abs(y[m][i] - exact_solution(x[i])), '\n')


# arguments: a = 0, b = 1, y_0 = 1, y_0' = 1, eps = 14, n = 10 OR n = 100 OR n = 1000;
# A part of the solution for n = 10: y[7, 5] = 1.6477524270386668, exact_solution(0.5) = 1.6487212707001282, eroare = 0.0009688436614614382
main()
