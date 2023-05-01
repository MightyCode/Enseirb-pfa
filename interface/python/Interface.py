class Interface:
    def __init__(self) -> None:
        self._initialized = False

        self.referenceEffects: list = []
        self.length = 0

    def initialized(self) -> bool:
        return self._initialized

    def read_project(self, path) -> None:
        print("readProject() : To override")

    def load_effect_from(self, path) -> None:
        print("loadCustomEffects() : To override")

    """
        (Should have done readProject before)
        Return the length of the scenarii in tick
    """
    def length(self) :
        return self.length

    """
        (Should do before do_scenarii)
        Compute eventual things before doing scenarii
    """
    def pre_compute(self):
        print("preCompute() : To override")

    
    def compute_tick(self, tick) -> None:
        print("computeTick() : To override")

    """
        Run a scenarii using all needed hardware
        
        That function should be call using thread
    """
    def do_scenarii(self):
        print("doScenarii() : To override")