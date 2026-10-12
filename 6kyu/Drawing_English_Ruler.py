class Ruler:
    def __init__(self,t:int,n:int):
        if t<2:
            raise ValueError("t must be >= 2")
        if n < 1:
            raise ValueError("n must be >= 1")
        self.t=t
        self.n=n

    def draw(self) -> str:
        default="-"
        for i in range(self.t-2):
            default=f"{default}\n"+"-"*(i+2)+f"\n{default}"
        return f"\n{default}\n".join("-"*self.t+f" {n}" for n in range(self.n+1))