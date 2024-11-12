from scipy import optimize
def f(v0, vf, n, a):
    return lambda x: vf - v0*(1+x)**n - a*(((1+x)**n-(1+x))/x)
def obtener_interes():
    return optimize.newton(f(100, 105.31, 2, 5), 1e-5)

print(obtener_interes())