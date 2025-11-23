# SaarthiAI - Multilingual Community Voice Assistant

<img src="https://img.shields.io/badge/Python-3.11-blue" alt="Python 3.11"/> <img src="https://img.shields.io/badge/FastAPI-0.121-green" alt="FastAPI"/> <img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License"/>

SaarthiAI is a multilingual voice-enabled community assistant that provides guidance on health, government schemes, and climate safety in Hindi, Telugu, and English.

## Features

🎤 **Voice Input** - Speak your queries using your browser's microphone  
🗣️ **Multilingual Support** - Available in English, Hindi (हिन्दी), and Telugu (తెలుగు)  
🏥 **Health Guidance** - First-aid advice for common health issues  
📋 **Scheme Information** - Government welfare scheme application guidance  
🌤️ **Climate Safety** - Disaster and weather emergency advice  
🔊 **Voice Responses** - Hear guidance in your selected language  
📱 **Responsive Design** - Works on desktop and mobile devices  
💾 **Offline Mode** - Cache last 5 responses for offline access  

## Tech Stack

**Backend:**
- Python 3.11
- FastAPI - Modern web framework
- SpeechRecognition - Audio transcription
- gTTS - Text-to-speech conversion
- Uvicorn - ASGI server

**Frontend:**
- HTML5 - Structure
- CSS3 - Responsive styling
- Vanilla JavaScript - Interactivity
- Web Audio API - Microphone access

## Project Structure

```
saarthiai/
├── main.py                 # FastAPI application & endpoints
├── models/
│   ├── __init__.py
│   └── logic.py           # Rule-based intent detection engine
├── utils/
│   ├── __init__.py
│   └── audio_helper.py    # Speech-to-text & text-to-speech
├── static/
│   ├── app.js             # Frontend JavaScript logic
│   └── style.css          # Responsive CSS styles
├── templates/
│   └── index.html         # Main web interface
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Installation & Setup

### Prerequisites
- Python 3.11 or higher
- Internet connection (for speech recognition and TTS)
- Microphone-enabled device

### Step 1: Install Dependencies

All dependencies are already installed on Replit. If running locally:

```bash
pip install fastapi uvicorn speechrecognition gtts pydub python-multipart aiofiles
```

### Step 2: Run the Application

```bash
python main.py
```

The server will start on `http://0.0.0.0:5000`

### Step 3: Access the Interface

Open your browser and navigate to:
```
http://localhost:5000
```

Or use the Replit webview.

## How to Use

1. **Select Language** - Choose from English, Hindi, or Telugu
2. **Press Microphone** - Click the "Press to Speak" button
3. **Speak Your Query** - Ask about health, schemes, or climate safety
4. **Listen to Response** - The assistant will provide guidance and play audio

### Example Queries

**Health (English):**
- "My child has a fever"
- "First aid for burns"
- "What to do for headache?"

**स्वास्थ्य (Hindi):**
- "मेरे बच्चे को बुखार है"
- "सिरदर्द के लिए क्या करें?"

**ఆరోగ్యం (Telugu):**
- "నా బిడ్డకు జ్వరం వచ్చింది"
- "తలనొప్పికి ఏమి చేయాలి?"

**Government Schemes:**
- "How to apply for Ayushman Bharat?"
- "PM Awas Yojana application"

**Climate Safety:**
- "Heatwave safety tips"
- "What to do during floods?"

## API Endpoints

### GET /
Serves the main web interface

### GET /health
Health check endpoint
```json
{
  "status": "healthy",
  "service": "SaarthiAI",
  "version": "1.0.0"
}
```

### POST /transcribe
Transcribe audio to text
- **Input:** Audio file (WAV), language code
- **Output:** Transcribed text

### POST /respond
Get guidance with audio response
- **Input:** Text query, language code
- **Output:** Audio file (MP3) with guidance

### POST /get-guidance
Get guidance text only
- **Input:** Text query, language code
- **Output:** JSON with guidance text and intent

## Intent Detection

The system uses a rule-based engine to detect user intent:

- **Health** - Keywords: fever, pain, sick, injury, etc.
- **Schemes** - Keywords: yojana, application, pension, etc.
- **Climate** - Keywords: heatwave, flood, warning, etc.
- **General** - Default fallback

## Offline Mode

SaarthiAI automatically caches the last 5 responses in your browser's localStorage. When the server is offline:
- Status indicator turns red
- Offline notification appears
- Cached responses are available for reference

## Customization

### Adding New Languages
Edit `utils/audio_helper.py` and `models/logic.py`:
```python
lang_map = {
    'en': 'en-US',
    'hi': 'hi-IN',
    'te': 'te-IN',
    'ta': 'ta-IN'  # Add Tamil
}
```

### Adding New Intents
Edit `models/logic.py` to add new keyword lists and response templates.

### Modifying UI
Edit `static/style.css` for styling and `static/app.js` for functionality.

## Troubleshooting

**Microphone not working:**
- Grant microphone permissions in browser
- Use HTTPS or localhost (required for mic access)
- Check browser console for errors

**Speech recognition fails:**
- Ensure internet connection is active
- Speak clearly and reduce background noise
- Check if language is correctly selected

**Server errors:**
- Check console logs for detailed errors
- Verify all dependencies are installed
- Ensure port 5000 is not in use

## Browser Compatibility

- ✅ Chrome/Chromium (Recommended)
- ✅ Firefox
- ✅ Edge
- ✅ Safari (iOS 14.3+)

## Security Considerations

- No user data is stored permanently
- Audio files are deleted after processing
- All communication over HTTPS in production
- CORS enabled for development

## Future Enhancements

- [ ] Add more regional languages
- [ ] Implement NLP for better intent detection
- [ ] Add voice activity detection
- [ ] Create admin panel for content management
- [ ] Add user authentication
- [ ] Integrate with government APIs
- [ ] Support for image-based queries

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - feel free to use and modify for your needs.

## Support

For issues and questions:
- Check the troubleshooting section
- Review console logs for errors
- Open an issue on GitHub

## Acknowledgments

- Google Speech Recognition API
- Google Text-to-Speech (gTTS)
- FastAPI framework
- Replit community

---

**Made with ❤️ for community empowerment**
