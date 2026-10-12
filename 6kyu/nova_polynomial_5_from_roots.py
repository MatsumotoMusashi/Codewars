def poly_from_roots(r):
    p=[1]
    for n in r:
        p=[(0 if i==0 else p[i-1])-n*p[i] for i in range(len(p))]+[1]
    return p