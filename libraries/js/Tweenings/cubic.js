class Cubic {
    static evaluate(tweeningBehaviour, t, b, c, d){
        switch(tweeningBehaviour) {
            case ETweeningBehaviour.IN:
                return Cubic.in(t,b,c,d);
            case ETweeningBehaviour.OUT:
                return Cubic.out(t,b,c,d);
            case ETweeningBehaviour.IN_OUT:
                return Cubic.inOut(t,b,c,d);
            default:
                return null;
        }
    }

    static in(t, b, c, d){
        return c * (t /= d) * t * t + b;
    }


    static out(t, b, c, d){
        return c * ((t=t/d - 1) * t * t + 1) + b;
    }

    static inOut(t, b, c, d){
        if ((t /= d / 2) < 1){
            return c / 2 * t * t * t + b;
        }
        
		return c / 2 * ((t -= 2) * t * t + 2) + b;
    }
}