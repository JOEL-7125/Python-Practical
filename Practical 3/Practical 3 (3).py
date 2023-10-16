# Q : Write a Python program to demonstrate different types of function argument
# a) Arbitrary argument

def greet(*names):
    for name in names:
        print("Good morning", name);

greet("Rahul", "Atharv", "Ayush");
