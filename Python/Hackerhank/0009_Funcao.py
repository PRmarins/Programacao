def print_formatted(number):
    # your code goes here
    i = len(f"{number:b}")

    for n in range (1,number + 1):
        
        print(f"{n:>{i}d} {n:>{i}o} {n:>{i}X} {n:>{i}b}")
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)