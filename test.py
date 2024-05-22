from pydub import AudioSegment
from pydub.utils import make_chunks
import numpy as np
import scipy.fftpack

def calculate_rms(chunk):
    samples = np.array(chunk.get_array_of_samples())
    return np.sqrt(np.mean(samples**2))

def calculate_zero_crossing_rate(chunk):
    samples = np.array(chunk.get_array_of_samples())
    zero_crossings = np.where(np.diff(np.sign(samples)))[0]
    return len(zero_crossings) / len(samples)

def calculate_spectral_centroid(chunk):
    samples = np.array(chunk.get_array_of_samples())
    magnitude_spectrum = np.abs(scipy.fftpack.fft(samples))
    length = len(samples)
    freqs = np.fft.fftfreq(length)
    centroid = np.sum(freqs * magnitude_spectrum) / np.sum(magnitude_spectrum)
    return centroid

def get_chunk_features(mp3_file):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_file)
    
    # Split the audio into chunks of 0.5 seconds (500 milliseconds)
    chunk_length_ms = 500  # 0.5 seconds
    chunks = make_chunks(audio, chunk_length_ms)
    
    # Iterate over each chunk and calculate various features
    for i, chunk in enumerate(chunks):
        amplitude = chunk.max
        rms = calculate_rms(chunk)
        zero_crossing_rate = calculate_zero_crossing_rate(chunk)
        spectral_centroid = calculate_spectral_centroid(chunk)
        dbfs = chunk.dBFS

        print(f"Chunk {i} (Time: {i * 0.5} - {(i + 1) * 0.5} seconds):")
        print(f"  Amplitude (Max): {amplitude}")
        print(f"  RMS: {rms:.2f}")
        print(f"  Zero Crossing Rate: {zero_crossing_rate:.2f}")
        print(f"  Spectral Centroid: {spectral_centroid:.2f}")
        print(f"  Amplitude (dBFS): {dbfs:.2f} dBFS")

# Example usage
mp3_file = "01-PRE_01.mp3"  # Replace with your MP3 file path
get_chunk_features(mp3_file)
