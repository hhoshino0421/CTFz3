# 関数定義
def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)

# 関数処理1
val = factorial(42)

print(val)

# 関数処理2
val2 = factorial.__doc__

print(val2)

# 関数処理3
val3 = type(factorial)

print(val3)

# 関数処理4
fact = factorial

print(fact)

# 関数処理5
val4 = fact(5)

print(val4)

# 関数処理6
fact2 = map(factorial, range(11))

print(fact2)

# 関数処理7
fact3 = list(map(fact,range(11)))

print(fact3)
