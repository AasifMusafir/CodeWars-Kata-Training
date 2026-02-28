def high_and_low(s):
    s=s.split()
    c=[]
    for i in s:
        c.append(int(i))
    mini=min(c)
    maxi=max(c)
    
    return f"{maxi} {mini}"