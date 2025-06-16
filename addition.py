import random

def add_numbers(numbers):
    count = 0
    while count < 4:
        total = sum(numbers)
        print(f"Addition result: {total}")
        if total % 2 == 0:
            return total, numbers
        else:
            new_num = random.randint(0, 9)
            print(f"Sum is odd, adding random number {new_num} to the list")
            numbers.append(new_num)
            count += 1
    return sum(numbers), numbers
