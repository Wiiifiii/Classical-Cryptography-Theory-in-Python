def chi_square_shift(cipher_text):
    from collections import Counter
    import string
    
    # English letter frequency (from a large corpus)
    ENG_FREQ = {'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7, 'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.2, 'k': 0.8, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9, 'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8, 'v': 1.0, 'w': 2.4, 'x': 0.2, 'y': 2.0, 'z': 0.1}
    n = sum(ENG_FREQ.values())
    expected = {k: v / n * len(cipher_text) for k, v in ENG_FREQ.items()}  # Scale expected freq by text length
    
    # Normalize ciphertext to lowercase and filter out non-alphabet characters
    cipher_text = ''.join(filter(str.isalpha, cipher_text.lower()))
    observed = Counter(cipher_text)  # Get observed frequency counts
    
    min_chi_sq, min_shift = float('inf'), 0
    
    # Test all possible shifts
    for shift in range(26):
        chi_sq = sum((observed.get(chr((ord(char) - 97 - shift) % 26 + 97), 0) - expected[char])**2 / expected[char] for char in string.ascii_lowercase)
        
        if chi_sq < min_chi_sq:
            min_chi_sq, min_shift = chi_sq, shift
    
    return min_shift, min_chi_sq

# Example use
cipher_text = "Värnodääx rods uyevex tävuoox. Wevvk yx wkdytk tk eenod yxqod. Eusx foxodda ckk vksxkdk,uex os cyduodk csda"
best_shift, min_chi_sq = chi_square_shift(cipher_text)
print("Best Shift:", best_shift, "with Chi-Square:", min_chi_sq)
