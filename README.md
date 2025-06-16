# Exercise_Graph

## Project Description

This project takes a list of user-input integers (between 0 and 9), performs a series of operations based on odd/even conditions:

1. **Addition Stage:**
   - Add all the numbers.
   - If sum is odd, add a random integer (1-9) and repeat (up to 3 times max).
   - If sum becomes even, move to multiplication stage.

2. **Multiplication Stage:**
   - Multiply all the numbers.
   - If product is odd, add a random integer (1-9) and repeat (up to 3 times max).
   - If product becomes even, move to division stage.

3. **Division Stage:**
   - Perform integer division: first element divided by last element.
   - Display the final result.

> ⚠️ If division by zero occurs, it is safely handled.

##  Project Structure

```bash
.
├── main.py          # Main controller script
├── addition.py      # Contains logic for addition stage
├── multiplication.py# Contains logic for multiplication stage
├── division.py      # Contains logic for division stage
└── README.md        # Project documentation
```

#  How to Run
## 1. Clone the Repository:
```bash
git clone <your-repo-link>
cd <your-repo-name>
```
# 2. Run the Program:

```bash
python3 main.py
```

#  Input Format

User will be prompted to enter comma-separated integers.

All integers must be between 0 and 9.

The program will keep asking until valid input is provided.

# Features

Fully automated odd/even checking.

Controlled retries up to 3 times for odd cases.

Random integer insertion logic.

Error handling for invalid input and division by zero.

