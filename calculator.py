def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num != 0:  # Avoid division by zero
            result /= num
    return result

def main():
    print("Welcome to my calculator!")
    n = int(input("How many numbers do you want to operate on? "))
    numbers = []
    
    for i in range(n):
        number = float(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    print("\nOperations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = int(input("Enter the operation (1/2/3/4): "))
    
    if choice == 1:
        result = add(numbers)
        operation = "addition"
    elif choice == 2:
        result = subtract(numbers)
        operation = "subtraction"
    elif choice == 3:
        result = multiply(numbers)
        operation = "multiplication"
    elif choice == 4:
        result = divide(numbers)
        operation = "division"
    else:
        print("Invalid choice")
        return

    print(f"The result of {operation} is: {result}")

if __name__ == "__main__":
    main()
