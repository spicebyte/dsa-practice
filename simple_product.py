# O(b)
def product(a:int, b:int) -> int:
    total = 0
    for i in range(b):
        total += a

    return total

def capture_input(prompt: str) -> int:
    while(True):
        try:
            user_input = int(input(prompt))
            return user_input
        except:
            pass

def main():
    print("Let's compute the product of two numbers")
    first = capture_input(prompt="Input first number: ")
    second = capture_input(prompt="Input second number: ")
    print("\nproduct:", product(a=first,b=second))

    return

if __name__ == "__main__":
    main()
