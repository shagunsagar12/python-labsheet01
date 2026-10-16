a = int(input("Enter a number = "))
b = int(input("Enter another number = "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)