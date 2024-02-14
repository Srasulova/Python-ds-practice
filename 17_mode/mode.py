def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counts = {}
    for item in nums:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    max_count = max(counts.values())
    max_keys = [key for key, value in counts.items() if value == max_count]
    
    return max_keys[0]




print(mode([3, 3, 1, 2, 1, 4, 4, 4, 4, 4, 5]))
print(mode([2, 2, 3, 3, 2, 2, 2, 2]))