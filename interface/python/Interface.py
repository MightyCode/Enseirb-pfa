class Interface:
    def __init__(self, stop_flag, verbose: bool = False) -> None:
        self._initialized = False
        self._verbose: bool = verbose

        self._referenceEffects: list = []
        self._length = 0
        
        self._stop_flag = stop_flag

    def initialized(self) -> bool:
        return self._initialized

    """
    Read project from a path
    """
    def read_project(self, path) -> None:
        print("readProject() : To override")
    
    """
    Load effect from a path, will be not called
    by external scripts, should be called locally when read_project.
    """
    def load_effect_from(self, path) -> None:
        print("loadCustomEffects() : To override")

    """
    (Should have done read_project before)
    Return the length of the scenarii in tick
    """
    def length(self) :
        return self.length

    """
    (Should be done before do_scenarii)
    Compute eventual things before doing scenarii
    """
    def pre_compute(self):
        print("preCompute() : To override")

    
    def compute_tick(self, tick) -> None:
        print("computeTick() : To override")

    """
    Run a scenarii using all needed hardware
    That function should be call using thread
    The user can also precise the tick start 
    """
    def do_scenarii(self, start_time: int=0):
        print("doScenarii() : To override")