def sum_digits(n:int) -> int:
    sum = 0
    while(n>0):
        sum += n % 10
        n //= 10
    return sum

def capture_input(prompt:str)-> int:
    while(True):
        try:
            user_input = int(input(prompt))
            return user_input
        except:
            pass

def main():
    print("Let's calculate the sum of the digits in a number")
    target = capture_input(prompt="Input target: ")
    print(sum_digits(n=target))

    return

if __name__ == "__main__":
    main()
