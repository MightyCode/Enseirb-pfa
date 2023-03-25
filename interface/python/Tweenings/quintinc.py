from ETweeningBehaviour import ETweeningBehaviour as ETB

class Quintic:
    def evaluate(tweeningBehaviour, t, b, c, d) :
        if tweeningBehaviour == ETB.IN:
            return Quintic.in_quintic(t,b,c,d)
        elif tweeningBehaviour == ETB.OUT:
            return Quintic.out(t,b,c,d)
        elif tweeningBehaviour == ETB.IN_OUT:
            return Quintic.inOut(t,b,c,d)

        return None

    def in_quintic(t, b, c, d):
        t = t / d
        return c * t * t * t * t * t + b
    


    def out(t, b, c, d):
        t = t / d - 1
        return c * (t * t * t * t * t + 1) + b
    

    def inOut(t, b, c, d):
        t = t / (d / 2)
        if (t < 1):
            return c / 2 * t * t * t * t * t + b
        
        t = t - 2
        return c / 2 * (t * t * t * t * t + 2) + b
    