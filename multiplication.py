import random

def multiply_numbers(numbers):
    count = 0
    result = 1
    while count < 4:
        # result = 1
        if count >= 1:
            result *= numbers[-1]
        else:
            for num in numbers:
                result *= num
        print(f"Multiplication result: {result}")
        if result % 2 == 0:
            return result, numbers
        else:
            new_num = random.randint(1,9)
            print(f"Product is odd, adding random number {new_num} to the list")
            numbers.append(new_num)
            count += 1
    result = 1
    for num in numbers:
        result *= num
    return result, numbers
