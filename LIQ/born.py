import sys
import os
import random
def born():
    n=random.randint(200001,300001)
    print(n)
    for i in range(0,n):
        x=random.randint(1,10000000)
        print(x,end=" ")
    print()

os.chdir("LIS")
for i in range(8,16):
    os.chdir("Test "+str(i))
    sys.stdout=open("LIS.inp","w")
    born()
    os.chdir("..")