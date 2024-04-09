import numpy as np
import math


def matrix_first_norm(matrix):
    return np.linalg.norm(matrix, ord=1)

def is_convergent(matrix):
    if matrix_first_norm(matrix) < 1:
        return True
    return False

# def find_iterations_count(alpha, beta, init_approx, precision):
#     a = math.log10(precision) + math.log10(abs(1-matrix_first_norm(init_approx))) - math.log(matrix_first_norm(beta))
#     b = math.log10(matrix_first_norm(alpha))
#     result = int((a / b) - 1)
#     return result

e = 0.0001

alpha_2 = np.array([
    [ 0.01,  0.15, -0.26],
    [-0.02,  0.32,  0.21],
    [-0.07, -0.04,  0.29],
])

beta_2 = np.array([
    0,
    0.41,
   -0.13,
])
# print((1-matrix_first_norm(beta_2)))
# print(matrix_first_norm(beta_2))
# print(matrix_first_norm(alpha_2))
# print(find_iterations_count(alpha_2, beta_2, beta_2, e))



print(math.log10(e))
print(math.log10(abs(1-matrix_first_norm(beta_2))))

print(math.log10((10**-4 * 0.46) / 0.54))
print(math.log10((e * abs(1-matrix_first_norm(beta_2))) / matrix_first_norm(beta_2)))
print(math.log10(matrix_first_norm(alpha_2)))

a = math.log10((e * abs(1-matrix_first_norm(beta_2))) / matrix_first_norm(beta_2))
b = math.log10(matrix_first_norm(alpha_2))

print(a/b - 1)






def find_iterations_count(alpha, beta, init_approx, precision):
    a = math.log10((precision * abs(1 - matrix_first_norm(init_approx))) / matrix_first_norm(beta))
    b = math.log10(matrix_first_norm(alpha))
    return int(a / b - 1)

print(find_iterations_count(alpha_2, beta_2, beta_2, e))


e_1 = 0.001

alpha_1 = np.array([
    [0.32, -0.18,  0.02,  0.21],
    [0.16,  0.12, -0.14,  0.27],
    [0.37,  0.27, -0.02, -0.24],
    [0.12,  0.21, -0.18,  0.25]
])

beta_1 = np.array([
     1.83,
    -0.65,
     2.23,
    -1.13
])

print(find_iterations_count(alpha_1, beta_1, beta_1, e))









