import sys
import os
import random
def born():
    a = random.uniform(-100, 100)
    b = random.uniform(-100, 100)
    print(a)
    print(b)
os.chdir("PNEXP")
for i in range(1,11):
    os.chdir("Test "+str(i))
    sys.stdout=open("PNEXP.inp","w")
    born()
    os.chdir("..")