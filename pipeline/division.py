def divide_numbers(context):
    numbers = context["numbers"]
    if numbers[-1] == 0:
        print("Cannot divide by zero. Returning None.")
        context["division_result"] = None
        return
    result = numbers[0] // numbers[-1]  # Integer division of first by last
    context["division_result"] = result
    return
