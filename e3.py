# EX3.Create function to find Max number in array [2,3,5,0,11,5,2]
def find_max_number(numbers):
    max_number = numbers[0]  
    for i in range(len(numbers)):
        if numbers[i] > max_number:
            max_number = numbers[i]
    return max_number
numbers = [2, 3, 5, 0, 11, 5, 2]
result = find_max_number(numbers)
print("max number: ",result)  

