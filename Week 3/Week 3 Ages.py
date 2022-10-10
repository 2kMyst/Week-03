age = 18
print("you are an adult" if age >= 18 else "you are not an adult, yet!")


for n in ["Jon", "Terry", "Kyle", "Joe", "Kacper",]:
    print(n)


for n in range(2, 11):
	print(n, "to the power of itself is", n**n)


print(not True)


colours = [ "Blue", "Black", "Orange" ]
print("The colour black is in the list : ", "Black" in colours)
print("The colour orange is in the list : ", "orange" in colours)


num1 = 100
num2 = 10

if num1 % num2 == 0:
	print("num1 is divisible by num2")
else:
    print("num1 is not divisible by num2")


num1 = 99
num2 = 70

if num1 < num2:
	print("num1 is less than num2")
elif num1 > num2:
    print("num1 is greater than num2")
else:
    print("num1 is equal to num2")




x = 10
y = 5
lowest = x if x < y else y
print(lowest)


num = input("please enter a number between 1 and 10 : ")
num = int(num)

if num <= 10 and num >= 1:
    print("In range!")
else:
    print("Not in range!")


x = input("Enter your first value ")
x = int(x)
y = input("Enter your second value ")
y = int(y)

if x > y:
    print("The value 'x' is larger than the value 'y'")
else:
    print("The value 'y' is larger than the value 'x'")



val1 = input("Pick a number ")
val1 = int(val1)
val2 = input("Pick another number ")
val2 = int(val2)
if val1 and val2 == 0:
    print("Division by 0 is not possible.")
else:
    print(val1 / val2)