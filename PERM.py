
n = 6
perm = []
while n >0:
    perm.append(n)
    n=n-1

perm

# def permutation(a, k=0):
#    if k == len(a):
#       print(a)
#    else:
#       for i in range(k, len(a)):
#          a[k], a[i] = a[i] ,a[k]
#          permutation(a, k+1)
#          a[k], a[i] = a[i], a[k]


def permutation(a, k=0):
    if k == 0 and a:
        global perm_count
        perm_count = 0

    if k == len(a):
        perm_count += 1
        print(' '.join(map(str, a)))
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i], a[k]
            permutation(a, k+1)
            a[k], a[i] = a[i], a[k]

    if k == 0:
        print(perm_count)
    
(permutation(perm))
