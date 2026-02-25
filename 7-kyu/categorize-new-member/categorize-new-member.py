def open_or_senior(data):
    lst=[]
    for i in data:
        if i[0]>=55 and i[1]>7:
            lst.append("Senior")
        else:
            lst.append("Open")
        
    return lst