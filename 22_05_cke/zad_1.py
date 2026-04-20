A = [8, 4, 9, 10, 5, 7]
n = len(A)
k = 0
for i in range(1, n +1):
    if i not in A:
        k += 1

print(k)
