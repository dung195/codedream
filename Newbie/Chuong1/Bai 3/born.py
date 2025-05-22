import sys
import os
import random
def born():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = random.randint(0, 10)
    d = random.randint(0, 10)
    print(a)
    print(b)
    print(c)
    print(d)

os.chdir("PNPOW2")
for i in range(1,11):
    os.chdir("Test "+str(i))
    sys.stdout=open("PNPOW2.inp","w")
    born()
    os.chdir("..")