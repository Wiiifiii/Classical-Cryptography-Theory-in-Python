import math

N = 14  # example value for N
T = 6  # example value for T

# Find e coprime with both N and T
for e in range(2, T):
    if math.gcd(e, N) == 1 and math.gcd(e, T) == 1:
        print(f"An appropriate value for e is: {e}")
        break
