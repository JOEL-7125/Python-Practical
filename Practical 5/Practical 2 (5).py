def recur_fact(n):
    if n==1:
        return n
    else:
        return n*recur_fact(n-1)

num=int(input("Enter the number: "));
if num<0:
    print("Sorry, Factorial does not exist for negative numbers.");
elif num==0:
    print("THe factorial of 0 is 1.");
else:
    print("The factorial of", num, " is", recur_fact(num))
