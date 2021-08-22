"""
# soma
[1, 2] + [ 2, 1] => [1+2, 2+1] = [3, 3]

# subtração
[1, 2] - [ 2, 1] => [1-2, 2-1] = [-1, 1]

# distance
sqrt((v_1 - w_1)** + ... + (v_n - w_n)**)
"""
from functools import reduce, partial
from math import sqrt
from typing import List

Vector = List[float]

###############################################################################################################


def vector_add(v: Vector, w: Vector) -> Vector:
    """ soma elementos correspondentes """
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]  # zip([1, 2], [2, 4]) -> 1 2, 2 4


# v1 = [1, 2]
# v2 = [2, 1, 3]
# print(f'{type(vector_add(v1, v2))}')
assert vector_add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

###############################################################################################################


def vector_subtract(v: Vector, w: Vector) -> Vector:
    """ subtrai elementos correspondentes """
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert vector_subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

###############################################################################################################


def vector_sum_v1(vectors: List[Vector]) -> Vector:
    """ soma todos os elementos correspondentes"""
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    result = vectors[0]  # Pega a primeira linha de indice 0
    for vector in vectors[1:]:  # Percorre apartir do indice 1
        result = vector_add(result, vector)
    return result


assert vector_sum_v1([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


vector_sum_v2 = partial(reduce, vector_add)  # partial(func1, func2) -> func1(func2) -> func3


assert vector_sum_v2([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def vector_sum_v3(vectors: List[Vector]) -> Vector:
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    return reduce(vector_add, vectors)  # reduce(func, data) -> func(data)


assert vector_sum_v3([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

###############################################################################################################


def scalar_multiply(c: float, v: Vector) -> Vector:
    """ c é um número, v é um vetor """
    return [c * v_i for v_i in v]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

###############################################################################################################


def vector_mean(vectors: List[Vector]) -> Vector:
    """ computar o vetor cujo i-ésimo elemento seja a média dos i-ésimos elementos dos vetores inclusos """
    n = len(vectors)  # len -> 3
    # vector_sum_v3([[1, 2], [3, 4], [5, 6]]) -> [9, 12]
    # scalar_multiply(1/3, [9, 12]) -> [3, 4]
    return scalar_multiply(1/n, vector_sum_v3(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

###############################################################################################################


# Produto Escalar
def dot_product(v: Vector, w: Vector) -> float:
    """ v_1 * W_1 + ... + v_n * w_n """
    # zip([1, 2, 3], [4, 5, 6]) -> (1, 4), (2, 5), (3, 6)
    # sum(4, 10, 18) -> 32
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot_product([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6

###############################################################################################################


# Soma dos quadrados de um vetor
def sum_of_squares(v: Vector) -> float:
    """ v_1 * v_1 + ... + v_n * v_n """
    return dot_product(v, v)


assert sum_of_squares([1, 2, 3]) == 14  # [1, 2, 3] * [1, 2, 3] -> 1 * 1 + 2 * 2 + 3 * 3

###############################################################################################################


def magnitude(v: Vector) -> float:
    return sqrt(sum_of_squares(v))


assert magnitude([3, 4]) == 5  # [3, 4] * [3, 4] -> 9 + 16 -> 25

###############################################################################################################


def squared_distance(v: Vector, w: Vector) -> float:
    """ (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2 """
    # vector_subtract([1, 2], [6, 9]) -> [5, 7]
    # sum_of_squares([5, 7]) -> [5, 7] * [5, 7] -> 25 + 49 -> 74
    return sum_of_squares(vector_subtract(v, w))


assert squared_distance([1, 2], [6, 9]) == 74

###############################################################################################################


def distance_v1(v: Vector, w: Vector) -> float:
    # squared_distance([1, 2], [6, 9]) == 74
    # sqrt(74) -> 8.602325267042627
    return sqrt(squared_distance(v, w))


# assert distance_v1([1, 2], [6, 9]) == 8.602325267042627


###############################################################################################################


def distance_v2(v: Vector, w: Vector) -> float:
    return magnitude(vector_subtract(v, w))


# assert distance_v2([1, 2], [1, 9]) == 7.0

###############################################################################################################
