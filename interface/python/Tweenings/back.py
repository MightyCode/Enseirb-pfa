from ETweeningBehaviour import ETweeningBehaviour as ETB

class Back:
    SWING_BACK_DEFAULT: float = 1.70158
    SWING_MULTIPLICATOR: float = 1.525

    def evaluate(tweeningBehaviour, t, b, c, d, arg1) :
        if tweeningBehaviour == ETB.IN:
            return Back.in_s(t,b,c,d,arg1)
        elif tweeningBehaviour == ETB.OUT:
            return Back.out_s(t,b,c,d,arg1)
        elif tweeningBehaviour == ETB.IN_OUT:
            return Back.inOut_s(t,b,c,d,arg1)

        return None
        

    def in_back(t, b, c, d) :
        s: float = Back.SWING_BACK_DEFAULT
        
        t = t / d

        return c * t * t *((s + 1) * t - s) + b


    def in_s(t, b, c, d, s):
        if (s == None) :
            return Back.in_back(t, b, c, d)

        t = t / d

        return c * t * t *((s + 1) * t - s) + b
    


    def out(t, b, c, d):
        s: float = Back.SWING_BACK_DEFAULT

        t = t = t / d - 1

        return c * (t * t * ((s + 1) * t + s) + 1) + b
    

    def out_s(t, b, c, d, s):
        if (s == None) :
            return Back.out(t, b, c, d)

        t = t / d - 1

        return c * (t * t *((s + 1) * t + s) + 1) + b
    

    
    def inOut(t, b, c, d):
        s: float = Back.SWING_BACK_DEFAULT * Back.SWING_MULTIPLICATOR

        t = t / (d / 2)

        if (t < 1):
            return c / 2 * (t * t * ((s + 1) * t - s)) + b

        t = t - 2

        return c / 2 * (t * t * ((s + 1) * t + s) + 2) + b
    

    def inOut_s(t, b, c, d, s):
        if (s == None) :
            return Back.inOut(t, b, c, d)

        t = t / (d / 2)
        s = s * Back.SWING_MULTIPLICATOR

        if (t < 1) :
            return c / 2 * (t * t * ((s + 1) * t - s)) + b

        t = t - 2

        return c / 2 * (t * t * ((s + 1) * t + s) + 2) + b
    