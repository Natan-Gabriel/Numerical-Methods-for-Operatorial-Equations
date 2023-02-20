from math import exp, e


def f(t, x):
    return 2 / 3 * exp(t) + 1 / 3 * x


def exact_solution(x):
    return exp(x)


def compute_precision(n):
    return 10 ** (-n)


def compute_max(x, m, n):
    result = 0
    for i in range(1, n):
        result = max(result, abs(x[m][i] - x[m - 1][i]))
    return result


def compute_sum(x, t, a, b, m, n, i):
    result = 0
    for j in range(1, i + 1):
        result += (t[j - 1] - a) * (b - t[i]) / (b - a) * f(t[j - 1], x[m][j - 1]) + (t[j] - a) * (b - t[i]) / (b - a) * f(t[j], x[m][j])
    for j in range(i + 1, n + 1):
        result += (t[i] - a) * (b - t[j - 1]) / (b - a) * f(t[j - 1], x[m][j - 1]) + (t[i] - a) * (b - t[j]) / (b - a) * f(t[j], x[m][j])
    return result


def main():
    a = float(input("a = "))
    b = float(input("b = "))
    alpha = float(input("alpha = "))
    beta = input("beta = ")
    if beta == "e":
        beta = e
    else:
        beta = float(beta)
    eps = int(input("eps = "))
    eps = compute_precision(eps)
    n = int(input("n = "))

    t = [(a + i * (b - a) / n) for i in range(0, n + 1)]

    x = [[0 for i in range(0, n + 1)]]
    for i in range(0, n + 1):
        x[0][i] = (t[i] - a) / (b - a) * beta + (b - t[i]) / (b - a) * alpha

    x.append([0 for i in range(0, n + 1)])

    m = 1
    while compute_max(x, m, n) >= eps:
        x.append([0 for i in range(0, n + 1)])
        x[m + 1][0] = alpha
        x[m + 1][n] = beta
        for i in range(1, n):
            x[m + 1][i] = (t[i] - a) / (b - a) * beta + (b - t[i]) / (b - a) * alpha - (b - a) / (2 * n) * compute_sum(x, t, a, b, m, n, i)
        m += 1

    print("\n" + "m =", m, '\n')
    for i in range(0, n + 1):
        print("x[" + str(m) + ", " + str(i) + "] =", x[m][i])
        print("exact_solution(" + str(t[i]) + ") =", exact_solution(t[i]))
        print("eroare =", abs(x[m][i] - exact_solution(t[i])), '\n')


# arguments: a = 0, b = 1, alpha = 1, beta = e, eps = 14, n = 10 OR n = 100 OR n = 1000;
# A part of the solution for n = 10: x[12, 5] = 1.648890586838407, exact_solution(0.5) = 1.6487212707001282, eroare = 0.00016931613827875225
main()
