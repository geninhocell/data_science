import matplotlib.pyplot as plt
from math import sqrt
from collections import Counter
from probability import (
    normal_probability_density,
    normal_cumulative_distribution,
    binomial
)

# xs = [x / 10.0 for x in range(-50, 50)]
# plt.plot(xs, [normal_probability_density(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
# plt.plot(xs, [normal_probability_density(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
# plt.plot(xs, [normal_probability_density(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
# plt.plot(xs, [normal_probability_density(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')
# plt.legend()
# plt.title('Diversas Funções de Densidade de Probabilidade Normais')
# plt.show()

# xs = [x / 10.0 for x in range(-50, 50)]
# plt.plot(xs, [normal_cumulative_distribution(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
# plt.plot(xs, [normal_cumulative_distribution(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
# plt.plot(xs, [normal_cumulative_distribution(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
# plt.plot(xs, [normal_cumulative_distribution(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')
# plt.legend(loc=4)  # bottom right
# plt.title('Diversas Funções de Densidade de Distribuição Cumulativa')
# plt.show()


# def make_hist(p, n, num_points):
#     data = [binomial(n, p) for _ in range(num_points)]
#
#     # usa um gráfico de barras para exibir as amostras binomiais atuais
#     histogram = Counter(data)
#     plt.bar([x - 0.4 for x in histogram.keys()],
#             [v / num_points for v in histogram.values()],
#             0.8,
#             color='0.75')
#
#     mu = p * n
#     sigma = sqrt(n * p * (1 - p))
#
#     # usa um gráfico de linhas para exibir uma aproximação do normal
#     xs = range(min(data), max(data) + 1)
#     ys = [normal_cumulative_distribution(i + 0.5, mu, sigma) - normal_cumulative_distribution(i - 0.5, mu, sigma)
#           for i in xs]
#
#     plt.plot(xs, ys)
#     plt.title('Distribuição Binomial vs. Aproximação Normal')
#     plt.show()
#
#
# make_hist(0.75, 100, 10000)
