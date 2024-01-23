import random
from fractions import Fraction

# Gerar as frações que serão usadas para formar as cartelas fracionárias
def gerar_fracoes_unicas(qtd_numeros, max_numerador=99):
    fracoes_unicas = set()

    # Ajuste dos denominadores para que sejam apenas potências de 2 e/ou 5
    denominadores = [2**i * 5**j for i in range(6) for j in range(6) if 2**i * 5**j <= 10]

    # Gera todas as frações possíveis com numerador e denominador que não formem dízimas
    for numerador in range(1, max_numerador + 1):
        for denominador in denominadores:
            fracao = Fraction(numerador, denominador)

            # Garante que a fração não é um número inteiro e que está na forma mais simplificada
            if fracao.denominator != 1 and fracao == fracao.limit_denominator():
                fracoes_unicas.add(fracao)

            # Se já temos frações suficientes, podemos parar de gerar mais
            if len(fracoes_unicas) == qtd_numeros:
                break
        if len(fracoes_unicas) == qtd_numeros:
            break

    # Se não conseguimos gerar frações suficientes, levantamos um erro
    if len(fracoes_unicas) < qtd_numeros:
        raise ValueError("Não foi possível gerar a quantidade solicitada de frações únicas que não formem dízimas.")

    # Embaralha as frações para garantir aleatoriedade e converte para strings
    fracoes_unicas = list(fracoes_unicas)
    random.shuffle(fracoes_unicas)

    # Seleciona a quantidade desejada de frações
    fracoes_selecionadas = fracoes_unicas[:qtd_numeros]

    # Converte as frações para strings no formato "numerador/denominador"
    return [f"{fracao.numerator}/{fracao.denominator}" for fracao in fracoes_selecionadas]

# Gerar os números decimais que serão usados para gerar as cartelas decimais
def gerar_numero_decimal(qtd_numeros):
    decimais = []
    for _ in range (qtd_numeros):
        possible_divisors = [2, 4, 5, 8, 10, 20, 25, 50, 100, 125, 200, 250, 500, 1000]
        divisor = random.choice(possible_divisors)
        numerador = random.randint(1, 9 * divisor)
        numero_decimal = numerador / divisor
        decimais.append(numero_decimal)
    return decimais

# Converte um decimal em sua fração equivalente, para usar no sorteio de cartelas decimais
def decimal_para_fracao_irredutivel(decimal):
    """Converte um decimal para a sua forma de fração irredutível."""
    fracao = Fraction(decimal).limit_denominator()  # Convertendo para fração e limitando o denominador
    return fracao