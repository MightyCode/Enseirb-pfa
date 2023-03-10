class Linear {
    static evaluate(tweeningBehaviour, t, b, c, d){
        switch(tweeningBehaviour) {
            case ETweeningBehaviour.IN:
                return Linear.in(t,b,c,d);
            case ETweeningBehaviour.OUT:
                return Linear.out(t,b,c,d);
            case ETweeningBehaviour.IN_OUT:
                return Linear.inOut(t,b,c,d);
            default:
                return null;
        }
    }
    

    static in(t, b, c, d){
        return c * t / d + b;
    }


    static out(t, b, c, d){
        return Linear.in(t, b, c, d);
    }

    static inOut(t, b, c, d){
        return Linear.in(t, b, c, d);
    }
}