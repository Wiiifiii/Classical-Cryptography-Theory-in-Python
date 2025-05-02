def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Shift character within its case (upper or lower)
            offset = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted_text += char  # Keep non-alphabet characters unchanged
    return encrypted_text

# Example
original_text = "Värnodääx rods uyevex tävuoox. Wevvk yx wkdytk tk eenod yxqod. Eusx foxodda ckk vksxkdk,uex os cyduodk csda"
shift = 16
encrypted = caesar_cipher(original_text, shift)
print("Encrypted:", encrypted)


print("Original: ", original_text)
print("Encrypted: ", encrypted)
#print("Decrypted: ", caesar_cipher(encrypted, -shift))