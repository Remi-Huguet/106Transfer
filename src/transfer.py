from sys import argv
from typing import List


def calcul_eq(I: List[str], j: float) -> float:
    result: float = 0
    n: int = len(I) - 1
    while n >= 0:
        result = (result * j) + float(I[n])
        n = n - 1
    return result


def main() -> int:
    result: float = 1.000
    a: float = 0.000
    n: int = len(argv)

    while a <= 1.001:
        for b in range(1, n, 2):
            den_I = argv[b + 1].split("*")
            num_I = argv[b].split("*")
            num = calcul_eq(num_I, a)
            den = calcul_eq(den_I, a)
            if den == 0:
                print("division par 0")
                exit(84)
            result = result * (float(num) / float(den))
        print(f"{a:.3f} -> {result:.5f}")
        a = a + 0.001
        result = 1.000
    return 0
