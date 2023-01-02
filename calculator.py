def main(): # define main() as a unction
    #integer ...
    #x = input ("what is the first input x? ")
    #y = input ("what is the second inpyt y? ")
    #z = int(x) + int(y)
    #print ("Answer", z)

    #x = int (input ("Enter x "))
    #y = int (input ("Enter y "))
    #print ("Answer:", x + y)

    # floatint point ...
    x = float (input ("Enter x: "))
    operator = input("operation: ")
    y = float (input ("Enter y: "))
    #print ("Answer:", x + y)
    # rounding  float numbers
    #s1 = round(x + y)
    #print ("Answer:", f"{s1:,}") # print out in the format 000,000,000
    #print ("Square is:", square(s1))
    #print ("Answer: ", f"{round(x/y): .2f}") # print out in the format 0.00
    add(x,y)
    minus(x,y)
    square(x)
    square(y)
    division(x,y)

def add(a, b): # function to add 2 numbers ...
    answer = a + b
    print (a,"+",b, "=", answer)

def minus(a, b): # function to substract 2 numbers ...
    answer = a - b
    print (a,"-",b, "=", answer)

def square(x): # function to square a number ...
    answer = int(x) * int(x)
    print (x,"*",x, "=", answer)

def division(x, y): # functon to divide 2 numbers ...
    answer = x/y
    print (x,"+",y, "=", answer)

if __name__ == "__main__":
    main()
