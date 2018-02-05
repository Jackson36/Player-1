def swap(str):
    x = list(str)
    for i in range(0,len(x),2):
        t=x[i]
        x[i]=s[i+1]
        x[i+1]=t
    
    return "".join(swap(x))
