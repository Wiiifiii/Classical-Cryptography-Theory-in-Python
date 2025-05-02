def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example
print("gcd(193, 553):", gcd(193, 553))
print("gcd(470101115, 38128805):", gcd(470101115, 38128805))
