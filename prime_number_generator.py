def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):  # Now this works because is_prime is defined above
            primes.append(num)
    return primes

up_to = int(input("Generate all prime numbers up to: "))
prime_list = generate_primes(up_to)
print(f"Prime numbers up to {up_to}:")
print(prime_list)
