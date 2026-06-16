import streamlit as st
import librosa
import soundfile as sf
import tempfile

from filters import (
    lowpass_filter,
    highpass_filter,
    bandpass_filter
)

from noise_reduction import reduce_noise

from visualization import (
    plot_waveform,
    plot_spectrum
)

st.set_page_config(
    page_title="Audio Filtering & Noise Suppression",
    layout="wide"
)

st.title("🎵 Audio Filtering & Noise Suppression")

uploaded_file = st.file_uploader(
    "Upload Audio File",
    type=["wav", "mp3"]
)

if uploaded_file is not None:

    audio, sr = librosa.load(
        uploaded_file,
        sr=None
    )

    st.success("Audio Uploaded Successfully")

    st.audio(uploaded_file)

    st.write("Sample Rate:", sr)
    st.write("Duration:", round(len(audio) / sr, 2), "seconds")

    st.subheader("Original Audio")

    st.pyplot(
        plot_waveform(
            audio,
            "Original Waveform"
        )
    )

    st.pyplot(
        plot_spectrum(
            audio,
            sr
        )
    )

    option = st.selectbox(
        "Select Processing Method",
        [
            "Low Pass Filter",
            "High Pass Filter",
            "Band Pass Filter",
            "Noise Reduction"
        ]
    )

    processed_audio = audio

    if option == "Low Pass Filter":

        cutoff = st.slider(
            "Cutoff Frequency (Hz)",
            100,
            10000,
            3000
        )

        processed_audio = lowpass_filter(
            audio,
            cutoff,
            sr
        )

    elif option == "High Pass Filter":

        cutoff = st.slider(
            "Cutoff Frequency (Hz)",
            100,
            10000,
            1000
        )

        processed_audio = highpass_filter(
            audio,
            cutoff,
            sr
        )

    elif option == "Band Pass Filter":

        lowcut = st.slider(
            "Low Frequency",
            100,
            5000,
            500
        )

        highcut = st.slider(
            "High Frequency",
            1000,
            10000,
            4000
        )

        processed_audio = bandpass_filter(
            audio,
            lowcut,
            highcut,
            sr
        )

    elif option == "Noise Reduction":

        threshold = st.slider(
            "Noise Threshold",
            0.001,
            0.1,
            0.02
        )

        processed_audio = reduce_noise(
            audio,
            threshold
        )

    st.subheader("Processed Audio")

    st.pyplot(
        plot_waveform(
            processed_audio,
            "Processed Waveform"
        )
    )

    st.pyplot(
        plot_spectrum(
            processed_audio,
            sr
        )
    )

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    sf.write(
        temp_file.name,
        processed_audio,
        sr
    )

    st.audio(temp_file.name)

    with open(temp_file.name, "rb") as f:

        st.download_button(
            label="Download Processed Audio",
            data=f,
            file_name="processed_audio.wav",
            mime="audio/wav"
        )