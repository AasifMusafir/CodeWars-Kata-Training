def find_even_index(arr):
    for i in range(len(arr)):
        left=sum(arr[:i])
        right=sum(arr[i+1:])
        
        if right==left:
            return i
        
    return -1
​