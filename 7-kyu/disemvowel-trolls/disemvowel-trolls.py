def disemvowel(string_):
    a=["a","e","i","o","u"]
    result=[i for i in string_ if i.lower() not in a]
    result="".join(result)
    
    return result