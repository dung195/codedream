import sys
import os
import random
def born():
    length = random.randint(1000, 3000)
    s = ""
    while len(s) < length:
        if random.choice([True, False]):
            # Generate a palindrome substring
            half = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(1, 5)))
            s += half + half[::-1]
        else:
            # Generate a non-palindrome substring
            non_palindrome = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(3, 7)))
            if non_palindrome != non_palindrome[::-1]:  # Ensure it's not accidentally a palindrome
                s += non_palindrome
    print(s[:length])  # Trim to the desired length
os.chdir("PLC")
for i in range(10,20):
    os.chdir("Test "+str(i))
    sys.stdout=open("LIS.inp","w")
    born()
    os.chdir("..")