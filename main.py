import scipy
from pydub import AudioSegment

"""
Main python file for 8bit music conversion
"""

_700kb = "file_example_MP3_700KB.mp3"

sound_file = AudioSegment.from_file(_700kb, "mp3")

print(type(sound_file))