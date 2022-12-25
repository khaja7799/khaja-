def factorial(x):
    """This is recursion function
     to find factorial of an integer"""
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
num=6
print("the factorial of",num,"is",factorial(num))


x=lambda a:a+10-20*23/10+50
print(x(10))