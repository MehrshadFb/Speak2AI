# Real-Time Audio-to-Text Application

## Description
This Python application performs real-time audio-to-text conversion, utilizing PyAudio for audio capture and WebSocket technology for efficient communication. It transcribes audio with AssemblyAI and employs OpenAI's GPT-3.5 model for generating intelligent responses. This project demonstrates expertise in AI technologies, real-time data streaming, and secure API integration.

## Features
- Real-time audio capturing.
- Audio transcription using AssemblyAI.
- Conversational AI responses using OpenAI's GPT-3.5.
- Secure API key management.

## Installation
```bash
pip install pyaudio websockets asyncio base64 json python-dotenv
```

## Usage
To run the application, execute:
```bash
python main.py
```
Ensure your API keys for AssemblyAI and OpenAI are set in your environment variables.

## Configuration
Set your API keys in the `.env` file:
```
API_KEY_ASSEMBLYAI=your_assemblyai_key_here
API_KEY_OPENAI=your_openai_key_here
```
