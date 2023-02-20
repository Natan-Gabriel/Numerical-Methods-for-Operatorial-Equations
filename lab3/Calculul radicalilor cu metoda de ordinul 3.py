def compute_precision(n):
    return 10 ** (-n)


def compute_next_element(x, a):
    return x * (x**2 + 3 * a) / (3 * x**2 + a)


def main():
    a = float(input("a = "))
    eps = int(input("eps = "))
    eps = compute_precision(eps)

    x = [a]

    x.append(compute_next_element(x[0], a))

    n = 1
    while abs(x[n] - x[n - 1]) >= eps:
        x.append(compute_next_element(x[n], a))
        n += 1

    print("n =", n)
    print("x[n] =", x[n])


# arguments: a = 2, eps = 4; expected solution: n = 3, x[n] = 1.414213562373095
main()
