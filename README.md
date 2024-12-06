# Chat with Kevin

This is a Streamlit-based application that enables users to interact with Kevin, an AI chatbot powered by the Ollama language model-llama3.2. Users can speak to Kevin through audio input, and the app transcribes the audio, processes the query, and provides a text and audio response.

---

## Features
- **Audio Input**: Speak to Kevin using the built-in audio recorder.
- **Speech-to-Text**: Transcribes user audio input into text using Google Speech Recognition.
- **AI Responses**: Generates conversational responses via the Ollama language model.
- **Audio Response**: Converts AI responses into speech and plays them back to the user.
- **Conversation History**: Maintains a history of the conversation in the sidebar.

---

## Requirements
### Prerequisites
Ensure you have the following installed on your system:
- Streamlit
- `audio_recorder_streamlit` library
- `langchain_community`
- `speech_recognition`
- `pyttsx3`
- `base64`
- Ollama (with `Kevin` model loaded locally and accessible at `http://localhost:11434`)

---

## Installation
-Download Ollama, make Kevin using the ModelFile
1. Clone the repository:
   ```bash
   git clone https://github.com/AbinJohn1632/Kevin_Chatbot_llama3.2.git
   cd Kevin_Chatbot_llama3.2
   ```

2. Install the required Python packages:

3. Making Kevin:
   ```bash
   ollama create Kevin -f ModelFile
   ollama run Kevin #running Kevin in cmd
   ```

---

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser (default: `http://localhost:8501`).

3. Interact with Kevin:
   - Press the **Record** button and speak.
   - Kevin will transcribe your input, generate a response, and play it back to you.

---

## File Structure
- `app.py`: Main application file containing the logic for audio recording, transcription, AI responses, and history management.
- `ModelFile`: file with Kevin description for the Ollama create from method.

---

## How It Works
1. **Audio Recording**: The app uses `audio_recorder_streamlit` to record user audio.
2. **Transcription**: `speech_recognition` converts the recorded audio into text.
3. **AI Response**: The transcribed text is sent to the Ollama API for a response.
4. **Text-to-Speech**: `pyttsx3` converts the response text into an audio file.
5. **Playback**: The audio response is automatically played back to the user.
6. **History**: Stores the conversation for review in the sidebar.

---

## Future Enhancements
- Add support for multiple languages in transcription and responses.
- Enhance the audio processing pipeline for better noise handling.
- Provide options to save the conversation history.

---

## Acknowledgments
- [Streamlit](https://streamlit.io) for building a powerful and easy-to-use web app framework.
- [Ollama](https://ollama.ai) for providing the llama3.2 language model.
- [Google Speech Recognition](https://cloud.google.com/speech-to-text) for accurate transcription. 
