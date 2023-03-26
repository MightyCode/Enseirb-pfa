from interface.python.Tweenings.ETweeningType import ETweeningType as ETT
from interface.python.Tweenings.back import Back
from interface.python.Tweenings.bounce import Bounce
from interface.python.Tweenings.linear import Linear
from interface.python.Tweenings.quartic import Quartic
from interface.python.Tweenings.quintinc import Quintic
from interface.python.Tweenings.sinusoidal import Sinusoidal
from interface.python.Tweenings.exponentional import Exponentional
from interface.python.Tweenings.elastic import Elastic
from interface.python.Tweenings.circular import Circular
from interface.python.Tweenings.cubic import Cubic
from interface.python.Tweenings.quadratic import Quadratic

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
        
