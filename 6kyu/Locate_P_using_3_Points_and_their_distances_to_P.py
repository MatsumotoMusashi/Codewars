from fractions import Fraction
def triangulate(A,dA,B,dB,C,dC):
    if A[0]!=B[0] and A[0]!=C[0]:
        P1,P2,P3,P4=Fraction(A[0]**2+A[1]**2-B[0]**2-B[1]**2+dB-dA,2*(A[0]-B[0])),Fraction(B[1]-A[1],A[0]-B[0]),Fraction(A[0]**2+A[1]**2-C[0]**2-C[1]**2+dC-dA,2*(A[0]-C[0])),Fraction(C[1]-A[1],A[0]-C[0])
        y=int((P3-P1)/(P2-P4))
        return (int(P1+P2*y),y)
    elif A[0]==B[0]:
        y=(A[0]**2+A[1]**2-B[0]**2-B[1]**2+dB-dA)//(2*(A[1]-B[1]))
        return (int(Fraction(A[0]**2+A[1]**2-C[0]**2-C[1]**2+dC-dA,2*(A[0]-C[0]))+Fraction(C[1]-A[1],A[0]-C[0])*y),y)
    else:
        y=(A[0]**2+A[1]**2-C[0]**2-C[1]**2+dC-dA)//(2*(A[1]-C[1]))
        return (int(Fraction(A[0]**2+A[1]**2-B[0]**2-B[1]**2+dB-dA,2*(A[0]-B[0]))+Fraction(B[1]-A[1],A[0]-B[0])*y),y)