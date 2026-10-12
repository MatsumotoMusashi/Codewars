def f2hex(fraction):
    i,f=int(eval(fraction)),eval(fraction)-int(eval(fraction))
    hi,hf=hex(i)[2:],""
    for _ in range(6):
        hf,f=hf+hex(int(f*16))[2:],f*16-int(f*16)
    return hi+f".{hf}".rstrip("0")*int(set(hf)!={"0"})