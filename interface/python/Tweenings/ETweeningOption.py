class ETweeningOption :
    DIRECT, DIRECT_MIRRORED, DIRECT_REVERSED, LOOP, LOOP_MIRRORRED, LOOP_REVERSED = range(6)

    def from_str(type: str) -> int:
        if type.upper() == "DIRECT":
            return ETweeningOption.DIRECT
        elif type.upper() == "DIRECT_MIRRORED":
            return ETweeningOption.DIRECT_MIRRORED
        elif type.upper() == "DIRECT_REVERSED":
            return ETweeningOption.DIRECT_REVERSED
        elif type.upper() == "LOOP":
            return ETweeningOption.LOOP
        elif type.upper() == "LOOP_MIRRORRED":
            return ETweeningOption.LOOP_MIRRORRED
        elif type.upper() == "LOOP_REVERSED":
            return ETweeningOption.LOOP_REVERSED
        
        return -1 