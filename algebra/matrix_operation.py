"""

"""
from typing import List, Tuple, Callable

Matrix = List[List[float]]
Vector = List[float]

# A has 2 rows and 3 columns
matrix_A: Matrix = [[1, 2, 3],
                    [4, 5, 6]]

# B has 3 rows and 2 columns
matrix_B: Matrix = [[1, 2],
                    [3, 4],
                    [5, 6]]

#####################################################################################################################


def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0  # number of elements in first row
    return num_rows, num_cols


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 rows, 3 columns
assert shape([]) == (0, 0)  # 0 rows, 0 columns

#####################################################################################################################


def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]  # A[i] is already the ith row


assert get_row([[1, 2], [4, 8]], 0) == [1, 2]

#####################################################################################################################


def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return [A_i[j] for A_i in A]


assert get_column([[1, 2], [4, 6]], 1) == [2, 6]

#####################################################################################################################


def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
    """ retorna a matriz num_rows X num_cols cuja entrada (i,j)th é entry_fn(i, j) """
    return [[entry_fn(i, j)
            for j in range(num_cols)]
            for i in range(num_rows)]


#####################################################################################################################


def is_diagonal(i: int, j: int) -> float:
    """ 1's na diagonal, 0's nos demais lugares """
    return 1 if i == j else 0


assert make_matrix(3, 3, is_diagonal) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

#####################################################################################################################


def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]

#####################################################################################################################

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

#            user 0  1  2  3  4  5  6  7  8  9
#
friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # user 0
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # user 1
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # user 2
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],  # user 3
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # user 4
                 [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # user 5
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 6
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 7
                 [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # user 8
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  # user 9

assert friend_matrix[0][2] == 1, "0 and 2 are friends"
assert friend_matrix[0][8] == 0, "0 and 8 are not friends"

# only need to look at one row
# [4, 6, 7]
friends_of_five = [i
                   for i, is_friend in enumerate(friend_matrix[5])
                   if is_friend]
