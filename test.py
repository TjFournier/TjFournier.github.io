def has_index_at_value(xs):
    '''
    Return True if xs[i] == i for any i.
    HINT:
    For this problem, you need access to the both the indexes and the values.
    Therefore, you cannot use a for loop that looks like
        for x in xs:
    and instead you must use a for loop that looks like
        for i in range(len(xs)):
    >>> has_index_at_value([0])
    True
    >>> has_index_at_value([1])
    False
    >>> has_index_at_value([1, 1])
    True
    >>> has_index_at_value([1, 0])
    False
    >>> has_index_at_value([0, 0])
    True
    >>> has_index_at_value([7, 3, 2, 8])
    True
    >>> has_index_at_value([2, 9, 5, 6, 19, 6, 6, 6, 6, 6])
    True
    >>> has_index_at_value([2, 9, 5, 4, 19, 4, 4, 4, 4, 4])
    False
    '''
    for i in range(len(xs)):
        x = xs[i]
        if x == i:
            return True
    return False
            