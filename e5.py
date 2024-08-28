# EX5.Create function to count of number 5 in array [2,3,5,0,11,5,2]
def count_number_five(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] == 5:
            count += 1
    return count
numbers = [2, 3, 5, 0, 11, 5, 2]
result = count_number_five(numbers)
print("count number5:",result)  