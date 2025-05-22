import os
import sys
import shutil
#os.system("python")
for i in range(1,20):
    shutil.copy("sol.py", f"PNPOW2/Test {i}")
    os.chdir("PNPOW2")
    os.chdir("Test "+str(i))
    os.system("python sol.py")
    os.remove("sol.py")
    os.chdir("..")
    os.chdir("..")