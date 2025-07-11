from pipeline_factory import build_pipeline
from pipeline_registry import get_ordered_pipeline

def get_user_input():
    while True:
        user_input = input("Enter comma-separated integers (each between 0 and 9): ")
        try:
            numbers = [int(num.strip()) for num in user_input.split(",")]
            if all(0 <= num <= 9 for num in numbers) and len(numbers) >= 1:
                return numbers
            else:
                print("All numbers must be integers between 0 and 9. Please try again.")
        except ValueError:
            print("Invalid input detected. Please enter integers separated by commas.")


def main():
    build_pipeline()

    context = {
        "numbers": get_user_input(),
        "addition_result": None,
        "multiplication_result": None,
        "division_result": None
    }

    for step in get_ordered_pipeline():
        try:
            step(context)
        except Exception as e:
            print(f"Step {step.__name__} failed: {e}")
            break

        if context["division_result"] is not None:
            print(f"Final Division Result: {context["division_result"]}")
    # numbers = get_user_input()

    # total, numbers = add_numbers(numbers)

    # if total % 2 == 0:
    #     product, numbers = multiply_numbers(numbers)

    #     if product % 2 == 0:
    #         result = divide_numbers(numbers)
    #         print(f"Final Division Result (integer): {result}")
    #     else:
    #         print(f"Multiplication result after retries is odd: {product}")
    # else:
    #     print(f"Addition result after retries is odd: {total}")

if __name__ == "__main__":
    main()
