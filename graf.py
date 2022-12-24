import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

symbol_x = sp.Symbol('x')
symbol_y = sp.Symbol('y')

def get_vector(a, b):
    return np.arange(a, b+1, 0.001)

def test(f, sym_x, v):
    if round(f.subs(sym_x, v),4) >= -0.1 and round(f.subs(sym_x, v),4) <= 0.1:
        print(f'Корень функции: {round(f.subs(sym_x, v), 4)}')
        return f.subs(sym_x, v)

def plot_2d_function(function1, a, b):
    f_x1 = sp.sympify(function1)
    print(f'Преобразование функции: {f_x1}')

    sol1 = sp.solveset(f_x1, symbol_x)
    # sol2 = [r for r in sp.solve(f_x1) if r.is_real]
    print(f'Какое-то представление корней: {sol1}')
    # print(sol2)

    # Create domain and image
    domain_x = get_vector(a, b)
    image = [f_x1.subs(symbol_x, value) for value in domain_x]
    image1 = [test(f_x1, symbol_x, value) for value in domain_x]

    # Plot the 2D function graph
    fig = plt.figure(figsize=(10, 20))
    plt.plot(domain_x, image1, 'rh')
    plt.plot(domain_x, image)
    plt.grid()
    plt.show()



