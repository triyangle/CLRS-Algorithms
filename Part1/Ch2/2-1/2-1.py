# 2.1-2
def insertion_sort(lst, reverse = False):
    """
    >>> a = [5, 2, 4, 6, 1, 3]
    >>> insertion_sort(a)
    >>> a
    [1, 2, 3, 4, 5, 6]
    >>> insertion_sort(a, True)
    >>> a
    [6, 5, 4, 3, 2, 1]
    """
    for j in range(1, len(lst)):
        key = lst[j]
        i = j - 1
        condition = lambda i: lst[i] < key if reverse else lst[i] > key
        while i >= 0 and condition(i):
            lst[i + 1] = lst[i]
            i -= 1
        lst[i + 1] = key

# 2.1-3
def search(lst, v):
    """
    >>> a = [5, 2, 4, 6, 1, 3]
    >>> for i in range(1, 7):
    ...     print(search(a, i))
    4
    1
    5
    2
    0
    3
    """
    i = 0
    while i < len(lst) and lst[i] != v:
        i += 1
    return None if i == len(lst) else i
