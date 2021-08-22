from collections import Counter

from matplotlib import pyplot as plt

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]


def decile(grade: float) -> int:
    return grade // 10 * 10


histogram = Counter(decile(grade) for grade in grades)

# move cada barra para a esquerda em 4
# dá para cada barra sua altura correta
# dá para cada barra a largura de 8
plt.bar([x - 4 for x in histogram.keys()], histogram.values(), 8)

# eixo x de -5 até 105
# eixo y de 0 até 5
plt.axis([-10, 102, 0, 5])

# rótulos do eixo x em 0, 10, ..., 100
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decil")
plt.ylabel("# de Alunos")
plt.title("Distribuição das Notas do Teste 1")

plt.show()
