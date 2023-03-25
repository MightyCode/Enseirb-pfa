from ETweeningBehaviour import ETweeningBehaviour as ETB
import math

class Sinusoidal:
    def evaluate(tweeningBehaviour, t, b, c, d) :
        if tweeningBehaviour == ETB.IN:
            return Sinusoidal.in_sinusoidal(t,b,c,d)
        elif tweeningBehaviour == ETB.OUT:
            return Sinusoidal.out(t,b,c,d)
        elif tweeningBehaviour == ETB.IN_OUT:
            return Sinusoidal.inOut(t,b,c,d)

        return None

    def in_sinusoidal(t, b, c, d):
        return -c * math.cos(t / d * (math.pi / 2)) + c + b
    

    def out(t, b, c, d):
        return c * math.sin(t / d * (math.pi / 2)) + b
    

    def inOut(t, b, c, d):
        return -c / 2 * (math.cos(math.pi * t / d) - 1) + b
    
    