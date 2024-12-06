import streamlit as st
from audio_recorder_streamlit import audio_recorder
import base64
from langchain_community.llms import Ollama
import speech_recognition as sr
import pyttsx3
import os

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError:
        return "API request error."

def autoplay(response_audio):
    with open(response_audio, "rb") as response:
        res = response.read()
    response64 = base64.b64encode(res).decode("utf-8")
    audio_html = f'<audio src="data:audio/mp3;base64,{response64}" controls autoplay></audio>'
    st.markdown(audio_html, unsafe_allow_html=True)

# Initialize Ollama 
ollama = Ollama(base_url="http://localhost:11434", model="Kevin")

if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar for history
st.sidebar.title("History")
for entry in st.session_state.history:
    st.sidebar.markdown(f"**User:** {entry['user']}")
    st.sidebar.markdown(f"**Kevin:** {entry['kevin']}")

st.title("Chat with Kevin")

# Record audio
st.write("Press the record button and speak.")
audio = audio_recorder()

if audio:
    sound_file = "temp.mp3"
    with open(sound_file, "wb") as f:
        f.write(audio)

    user_input = transcribe_audio(sound_file)
    st.write("User: " + user_input)

    if user_input and user_input != "Could not understand the audio.":
        response = ollama(user_input)
        kevin_response = response["text"] if isinstance(response, dict) else response
        st.write("Kevin: " + kevin_response)

        # Save to history
        st.session_state.history.append({"user": user_input, "kevin": kevin_response})

        # Generate response audio
        response_audio = "response.mp3"
        engine = pyttsx3.init()
        engine.save_to_file(kevin_response, response_audio)
        engine.runAndWait()

        autoplay(response_audio)

    if os.path.exists(sound_file):
        os.remove(sound_file)
    if os.path.exists(response_audio):
        os.remove(response_audio)
