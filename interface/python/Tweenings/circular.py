from ETweeningBehaviour import ETweeningBehaviour as ETB
import math

class Circular:
    def evaluate(tweeningBehaviour, t, b, c, d) :
        if tweeningBehaviour == ETB.IN:
            return Circular.in_circular(t,b,c,d)
        elif tweeningBehaviour == ETB.OUT:
            return Circular.out(t,b,c,d)
        elif tweeningBehaviour == ETB.IN_OUT:
            return Circular.inOut(t,b,c,d)

        return None

    def in_circular(t, b, c, d):
        t = t / d
        return -c * (math.sqrt(1 - t * t) - 1) + b
    


    def out(t, b, c, d):
        t = t / d - 1
        return c * math.sqrt(1 - t * t) + b
    

    
    def inOut(t, b, c, d):
        t = t / (d / 2)
        if (t < 1):
            return -c / 2 * (math.sqrt(1 - t * t) - 1) + b
        
        t = t - 2
        return c / 2 * (math.sqrt(1 - t * t) + 1) + b
