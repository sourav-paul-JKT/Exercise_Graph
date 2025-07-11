import random

def add_numbers(context):
    count = 0
    numbers = context["numbers"]
    while count < 4:
        total = sum(numbers)
        print(f"Addition result: {total}")
        if total % 2 == 0:
            context["addition_result"] = total
            return
        else:
            new_num = random.randint(1, 9)
            print(f"Sum is odd, adding random number {new_num} to the list")
            numbers.append(new_num)
            count += 1
    context["addition_result"] = sum(numbers)
    context["numbers"] = numbers
