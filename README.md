# Jarvis Voice Assistant

A Python-based voice assistant that responds to a wake word and handles commands including web navigation, music playback, news reading, and general queries via OpenAI.

---

## Overview

Jarvis listens continuously for the wake word "Jarvis". Once triggered, it captures a voice command, processes it, and responds — either by opening a website, playing a song, reading news headlines, or falling back to GPT-3.5-turbo for anything it does not explicitly handle.

The project uses Google Speech Recognition for input, gTTS + pygame for audio output, and the OpenAI API as a general-purpose fallback brain.

---

## Features

- Wake word detection ("Jarvis") via microphone
- Opens websites on voice command: Google, YouTube, Spotify, LinkedIn
- Plays songs from a local music library by opening YouTube links
- Reads top Indian news headlines using the NewsAPI
- Handles unrecognized commands through OpenAI GPT-3.5-turbo
- Text-to-speech output using Google TTS and pygame for playback

---

## Tech Stack

| Component        | Library / Service              |
|------------------|-------------------------------|
| Speech input     | SpeechRecognition, PyAudio    |
| Text-to-speech   | gTTS, pygame                  |
| AI responses     | OpenAI API (gpt-3.5-turbo)    |
| News headlines   | NewsAPI                       |
| Browser control  | webbrowser (stdlib)           |
| Audio playback   | pygame                        |

---

## Project Structure

```
jarvis-voice-assistant/
├── main.py            # Core assistant logic, wake word loop, command handler
├── music_library.py   # Dictionary mapping song names to YouTube URLs
├── client.py          # Standalone test script for the OpenAI API
├── requirements.txt   # Python dependencies
├── .env.example       # Template for environment variables
├── .gitignore
└── README.md
```

---

## Requirements

- Python 3.8 or higher
- A working microphone
- Internet connection (required for speech recognition, gTTS, OpenAI, and NewsAPI)

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. On Linux, you may also need:

```bash
sudo apt-get install python3-pyaudio portaudio19-dev
```

---

## Environment Setup

Copy the example file and fill in your API keys:

```bash
cp .env.example .env
```

Open `.env` and set the following:

```
OPENAI_API_KEY=your_openai_api_key_here
NEWS_API_KEY=your_newsapi_key_here
```

- OpenAI API key: https://platform.openai.com/api-keys
- NewsAPI key: https://newsapi.org/register

---

## Usage

Run the assistant:

```bash
python main.py
```

The assistant will initialize and start listening. Say **"Jarvis"** to activate it, then give a command.

**Supported voice commands:**

| Say this              | What happens                              |
|-----------------------|-------------------------------------------|
| Jarvis                | Activates the assistant                   |
| open google           | Opens google.com in the browser           |
| open youtube          | Opens youtube.com in the browser          |
| open spotify          | Opens spotify.com in the browser          |
| open linkedin         | Opens linkedin.com in the browser         |
| play borderline       | Opens the song's YouTube link             |
| play reflections      | Opens the song's YouTube link             |
| play timeless         | Opens the song's YouTube link             |
| news                  | Reads top Indian headlines aloud          |
| anything else         | Sent to OpenAI and answered via voice     |

---

## Adding Songs

Open `music_library.py` and add entries to the dictionary. Keys must be lowercase and match what you will say:

```python
music = {
    "song name": "https://youtube.com/...",
}
```

---

## Configuration

All API keys should be stored in a `.env` file and loaded at runtime using `python-dotenv`. Never commit real keys to version control.

---

## Screenshots

> Add screenshots or a screen recording of the assistant running here.

---

## Known Limitations

- Music playback relies on YouTube links opening in a browser, not in-app audio streaming.
- Speech recognition requires an active internet connection (Google Speech API).
- The music library is a static dictionary and must be updated manually.
- `pyttsx3` is imported as a fallback TTS engine but is not used in the main speech flow.

---

## Future Improvements

- Load API keys from a `.env` file using `python-dotenv`
- Add support for setting reminders or timers
- Expand the music library or integrate with Spotify API for real playback
- Replace static site list with a more flexible browser command parser
- Add conversation memory so Jarvis maintains context across turns

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## Security

If you find a security vulnerability, please follow the process described in [SECURITY.md](SECURITY.md). Do not open a public issue.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Author

**Kashish Arya**
B.Tech Computer Science | Meerut, Uttar Pradesh

GitHub: [github.com/your-username](https://github.com/your-username)
LinkedIn: [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)
