import os
import timeit
import random

with open("test.txt", "w") as file:
    while (os.path.getsize('test.txt') / (1000 * 1000)) < 50:
            file.write(str(random.randrange(50)) + '\n')

s = """
summa = 0
with open ("test.txt","r") as file:
 for line in file.readlines():
    if line.strip().isdigit():
        summa+=int(line.strip())
"""
print(timeit.timeit(s, number=10))

s = """
summa = 0
with open ("test.txt","r") as file2:
 for line in file2:
    if line.strip().isdigit():
        summa+=int(line.strip())
"""
print(timeit.timeit(s, number=10))

s = """
summa = 0
with open ("test.txt","r") as file3:
  summa = sum(int(line.strip()) for line in file3 if line.strip().isdigit())
"""
print(timeit.timeit(s, number=10))