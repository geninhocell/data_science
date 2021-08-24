import matplotlib.pyplot as plt
from probability import normal_probability_density, normal_cumulative_distribution

# xs = [x / 10.0 for x in range(-50, 50)]
# plt.plot(xs, [normal_probability_density(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
# plt.plot(xs, [normal_probability_density(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
# plt.plot(xs, [normal_probability_density(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
# plt.plot(xs, [normal_probability_density(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')
# plt.legend()
# plt.title('Diversas Funções de Densidade de Probabilidade Normais')
# plt.show()

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_cumulative_distribution(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [normal_cumulative_distribution(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
plt.plot(xs, [normal_cumulative_distribution(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_cumulative_distribution(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')
plt.legend(loc=4)  # bottom right
plt.title('Diversas Funções de Densidade de Distribuição Cumulativa')
plt.show()
