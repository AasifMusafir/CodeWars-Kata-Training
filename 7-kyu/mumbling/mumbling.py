def accum(st):
    result=[]
    for i,ch in enumerate(st):
        s=ch.upper()+ch.lower()*i
        result.append(s)
    
    return "-".join(result)