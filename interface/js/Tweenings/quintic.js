class Quintic {
    static evaluate(tweeningBehaviour, t, b, c, d){
        switch(tweeningBehaviour) {
            case ETweeningBehaviour.IN:
                return Quintic.in(t,b,c,d);
            case ETweeningBehaviour.OUT:
                return Quintic.out(t,b,c,d);
            case ETweeningBehaviour.IN_OUT:
                return Quintic.inOut(t,b,c,d);
            default:
                return null;
        }
    }
    

    static in(t, b, c, d){
        return c * (t /= d) * t * t * t * t + b;
    }


    static out(t, b, c, d){
        return c * ((t = t / d - 1) * t * t * t * t + 1) + b;
    }

    static inOut(t, b, c, d){
        if ((t /= d / 2) < 1){
            return c / 2 * t * t * t * t * t + b;
        } 
		
        return c / 2 * ((t -= 2) * t * t * t * t + 2) + b;
    }
}