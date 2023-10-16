# Q : Write a Python program to implement recursion for problems such as Fibonacci series, Factorial, etc.
# a) Fibbonacci series using recursion

def recur_fibo(n):
    if n<=1:
        return n;
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2));
nterms=int(input("How many terms?\n"));
if nterms<=0:
    print("\nPlease enter a positive number");
else:
    print("\nFibonacci Sequence:");
for i in range(nterms):
    print(recur_fibo(i));
