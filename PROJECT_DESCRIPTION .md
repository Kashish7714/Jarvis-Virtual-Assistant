# Project Description — For Resume / LinkedIn / Portfolio

---

## One-line summary (GitHub About section)

> Python voice assistant with wake word detection, OpenAI integration, and news/music/browser control.

---

## Resume — Projects Section

**Jarvis Voice Assistant** | Python, OpenAI API, SpeechRecognition, gTTS, NewsAPI
- Built a wake-word-activated voice assistant in Python that listens for "Jarvis" and processes spoken commands
- Integrated OpenAI GPT-3.5-turbo as a fallback to handle open-ended voice queries not covered by explicit rules
- Used Google Speech Recognition for audio input and gTTS + pygame for text-to-speech output
- Implemented voice-controlled web navigation, YouTube music playback, and live news reading via NewsAPI
- Structured command handling logic with clear separation between explicit rules and AI-powered fallback

---

## LinkedIn Project Description

Jarvis is a Python voice assistant I built to get hands-on with speech recognition, API integration, and real-time audio I/O in Python.

It works by continuously listening for the wake word "Jarvis". Once activated, it processes the spoken command — opening websites, playing music via YouTube, reading Indian news headlines aloud, or passing the query to GPT-3.5-turbo for a spoken response.

Tech used: Python, SpeechRecognition, gTTS, pygame, OpenAI API, NewsAPI, webbrowser.

GitHub: [link]

---

## Portfolio Website Description

**Jarvis Voice Assistant**

A voice-activated assistant built in Python that responds to a wake word and handles a range of spoken commands — from opening websites and playing music to reading live news and answering questions through OpenAI's GPT-3.5-turbo.

The project involved working with audio input/output pipelines, third-party REST APIs, and designing a clean command-processing flow that separates hard-coded rules from AI-powered responses.

---

## GitHub Repository Optimization

**Recommended repo name:** `jarvis-voice-assistant`

**Recommended description:**
> Wake word activated Python voice assistant with OpenAI, NewsAPI, and speech recognition.

**Recommended topics/tags:**
```
python, voice-assistant, speech-recognition, openai, text-to-speech, gtts,
newsapi, pygame, automation, nlp, beginner-project
```

**Visibility:** Public (good for portfolio and recruiter visibility)

**Do NOT upload:**
- `.env` (contains real API keys)
- `temp.mp3` (auto-generated at runtime, already in `.gitignore`)
- `__pycache__/` (already in `.gitignore`)
- `venv/` (already in `.gitignore`)
