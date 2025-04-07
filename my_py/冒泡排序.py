"""

冒泡

a = [97, 8, 98, 89, 4, 5]

for i in range(len(a)):
    for j in range(i, len(a) - 1):
        j += 1
        dd=a[j]
        if a[i] > a[j]:
            c = a[i]
            a[i] = a[j]
            a[j] = c

print(a)

"""

