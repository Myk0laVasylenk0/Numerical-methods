import numpy as np
import math


# def round_np_array(np_arr, digit):
#     lst = np_arr.tolist()
#     lst1 = [round(x, digit) for x in lst]
#     return lst1

def matrix_first_norm(matrix):
    return np.linalg.norm(matrix, ord=1)


def is_convergent(matrix):
    if matrix_first_norm(matrix) < 1:
        return True
    return False


def find_iterations_count(alpha, beta, init_approx, precision):
    a = math.log10((precision * abs(1 - matrix_first_norm(init_approx))) / matrix_first_norm(beta))
    b = math.log10(matrix_first_norm(alpha))
    return int(a / b - 1)


def simple_iterations_method(alpha, beta, init_approx, precision):
    x_curr = init_approx
    x_prev = np.zeros(np.shape(x_curr)[0])
    x_next = np.zeros(np.shape(x_curr)[0])
    curr_precison = (matrix_first_norm(x_next + (-1 * x_curr)))
    curr_iter = 0
    while curr_precison > precision:
        x_next = np.add(np.dot(alpha, x_curr), beta)
        x_prev = x_curr

        curr_precison = (matrix_first_norm(x_next + (-1 * x_curr)))

        x_curr = x_next
        curr_iter += 1

    return np.vstack((x_curr))

e = 10**-3

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
print(simple_iterations_method(alpha_1, beta_1, beta_1, e))