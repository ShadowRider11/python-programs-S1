def fibonacci_series(n):
    a = 0
    b = 1
    
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci series up to 1 term:")
        print(a)
    else:
        print(f"Fibonacci series up to",n,"terms:")
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            print(c)
            a = b
            b = c

num_terms =int(input("Enter a number:"))
fibonacci_series(num_terms)
