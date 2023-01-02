def main():
    x = int (input("What is x? "))
    if (is_even(x)):
        print ("X is EVEN")
    else:
        print ("X is ODD")
    

def is_even(n):
    if (n%2 == 0):
        return True
    else:
        return False

if (__name__ == "__main__"):
    main()