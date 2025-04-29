import os
import sys
import shutil
os.system("g++ sol.cpp -o sol.exe")
for i in range(1,16):
    shutil.copy("sol.exe", f"LIS/Test {i}")
    os.chdir("LIS")
    os.chdir("Test "+str(i))
    os.system(".\sol.exe")
    os.remove("sol.exe")
    os.chdir("..")
    os.chdir("..")