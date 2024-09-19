import soundfile as sf
import numpy as np

# Generate a simple sine wave
rate = 22050
t = np.linspace(0, 1, rate)
x = 0.5 * np.sin(2 * np.pi * 440 * t)

# Write and read the file
sf.write('test.wav', x, rate)
data, samplerate = sf.read('test.wav')

print("Sound file written and read successfully.")
