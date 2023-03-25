class Exponentional {
    static evaluate(tweeningBehaviour, t, b, c, d){
        switch(tweeningBehaviour) {
            case ETweeningBehaviour.IN:
                return Exponentional.in(t,b,c,d);
            case ETweeningBehaviour.OUT:
                return Exponentional.out(t,b,c,d);
            case ETweeningBehaviour.IN_OUT:
                return Exponentional.inOut(t,b,c,d);
            default:
                return null;
        }
    }
    

    static in(t, b, c, d){
        return (t == 0) ? b : c * Math.pow(2, 10 * (t / d - 1)) + b;
    }


    static out(t, b, c, d){
        return (t == d) ? b + c : c * (-Math.pow(2, -10 * t / d) + 1) + b;	
    }

    
    static inOut(t, b, c, d){
        if (t == 0) 
            return b;

		if (t == d) 
            return b + c;
            
		if ((t /= d / 2) < 1) 
            return c / 2 * Math.pow(2, 10 * (t - 1)) + b;

		return c / 2 * (-Math.pow(2, -10 * --t) + 2) + b;
    }
}