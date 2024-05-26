s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
set1 = set(s1)
set2 = set(s2)
if set1.issubset(set2):
    print("True")
else:
    print("False")