from ETweeningBehaviour import ETweeningBehaviour as ETB

class Bounce:
    def evaluate(tweeningBehaviour, t, b, c, d) :
        if tweeningBehaviour == ETB.IN:
            return Bounce.in_bounce(t,b,c,d)
        elif tweeningBehaviour == ETB.OUT:
            return Bounce.out(t,b,c,d)
        elif tweeningBehaviour == ETB.IN_OUT:
            return Bounce.inOut(t,b,c,d)

        return None
    

    def in_bounce(t, b, c, d):
        return c - Bounce.out(d - t, 0, c, d) + b
    

    def out(t, b, c, d):
        t = t / d
        if (t < (1 / 2.75)):
            return c * (7.5625 * t * t) + b
        elif (t < (2 / 2.75)) :
            t = t - (1.5 / 2.75)
            return c*(7.5625 * t * t + 0.75) + b
        elif (t < (2.5 / 2.75)) :
            t = t - (2.25 / 2.75)
            return c*(7.5625 * t * t + .9375) + b

        t = t - (2.625 / 2.75)
        return c*(7.5625 * t * t + .984375) + b
		
    
    
    def inOut(t, b, c, d) :
        if (t < d / 2):
            return Bounce.in_bounce(t * 2, 0, c, d) / 2 + b
        
        return Bounce.out(t * 2 -d, 0, c, d) / 2 + c / 2 + b
        
    
