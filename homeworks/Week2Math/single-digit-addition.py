#!/usr/bin/env python
import random as r

print("Generating single digit addition, with single digit answers")
for i in range(10):
    a = 99
    b = 99
    while a+b >= 10:
        a = r.randint(1, 10)
        b = r.randint(1, 10)
    print(str(a) + " + " + str(b) + " = " + str(a+b))

