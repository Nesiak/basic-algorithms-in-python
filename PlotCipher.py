def plot_cipher(text):
    result = ''
    n = len(text)
    
    for i in range(0, n, 4):
        result += text[i]
    for i in range(1, n, 2):
        result += text[i]
    for i in range (2, n, 4):
        result += text[i]
    
    return result
