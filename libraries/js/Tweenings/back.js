class Back {
    static SWING_BACK_DEFAULT = 1.70158;
    static SWING_MULTIPLICATOR = 1.525;

    static evaluate(tweeningBehaviour, t, b, c, d, arg1){
        switch(tweeningBehaviour) {
            case ETweeningBehaviour.IN:
                return Back.in_s(t,b,c,d,arg1);
            case ETweeningBehaviour.OUT:
                return Back.out_s(t,b,c,d,arg1);
            case ETweeningBehaviour.IN_OUT:
                return Back.inOut_s(t,b,c,d,arg1);
            default:
                return null;
        }
    }
    

    static in(t, b, c, d){
        var s = Back.SWING_BACK_DEFAULT;

		return c * (t /= d) * t *((s + 1) * t - s) + b;
    }


    static in_s(t, b, c, d, s){
        if (s == null)
            return Back.in(t, b, c, d);

        return c * (t /= d) * t *((s + 1) * t - s) + b;
    }


    static out(t, b, c, d){
        var s = Back.SWING_BACK_DEFAULT;

		return c * ((t = t / d - 1) * t * ((s + 1) * t + s) + 1) + b;
    }

    static out_s(t, b, c, d, s){
        if (s == null)
            return Back.out(t, b, c, d);

        return c * ((t = t / d - 1) * t *((s + 1) * t + s) + 1) + b;
    }

    
    static inOut(t, b, c, d){
        var s = Back.SWING_BACK_DEFAULT;

		if ((t /= d / 2) < 1) 
            return c / 2 * (t * t * (((s *= (Back.SWING_MULTIPLICATOR)) + 1) * t - s)) + b;

		return c / 2 * ((t -= 2) * t * (((s *= (Back.SWING_MULTIPLICATOR)) + 1) * t + s) + 2) + b;
    }

    static inOut_s(t, b, c, d, s){
        if (s == null)
            return Back.inOut(t, b, c, d);

        if ((t /= d / 2) < 1) 
            return c / 2 * (t * t * (((s *= (Back.SWING_MULTIPLICATOR)) + 1) * t - s)) + b;

		return c / 2 * ((t -= 2) * t * (((s *= (Back.SWING_MULTIPLICATOR)) + 1) * t + s) + 2) + b;
    }
}