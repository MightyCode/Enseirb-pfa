class Circular {
    static evaluate(tweeningBehaviour, t, b, c, d){
        switch(tweeningBehaviour) {
            case ETweeningBehaviour.IN:
                return Circular.in(t,b,c,d);
            case ETweeningBehaviour.OUT:
                return Circular.out(t,b,c,d);
            case ETweeningBehaviour.IN_OUT:
                return Circular.inOut(t,b,c,d);
            default:
                return null;
        }
    }
    

    static in(t, b, c, d){
        return -c * (Math.sqrt(1 - (t /= d) * t) - 1) + b;
    }


    static out(t, b, c, d){
        return c * Math.sqrt(1 - (t = t / d -1) * t) + b;
    }

    
    static inOut(t, b, c, d){
        if ((t /= d / 2) < 1){ 
            return -c / 2 * (Math.sqrt(1 - t * t) - 1) + b;
        }

		return c / 2 * (Math.sqrt(1 - (t -= 2) * t) + 1) + b;
    }
}