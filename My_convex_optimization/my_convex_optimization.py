import matplotlib.pyplot as plt, numpy as np
from scipy.optimize import minimize_scalar

def custom_function(x):
    return (x - 2)**4 + x**2

def plot_function(func, values):
    plt.plot(values, func(values))
    return func(values)

def find_root_bisection(func, lower_bound, upper_bound):
    precision = 0.01
    while (upper_bound - lower_bound) >= precision:
        x = (lower_bound + upper_bound) / 2
        if func(x) == 0.0:
            break
        if func(x) * func(lower_bound) < 0:
            upper_bound = x
        else:
            lower_bound = x
    return x

def find_root_newton_raphson(func, func_derivative, start, precision=0.001):
    x = start
    while abs(func(x)) > precision:
        x = x - func(x) / func_derivative(x)
    return x

def gradient_descent(func, func_derivative, start, learning_rate=0.1, precision=0.001):
    x = start
    while abs(func_derivative(x)) > precision:
        x -= learning_rate * func_derivative(x)
    return x

def solve_linear_problem(A, b, c):
    from scipy.optimize import linprog
    result = linprog(c, A_ub=A, b_ub=b, method='simplex')
    return result.fun, result.x

custom_function_derivative = lambda x: 4 * ((x - 2) ** 3) + 2 * x

def find_minimum_gradient_descent(func, func_derivative, start, learning_rate=0.1, precision=0.001):
    x = start
    while abs(func_derivative(x)) > precision:
        x -= learning_rate * func_derivative(x)
    return x, func(x)

def print_a_function(func, values):
    plt.plot(values, func(values))
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Epic Function Visualization')
    plt.grid(True)
    plt.show()

custom_A_matrix = np.array([[3, -2], [1, 4], [2, 1]])
custom_b_vector = np.array([5, 9, 4])
custom_c_vector = np.array([2, -1])

def main():
    optimization_result = minimize_scalar(custom_function, method='brent')
    optimal_x, optimal_value = optimization_result.x, optimization_result.fun
    print('Optimal x: {:.2f}, f(optimal x): {:.2f}'.format(optimal_x, optimal_value))

    x_range = np.linspace(optimal_x - 1, optimal_x + 1, 100)
    plot_function(custom_function, x_range)
    plt.scatter(optimal_x, optimal_value, color='red', marker='x', label='Minimum Point')
    plt.grid(True)
    plt.legend(loc=1)
    plt.title('Function Plot')
    plt.show()

    root_bisection = find_root_bisection(custom_function, -2, 3)
    print("Root found using bisection:", root_bisection)

    root_newton_raphson = find_root_newton_raphson(custom_function, custom_function_derivative, -1)
    print("Root discovered with Newton-Raphson:", root_newton_raphson)

    minimum_x, minimum_f = find_minimum_gradient_descent(custom_function, custom_function_derivative, -1)
    print("Minimum x found using gradient descent:", minimum_x)
    print("f(minimum x) using gradient descent:", minimum_f)

    optimal_value, optimal_arg = solve_linear_problem(custom_A_matrix, custom_b_vector, custom_c_vector)
    print("Optimal value:", optimal_value, "reached for x =", optimal_arg)

    x_range_print = np.linspace(-3, 3, 100)
    print_a_function(custom_function, x_range_print)

if __name__ == "__main__":
    main()
