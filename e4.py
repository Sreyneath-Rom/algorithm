# EX4.Create function to find Min number in array [2,3,5,0,11,5,2]
def find_min_number(numbers):
    min_number = numbers[0] 
    for i in range(len(numbers)):
        if numbers[i] < min_number:
            min_number = numbers[i]
    return min_number
numbers = [2, 3, 5, 0, 11, 5, 2]
result = find_min_number(numbers)
print("min number: ",result)
