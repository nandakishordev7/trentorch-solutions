def is_subset(a, b):
    """
    a, b: Python sets

    Returns:
        True if every element of a is also in b (a is a subset of b,
        written a subseteq b), False otherwise.
    """
    # TODO: Implement using Python's own set operations.
    return a.issubset(b)
    pass


def argmax(values):
    best_index = 0
    best_value = values[0]
    for i,v in enumerate(values):
        if v > best_value:
            best_value = v
            best_index = i 
    return best_index
    pass
