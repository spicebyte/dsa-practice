def mod(a:int, b:int) -> int:
    if(b <= 0):
        return -1
    else:
        div = a // b
        rem = a - ( b * div)
        return rem

def capture_input(prompt: str) -> int:
    while(True):
        try:
            user_input = int(input(prompt))
            return user_input
        except:
            pass

def main():
    print("Let's do some mod operations")
    a = capture_input(prompt="Input value for a: ")
    b = capture_input(prompt="Input value for b: ")

    print("a % b =", mod(a=a,b=b))
    return

if __name__ == "__main__":
    main()
