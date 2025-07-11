def check_addition_result(context):
    result = context.get("addition_result")
    if result is not None:
        label = "Addition"
        print(f"{label} result is {'EVEN' if result % 2 == 0 else 'ODD'}.")

def check_multiplication_result(context):
    result = context.get("multiplication_result")
    if result is not None:
        label = "Multiplication"
        print(f"{label} result is {'EVEN' if result % 2 == 0 else 'ODD'}.")
