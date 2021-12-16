def counting_sort(alist, largest):
    c = [0] * (largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1

    c[0] = c[0] - 1
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(alist)

    for x in reversed(alist):
        result[c[x]] = x
        c[x] = c[x] - 1

    return result


alist = [3, 4, 1, 2, 6, 8, 9]
k = max(alist)
sorted_list = counting_sort(alist, k)
print(sorted_list)
