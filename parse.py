from pydub import AudioSegment
from pydub.utils import make_chunks
import glob, os

current_directory = os.getcwd()
f = open("amplitudes.txt", "w")

items = glob.glob("*.mp3")
sorted_items = sorted(items)

for filename in sorted_items:
    f.write(f"{filename}, ")
    sound = AudioSegment.from_file(filename, format="mp3")
    chunks = make_chunks(sound, 200)
    peak_amplitude = sound.max
    array_string = "["

    highest_amplitude = 0

	#first get lowest amplitude
    for i, chunk in enumerate(chunks):
        amplitude = chunk.max
        if amplitude > highest_amplitude:
            highest_amplitude = amplitude

    # print(f"max:{highest_amplitude} min:{lowest_amplitude}")

    for i, chunk in enumerate(chunks):
        amplitude = chunk.max
        array_string += f"{(amplitude/highest_amplitude*100):0.0f},"
        
    array_string = array_string.rstrip(array_string[-1])
    array_string += "]\n"
    f.write(array_string)

f.close()
