
def fibonacci_series(n):
    fib = [0, 1]
    if n <= 0:
        return "please enter a positive integer."
    
    elif n == 1:
        return [0]
    
    elif n == 2:
        return fib
    
    else:
        for i in range(2 , n):
            p = fib[i-1] + fib[i-2]
            fib.append(p)
        return fib
        
# n = 10
print(fibonacci_series(int(input("Enter a value for fibonacci series: "))))