num = int(input("Enter the total numbers you want to enter : "))
square = 0
for i in range(num) :
    a = int(input("Enter the number : "))
    square = square + a*a
    average = square / num
print("Average of Sum of the squares of the numbers : ", average)