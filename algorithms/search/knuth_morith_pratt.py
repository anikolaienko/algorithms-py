def knuthMorrisPratt(string, substring):
    prefix_idx = [0] * len(substring)
    
    j = 0
    for i in range(1, len(substring)):
        if substring[i] == substring[j]:
            if i + 1 < len(substring):
                j += 1
                prefix_idx[i + 1] = j
        else:
            j = prefix_idx[i]
            while j > 0 and substring[i] != substring[j]:
                j = prefix_idx[j]
            if j > 0:
                j += 1
                prefix_idx[i + 1] = j

    j = 0
    for i in range(1, len(string)):
        if string[i] == substring[j]:
            j += 1
            if j == len(substring):
                return True
        else:
            while j > 0 and substring[j] != string[i]:
                j = prefix_idx[j]

            if j > 0:
                j += 1
    
    return False
