const ETweeningOption = {
    DIRECT : 0,
    DIRECT_MIRRORED : 1,
    DIRECT_REVERSE : 2,
    LOOP: 3,
    LOOP_REVERSED: 4,
    LOOP_MIRRORED : 5,
}

class Tweening {
    static evaluate(tweeningType, tweeningBehaviour, t, b, c, d, arg1, arg2){
        switch(tweeningType){
            case ETweeningType.LINEAR:
                return Linear.evaluate(tweeningBehaviour, t, b, c, d);
            case ETweeningType.QUADRATIC:
                return Quadratic.evaluate(tweeningBehaviour, t, b, c, d);
            case ETweeningType.CUBIC:
                return Cubic.evaluate(tweeningBehaviour, t, b, c, d);
            case ETweeningType.QUARTIC:
                return Quartic.evaluate(tweeningBehaviour, t, b, c, d);
            case ETweeningType.QUINTIC:
                return Quintic.evaluate(tweeningBehaviour, t, b, c, d);
            case ETweeningType.SINUSOIDAL:
                return Sinusoidal.evaluate(tweeningBehaviour, t, b, c, d);
            case ETweeningType.EXPONENTIAL:
                return Exponentional.evaluate(tweeningBehaviour, t, b, c, d);
            case ETweeningType.CIRCULAR:
                return Circular.evaluate(tweeningBehaviour, t, b, c, d);
            case ETweeningType.ELASTIC:
                return Elastic.evaluate(tweeningBehaviour, t, b, c, d, arg1, arg2);
            case ETweeningType.BACK:
                return Back.evaluate(tweeningBehaviour, t, b, c, d, arg1);
            case ETweeningType.BOUNCE:
                return Bounce.evaluate(tweeningBehaviour, t, b, c, d);
            default:
                return null;
        }
    }

    constructor(){
        this._tweeningType = null;
        this._tweeningConst = null;
        this._tweeningOption = ETweeningOption.DIRECT;

        this._timer = new Timer();
        this._beginningValue = 0;
        this._endValue = 0;
        this._rangeValue = 0;

        this._value = 0;

        this._onLoopByReverse = false;
        this._mirrored = false;

        this._addArg1 = null;
        this._addArg2 = null;
    }

    // t: currentTimer, b: beginning value, c: change in value, d: duration

    update(){
        this._timer.update();

        if (this._timer.finished){
            if (this._tweeningOption == ETweeningOption.DIRECT_MIRRORED) {
                if (!this._mirrored){
                    this._mirrored = true;
                    this._timer.resetStart();
                }
            } else if (this._tweeningOption == ETweeningOption.DIRECT_REVERSE) {
                if (!this._onLoopByReverse){
                    this._onLoopByReverse = true;
                    this._timer.resetStart();
                }
            } else if (this._tweeningOption == ETweeningOption.LOOP){
                var plus = this._timer.elapsedTime - this._timer.aimedTime;
                this._timer.resetStart();
                this._timer.forceTime(plus);
            } else if (this._tweeningOption == ETweeningOption.LOOP_REVERSED){
                var plus = this._timer.elapsedTime - this._timer.aimedTime;
                this._onLoopByReverse = !this._onLoopByReverse;
                this._timer.resetStart();
            } else if(this._tweeningOption == ETweeningOption.LOOP_MIRRORED) {
                var plus = this._timer.elapsedTime - this._timer.aimedTime;
                this._mirrored = !this._mirrored;
                this._timer.resetStart();
            }
        }

        var tmpTimeValue = this._timer.elapsedTime;
        var beginValue = this._beginningValue;
        var rangeValue = this._rangeValue;

        if (rangeValue == 0){
            return beginValue;
        }

        if (this._onLoopByReverse){
            tmpTimeValue = this._timer.aimedTime - tmpTimeValue;
        }

        if (this._mirrored){
            var beginValue = this._endValue;
            var rangeValue = -this._rangeValue;
        }

        
        this._value = Tweening.evaluate(this._tweeningType, this._tweeningConst, 
            tmpTimeValue, beginValue, rangeValue, this._timer.aimedTime, this._addArg1, this._addArg2);
    }


    setTweeningOption(tweeningOption){
        this._tweeningOption = tweeningOption;

        this._timer.setElapsedTimeCapped((
                    tweeningOption == ETweeningOption.LOOP 
                 || tweeningOption == ETweeningOption.LOOP_REVERSED 
                 || tweeningOption == ETweeningOption.LOOP_MIRRORED));

        return this;
    }


    setTweeningValues(tweeningType, tweeningConst){
        this._tweeningType = tweeningType;
        this._tweeningConst = tweeningConst;

        return this;
    }


    initTwoValue(time, beginningValue, endValue){
        return this.initRangeValue(time, beginningValue, endValue - beginningValue);
    }


    initRangeValue(time, beginningValue, range){
        this._timer.start(time);
        this._beginningValue = beginningValue;
        this._rangeValue = range;

        this._endValue = range + beginningValue;

        this._value = this._beginningValue;

        return this;
    }


    setAdditionnalArguments(arg1, arg2){
        this._addArg1 = arg1;
        this._addArg2 = arg2;
    }


    initRandomTweening(){
        this._timer.forceRandomTime();

        if (this._tweeningOption == ETweeningOption.DIRECT_MIRRORED || this._tweeningOption == ETweeningOption.LOOP_MIRRORED){
            if (Math.random() >= 0.5){
                this._mirrored = true;
            }
        } else if (this._tweeningOption == ETweeningOption.DIRECT_REVERSE || this._tweeningOption == ETweeningOption.LOOP_REVERSED){
            if (Math.random() >= 0.5){
                this._onLoopByReverse = true;
            }
        }

        return this;
    }

    get value (){
        return this._value;
    }

    // Not is in infinityLoop
    get finished(){
        if (this._tweeningOption == ETweeningOption.DIRECT){
            return this._timer.finished;
        } else if (this._tweeningOption == ETweeningOption.DIRECT_REVERSE){
            return this._timer.finished && this._onLoopByReverse;
        }  else if (this._tweeningOption == ETweeningOption.DIRECT_MIRRORED){
            return this._timer.finished && this._mirrored;
        }
        return false;
    }

        
    get addArg1(){
        return this._addArg1;
    }

    get addArg2(){
        return this._addArg2;
    }
}