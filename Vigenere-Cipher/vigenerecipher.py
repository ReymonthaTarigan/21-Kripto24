def vigenere_encrypt(plaintext, key):
    encrypted_text = []
    key_length = len(key)
    key_index = 0
    
    for char in plaintext:
        if char.isalpha(): 
            shift = ord(key[key_index].lower()) - ord('a')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            
            encrypted_text.append(encrypted_char)
            key_index = (key_index + 1) % key_length  
        else:
            encrypted_text.append(char)  
    
    return ''.join(encrypted_text)


def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():  
            shift = ord(key[key_index].lower()) - ord('a')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            decrypted_text.append(decrypted_char)
            key_index = (key_index + 1) % key_length 
        else:
            decrypted_text.append(char)  
    
    return ''.join(decrypted_text)



plaintext = input("Masukkan teks: ").upper()
key = input("Masukkan kunci: ").lower()


encrypted_text = vigenere_encrypt(plaintext, key)
decrypted_text = vigenere_decrypt(encrypted_text, key)


print("Teks terenkripsi:", encrypted_text)
print("Teks terdekripsi:", decrypted_text)
