def hamming(s1, s2):
    dist = 0

    if len(s1) != len(s2):
        print("Sequências com tamanhos distintos")
        return None
    else:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                dist += 1
    return dist