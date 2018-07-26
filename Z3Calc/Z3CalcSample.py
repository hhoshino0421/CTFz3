from z3 import *

x = Int("x")

s = Solver()
#s.add(x ** x - 6 * x + 9 == 0)
#s.add(x + 1 == 3)                  #OK
s.add(x ** x - 6 * x + 9 == 0)      #NG unknownとなる

r = s.check()
print(r)

if r == sat:
    m = s.model()

    print(m[x].as_long())




x = Real('x')
y = Real('y')
s = Solver()
s.add(x + y > 5, x > 1, y > 1)
print(s.check())
print(s.model())
