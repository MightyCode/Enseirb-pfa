class Elastic {
    static evaluate(tweeningBehaviour, t, b, c, d, arg1, arg2){
        switch(tweeningBehaviour) {
            case ETweeningBehaviour.IN:
                return Elastic.in_ap(t,b,c,d,arg1,arg2);
            case ETweeningBehaviour.OUT:
                return Elastic.out_ap(t,b,c,d,arg1,arg2);
            case ETweeningBehaviour.IN_OUT:
                return Elastic.inOut_ap(t,b,c,d,arg1,arg2);
            default:
                return null;
        }
    }
    

    static in(t, b, c, d){
        if (t == 0) 
            return b;  
        
        if ((t /= d) == 1) 
            return b + c;

		var p = d * 0.3;
		var a = c; 
		var s = p / 4;
		return -(a * Math.pow(2, 10 * (t -= 1)) * Math.sin((t * d - s) * (2 * Math.PI) / p)) + b;
    }


    static in_ap(t, b, c, d, a, p){
        if (a == null || p == null)
            return Elastic.in(t, b, c, d);

        var s;
        if (t == 0) 
            return b;  
            
        if ((t /= d) == 1) 
            return b + c;  

        if (a < Math.abs(c)) { 
            a = c; 
            s = p / 4; 
        } else {
            s = p / (2 * Math.PI) * Math.asin(c / a);
        }

        return -(a * Math.pow(2, 10 * (t -= 1)) * Math.sin((t * d - s) * (2 * Math.PI) / p)) + b;
    }


    static out(t, b, c, d){
        if (t == 0) 
            return b;  
        
        if ((t /= d) == 1) 
            return b + c;

		var p = d * 0.3;
		var a = c; 
		var s = p / 4;
		
        return (a * Math.pow(2, -10 * t) * Math.sin((t * d - s) * (2 * Math.PI) / p) + c + b);
    }

    static out_ap(t, b, c, d, a, p){
        if (a == null || p == null)
            return Elastic.out(t, b, c, d);

        var s;
		if (t == 0) 
            return b;  
            
        if ((t /= d) == 1) 
            return b + c;

		if (a < Math.abs(c)) { 
            a = c;  
            s = p / 4;
        } else { 
            s = p / (2 * Math.PI) * Math.asin(c / a);
        }
		
        return (a * Math.pow(2, -10 * t) * Math.sin((t * d - s) * (2 * Math.PI) / p) + c + b);	
    }

    
    static inOut(t, b, c, d){
        if (t == 0) 
            return b;  
            
        if ((t /= d / 2) == 2) 
            return b + c; 
		
        var p = d * (0.3 * 1.5);
		var a = c; 
		var s = p / 4;

		if (t < 1) return -0.5 * (a * Math.pow(2, 10 * (t -= 1)) * Math.sin((t * d - s) * (2 * Math.PI) / p)) + b;

		return a * Math.pow(2, -10 * (t -= 1)) * Math.sin((t * d - s) * (2 * Math.PI) / p) * 0.5 + c + b;
    }


    static inOut_ap(t, b, c, d, a, p){
        if (a == null || p == null)
            return Elastic.inOut(t, b, c, d);

        var s;
		if (t == 0) 
            return b;  
        
        if ((t /= d / 2) == 2) 
            return b+c;
              
		if (a < Math.abs(c)) { 
            a = c; 
            s = p / 4; 
        } else { 
            s = p / (2 * Math.PI) * Math.asin(c / a);
        }

		if (t < 1) 
            return -0.5 * (a * Math.pow(2, 10 * (t -= 1)) * Math.sin((t * d - s) * (2 * Math.PI) / p)) + b;

		return a*Math.pow(2, -10 * (t -= 1)) * Math.sin((t * d - s) * (2 * Math.PI) / p) * 0.5 + c + b;
    }
}