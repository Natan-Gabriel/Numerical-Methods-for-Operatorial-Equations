def f(t, x):
    return 23 / (t + 1) ** 5 + x ** 5


def exact_solution(t):
    return 1 / (t + 1)


def h(t, s, a, b):
    return 1 / 6 * ((s - a) / (b - a)) ** 2 * (1 - (t - a) / (b - a)) ** 2 * ((t - a) / (b - a) - (s - a) / (b - a) + 2 * (1 - (s - a) / (b - a)) * ((t - a) / (b - a)))


def k(t, s, a, b):
    return 1 / 6 * ((t - a) / (b - a)) ** 2 * (1 - (s - a) / (b - a)) ** 2 * ((s - a) / (b - a) - (t - a) / (b - a) + 2 * (1 - (t - a) / (b - a)) * ((s - a) / (b - a)))


def compute_precision(n):
    return 10 ** (-n)


def compute_sum(x, t, i, m, n, a, b):
    result = 0
    for j in range(1, i + 1):
        result += h(t[i], t[j - 1], a, b) * f(t[j - 1], x[m - 1][j - 1]) + h(t[i], t[j], a, b) * f(t[j], x[m - 1][j])
    for j in range(i + 1, n + 1):
        result += k(t[i], t[j - 1], a, b) * f(t[j - 1], x[m - 1][j - 1]) + k(t[i], t[j], a, b) * f(t[j], x[m - 1][j])
    return result


def compute_max(x, m, n):
    result = 0
    for i in range(1, n):
        result = max(result, abs(x[m][i] - x[m - 1][i]))
    return result


def main():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    d = float(input("d = "))
    w = float(input("w = "))
    r = float(input("r = "))
    eps = int(input("eps = "))
    eps = compute_precision(eps)
    n = int(input("n = "))

    t = [(a + i * (b - a) / n) for i in range(0, n + 1)]

    g = [0 for _ in range(0, n + 1)]
    for i in range(0, n + 1):
        g[i] += (b - t[i]) ** 2 * (2 * (t[i] - a) + (b - a)) * c / (b - a)**3
        g[i] += (t[i] - a) ** 2 * (2 * (b - t[i]) + (b - a)) * d / (b - a)**3
        g[i] += (b - t[i]) ** 2 * (t[i] - a) * w / (b - a)**2
        g[i] -= (t[i] - a) ** 2 * (b - t[i]) * r / (b - a)**2

    x = [[g[i] for i in range(0, n + 1)]]

    m = 0
    while True:
        m += 1
        x.append([0 for _ in range(0, n + 1)])
        x[m][0] = c
        x[m][n] = d
        for i in range(1, n):
            x[m][i] = g[i] + (b - a) / (2 * n) * compute_sum(x, t, i, m, n, a, b)
        if compute_max(x, m, n) < eps:
            break

    print("\n" + "m =", m, '\n')
    for i in range(0, n + 1):
        print("x[" + str(m) + ", " + str(i) + "] =", x[m][i])
        print("exact_solution(" + str(t[i]) + ") =", exact_solution(t[i]))
        print("eroare =", abs(x[m][i] - exact_solution(t[i])), '\n')


# arguments: a = 0, b = 1, c = 1, d = 0.5, w = -1, r = -0.25, eps = 14, n = 10 OR n = 100 OR n = 1000;
# A part of the solution for n = 10: x[6, 4] = 0.7142773480157082, exact_solution(0.4) = 0.7142857142857143, eroare = 8.366270006110454e-06
main()
