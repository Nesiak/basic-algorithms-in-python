def sort(str):
    n = len(str)
    str = list(str)
    
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if str[i] > str[i + 1]:
                str[i], str[i + 1] = str[i + 1], str[i]
            
    str = ' '.join(str)
    return str
    
def isAnagram(str1, str2):
    if len(str1) == len(str2):
        if sort(str1) == sort(str2):
            return True
        else:
            return False
    else:
        return False
