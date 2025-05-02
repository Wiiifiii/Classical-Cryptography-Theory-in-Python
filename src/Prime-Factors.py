def prime_factors(n):
    factors = []
    # Test for number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # n must be odd at this point, thus skip even numbers and test only odd ones
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    return factors

# Numbers to factorize
numbers = [505, 153, 35035, 44503]

# Calculate prime factors for each number
results = {num: prime_factors(num) for num in numbers}

# Print the results
for num, factors in results.items():
    print(f"Prime factors of {num} are: {factors}")
