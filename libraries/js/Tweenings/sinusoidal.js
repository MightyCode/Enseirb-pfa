class Sinusoidal {
    static evaluate(tweeningBehaviour, t, b, c, d){
        switch(tweeningBehaviour) {
            case ETweeningBehaviour.IN:
                return Sinusoidal.in(t,b,c,d);
            case ETweeningBehaviour.OUT:
                return Sinusoidal.out(t,b,c,d);
            case ETweeningBehaviour.IN_OUT:
                return Sinusoidal.inOut(t,b,c,d);
            default:
                return null;
        }
    }
    

    static in(t, b, c, d){
        return -c * Math.cos(t / d * (Math.PI / 2)) + c + b;
    }


    static out(t, b, c, d){
        return c * Math.sin(t / d * (Math.PI / 2)) + b;
    }

    static inOut(t, b, c, d){
        return -c / 2 * (Math.cos(Math.PI * t / d) - 1) + b;
    }
}