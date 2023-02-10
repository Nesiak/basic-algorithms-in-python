def cesar_cipher(text, alphabet, key):
    result = ''
    dlT = len(text)
    dlA = len(alphabet)
    
    for i in range(dlT):
        for j in range(dlA):
            if text[i] == alphabet[j]:
                result += alphabet[(j + key) % dlA]
    
    return result
    
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
