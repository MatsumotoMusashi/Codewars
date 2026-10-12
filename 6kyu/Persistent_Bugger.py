def persistence(n):
    # your code
    time = 0
    while 2 <= len(str(n)):
        time += 1
        s = 1
        for a in str(n):
            s *= int(a)
        n = s
    return time  