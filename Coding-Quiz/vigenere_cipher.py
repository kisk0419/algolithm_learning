import string

ALPHABET = string.ascii_uppercase

def generate_key(message: str, keyword: str) -> str:
    # message:ATTACKAT
    # keyword:LEMON
    # key:    LEMONLEM
    keyword_num = len(message) // len(keyword)
    keyword_mod = int(len(message) % len(keyword))
    key = keyword * keyword_num + keyword[:keyword_mod]
    return key


def encrypt_vigenere_cipher(message: str, keyword: str) -> str:
    key = generate_key(message, keyword)
    encrypted_message = ''
    len_message = len(message)
    len_alphabet = len(ALPHABET)

    for i in range(0, len_message):
        if message[i] not in ALPHABET:
            encrypted_message += message[i]
            continue
        # index = int((ALPHABET.index(message[i]) + ALPHABET.index(key[i])) % len_alphabet)
        # encrypted_message += ALPHABET[index]
        index = (ord(message[i]) + ord(key[i])) % (ord('Z') - ord('A') + 1)
        encrypted_message += chr(ord('A') + index)
    
    return encrypted_message


def decrypt_vigenere_cipher(encrypted_message: str, keyword: str) -> str:
    key = generate_key(encrypted_message, keyword)
    decrypted_message = ''
    len_message = len(encrypted_message)
    len_alphabet = len(ALPHABET)

    for i in range(0, len_message):
        if encrypted_message[i] not in ALPHABET:
            decrypted_message += encrypted_message[i]
            continue
        # index = int((ALPHABET.index(encrypted_message[i]) - ALPHABET.index(key[i]) + len_alphabet) % len_alphabet)
        # decrypted_message += ALPHABET[index]
        index = (ord(encrypted_message[i]) - ord(key[i]) + ord('Z') - ord('A') + 1) % (ord('Z') - ord('A') + 1)
        decrypted_message += chr(ord('A') + index)
    
    return decrypted_message


if __name__ == '__main__':
    message = 'ATTACK SILICON VALLEY'
    keyword = 'CAT'

    e = encrypt_vigenere_cipher(message, keyword)
    print('encrypted_message', e)
    e = decrypt_vigenere_cipher(e, keyword)
    print('decrypted_message', e)
