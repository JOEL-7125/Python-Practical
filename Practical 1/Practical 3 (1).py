# Q : Design a Simple Calculator using if else statement

print("|===[ Calculator ]===|");

#Asking user what operations to do?
print("\n1 • Addition");
print("2 • Substraction");
print("3 • Multiplication");
print("4 • Division");
print("\nType the operations according to numbers.");
opt=int(input("What operations would you like to do: "));

#Requesting two number to do operations
a=int(input("\nEnter first number: "));
b=int(input("Enter second number: "));
print();

#If else conditions to do any one type of operation selected by user
if (opt==1):
    print("Addition of {} and {} is:".format(a, b), a+b);
elif (opt==2):
    print("Substraction of {} and {} is:".format(a, b), a-b);
elif (opt==3):
    print("Product of {} and {} is:".format(a, b), a*b);
elif (opt==4):
    print("Division of {} and {} is:".format(a, b), a/b);
