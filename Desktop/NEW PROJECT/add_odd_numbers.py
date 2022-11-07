start_point = int(input("Enter the start point :"))
endpoint = int(input("Enter the endpoint :"))
sum_of_numbers = 0
step = 2
for i in range(start_point, endpoint, step):
    print(i)
    sum_of_numbers = sum_of_numbers + i
print("The sum of numbers between {} and {} is {}".format(start_point, endpoint, sum_of_numbers))