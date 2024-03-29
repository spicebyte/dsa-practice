"""
Fibonacci sequence
- starts with 0 and 1
- i.e. 0,1,1,2,3,5,8,13,21,34
- each subsequent number is the sum of the previous two number
"""
import os, time
def fib_seq_1(level: int):
    # Base case
    if(level == 0):
        return 0
    if(level == 1):
        return 1
    else:
        return fib_seq_1(level-1) + fib_seq_1(level-2)

def main():
    level = int(input("Select levels: "))
    while(level < 2):
        level = int(input("Select levels: "))

    builder = ""
    for i in range(level + 1):
        builder += str(fib_seq_1(i)) + " "
        os.system(command="clear")
        print(builder)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
