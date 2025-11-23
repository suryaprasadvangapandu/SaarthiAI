# SaarthiAI - Multilingual Community Voice Assistant

## Overview

SaarthiAI is a voice-enabled multilingual assistant designed to serve rural and underserved communities in India. The application provides guidance on health emergencies, government welfare schemes, and climate safety through voice interactions in English, Hindi, and Telugu. Built with a FastAPI backend and vanilla JavaScript frontend, the system uses rule-based intent detection to classify user queries and provide contextual step-by-step guidance.

The application emphasizes accessibility through voice-first interactions, multilingual support, and offline caching capabilities for the last 5 responses.

## Recent Changes

### November 23, 2025 - Major Enhancement Update

**UI Redesign:**
- Completely redesigned interface with modern animated gradient background (purple-pink)
- Implemented Inter font family for improved readability
- Added smooth transitions, hover effects, and pulse animations
- Enhanced responsive design for mobile and tablet devices
- Improved visual hierarchy and color scheme

**Knowledge Base Expansion:**

*Health Guidance - Now includes comprehensive multilingual content:*
- **Fever**: Complete treatment guide with danger signs, prevention measures (EN/HI/TE)
- **Cold & Cough**: Detailed symptoms, home treatment, medications, prevention (EN/HI/TE)
- **Stomach Problems**: Diarrhea, vomiting, food poisoning treatment with danger signs (EN/HI/TE)
- **General Health**: First-aid kit essentials, emergency numbers, healthy living tips (EN/HI/TE)

*Government Schemes - Comprehensive information:*
- 7+ major Indian welfare schemes (PMAY, Ayushman Bharat, Ujjwala, PM-KISAN, pension, Mudra loans, scholarships)
- Detailed eligibility criteria, benefits, and application processes
- Step-by-step guides for online and offline applications
- Required documents list and helpline numbers
- All content available in English, Hindi, and Telugu

*Climate Safety - Expanded emergency guidance:*
- **Heatwave**: Protection measures, heat cramps/exhaustion/stroke treatment
- **Flood**: Before/during/after safety protocols, evacuation procedures
- **General Emergencies**: Cyclone, lightning, earthquake, drought, air pollution
- Emergency preparedness kit recommendations
- Family emergency planning guidelines

**Technical Improvements:**
- Enhanced keyword detection with expanded Telugu vocabulary (జలుబు, వాంతులు)
- Fixed multilingual routing issues - all languages now receive intent-specific guidance
- Resolved keyword conflicts between health and scheme categories
- Improved accuracy of intent classification across all three languages

**Quality Assurance:**
- All multilingual paths tested and verified
- No fallback to generic responses for specific health conditions
- Scheme queries correctly route regardless of health-related terminology
- Production-ready with architect approval

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Technology Stack**: Vanilla JavaScript, HTML5, CSS3, Web Audio API

**Design Pattern**: Single-page application with event-driven architecture

The frontend is built entirely with vanilla JavaScript to minimize dependencies and ensure broad browser compatibility. Key architectural decisions include:

1. **Voice Input Handling**: Uses the browser's MediaRecorder API to capture audio directly from the user's microphone, eliminating the need for third-party SDN integrations
   - **Rationale**: Native browser APIs provide better security, lower latency, and work across modern browsers without additional libraries
   - **Alternative considered**: WebRTC - rejected due to unnecessary complexity for one-way audio capture

2. **Offline-First Caching**: Implements localStorage-based caching for the last 5 responses
   - **Rationale**: Enables basic functionality in areas with unreliable internet connectivity
   - **Limitation**: Only text responses are cached; audio files are not cached due to storage constraints

3. **Responsive Design**: Mobile-first CSS with gradient backgrounds and chat-bubble UI
   - **Rationale**: Target users are likely to access the service via mobile devices

### Backend Architecture

**Technology Stack**: Python 3.11, FastAPI, Uvicorn ASGI server

**Design Pattern**: RESTful API with layered architecture (routes → business logic → utilities)

1. **Rule-Based Intent Engine** (`models/logic.py`)
   - **Approach**: Keyword matching against predefined lists for three categories (health, schemes, climate)
   - **Rationale**: Rule-based system chosen over ML models for simplicity, predictability, and zero training requirements
   - **Pros**: Deterministic, no training data needed, easy to debug, language-agnostic (supports Hindi/Telugu keywords)
   - **Cons**: Limited to predefined keywords, cannot handle complex or ambiguous queries
   - **Alternative considered**: LLM-based intent detection - rejected due to cost, latency, and internet dependency

