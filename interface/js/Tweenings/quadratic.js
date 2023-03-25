class Quadratic {
    static evaluate(tweeningBehaviour, t, b, c, d){
        switch(tweeningBehaviour) {
            case ETweeningBehaviour.IN:
                return Quadratic.in(t,b,c,d);
            case ETweeningBehaviour.OUT:
                return Quadratic.out(t,b,c,d);
            case ETweeningBehaviour.IN_OUT:
                return Quadratic.inOut(t,b,c,d);
            default:
                return null;
        }
    }

    static in(t, b, c, d){
        return c * (t /= d) * t + b;
    }


    static out(t, b, c, d){
        return -c * (t /= d) * (t - 2) + b;
    }

    static inOut(t, b, c, d){
        if ((t /= d / 2) < 1) {
            return c / 2 * t * t + b;
        }

		return -c / 2 * ((--t) * (t - 2) - 1) + b;
    }
}