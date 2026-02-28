def descending_order(num):
    s=str(num)
    lst=list(s)
    lst.sort(reverse=True)
    s_new=''
    for i in lst:
        s_new+=str(i)
        
    return int(s_new)