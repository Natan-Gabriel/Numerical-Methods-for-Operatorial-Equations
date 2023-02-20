from math import exp, cos, sin, pi


def r(x):
    return 1


def f(x):
    return 2 * exp(-x) * cos(x) + exp(-x) * sin(x)


def exact_solution(x):
    return exp(-x) * sin(x)


def main():
    a = float(input("a = "))
    b = input("b = ")
    if b == "pi":
        b = pi
    else:
        b = float(b)
    n = int(input("n = "))

    h = (b - a) / n
    z = -1
    t = [(a + i * h) for i in range(0, n + 1)]

    rr = [(r(t[i]) * h**2) for i in range(0, n)]
    ff = [(f(t[i]) * h**2) for i in range(0, n)]
    y = [(2 + rr[i]) for i in range(0, n)]

    u = [0 for _ in range(0, n)]
    w = [0 for _ in range(0, n)]
    u[1] = z / y[1]
    for i in range(2, n - 1):
        w[i] = y[i] - u[i - 1] * z
        u[i] = z / w[i]

    w[n - 1] = y[n - 1] - u[n - 2] * z

    p = [0 for _ in range(0, n)]
    p[1] = ff[1] / 2
    for i in range(2, n):
        p[i] = (ff[i] - z * p[i - 1]) / w[i]

    v = [0 for _ in range(0, n + 1)]
    v[n - 1] = p[n - 1]
    for i in range(n - 2, 0, -1):
        v[i] = p[i] - u[i] * v[i + 1]

    print()
    for i in range(0, n + 1):
        print("v[" + str(i) + "] =", v[i])
        print("exact_solution(" + str(t[i]) + ") =", exact_solution(t[i]))
        print("eroare =", abs(v[i] - exact_solution(t[i])), '\n')


# arguments: a = 0, b = pi, n = 10 OR n = 100 OR n = 1000;
# A part of the solution for n = 10: v[5] = 0.20558067687231887, exact_solution(1.5707963267948966) = 0.20787957635076193, eroare = 0.002298899478443056
main()
