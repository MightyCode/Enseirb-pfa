class ETweeningBehaviour:
    IN, OUT, IN_OUT = range(3)

    def from_str(type: str) -> int:
        if type.upper() == "IN":
            return ETweeningBehaviour.IN
        elif type.upper() == "OUT":
            return ETweeningBehaviour.OUT
        elif type.upper() == "IN_OUT":
            return ETweeningBehaviour.IN_OUT
        
        return -1 