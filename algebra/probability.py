"""
Obter número par?
Experimento Aleatório: Lançamento de dado
Espaço Amostral: 1 2 3 4 5 6
Evento: 2 4 6

P(E) = número de elementos do evento / número de elementos do Espaço Amostral
P(E) = 2 4 6 / 1 2 3 4 5 6 -> 3/6 -> 1/2

Eventos Independentes: Mesmo Espaço Amostral
P(A e B) = P(A) * P(B)

Eventos Dependentes: Mudança do Espaço Amostral
p(A e B) = P(A)/EA1 * P(B)/EA2

Condicional
P(E|F) = P(E, F) / P(F)
Dada a condição do evento ser Homem ou Mulher
---------------------------------------------------------------
| NACIONALIDADE         HOMEM           MULHER           TOTAL |
---------------------------------------------------------------
| BRASILEIROS           27              14               41    |
| ARGENTINOS            23              16               39    |
---------------------------------------------------------------
| TOTAL                 50              30               80    |
---------------------------------------------------------------
P(BRA, H) = 27/80
P(ARG, H) = 23/80
P(H) = 50/80
P(BRA, H) = (27/80)/(50/80) = 27/50
p(ARG, H) = (23/80) / (50/80) = 23/50

P(M) = 1/2
P(H, H) = 1/4
P(M, M) = 1/4
P(M, H) = 1/2
P((M,M), M) = (1/4) / (1/2) = 1/2
"""
import random
from math import pi, sqrt, exp, erf


def random_kid():
    return random.choice(["boy", "girl"])


"""
# ambas as meninas 
{'younger': 'girl', 'older': 'girl'}
"""
both_girls = 0
"""
# menina mais velha 
[
    {'younger': 'girl', 'older': 'girl'}, 
    {'younger': 'boy', 'older': 'girl'},
]
"""
older_girl = 0

"""
# qualquer uma das meninas     
[
    {'younger': 'girl', 'older': 'girl'}, 
    {'younger': 'boy', 'older': 'girl'}, 
    {'younger': 'girl', 'older': 'boy'}
]
"""
either_girl = 0

both_boy = 0  # ambas as meninos
older_boy = 0  # menino mais velho
either_boy = 0  # qualquer um dos meninos

random.seed(0)
for _ in range(10000):
    younger = random_kid()  # Mais jovem
    older = random_kid()  # Mais velho
    if older == 'girl':
        older_girl += 1
    if older == 'girl' and younger == 'girl':
        both_girls += 1
    if older == 'girl' or younger == 'girl':
        either_girl += 1
    if older == 'boy':
        older_boy += 1
    if older == 'boy' and younger == 'boy':
        both_boy += 1
    if older == 'boy' or younger == 'boy':
        either_boy += 1

# print(f'{both_girls=} # ambas as meninas \n'
#       f'{older_girl=} # menina mais velha\n'
#       f'{either_girl=} # qualquer uma das meninas\n\n')
#
# print(f'({both_girls=}) / ({older_girl=}) = ', both_girls / older_girl)
# print(f'({both_girls=}) / ({either_girl=}) = ', both_girls / either_girl)
#
# print(f'\n({both_boy=}) / ({older_boy=}) = ', both_boy / older_boy)
# print(f'({both_boy=}) / ({either_boy=}) = ', both_boy / either_boy)

"""
Thomas Bayes 1701 - 1761
Teorema de Bayes 1763

P(Ai|A) = P(Ai e A) / P(A)

(P(Ai) * P(A|Ai)) / (P(Ai) * P(A|Ai) + ... + P(An) * P(A|An))

=======================================================================================================================

https://www.youtube.com/watch?v=9OOZf4klOeM

Exemplo 1
Numa indústria, os parafusos são feitos em duas máquinas: A e B. 
A Primeira é responsável por 30% da produção e a outra pelo restante.
A máquina A produz 2% de peças defeituosas e a B produz 1%

a) Qual a probabilidade de ser produzida uma peça defeituosa?

D -> Defeituosa
                                Eventos distintos
P(D) -> P[(A e B) u (B e D)] = P(A e D) + P(B e D)

                . 2% (D|A)
              . 
             o
           .  .
     30% .      . 98 %
       .
     o 
       .
        .       . 1% (D|B)
      70% .   .
            o
              .
                . 99%
             
P(D) = (P(A) * P(D|A)) + (P(B) * P(D|B))  
P(D) = (0.3 * 0.02) + (0.7 * 0.01)

b) Qual a probabilidade de uma peça defeituosa ter sido produzida pela máquina A?

P(A|D) = P(A e D) / P(D)
P(A|D) = P(A) * P(D|A) / (P(A) * P(D|A) + P(B) * P(D|B))
P(A|D) = 0.3 * 0.02 / ((0.3 * 0.02) + (0.7 * 0.01)) = 46.1%

=======================================================================================================================

https://www.youtube.com/watch?v=I643PqSrETM
Exemplo 2
- Acerto do teste 90%
- 1% da população tem a doença
- População 1000 
    - 99% de 1000 = 990 não tem
        - 90% de 990 = 891 acertos
        - 10% de 990 = 99 erros
    - 1% de 1000 = 10 tem
        - 90% de 10 = 9 acertos
        - 10% de 10 = 1 erro
        
99 + 9 = 108 pessoas positivo para a doença, sendo que 9 realmente tinham a doença

P(A) = 9 / 108 = 8.3%

- São dois eventos:
    - A Ter a doença
    - B Exame positivo
    
- Dado que o exame deu positivo, qual a probabilidade de ter a doença?

P(B|A) * P(A)  # B Probabilidade do exame positivo, A já tendo a doença
P(B|Ã) * P(Ã)  # B Probabilidade do exame positivo, Â não tendo a doença

P(A|B) = P(B|A) * P(A) / P(B)

P(B) = P(B|A) * P(A) + P(B|Ã) * P(Ã)

P(A|B) = 0.9 * 0.01 / 0.9 * 0.01 + 0.1 * 0.99 = 8.3%

"""

