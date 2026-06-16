import matplotlib.pyplot as plt
import numpy as np


def plot_waveform(audio, title="Waveform"):

    fig, ax = plt.subplots(figsize=(10, 3))

    ax.plot(audio)

    ax.set_title(title)
    ax.set_xlabel("Samples")
    ax.set_ylabel("Amplitude")

    return fig


def plot_spectrum(audio, sr):

    fig, ax = plt.subplots(figsize=(10, 3))

    spectrum = np.abs(np.fft.rfft(audio))
    freq = np.fft.rfftfreq(len(audio), 1 / sr)

    ax.plot(freq, spectrum)

    ax.set_title("Frequency Spectrum")
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Magnitude")

    return fig