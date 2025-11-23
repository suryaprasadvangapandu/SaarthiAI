"""
Audio processing utilities for SaarthiAI
Handles speech-to-text and text-to-speech conversions
"""

import speech_recognition as sr
from gtts import gTTS
import os
from io import BytesIO
import logging
from pydub import AudioSegment

logger = logging.getLogger(__name__)

class AudioHelper:
    """
    Handles audio transcription and text-to-speech conversion
    """
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        # Adjust for ambient noise
        self.recognizer.energy_threshold = 4000
        self.recognizer.dynamic_energy_threshold = True
    
    def convert_to_wav(self, input_path, output_path):
        """
        Convert audio file to WAV format using pydub
        
        Args:
            input_path: Path to input audio file (any format)
            output_path: Path to output WAV file
        
        Returns:
            Path to converted WAV file
        """
        try:
            # Detect file format from extension or try common formats
            audio = None
            try:
                # Try as WebM (common browser format)
                audio = AudioSegment.from_file(input_path, format="webm")
            except:
                try:
                    # Try as generic audio file
                    audio = AudioSegment.from_file(input_path)
                except Exception as e:
                    logger.error(f"Could not load audio file: {e}")
                    raise
            
            # Export as WAV with proper settings
            audio.export(
                output_path,
                format="wav",
                parameters=["-ar", "16000", "-ac", "1"]  # 16kHz mono
            )
            
            logger.info(f"Converted audio to WAV: {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"Error converting audio: {e}")
            raise
    
    def transcribe_audio(self, audio_file_path, language='en'):
        """
        Convert speech audio to text
        
        Args:
            audio_file_path: Path to the audio file
            language: Language code (en, hi, te)
        
        Returns:
            Transcribed text string
        """
        wav_path = None
        try:
            # Map language codes to Google Speech Recognition codes
            lang_map = {
                'en': 'en-US',
                'hi': 'hi-IN',
                'te': 'te-IN'
            }
            
            google_lang = lang_map.get(language, 'en-US')
            
            logger.info(f"Transcribing file: {audio_file_path}, language: {language}")
            
            # ALWAYS convert the audio file - browser may create fake .wav files
            # that are actually WebM or other formats
            wav_path = audio_file_path.replace(os.path.splitext(audio_file_path)[1], '_converted.wav')
            logger.info(f"Converting audio file to proper WAV format: {wav_path}")
            try:
                self.convert_to_wav(audio_file_path, wav_path)
                if not os.path.exists(wav_path):
                    raise Exception(f"Converted WAV file not found: {wav_path}")
                file_to_use = wav_path
                logger.info(f"Conversion successful, file size: {os.path.getsize(wav_path)} bytes")
            except Exception as conv_error:
                logger.error(f"Audio conversion failed: {conv_error}")
                raise Exception(f"Could not convert audio format: {str(conv_error)}")
            
            # Load audio file
            logger.info(f"Loading audio file for recognition: {file_to_use}")
            with sr.AudioFile(file_to_use) as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                # Record the audio
                audio_data = self.recognizer.record(source)
            
            logger.info("Audio loaded successfully, sending to Google Speech Recognition")
            
            # Recognize speech using Google Speech Recognition
            text = self.recognizer.recognize_google(
                audio_data, 
                language=google_lang
            )
            
            logger.info(f"Transcribed text: {text}")
            return text
            
        except sr.UnknownValueError:
            logger.error("Could not understand audio")
            return "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            logger.error(f"Could not request results; {e}")
            return "Sorry, there was an error processing your request."
        except Exception as e:
            logger.error(f"Error in transcription: {e}")
            return f"Error: {str(e)}"
        
        finally:
            # Clean up converted WAV file
            if wav_path and os.path.exists(wav_path):
                try:
                    os.unlink(wav_path)
                    logger.info(f"Cleaned up temp WAV file: {wav_path}")
                except Exception as e:
                    logger.warning(f"Could not delete temp WAV file: {e}")
    
    def text_to_speech(self, text, language='en'):
        """
        Convert text to speech audio
        
        Args:
            text: Text to convert
            language: Language code (en, hi, te)
        
        Returns:
            BytesIO object containing MP3 audio data
        """
        try:
            # Map language codes to gTTS codes
            lang_map = {
                'en': 'en',
                'hi': 'hi',
                'te': 'te'
            }
            
            gtts_lang = lang_map.get(language, 'en')
            
            # Create text-to-speech object
            tts = gTTS(text=text, lang=gtts_lang, slow=False)
            
            # Save to BytesIO object (in-memory file)
            audio_buffer = BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)
            
            logger.info(f"Generated speech for text: {text[:50]}...")
            return audio_buffer
            
        except Exception as e:
            logger.error(f"Error in text-to-speech: {e}")
            raise
    
    def save_tts_to_file(self, text, output_path, language='en'):
        """
        Save text-to-speech to file
        
        Args:
            text: Text to convert
            output_path: Path to save the audio file
            language: Language code
        """
        try:
            audio_buffer = self.text_to_speech(text, language)
            
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Write to file
            with open(output_path, 'wb') as f:
                f.write(audio_buffer.read())
            
            logger.info(f"Saved audio to {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"Error saving TTS to file: {e}")
            raise