"""

https://www.youtube.com/watch?v=4EgmVmryowE : Estatística - Aula 09 - Variáveis Aleatórias

Variável Aleatória

Exemplo 1

     A   a
    -------
A  | AA  Aa
a  | Aa  aa

P(AA) = 1/4
P(Aa) = 1/2
P(aa) = 1/4
-----------------
Exemplo 2

Numa agencia bancaria existem 5 caixas eletronicos, sendo a probabilidade es estar ocupado 0.4.
Qual função descreve a probabilidade de utilização dos diferente caixas?

X: Números de caixas ocupados

X = 0 1 2 3 4 5

Probabilidade de o caixa estar desocupado, sendo 0.4 de ocupado menos 1 = 0.6

P(X = 0) = 0.6^5                = 0.07776
P(X = 1) = 5 * 0.4 * 0.6^4      = 0.2592
P(X = 2) = 10 * 0.4^2 * 0.6^3   = 0.3456
P(X = 3) = 10 * 0.4^3 * 0.6^2   = 0.2304
P(X = 4) = 5 * 0.4^4 * 0.6      = 0.0768
P(X = 5) = 0.4^5                = 0.01024

 

P(X = k) = C x,k * 0.4^k * 0.6^(5-k)

          5           5!          5 * 4 * 3!    5 * 4     20
C x,k    --- =   ------------  = ----------- = ------- = --- = 10
          2       2!(5 - 2)!         2!3!         2       10


X = 5 caixas

# Discreta Propriedades

a) P(X = Xo) >= 0
b) ∑ P(X = Xo) = 1

# Continua Propriedades
- Associada a um intervalo
a) f(x) >= 0

   a 
b) ∫ f(x)dx = P(a < x <= b), b > a
   b
   
  +∞   
c) ∫ f(x)dx = 1
  -∞

"""


# X e X + h = h * f(x) se h for pequeno
def uniform_probability_density(x: float) -> int:
    return 1 if 0 <= x < 1 else 0


assert uniform_probability_density(0.1) == 1
assert uniform_probability_density(-0.1) == 0
assert uniform_probability_density(1) == 0


# f(x|μ,σ) =     1      exp(- (x - μ)²)
#              √(2πσ)         2σ²
def uniform_cumulative_distribution(x: float) -> float:
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


assert uniform_cumulative_distribution(-0.1) == 0
assert uniform_cumulative_distribution(0.1) == 0.1
assert uniform_cumulative_distribution(1) == 1


def normal_probability_density(x: float, mu=0, sigma=1) -> float:
    sqrt_two_pi = sqrt(2 * pi)
    return exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma)


assert normal_probability_density(0.5) == 0.3520653267642995


def normal_cumulative_distribution(x: float, mu=0, sigma=1) -> float:
    return (1 + erf((x - mu) / sqrt(2) / sigma)) / 2


assert normal_cumulative_distribution(2) == 0.9772498680518209


# A função divide em dois intervalos repetidamente até diminuir para um Z próximo o suficiente da probabilidade desejada
def inverse_normal_cumulative_distribution(p: float, mu=0, sigma=1, tolerance=0.00001) -> float:
    """ Encontra o inverso mais próximo usando a busca binária """

    # se não for padrão, computa o padrão e redimensiona
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cumulative_distribution(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0  # normal_cumulative_distribution(-10) está (muito perto de) 0
    hi_z, hi_p = 10.0, 1  # normal_cumulative_distribution(10) está (muito perto de) 1

    while hi_z - low_z > tolerance:
        # considera o ponto do meio e o valor da função de distribuição cumulativa lá
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cumulative_distribution(mid_z)
        if mid_p < p:
            # o ponto do meio ainda está baixo, procura acima
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # o ponto do meio ainda está alta, procura abaixo
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z


