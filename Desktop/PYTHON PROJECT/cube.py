num = int(input("Enter the total numbers you want to enter : "))
cube = 0
for i in range(num) :
    a = int(input("Enter the number : "))
    cube = cube + a*a*a
    average = cube / num
print("Average of Sum of the cubes of the numbers : ", average)