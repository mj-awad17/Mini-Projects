import streamlit as st
from gtts import gTTS
from io import BytesIO
import time

# Set page configuration (tab name)
st.set_page_config(page_title="Text to Speech", page_icon="🎙️")

# Dictionary to map language codes to full names
LANGUAGES = {
    "ar": "Arabic", "bn": "Bengali", "zh": "Chinese", "nl": "Dutch",
    "en": "English", "fr": "French", "de": "German",
    "el": "Greek", "he": "Hebrew", "hi": "Hindi", "it": "Italian",
    "ja": "Japanese", "ko": "Korean", "ms": "Malay", "no": "Norwegian",
    "pl": "Polish", "pt": "Portuguese", "ru": "Russian", "es": "Spanish",
    "sv": "Swedish", "th": "Thai", "tr": "Turkish", "ur": "Urdu",
    "vi": "Vietnamese",
}

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp

# Custom CSS for adaptive background and text styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #6a11cb, #2575fc);
        color: white;
    }
    .stTextInput > div > div > input,
    .stTextArea textarea,
    .stSelectbox > div > div > select {
        background: #ffffff;
        color: #000000;
        border: 1px solid #cccccc;
        border-radius: 5px;
        padding: 8px;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea textarea:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #2575fc;
    }
    .stButton>button {
        background-color: #2575fc;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #6a11cb;
    }
    .stMarkdown {
        color: white;
    }
    .stAudio {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App layout
st.title("🎙️ Text-to-Speech App")

# Instructions in the sidebar
st.sidebar.header("📝 Instructions")
st.sidebar.markdown(
    """
    1. Choose a language from the dropdown menu.
    2. Enter the text you want to convert in the text box.
    3. Click 'Convert to Speech' to generate audio.
    4. Use the 'Download' button to save the audio file.
    """
)

# Main content
st.markdown("### 🌍 Choose Your Language")
lang_code = st.selectbox(
    "Select language",
    options=list(LANGUAGES.keys()),
    format_func=lambda x: f"{LANGUAGES[x]} ({x})"
)

st.markdown("### ✍️ Enter Your Text")
user_text = st.text_area("Type or paste your text here:", "Hello, world!")

# Convert text to speech and provide download button
if st.button("🔊 Convert to Speech"):
    if user_text:
        with st.spinner("🎵 Generating audio..."):
            time.sleep(2)  # 2-second loading simulation
            audio_file = text_to_speech(user_text, lang_code)
            st.audio(audio_file, format='audio/mp3')
        
            # Make the audio file downloadable
            st.download_button(
                label="📥 Download Audio",
                data=audio_file,
                file_name="output.mp3",
                mime="audio/mp3"
            )
            st.balloons()
    else:
        st.error("⚠️ Please enter some text!")

st.markdown("---")
st.markdown("Developed by Muhammad Jawad")
