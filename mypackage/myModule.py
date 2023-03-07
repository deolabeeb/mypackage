def top_n(items, n):
    """
    return the top n term in an array, in descending order.
    
    Args:
        items(Array): List or array-like object
        n (int): Number of items to return
        
    Return:
        Array: Top n terms in an array in dscsending order
        
    Egs:
       >>> top_n([8, 3, 2, 7, 4], 3)
            [8, 7, 3]
    
    """
    
    items = sorted(items, reverse=True)
    items = items[:n]
    return items

