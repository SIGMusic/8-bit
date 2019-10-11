import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
import librosa
import IPython.display as display

"""
Main python file for 8bit music conversion
"""

# Load in sample MP3 file
audio, sampling_rate = librosa.core.load("file_example_MP3_1MG.mp3")

# Display audio file
# print("Example Audio:")
# display.display(display.Audio(audio, rate = sampling_rate))

plt.plot(audio)
plt.xlabel("Time in Samples")
plt.ylabel("Amplitude")
plt.savefig("Time in Samples")

# Plot waveform spectrogram
freqs, times, spectrogram = signal.spectrogram(audio, sampling_rate)
# We will have to take the log of the absolute value of the spectrogram in order to look at magnitude.
#  Taking the absolute value removes information about phase, which isn't too important to us right now.
#  Taking the log just adds contrast to our image. We wouldn't see any colors if we didn't do that.
#  We also add 1e-10 so that we don't happen to take the log of 0.
plt.pcolormesh(times, freqs, np.log(np.abs(spectrogram) + 1e-10))
plt.colorbar()
plt.xlabel("Time in Seconds")
plt.ylabel("Frequency in Hertz")
plt.savefig("Time in Seconds")