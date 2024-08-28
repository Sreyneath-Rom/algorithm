# EX7.Create function to count negative number in array [-1,11,2,0,-1,4]
def count_negative_numbers(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] < 0:
            count += 1
    return count
numbers = [-1, 11, 2, 0, -1, 4]
result = count_negative_numbers(numbers)
print("count negative number: ",result)  
