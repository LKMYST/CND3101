# ===== Exercise 1 =====
import numpy as np

np.random.seed(21)
random_integers = np.random.randint(1, high=500000, size=(20, 5))
# [1] is already given


# ===== Exercise 2 =====
random_integers[:, 1].mean()    # 214895.8


# ===== Exercise 3 =====
random_integers[:5, 2:4].mean() # 286058.5


# ===== Exercise 4 =====
first_matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(first_matrix)
# [2]: [[1 2 3]
#       [4 5 6]]

second_matrix = np.array([1, 2, 3])
print(second_matrix)
# [3]: [1 2 3]

first_matrix + second_matrix
# [3]: [[2 4 6]
#       [5 7 9]]


# ===== Exercise 5 =====
my_vector = np.array([1, 2, 3, 4, 5, 6])
selection = my_vector % 2 == 0
my_vector[selection]
# [2 4 6]


# ===== Exercise 6 =====
# checked Exercise 4 & 5
my_array = np.array([1, 2, 3, 4])
# [4]: [1 2 3 4]
my_slice = my_array[1:3]
# [5]: [2 3]
my_slice[0] = -1
# [6]: [-1 3]
# [7]: [1 -1 3 4]
# [8]: -1

x = [1, 2, 3]
y = x[0:2]
y[0] = "a change"
# [9]: ["a change", 2]
# [10]: [1, 2, 3]

my_array = np.array([1, 2, 3])
my_slice = my_array[1:3]
my_slice[0] = -1
# [11]: [1 -1 3]

my_array = np.array([1, 2, 3])
my_slice = my_array[[1, 2]]
my_slice[0] = -1
# [12]: [1 2 3]

my_array = np.array([1, 2, 3])
my_slice = my_array[1:3]
my_slice = my_slice * 2
# [13]: [4 6]
# [14]: [1 2 3]

my_array = np.array([1, 2, 3])
my_slice = my_array[1:3]
my_slice[:] = my_slice * 2
# [15]: [4 6]
# [16]: [1 4 6]


# ===== Exercise 7 =====
my_array = np.array([[1, 2, 3],[4, 5, 6]])
print(my_array)
# [17]: [[1 2 3]
#        [4 5 6]]

my_slice = my_array[:, 1:3]
# [17]: [[2 3]
#        [5 6]]


# ===== Exercise 8 =====
my_array[:, :] = my_array * 2
# my_slice: [[4 6]
#            [10 12]]
