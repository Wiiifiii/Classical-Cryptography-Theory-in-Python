def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    if s == target:
        return partial
    if s >= target:
        return False

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        result = subset_sum(remaining, target, partial + [n])
        if result:
            return result
        
    return False

def generate_random_numbers(size, max_val=100):
    return [random.randint(-max_val, max_val) for _ in range(size)]

if __name__ == "__main__":
    import random
    import time

    sizes = [10, 15, 20]

    for size in sizes:
        numbers = generate_random_numbers(size)
        target = random.randint(-size * 10, size * 10)

        start_time = time.time()
        subset = subset_sum(numbers, target)
        end_time = time.time()
        
        print(f"Set of random numbers: {numbers}")
        print(f"Size: {size}, Target: {target}, Time taken: {end_time - start_time:.5f} seconds")
        if subset:
            print(f"Found a valid subset: {subset}")
        else:
            print("No subset with the required sum was found.")