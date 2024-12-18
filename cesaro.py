import random
import math


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def calculate_pi(iters):
    primes_counter = 0

    for _ in range(iters):
        x = random.randint(1, 1000000)
        y = random.randint(1, 1000000)
        if nwd(x, y) == 1:
            primes_counter += 1

    probability = primes_counter / iters
    calculated_pi = math.sqrt(6 / probability)
    return calculated_pi


if __name__ == '__main__':
    iterations = 30000000
    pi_value = calculate_pi(iterations)
    print(f'Przybliżona wartość liczby pi po {iterations} iteracjach wynosi: {pi_value}')
