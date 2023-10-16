# Q : Write a program to design and develop a python program to implement various control statement using suitable examples

letter=input("Enter any alphabet:");
if letter in ("a", "e", "i", "o", "u"):
    print("%s is a vowel" %letter);
elif letter=="y":
    print("Sometimes letter y stands for vowel, sometimes stand for consonant");
else:
    print("%s is a consonant" %letter);
