def wabbits(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return wabbits(n-1, k) + k * wabbits(n-2, k)

print(wabbits(29, 2))  # Should compute the number of rabbit pairs after 5 months with each pair producing 3 pairs.
