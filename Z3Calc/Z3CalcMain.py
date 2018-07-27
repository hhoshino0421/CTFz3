from z3 import *

x = IntVector("x", 12)

s = Solver()

s.add(x[0] * -72 + x[1] * -74 + x[2] * 91 + x[3] * 59 + x[4] * 53 + x[5] * -95 + x[6] * -32 + x[7] * -39\
      + x[8] * 93 + x[9] * 76 + x[10] * -31 + x[11] * 22 == 4885)

s.add(x[0] * 78 + x[1] * -84 + x[2] * -96 + x[3] * 69 + x[4] * -21 + x[5] * -72 + x[6] * 89 + x[7] * -26\
      + x[8] * 21 + x[9] * 65 + x[10] * 3 + x[11] * 49 == 10656)

s.add(x[0] * -46 + x[1] * 11 + x[2] * -39 + x[3] * 54 + x[4] * 57 + x[5] * -14 + x[6] * 59 + x[7] * -10 \
      + x[8] * 77 + x[9] * -34 + x[10] * 0 + x[11] * 99 == 14249)

s.add(x[0] * 27 + x[1] * 4 + x[2] * 52 + x[3] * 23 + x[4] * -1 + x[5] * 43 + x[6] * -41 + x[7] *13 \
      + x[8] * 9 + x[9] * -70 + x[10] * -16 + x[11] * 91 == 7244)

s.add(x[0] * 60 + x[1] * -92 + x[2] * 84 + x[3] * 58 + x[4] * -8 + x[5] * -6 + x[6] * 91 + x[7] * 8 \
      + x[8] * -30 + x[9] * -11 + x[10] * -5 + x[11] * -96 == -17152)

s.add(x[0] * -91 + x[1] * -16 + x[2] * -96 + x[3] * 51 + x[4] * -56 + x[5] * -85 + x[6] * -52 + x[7] * 46\
      + x[8] * -78 + x[9] * 87 + x[10] * 96 + x[11] * -83 == -22439)





r = s.check()
print(r)

if r == sat:
    m = s.model()
    for i in range(12):
        print(m[x[i]].as_long())

