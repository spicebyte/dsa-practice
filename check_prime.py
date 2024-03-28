"""
- Only need to check up to square root
- Can start from 2
- if past root return True
- O(n**(1/2))
"""

def is_prime(num):
    factor = 2

    while(factor * factor <= num):
        if(num % factor == 0):
            return False
        else:
            factor += 1

    return True

def main():
    prompt = input("input number to check if prime: ")
    prompt = int(prompt)

    if(is_prime(prompt) == True):
        print("Yes", prompt, " is prime!!!")
    else:
        print("No", prompt, " is not prime.")

    return

if __name__ == "__main__":
    main()
