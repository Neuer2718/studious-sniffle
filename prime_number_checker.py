import math

def is_prime(n):
    # Check if number is less than or equal to 1 (not prime)
    if n <= 1:
        return False
    # 2 is the only even prime number
    elif n == 2:
        return True
    # Eliminate all other even numbers
    elif n % 2 == 0:
        return False

    # Check for divisors from 3 up to the square root of n, skipping even numbers
    for i in range(3, math.isqrt(n) + 1, 2):
        # If a divisor is found, n is not prime
        if n % i == 0:
            return False

    # If no divisors were found, n is prime
    return True

# Ask the user to enter a number
def get_user_input():
    while True:
        try:
            return int(input("Enter a number to check if it is prime: "))
        except ValueError:
            print("❌ That wasn't a valid number. Please enter an integer.")

# Print the result in a friendly way
def print_result(number):
    if is_prime(number):
        print(f"✅ {number} is a prime number!")
    else:
        print(f"❌ {number} is not a prime number.")

# Main loop
def main():
    print("🔢 Welcome to the Prime Number Checker!")
    while True:
        number = get_user_input()
        print_result(number)
        again = input("Would you like to check another number? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Thanks for using the Prime Checker. Goodbye!")
            break

# Run the program
main()
