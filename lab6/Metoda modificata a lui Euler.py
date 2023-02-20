from math import exp


def f(x, y):
    return x + y


def exact_solution(x):
    return 2 * exp(x) - x - 1


def main():
    x_0 = float(input("x[0] = "))
    y_0 = float(input("y[0] = "))
    t = float(input("T = "))
    n = int(input("n = "))

    h = t / n
    x = [x_0]
    y = [y_0]
    k = [0]
    u = [0]

    for i in range(1, n + 1):
        x.append(x[0] + i * h)
        k.append(f(x[i - 1], y[i - 1]))
        u.append(f(x[i - 1] + h/2, y[i - 1] + h/2 * k[i]))
        y.append(y[i - 1] + h * u[i])
        print("y[" + str(i) + "] =", y[i])
        print("exact_solution(" + str(x[i]) + ") =", exact_solution(x[i]))
        print("eroare =", abs(y[i] - exact_solution(x[i])), '\n')


# arguments: x[0] = 0, y[0] = 1, t = 1, n = 10 OR n = 100 OR n = 1000;
# A part of the solution for n = 10: y[5] = 1.7948935318812502, exact_solution(0.5) = 1.7974425414002564, eroare = 0.0025490095190061623
main()
