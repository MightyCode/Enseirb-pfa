from interface.python.Tweenings.ETweeningBehaviour import ETweeningBehaviour as ETB

class Quadratic:
    def evaluate(tweeningBehaviour, t, b, c, d) :
        if tweeningBehaviour == ETB.IN:
            return Quadratic.in_quadratic(t,b,c,d)
        elif tweeningBehaviour == ETB.OUT:
            return Quadratic.out(t,b,c,d)
        elif tweeningBehaviour == ETB.IN_OUT:
            return Quadratic.inOut(t,b,c,d)

        return None

    def in_quadratic(t, b, c, d):
        t = t / d
        return c * t * t + b
    

    def out(t, b, c, d):
        t = t / d
        return -c * t * (t - 2) + b
    

    def inOut(t, b, c, d):
        t = t / (d / 2)
        if (t < 1):
            return c / 2 * t * t + b
        
        t = t - 1
        return -c / 2 * (t * (t - 2) - 1) + b

    