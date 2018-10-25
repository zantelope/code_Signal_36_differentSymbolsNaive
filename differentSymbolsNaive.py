def differentSymbolsNaive(s):

    ### empty array to hold unique characters
    uniqueChars = []
    
    ### check if each char is in the uniqueChars list.
    ### if it isn't, append uniqueChars with char.
    ### if it is, continue.
    for char in s:
        if char not in uniqueChars:
            uniqueChars.append(char)
        else:
            continue
    
    return len(uniqueChars)
