def top_n(item, n):
    """Returns the top n items in an array, in desc order
    
    Args:
        item(array): list or array-like object
        n(int): num of items to return
    
    Returns:
        array: top n items in desc order
        
    Egs:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]
    """
    
    for i in range(n):        # Keep sorting until we have the n items
        for j in range(len(item)-1-i):
            
            if item[j] > item[j+1]:      # if this item is greater than the next item
                item[j], item[j+1] = item[j+1], item[j]   # swap the two
    
    # Getting the last two item
    top_n = item[-n:]
    
    # return in decending order
    return top_n[::-1]