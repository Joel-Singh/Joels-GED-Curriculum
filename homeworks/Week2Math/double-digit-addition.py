#!/usr/bin/env python
import random as r

print("Generating double digit addition")
for i in range(10):
    a = r.randint(1, 99)
    b = r.randint(1, 99)
    print(str(a) + " + " + str(b) + " = " + str(a+b))

