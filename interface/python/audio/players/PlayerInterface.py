class PlayerInterface:
    def __init__(self, stop_event) -> None:
        self._stop_event = stop_event   

    def play(self, audio_results: list, start_time: float, sample_rate: int):
        print("play : to override")