# EX2.Create function to sum odd number in array [1,2,3,4,5,6]
def sum_odd_numbers(numbers):
    sum = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            sum += numbers[i]
    return sum

numbers = [1, 2, 3, 4, 5, 6]
result = sum_odd_numbers(numbers)
print("sum odd number: ",result)

