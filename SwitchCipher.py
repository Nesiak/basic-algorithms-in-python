def SwitchCipher(text):
    tekstTab = []
    
    for i in text:
        textTab.append(i)
    
    n = len(textTab)
    
    for i in range(0, n - 1, 2):
        tmp = textTab[i]
        textTab[i] = textTab[i + 1]
        textTab[i + 1] = tmp
    
    subtitle = ''
    for i in textTab:
        subtitle += i
    return subtitle
