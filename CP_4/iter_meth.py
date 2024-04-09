
import numpy as np
import math

def _round_nparr_(array, digit):
    out_arr = np.array([])
    for i in array:
        i = round(i, digit)
        out_arr.append(i)
    return out_arr

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
    # one more iteration so that we will be able to round numbers
    x_next = np.add(np.dot(alpha, x_curr), beta)
    x_prev = x_curr
    curr_precison = (matrix_first_norm(x_next + (-1 * x_curr)))
    x_curr = x_next
    curr_iter += 1

    print(f"Iteration {curr_iter}")
    print(f"x_prev: {x_prev}")
    print(f"x_curr: {x_curr}")
    print(f"x_next: {x_next}")
    print(f"curr_precison: {curr_precison}")
    to_round = len((str(precision).split("."))[1])
    answer = np.round(x_curr, to_round + 2)
    answer = np.round(answer, to_round + 1)
    # answer = np.round(answer, to_round)
    print(f"answer: {answer}")


e = 0.001

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


beta_2 = np.array([
     1.83,
    -0.65,
     2.23,
    -1.13
])

beta_2 = _round_nparr_(beta_2, 2)
print(beta_2)

# simple_iterations_method(alpha_1, beta_1, beta_1, e)


# print(np.around(-1.5105, 3))
# np.array([1.55, 2.65])





















# e = 0.001
#
# x_1 = np.array([0.75, 0.95, 1.14, 1.36])
# x_2 = np.array([0.8106, 1.0118, 1.2117, 1.4077])
# x_3 = np.array([0.7978, 0.9977, 1.1975, 1.3983])
# x_4 = np.array([0.8004, 1.0005, 1.2005, 1.4003])
# x_5 = np.array([0.7999, 0.9999, 1.1999, 1.3999])
# print(np.shape(x_1)[0])
#
# print(
#     (matrix_first_norm(x_2 + (-1 * x_1)))
# )
# print((matrix_first_norm(x_3 + (-1 * x_2))))
# print((matrix_first_norm(x_4 + (-1 * x_3))))
# print((matrix_first_norm(x_5 + (-1 * x_4))))



