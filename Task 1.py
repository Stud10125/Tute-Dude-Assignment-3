def Factorial(n):
    if n<2:
        return 1
    else:
        return n*(Factorial(n-1))

a=int(input("Enter a number: "))
print(f"Factorial of {a} is:",Factorial(a))
    


