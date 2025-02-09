
def math (var):
    import math
    out = 1 / (1 + (math.e ** -var))
    return out

print(math(2))

def quad(a, b, c):
    import math
    top_pos = -b + math.sqrt(b**2 - 4*a*c)
    top_neg = -b - math.sqrt(b**2 - 4*a*c)
    bot = 2*a

    out = top_pos / bot and top_neg / bot
    return out

print(quad(1, -2, 3))

# def ke(m, v):
#     out = .5*m*(v**2)
#     return out

# def f(g, m , m2, r):
#     out = g* ((m * m2) / (r**2))
#     return out

