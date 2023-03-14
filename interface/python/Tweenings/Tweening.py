from ETweeningType import ETweeningType as ETT
from back import Back
from bounce import Bounce
from linear import Linear
from quartic import Quartic
from quintinc import Quintic
from sinusoidal import Sinusoidal
from exponentional import Exponentional
from elastic import Elastic
from circular import Circular
from cubic import Cubic
from quadratic import Quadratic

class Tweening :
    # 
    # t: current advancement, b: beginning value, c: change in value, d: total advancement
    def evaluate(tweeningType, tweeningBehaviour, t, b, c, d, arg1, arg2):
        if tweeningType == ETT.LINEAR:
            return Linear.evaluate(tweeningBehaviour, t, b, c, d)
        elif tweeningType == ETT.QUADRATIC:
            return Quadratic.evaluate(tweeningBehaviour, t, b, c, d)
        elif tweeningType == ETT.QUARTIC:
            return Quartic.evaluate(tweeningBehaviour, t, b, c, d)
        elif tweeningType == ETT.QUINTIC:
            return Quintic.evaluate(tweeningBehaviour, t, b, c, d)
        elif tweeningType == ETT.SINUSOIDAL:
            return Sinusoidal.evaluate(tweeningBehaviour, t, b, c, d)
        elif tweeningType == ETT.EXPONENTIAL:
            return Exponentional.evaluate(tweeningBehaviour, t, b, c, d)
        elif tweeningType == ETT.CIRCULAR:
            return Circular.evaluate(tweeningBehaviour, t, b, c, d)
        elif tweeningType == ETT.ELASTIC:
            return Elastic.evaluate(tweeningBehaviour, t, b, c, d, arg1, arg2)
        elif tweeningType == ETT.BACK:
            return Back.evaluate(tweeningBehaviour, t, b, c, d, arg1)
        elif tweeningType == ETT.CUBIC:
            return Cubic.evaluate(tweeningBehaviour, t, b, c, d)
        elif tweeningType == ETT.BOUNCE:
            return Bounce.evaluate(tweeningBehaviour, t, b, c, d)

        return None
        
