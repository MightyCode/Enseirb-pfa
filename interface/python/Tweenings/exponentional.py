from interface.python.Tweenings.ETweeningBehaviour import ETweeningBehaviour as ETB
import math

class Exponentional:
    def evaluate(tweeningBehaviour, t, b, c, d) :
        if tweeningBehaviour == ETB.IN:
            return Exponentional.in_exponential(t,b,c,d)
        elif tweeningBehaviour == ETB.OUT:
            return Exponentional.out(t,b,c,d)
        elif tweeningBehaviour == ETB.IN_OUT:
            return Exponentional.inOut(t,b,c,d)

        return None

    
    def in_exponential(t, b, c, d):
        if t == 0:
            return b

        return  c * math.pow(2, 10 * (t / d - 1)) + b
    


    def out(t, b, c, d):
        if (t == d):
            return b + c

        return c * (-math.pow(2, -10 * t / d) + 1) + b;	

    
    def inOut(t, b, c, d):
        if (t == 0):
            return b

        if (t == d): 
            return b + c
        
        t = t / (d / 2)
        if (t < 1): 
            return c / 2 * math.pow(2, 10 * (t - 1)) + b

        return c / 2 * (-math.pow(2, -10 * (t - 1)) + 2) + b
    