def berlin_clock(time):
    h,m,s=[int(i) for i in time.split(":")]
    return "\n".join(["YO"[s%2],"R"*(h//5)+"O"*(4-h//5),"R"*(h%5)+"O"*(4-h%5),"YYRYYRYYRYY"[:m//5]+"O"*(11-m//5),"Y"*(m%5)+"O"*(4-m%5)])