def euler_totient(n):
    if n == 0:
        return 0
    result = n
    p = 2
    
    # Check for each number to see if it is a factor of n
    while p * p <= n:
        # Check if p is a divisor of n
        if n % p == 0:
            # If yes, then it is a prime factor, apply the totient formula part
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    
    # This condition is checked to see if n becomes a prime number greater than 1
    if n > 1:
        result -= result // n
    
    return result

# Example usage
print("Φ(117):", euler_totient(117))   # Multiple prime factors
print("Φ(34327):", euler_totient(34327))   # A product of primes
print("Φ(2**8):", euler_totient(2**8))  # Power of a prime
print("Φ(510510):", euler_totient(510510))  # Product of first few primes
