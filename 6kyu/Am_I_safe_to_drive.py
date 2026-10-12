def drive(drinks,finished,drive_time):
    alc=float(format(sum(ABV*ml for ABV,ml in drinks)/1000,".2f"))
    h1,m1,h2,m2=[int(n) for n in finished.split(":")+drive_time.split(":")]
    return [alc,alc<24*int(h2<h1 or (h2==h1 and m2<=m1))+h2-h1+(m2-m1)/60]