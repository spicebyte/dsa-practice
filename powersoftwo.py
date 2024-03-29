"""
Recursive Method
- Print all powers of 2 starting from 1 to n (inclusive)
"""
def powersoftwo(target: int) -> int:
    if(target <= 0):
        return 0
   
    elif(target == 1):
        print(target)
        return 1
    
    previous = powersoftwo(target=target//2)
    current = previous * 2
    print(current)
    return current

def capture_input() -> int:
    while(True):
        try:
            target = int(input("Input target integer: "))
            return target
        except:
            pass

def main():
    target = capture_input()
    powersoftwo(target=target)
    return

if __name__ == "__main__":
    main()
