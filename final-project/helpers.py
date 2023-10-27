import random
from fractions import Fraction

def gerar_numero_fracionario():
    numerador = random.randint(1, 9)
    denominador = random.randint(2, 9)
    fracao = Fraction(numerador, denominador)
    return fracao

def gerar_numero_decimal():
    possible_divisors = [2, 4, 5, 8, 10, 20, 25, 50, 100, 125, 200, 250, 500, 1000]
    divisor = random.choice(possible_divisors)
    numerador = random.randint(1, 9 * divisor)
    numero_decimal = numerador / divisor
    return numero_decimal

def gerar_numero_ambos():
    escolha = random.choice(["fracionario", "decimal"])
    if escolha == "fracionario":
        return gerar_numero_fracionario()
    else:
        return gerar_numero_decimal()

def serialize_fraction(obj):
    if isinstance(obj, Fraction):
        return float(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")
