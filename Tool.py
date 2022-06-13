import numpy as np
import random


def Reduction(S: list, A: np.array):
    R = np.matmul(np.array(S), A)
    return R.tolist()


def CalcA(B: list, P: list):
    _B = np.linalg.inv(np.array(B))
    A = np.matmul(_B, np.matmul(np.array(P), np.array(B)))
    return A


def Randomization(h_coefficient: list, q_coefficient: list, n: int, t: int):
    random_h_coefficient = h_coefficient[:]
    for j in range(n):
        random_h_coefficient = [(random_h_coefficient[idx] + q_coefficient[idx]) for idx in range(t)]
    return random_h_coefficient


def CreatePoly(deg, E, secret):
    newPoly = [secret]
    for d in range(deg):
        random_coefficient = random.randint(1, E)
        newPoly.append(random_coefficient)
    return newPoly


def CalcPoly(poly_coefficient, number):
    add_sum = 0
    for idx, coefficient in enumerate(poly_coefficient):
        add_sum += coefficient * number ** idx
    return add_sum

def CalcLagrange(idx_list, y_list, E, t):
    add_sum = 0
    for i in range(t):
        mul_sum = 1.0
        for j in range(t):
            if i == j:
                continue
            mul_sum *= -Get_Fraction_Mod(idx_list[j], idx_list[i] - idx_list[j], E)
        add_sum += y_list[i] * mul_sum
    return add_sum % E

def Rapid_Mod(x, k, p):
    ret = 1
    while k:
        if k & 1:
            ret = ret * x % p
        k >>= 1
        x = (x * x) % p
    return ret

def Get_Fraction_Mod(numerator, denominator, p):
    return ((numerator % p) * Rapid_Mod(denominator, p - 2, p)) % p