2. **Audio Processing Pipeline** (`utils/audio_helper.py`)
   - **Speech-to-Text**: Google Speech Recognition API via the `speech_recognition` library
   - **Text-to-Speech**: gTTS (Google Text-to-Speech) library
   - **Rationale**: Both services are free, support multiple Indian languages (Hindi, Telugu), and have acceptable latency
   - **Limitation**: Requires internet connectivity; offline STT/TTS not implemented

3. **Temporary File Management**
   - **Approach**: Audio files are stored in a `temp_audio/` directory and cleaned up after processing
   - **Rationale**: Prevents disk space accumulation while allowing file-based audio processing
   - **Security consideration**: File paths should be sanitized in production to prevent directory traversal attacks

4. **CORS Configuration**
   - **Current setting**: Allow all origins (`allow_origins=["*"]`)
   - **Rationale**: Simplifies development and testing
   - **Production requirement**: Must be restricted to specific frontend domains

### API Structure

**Endpoint Design**:
- `/health` - Health check endpoint for frontend status monitoring
- `/transcribe` - Accepts audio file, returns transcribed text
- `/respond` - Accepts text query + language, returns guidance text and audio file
- Static file serving at `/static/` for frontend assets

**Request/Response Flow**:
1. User speaks → Frontend captures audio → POST to `/transcribe`
2. Backend converts audio to text → Returns transcription
3. Frontend sends text to `/respond` with language parameter
4. Backend detects intent → Generates guidance → Converts to speech → Returns both text and audio
5. Frontend displays text in chat bubble and plays audio response

### Data Storage

**Current State**: No persistent database

The application is entirely stateless with no user data persistence. All interactions are ephemeral except for client-side caching in localStorage.

**Rationale**: 
- Simplifies deployment and reduces infrastructure requirements
- No privacy concerns from stored user queries
- Suitable for a proof-of-concept or MVP

**Future consideration**: Adding a database (SQLite, PostgreSQL) could enable:
- Query history and analytics
- Personalized responses based on user patterns
- Feedback collection for improving intent detection

### Authentication & Authorization

**Current State**: No authentication implemented

The application is publicly accessible without user accounts or API keys.

**Rationale**: 
- Target users (rural communities) may not have email accounts or technical literacy for account management
- Reduces barrier to entry
- Appropriate for public information services

**Security trade-off**: System is vulnerable to abuse (spam, resource exhaustion) without rate limiting

## External Dependencies

### Third-Party Services

1. **Google Speech Recognition API**
   - **Purpose**: Speech-to-text conversion
   - **Language support**: English (en-US), Hindi (hi-IN), Telugu (te-IN)
   - **Integration**: Via `speech_recognition` Python library
   - **Requirement**: Internet connectivity
   - **Limitation**: Free tier has usage quotas

2. **Google Text-to-Speech (gTTS)**
   - **Purpose**: Text-to-speech conversion
   - **Language support**: Multiple languages including Hindi and Telugu
   - **Integration**: Via `gtts` Python library
   - **Requirement**: Internet connectivity
   - **Note**: Uses Google Translate's TTS engine

### Python Libraries

- **FastAPI** (0.121.3): Modern async web framework with automatic OpenAPI documentation
- **Uvicorn** (0.38.0): Lightning-fast ASGI server
- **SpeechRecognition** (3.14.4): Unified interface for multiple speech recognition engines
- **gTTS** (2.5.4): Google Text-to-Speech wrapper
- **pydub** (0.25.1): Audio manipulation library (currently installed but not actively used in core flow)
- **python-multipart** (0.0.20): Required for FastAPI file upload handling
- **aiofiles** (25.1.0): Async file I/O for improved performance

### Browser APIs

- **MediaRecorder API**: Captures audio from user's microphone
- **Web Audio API**: Audio playback and manipulation
- **localStorage API**: Client-side caching of recent responses
- **Fetch API**: HTTP requests to backend

### Infrastructure Requirements

- **Python 3.11+**: Required for modern async features
- **File system access**: For temporary audio file storage
- **Network access**: For external API calls (Google services)
- **CORS-enabled server**: For frontend-backend communication

### Deployment Considerations

- No database server required
- Lightweight resource footprint (suitable for free-tier hosting)
- `temp_audio/` directory must be writable
- Environment should support outbound HTTPS for Google API calls