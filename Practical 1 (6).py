list1=["red", "green", "blue", "black", "white"];
list2=[14, 12, 13];
print("Elements of list1:", list1);
print("Elements of list2:", list2);

print("Length of list1:", len(list1));
print("Length of list1:", len(list1));

list1.sort();
print("List1 after sorting:", list1);

list1.insert(2, "pink");
print(list1);

list1.append("yellow");
print("List after append:", list1);

list2.sort();
print("List2 after sorting:", list2);

list1.remove("blue");
print("List1 after removing a element:", list1);

print("Slicing:", list1[:4]);
print(list1[2:4]);

list1.reverse();
print("List1 after reversed:", list1);

list1.extend(list2);
print("Extended list:", list1);
