"""
Fibonacci sequence
- starts with 0 and 1
- Leverage Caching
- i.e. 0,1,1,2,3,5,8,13,21,34
- each subsequent number is the sum of the previous two number
"""
import os, time
from typing import List

def fib_seq(level: int, cache: List[int]) -> int:
    # Base case
    if(level <= 0):
        return 0
    elif(level == 1):
        return 1
    elif(cache[level] > 0):
        return cache[level]

    cache[level] = fib_seq(level-1, cache) + fib_seq(level-2, cache)
    
    return cache[level]

def main():
    level = int(input("Select levels: "))
    while(level < 2):
        level = int(input("Select levels: "))

    cache = [0 for i in range(level + 1)]
    builder = ""
    for i in range(level + 1):
        builder += str(fib_seq(i, cache)) + " "
        os.system(command="clear")
        print(builder)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
