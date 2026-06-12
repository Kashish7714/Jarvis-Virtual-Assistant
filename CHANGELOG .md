# Changelog

All notable changes to this project will be documented here.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.0.0] - 2025-06-12

### Added

- Wake word detection using SpeechRecognition and Google Speech API
- Voice command processing for opening Google, YouTube, Spotify, and LinkedIn
- Music playback via YouTube links using a local song dictionary (`music_library.py`)
- News headlines feature using NewsAPI (top Indian headlines, read aloud)
- AI fallback using OpenAI GPT-3.5-turbo for commands not explicitly handled
- Text-to-speech output using gTTS and pygame
- Fallback TTS engine using pyttsx3 (`speak_old`)
- Standalone OpenAI API test script (`client.py`)

### Fixed

- Corrected `gTTs` import to `gTTS` (capital S)
- Fixed indentation: `speak()` function's audio cleanup loop was running at module level instead of inside the function
- Fixed `if __name__ == "__main__":` block that was incorrectly nested inside `processcommand()`
- Fixed missing parentheses on `sr.Microphone` call
- Fixed wake word comparison: `word.lower() == "Jarvis"` now correctly compares to `"jarvis"`
- Increased `phrase_time_limit` from 1 to 5 seconds for reliable wake word capture
- Fixed syntax error in `client.py` caused by missing closing parenthesis on `OpenAI()` constructor
- Fixed `music_library.py` keys: removed leading spaces, normalized to lowercase, removed trailing comma inside last URL string
