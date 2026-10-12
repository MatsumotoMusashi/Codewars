num=["zero","one","two","three","four","five","six","seven","eight","nine"]
odd_f=lambda n: "".join("".join(num[int(n[d-1])].upper() if i%2==0 else num[int(n[d-1])] for i in range(d//len(num[int(n[d-1])])))+(num[int(n[d-1])].upper() if (d//len(num[int(n[d-1])]))%2==0 else num[int(n[d-1])])[:d%len(num[int(n[d-1])])] if int(n[d-1])%2==1 else n[d-1] for d in range(1,len(n)+1))
even_f=lambda n: "".join("".join(num[int(n[d-1])] if i%2==0 else num[int(n[d-1])].upper() for i in range(d//len(num[int(n[d-1])])))+(num[int(n[d-1])] if (d//len(num[int(n[d-1])]))%2==0 else num[int(n[d-1])].upper())[:d%len(num[int(n[d-1])])] if int(n[d-1])%2==0 else n[d-1] for d in range(1,len(n)+1))
def conv(num):
    return [even_f,odd_f][len(str(num))%2](str(num))