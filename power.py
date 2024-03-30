# O(b) : a**b
def power(a: int, b: int):
    if (b < 0):
        return 1 / power(a= a, b= -1 * b)
    elif(b == 0):
        return 1
    else:
        return a * power(a= a, b=b-1)

def capture_input(prompt:str) -> int:
    while(True):
        try:
            user_input = int(input(prompt))
            return user_input
        except:
            pass

def main():
    print("let's compute a to the power of b")
    first = capture_input(prompt="Input value for a: ")
    second = capture_input(prompt="Input value for b: ")

    print("a ** b =", power(a=first, b=second))
    return

if __name__ == "__main__":
    main()
