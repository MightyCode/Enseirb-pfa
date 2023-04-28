class Interface:
    def __init__(self) -> None:
        self._initialize = False

        self.referenceEffects: list = []
        self.length = 0

    def isInitialized(self) -> bool:
        return self._initialize

    def readProject(self, path) -> None:
        print("readProject() : To override")

    def loadCustomEffects(self, path) -> None:
        print("loadCustomEffects() : To override")

    """
        (Should have done readProject before)
        Return the length of the scenarii in tick
    """
    def length(self) :
        return self.length

    def computeTick(self, tick) -> None:
        print("computeTick() : To override")

    """
        (Should do before )
        Compute eventual things before doing scenarii
    """
    def preCompute(self):
        print("preCompute() : To override")

    """
        Run a scenarii using all needed hardware
        
        That function should be call using thread
    """
    def doScenarii(self):
        print("doScenarii() : To override")