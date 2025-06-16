def divide_numbers(numbers):
    if numbers[-1] == 0:
        print("Cannot divide by zero. Returning None.")
        return None  
    result = numbers[0] // numbers[-1]  # Integer division of first by last
    return result
