import os
import sys
import shutil
os.system("g++ sol.cpp -o sol.exe")
for i in range(1,20):
    shutil.copy("sol.exe", f"PNEXP/Test {i}")
    os.chdir("PNEXP")
    os.chdir("Test "+str(i))
    os.system(".\sol.exe")
    os.remove("sol.exe")
    os.chdir("..")
    os.chdir("..")