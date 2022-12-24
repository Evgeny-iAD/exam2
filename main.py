import separation, graf
def print_fx(name):
    print(f'Решаем функцию {name}')

a_value = -3
b_value = 3

if __name__ == '__main__':
    with open('func.txt') as fx:
        f = fx.readline()
    print_fx(f'{f}')
    list_f = separation.rep(f)
    graf.plot_2d_function(list_f, a_value, b_value)


