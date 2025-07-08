def factorial(n):
    x=1
    if n<2:
        print("factorial is: 1")
    else:
        for i in range (1,n+1):
            x *= i
        print(f"factorial is: {x}")        
factorial(5)




