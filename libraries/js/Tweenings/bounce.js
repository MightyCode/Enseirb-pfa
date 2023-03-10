class Bounce {
    static evaluate(tweeningBehaviour, t, b, c, d){
        switch(tweeningBehaviour) {
            case ETweeningBehaviour.IN:
                return Bounce.in(t,b,c,d);
            case ETweeningBehaviour.OUT:
                return Bounce.out(t,b,c,d);
            case ETweeningBehaviour.IN_OUT:
                return Bounce.inOut(t,b,c,d);
            default:
                return null;
        }
    }
    

    static in(t, b, c, d){
        return c - Bounce.out(d - t, 0, c, d) + b;
    }

    static out(t, b, c, d){
        if ((t /= d) < (1 / 2.75)) {
			return c * (7.5625 * t * t) + b;
		} else if (t < (2 / 2.75)) {
			return c*(7.5625 * (t -= (1.5 / 2.75)) * t + 0.75) + b;
		} else if (t < (2.5 / 2.75)) {
			return c*(7.5625 * (t -= (2.25 / 2.75)) * t + .9375) + b;
		} else {
			return c*(7.5625 * (t -= (2.625 / 2.75)) * t + .984375) + b;
		}
    }
    
    static inOut(t, b, c, d){
        if (t < d / 2){
            return Bounce.in(t * 2, 0, c, d) / 2 + b;
        } else {
            return Bounce.out(t * 2 -d, 0, c, d) / 2 + c / 2 + b;
        }
    }
}