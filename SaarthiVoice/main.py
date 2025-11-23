"""
SaarthiAI - Multilingual Community Voice Assistant
Main FastAPI application with REST API endpoints
"""

from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import logging
from pathlib import Path
import tempfile
import shutil

# Import custom modules
from models.logic import IntentEngine
from utils.audio_helper import AudioHelper

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="SaarthiAI",
    description="Multilingual Community Voice Assistant",
    version="1.0.0"
)

# Enable CORS (Cross-Origin Resource Sharing) for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins in development
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create temp directory for audio files
TEMP_DIR = Path("temp_audio")
TEMP_DIR.mkdir(exist_ok=True)

# Initialize intent engine and audio helper
intent_engine = IntentEngine()
audio_helper = AudioHelper()


@app.get("/")
async def root():
    """
    Serve the main HTML page
    """
    return FileResponse("templates/index.html")


@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify server is running
    Returns server status
    """
    return {
        "status": "healthy",
        "service": "SaarthiAI",
        "version": "1.0.0"
    }


@app.post("/transcribe")
async def transcribe_audio(
    audio: UploadFile = File(...),
    language: str = Form(default="en")
):
    """
    Transcribe audio file to text
    
    Args:
        audio: Audio file (WAV format)
        language: Language code (en, hi, te)
    
    Returns:
        JSON with transcribed text
    """
    temp_file = None
    try:
        # Validate language
        if language not in ['en', 'hi', 'te']:
            raise HTTPException(status_code=400, detail="Unsupported language")
        
        # Secure filename handling - prevent None and path traversal
        if not audio.filename:
            safe_filename = "audio.wav"
        else:
            # Remove directory separators to prevent path traversal
            safe_filename = os.path.basename(audio.filename)
        
        # Create unique temp file to avoid collisions
        import uuid
        unique_id = uuid.uuid4().hex[:8]
        temp_file = TEMP_DIR / f"temp_{unique_id}_{safe_filename}"
        
        # Save uploaded file temporarily
        with temp_file.open("wb") as buffer:
            shutil.copyfileobj(audio.file, buffer)
        
        # Transcribe audio to text
        text = audio_helper.transcribe_audio(str(temp_file), language)
        
        logger.info(f"Transcribed: {text}")
        
        return {
            "success": True,
            "text": text,
            "language": language
        }
        
    except Exception as e:
        logger.error(f"Transcription error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        # Always clean up temp file
        if temp_file and temp_file.exists():
            try:
                temp_file.unlink()
            except Exception as cleanup_error:
                logger.warning(f"Failed to cleanup temp file: {cleanup_error}")


@app.post("/respond")
async def generate_response(
    text: str = Form(...),
    language: str = Form(default="en")
):
    """
    Generate guidance response and audio for user query
    
    Args:
        text: User query text
        language: Language code (en, hi, te)
    
    Returns:
        Streaming audio response
    """
    try:
        # Validate language
        if language not in ['en', 'hi', 'te']:
            raise HTTPException(status_code=400, detail="Unsupported language")
        
        # Get guidance from intent engine
        response_data = intent_engine.get_guidance(text, language)
        guidance_text = response_data['guidance']
        
        logger.info(f"Intent: {response_data['intent']}, Language: {language}")
        
        # Generate speech audio
        audio_buffer = audio_helper.text_to_speech(guidance_text, language)
        
        # Return audio as streaming response (removed illegal headers with newlines)
        return StreamingResponse(
            audio_buffer,
            media_type="audio/mpeg",
            headers={
                "Content-Disposition": "attachment; filename=response.mp3",
                "X-Intent": response_data['intent']
            }
        )
        
    except Exception as e:
        logger.error(f"Response generation error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/get-guidance")
async def get_guidance_text(
    text: str = Form(...),
    language: str = Form(default="en")
):
    """
    Get guidance text without audio (for offline mode caching)
    
    Args:
        text: User query text
        language: Language code (en, hi, te)
    
    Returns:
        JSON with guidance text and intent
    """
    try:
        # Validate language
        if language not in ['en', 'hi', 'te']:
            raise HTTPException(status_code=400, detail="Unsupported language")
        
        # Get guidance from intent engine
        response_data = intent_engine.get_guidance(text, language)
        
        return {
            "success": True,
            "text": text,
            "intent": response_data['intent'],
            "guidance": response_data['guidance'],
            "language": language
        }
        
    except Exception as e:
        logger.error(f"Guidance error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# Cleanup temp files on shutdown
@app.on_event("shutdown")
async def cleanup():
    """Clean up temporary files on server shutdown"""
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)
    logger.info("Cleaned up temporary files")


if __name__ == "__main__":
    # Run the server
    # Bind to 0.0.0.0:5000 for Replit compatibility
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5000,
        reload=True,
        log_level="info"
    )
