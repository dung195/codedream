import sys
import os
import random
def born():
    a = random.randint(1, 10000)
    mod=random.randint(1,10000)
    print(a)
    print(mod)
    

os.chdir("PNMOD")
for i in range(1,11):
    os.chdir("Test "+str(i))
    sys.stdout=open("PNMOD.inp","w")
    born()
    os.chdir("..")