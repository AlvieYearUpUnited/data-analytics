# Alvie Ahmed
# Week 6 Exercise 2.D: Lambdas and generators
# Lab 1

# -------------------------------------------------------------------------

doubler = lambda n: n * 2

print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

tripler = lambda n: n * 3

print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

def multiplier(times):
    return lambda n: n * times

times4 = multiplier(4)
times5 = multiplier(5)
times6 = multiplier(6)
times7 = multiplier(7)
times8 = multiplier(8)
times9 = multiplier(9)
times10 = multiplier(10)

print(times4(10))
print(times5(6))
print(times6(5))
print(times7('six'))
print(times8(-8))
print(times9(10))
print(times10(4))