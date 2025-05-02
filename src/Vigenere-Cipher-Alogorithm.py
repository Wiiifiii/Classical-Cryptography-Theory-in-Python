def vigenere_encrypt(plaintext, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    keyword_repeated = ""
    plaintext = plaintext.upper().replace(" ", "")
    keyword = keyword.upper().replace(" ", "")
    result = ""

    # Extend the keyword to match the length of the plaintext
    for i in range(len(plaintext)):
        keyword_repeated += keyword[i % len(keyword)]

    # Encrypt the plaintext
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():  # Check if the character is a letter
            shift = alphabet.index(keyword_repeated[i])
            new_index = (alphabet.index(plaintext[i]) + shift) % 29 # in english it is 26
            result += alphabet[new_index]
        else:
            result += plaintext[i]

    return result

def vigenere_decrypt(ciphertext, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    keyword_repeated = ""
    ciphertext = ciphertext.upper().replace(" ", "")
    keyword = keyword.upper().replace(" ", "")
    result = ""

    # Extend the keyword to match the length of the ciphertext
    for i in range(len(ciphertext)):
        keyword_repeated += keyword[i % len(keyword)]

    # Decrypt the ciphertext
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = alphabet.index(keyword_repeated[i])
            new_index = (alphabet.index(ciphertext[i]) - shift) % 29 # in english it is 26
            result += alphabet[new_index]
        else:
            result += ciphertext[i]

    return result

# Example usage
plaintext = """Suomenlahdella kaapelin rikkomisesta epaillyn Eagle S:n ankkuri on löytynyt merenpohjasta.
Ylen tietojen mukaan ankkurin nosti Ruotsin Puolustusvoimien monitoimialus HMS Belos."""
keyword = "LASKENNANPERUSMALLIT"
encrypted = vigenere_encrypt(plaintext, keyword)
decrypted = vigenere_decrypt(encrypted, keyword)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
