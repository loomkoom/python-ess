def ritsen(l1, l2):
    a, b = 0, 0
    while a < len(l2):
        if l2[a] < l1[b]:
            rits = b
        else:
            rits = b + 1
        if b == len(l1) - 1:
            l1.extend(l2[a:])
            break
        l1.insert(rits, l2[a])

        a += 1
        b += 2


def ritsen(l1, l2):
    orig_len = len(l1)

    i = min(len(l1), len(l2)) - 1
    l1.extend([None for k in range(len(l2))])
    if orig_len > len(l2):
        l1[orig_len + 1:] = l1[len(l2):orig_len]
    print(i)
    print(l1)

    while i >= 0:
        klein = min(l1[i], l2[i])
        groot = max(l1[i], l2[i])

        l1[i * 2] = klein
        l1[i * 2 + 1] = groot

        print(l1, l2, i, sep = "  |  ")
        i -= 1
    if len(l2) > orig_len:
        l1[2 * orig_len:] = l2[orig_len:]
    print(l1)


lijst1 = [2, 5, 1, 12, 7, 8, 9]
lijst2 = [1, 5, 8, 6]
ritsen(lijst1, lijst2)
assert lijst1 == [1, 2, 5, 5, 1, 8, 6, 12, 7, 8, 9]
print("\n")
lijst1 = [1, 12, 3, 6]
lijst2 = [4, 6, 8, 10, 12, 14]

ritsen(lijst1, lijst2)
assert lijst1 == [1, 4, 6, 12, 3, 8, 6, 10, 12, 14]
