# Integer division assume positive integers for input
# O(a//b)
def intdiv(a:int, b:int) -> int:
    rem = a
    count = 0
    while(rem >= b):
        count += 1
        rem -= b

    return count

def capture_input(prompt:str) -> int:
    while(True):
        try:
            user_input = int(input(prompt))
            return user_input
        except:
            pass

def main():
    print("Let's do some integer divison")
    a = capture_input(prompt="Input value for a: ")
    b = capture_input(prompt="Input value for b: ")
    print("a // b =", intdiv(a=a,b=b))
    return

if __name__ == "__main__":
    main()
