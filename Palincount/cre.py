import sys
import os
os.chdir("PLC")
for i in range(1,20):
    os.mkdir("Test "+str(i))