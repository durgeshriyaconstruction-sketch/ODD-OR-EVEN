while True:
    v = int(input("Enter a number(or 0 to exit ):"))
    if v == 0:
        break 
    if v % 2 == 0:
        print("The number is even")
    else:        
        print("The number is odd")