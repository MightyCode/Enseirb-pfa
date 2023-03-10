from ETweeningBehaviour import ETweeningBehaviour as ETB

class Linear:
    def evaluate(tweeningBehaviour, t, b, c, d) :
        if tweeningBehaviour == ETB.IN:
            return Linear.in_linear(t,b,c,d)
        elif tweeningBehaviour == ETB.OUT:
            return Linear.out(t,b,c,d)
        elif tweeningBehaviour == ETB.IN_OUT:
            return Linear.inOut(t,b,c,d)

        return None

    def in_linear(t, b, c, d):
        return c * t / d + b
    


    def out(t, b, c, d):
        return Linear.in_linear(t, b, c, d)
    

    def inOut(t, b, c, d):
        return Linear.in_linear(t, b, c, d)
    
