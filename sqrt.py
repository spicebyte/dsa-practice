def sqrt(n:int):
    return sqrt_helper(n=n, min=1, max=n)

def sqrt_helper(n:int, min:int, max:int):
    if(max < min):
        return -1
    guess = (min+max) // 2
    guess_square = guess * guess
    if( guess_square == n):
        return guess
    elif(guess_square > n):
        return sqrt_helper(n=n,min=min,max=guess-1)
    else:
        return sqrt_helper(n=n,min = guess +1, max=max)

def capture_input(prompt:str) -> int:
    while(True):
        try:
            user_input = int(input(prompt))
            return user_input
        except:
            pass

def main():
    print("Let's calculate the square root of a number")
    target = capture_input("Input integer: ")
    print("Calculation:", sqrt(n=target))
    return

if __name__ == "__main__":
    main()
