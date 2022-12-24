
def replace(x):
    if x == 'x':
        return '*x'
    else:
        return x

def convert_str(x):
    s = ''
    for i in x:
        s = s + i
    return s

def rep(x):
    x = x[7:].replace(' ', '')
    st = convert_str(replace(i) for i in x)
    st = st.replace('cos(*x)', 'cos(x)')
    return st