def top_n(items,n):
    """ return the top n items in an array, i desc order
    
    Args:
        items (array): list or array-like object
        n (int): no. of item to return
        
    Return:
        array: top n items in desc order"""
    
    for i in range(n):
        for j in range(len(items)-1-j):
            if items[j]> items[j+1]:
                items[j], items[j+1]= items[j+1],items[j]

    top_n = items[-n:]
    return top_n[::-1]