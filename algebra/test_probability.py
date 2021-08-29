from probability import (
    normal_approximation_to_binomial,
    normal_two_sided_bounds,
    normal_probability_between
)

# lançamento de uma moeda 1000 vezes
# nossa hipótese é de honestidade 0.5
# mu (média) = 500
# sigma (desvio padrão) = 15.8
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

# print(f'{mu_0=}\n{sigma_0=}')

# significância (entre 5% e 1%)
# fazer erro do tipo 1 (falso positivo)
normal_two = normal_two_sided_bounds(0.95, mu_0, sigma_0)

# print(f'{normal_two=}')

# erro tipo 2 (falso negativo)

# 95% dos limites baseados na premissa p é 0.5
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

# print(f'{lo=}\n{hi=}')


# mi e sigma reais baseados em p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# print(f'{mu_1=}\n{sigma_1=}')


# um erro tipo 2 significa que falhamos ao rejeitar a hipótese nula
# que acontecerá quando X ainda estiver em nosso intervalo original
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability

print(f'{power=}')


