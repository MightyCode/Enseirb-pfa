from pydub import AudioSegment
import numpy as np

# Load the sound file as a Pydub AudioSegment object
sound: AudioSegment = AudioSegment.from_file("interface/python/audio/sound/retro.wav")
sound.get_frame

# Create a time array for the sinusoidal wave
duration = sound.duration_seconds
t = np.linspace(0, duration, len(sound.get_array_of_samples()))

# Compute the sinusoidal wave with a frequency of 1 Hz
modulation = np.sin(2 * np.pi * 1 * t)

# Scale the modulation to the range [0, 1] and convert to dB
modulation = 20 * np.log10(0.5 * modulation + 0.5)

# Apply the modulation to the left and right channels of the sound
left_channel, right_channel = sound.split_to_mono()
left_channel = left_channel.apply_gain_typed(modulation, 2)
right_channel = right_channel.apply_gain_typed(modulation, 2)

# Mix the channels back into a stereo sound
stereo_sound = AudioSegment.from_mono_audiosegments(left_channel, right_channel)

# Export the modulated sound to a file
stereo_sound.export("output_sound.wav", format="wav")