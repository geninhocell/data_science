from matplotlib import pyplot as plt

test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)

plt.title("Os eixos não são compatíveis")
plt.xlabel("nota do teste 2")
plt.ylabel("nota do teste 1")

# plt.axis([50, 110, 50, 110])

plt.show()
