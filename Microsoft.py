def digits_sorted(i):
    """
    Use recursive method to write a function to check if all the digits of an integer are in non-descending order.
    Duplicates allowed.
    """
    i = abs(i)
    if i < 10:
        return True
    j = i / 10
    if j % 10 > i % 10:
        return False
    if not digits_sorted(j):
        return False
    return True


def order(codes):
    """
    Sort an array that contains only 1's, 2's, and 3's.
    """
    if not codes or len(codes) < 2:
        return
    length = len(codes)
    start, mid, end = 0, 0, length - 1
    while start < length and codes[start] == 1:
        start += 1
    while end >= 0 and codes[end] == 3:
        end -= 1
    mid = start
    while start < end:
        if codes[mid] == 1:
            codes[start], codes[mid] = codes[mid], codes[start]
            start += 1
        elif codes[mid] == 3:
            codes[end], codes[mid] = codes[mid], codes[end]
            end -= 1
        else:
            mid += 1
    return codes
