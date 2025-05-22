import sys
import os
import random
def born():
    a=random.randint(0,101)
    print(a)
os.chdir("PNIOI1")
for i in range(1,20):
    os.chdir("Test "+str(i))
    sys.stdout=open("PNIOI1.inp","w")
    born()
    os.chdir("..")