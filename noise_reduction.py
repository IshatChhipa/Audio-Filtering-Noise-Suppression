import numpy as np


def reduce_noise(audio, threshold=0.02):

    cleaned_audio = np.copy(audio)

    cleaned_audio[
        np.abs(cleaned_audio) < threshold
    ] = 0

    return cleaned_audio