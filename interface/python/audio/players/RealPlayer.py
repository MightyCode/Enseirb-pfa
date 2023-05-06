from random import sample
from interface.python.audio.players.PlayerInterface import PlayerInterface

class RealPlayer(PlayerInterface):
    def __init__(self, stop_event) -> None:
        super().__init__(stop_event) # -> stop_event.is_set()

    def play(self, audio_results: list, start_time: float, sample_rate: int):
        #To do
        start_tick: int = int(start_time * sample_rate)

        pass