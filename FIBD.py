# def wabbits(n, k):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return wabbits(n-1, k) + k * wabbits(n-2, k)

#Solution by https://github.com/zonghui0228/rosalind-solutions
def num_rabbits(n, m):
    # n is the n-th month.
    # m is that a rabbit live for m month.
    # in the first month, the num of rabbit is 1. 
    num_list = []
    num_list.append(0)
    num_list.append(1)
    for i in range(1, n+1, 1):
        if i < m:
            num_list.append(num_list[i] + num_list[i-1])
        if i == m:
            num_list.append(num_list[i] + num_list[i-1] - num_list[i-m+1])
        if i > m:
            num_list.append(num_list[i] + num_list[i-1] - num_list[i-m])
    # print(num_list)
    return num_list[n]

num_rabbits(80,18)