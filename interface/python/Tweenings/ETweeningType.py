class ETweeningType:
    LINEAR, \
    QUADRATIC, \
    CUBIC, \
    QUARTIC, \
    QUINTIC, \
    SINUSOIDAL, \
    EXPONENTIAL, \
    CIRCULAR, \
    ELASTIC, \
    BACK, \
    BOUNCE = range(11)

    def from_str(type: str) -> int:
        if type.upper() == "LINEAR":
            return ETweeningType.LINEAR
        elif type.upper() == "QUADRATIC":
            return ETweeningType.QUADRATIC
        elif type.upper() == "CUBIC":
            return ETweeningType.CUBIC
        elif type.upper() == "QUARTIC":
            return ETweeningType.QUARTIC
        elif type.upper() == "QUINTIC":
            return ETweeningType.QUINTIC
        elif type.upper() == "SINUSOIDAL":
            return ETweeningType.SINUSOIDAL
        elif type.upper() == "EXPONENTIAL":
            return ETweeningType.EXPONENTIAL
        elif type.upper() == "CIRCULAR":
            return ETweeningType.CIRCULAR
        elif type.upper() == "ELASTIC":
            return ETweeningType.ELASTIC
        elif type.upper() == "BACK":
            return ETweeningType.BACK
        elif type.upper() == "BOUNCE":
            return ETweeningType.BOUNCE
        
        return -1