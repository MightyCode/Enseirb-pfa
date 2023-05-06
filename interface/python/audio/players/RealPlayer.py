import jack
import soundfile as sf
try:
    import queue  # Python 3.x
except ImportError:
    import Queue as queue  # Python 2.x
import sys
import os
import threading
from random import sample
from interface.python.audio.players.PlayerInterface import PlayerInterface

class RealPlayer(PlayerInterface):
    def __init__(self, client_name, stop_event) -> None:
        super().__init__(stop_event) # -> stop_event.is_set()
        self.buffersize = 20
        self.client = jack.Client(client_name)
        self.queues = []

    def callback(self, frames):
        side = 0
        for i in range(20):#len(self.client.outports)):
            if frames != self.client.blocksize:
                self.stop_callback('blocksize must not be changed, I quit!')
            data = self.queues[i%10].get_nowait()
            #self.client.outports[i].get_array()[:] = data.T[side] 
            print(data.T[side])
            side = (len(data.T) - 1) - side
    def stop_callback(self, msg=''):
        if msg:
            self.print_error(msg)
        for port in self.client.outports:
            port.get_array().fill(0)
        raise jack.CallbackExit
    
    def print_error(*args):
        print(*args, file=sys.stderr)

    def xrun(self, delay):
        self.print_error("An xrun occured, increase JACK's period size?")
    
    def shutdown(self, status, reason):
        self.print_error('JACK shutdown!')
        self.print_error('status:', status)
        self.print_error('reason:', reason)

    def play(self, audio_results: list, start_time: float, sample_rate: int):
        #To do
        start_tick: int = int(start_time * sample_rate)

        client = self.client

        blocksize = client.blocksize
        samplerate = client.samplerate
        buffersize = self.buffersize
        client.set_xrun_callback(self.xrun)
        client.set_shutdown_callback(self.shutdown)
        client.set_process_callback(self.callback)

        print(f'blocksize : {blocksize}, samplerate : {samplerate}')

        filenames = os.listdir('out')
        filenames.sort()

        block_generators = []

        for i in range(10):
            self.queues.append(queue.Queue(maxsize=buffersize))

        i=0
        for filename in filenames:
            f = sf.SoundFile('out/'+filename)
            f.seek(start_tick)
            block_generators.append(f.blocks(blocksize=blocksize, dtype='float32', always_2d=True, fill_value=0))
            for _, data in zip(range(buffersize), block_generators[-1]):
                self.queues[i].put_nowait(data)
            i+=1

        with client:
            """
            target_ports = client.get_ports(
                is_physical=True, is_input=True, is_audio=True)
            print(target_ports)
            for i in range(len(target_ports)):
                client.outports.register(f'out_{i+1}')
                client.outports[i].connect(target_ports[i])"""

            timeout = blocksize * buffersize / samplerate
            
            for d0,d1,d2,d3,d4,d5,d6,d7,d8,d9 in zip(block_generators[0],
                                                    block_generators[1],
                                                    block_generators[2],
                                                    block_generators[3],
                                                    block_generators[4],
                                                    block_generators[5],
                                                    block_generators[6],
                                                    block_generators[7],
                                                    block_generators[8],
                                                    block_generators[9],
                                                    ):
                self.queues[0].put(d0, timeout=timeout)
                self.queues[1].put(d1, timeout=timeout)    
                self.queues[2].put(d2, timeout=timeout)    
                self.queues[3].put(d3, timeout=timeout)    
                self.queues[4].put(d4, timeout=timeout)    
                self.queues[5].put(d5, timeout=timeout)    
                self.queues[6].put(d6, timeout=timeout)    
                self.queues[7].put(d7, timeout=timeout)    
                self.queues[8].put(d8, timeout=timeout)    
                self.queues[9].put(d9, timeout=timeout)