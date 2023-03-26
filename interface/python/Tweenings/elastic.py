from interface.python.Tweenings.ETweeningBehaviour import ETweeningBehaviour as ETB
import math

class Elastic:
    def evaluate(tweeningBehaviour, t, b, c, d, arg1, arg2) :
        if tweeningBehaviour == ETB.IN:
            return Elastic.in_ap(t,b,c,d, arg1, arg2)
        elif tweeningBehaviour == ETB.OUT:
            return Elastic.out_ap(t,b,c,d, arg1, arg2)
        elif tweeningBehaviour == ETB.IN_OUT:
            return Elastic.inOut_ap(t,b,c,d, arg1, arg2)

        return None

    def in_elastic(t, b, c, d):
        if (t == 0):
            return b

        t = t / d

        if (t == 1) :
            return b + c

        p: float = d * 0.3
        a: float = c
        s: float = p / 4

        t = t - 1
        
        return -(a * math.pow(2, 10 * t) * math.sin((t * d - s) * (2 * math.pi) / p)) + b

    def in_ap(t, b, c, d, a, p):
        if (a == None or p == None):
            return Elastic.in_elastic(t, b, c, d)

        s = 0
        if (t == 0):
            return b
        
        t = t / d
        if (t == 1):
            return b + c;  

        if (a < math.abs(c)):
            a = c; 
            s = p / 4; 
        else :
            s = p / (2 * math.pi) * math.asin(c / a)
        
        t = t - 1    
        return -(a * math.pow(2, 10 * t) * math.sin((t * d - s) * (2 * math.pi) / p)) + b
    


    def out(t, b, c, d):
        if (t == 0):
            return b;  
        
        t = t / d
        if (t == 1):
            return b + c

        p = d * 0.3
        a = c
        s = p / 4
		
        return (a * math.pow(2, -10 * t) * math.sin((t * d - s) * (2 * math.pi) / p) + c + b)
    

    def out_ap(t, b, c, d, a, p):
        if (a == None or p == None):
            return Elastic.out(t, b, c, d)

        s = 0
        if (t == 0): 
            return b;  
        
        t = t / d
        if (t == 1):
            return b + c

        if (a < math.abs(c)) :
            a = c
            s = p / 4
        else : 
            s = p / (2 * math.pi) * math.asin(c / a)
        
		
        return (a * math.pow(2, -10 * t) * math.sin((t * d - s) * (2 * math.pi) / p) + c + b)	
    

    def inOut(t, b, c, d):
        if (t == 0):
            return b
            
        t = t / (d / 2)    
        if (t == 2):
            return b + c
		
        p = d * (0.3 * 1.5)
        a = c; 
        s = p / 4
        t = t - 1

        if (t < 1):
            return -0.5 * (a * math.pow(2, 10 * t) * math.sin((t * d - s) * (2 * math.pi) / p)) + b

        return a * math.pow(2, -10 * t) * math.sin((t * d - s) * (2 * math.pi) / p) * 0.5 + c + b
    


    def inOut_ap(t, b, c, d, a, p):
        if (a == None or p == None):
            return Elastic.inOut(t, b, c, d)

        s = 2
        if (t == 0): 
            return b
        
        t = t / (d / 2)
        if (t == 2): 
            return b+c
              
        if (a < math.abs(c)):
            a = c
            s = p / 4
        else: 
            s = p / (2 * math.pi) * math.asin(c / a)

        t = t - 1

        if (t < 1):
            return -0.5 * (a * math.pow(2, 10 * t) * math.sin((t * d - s) * (2 * math.pi) / p)) + b

        return a*math.pow(2, -10 * t) * math.sin((t * d - s) * (2 * math.pi) / p) * 0.5 + c + b
