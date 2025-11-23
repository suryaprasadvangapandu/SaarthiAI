// SaarthiAI - Frontend JavaScript

// Global variables
let mediaRecorder;
let audioChunks = [];
let isRecording = false;
let isOnline = true;
const MAX_CACHED_RESPONSES = 5;

// DOM elements
const micButton = document.getElementById('mic-button');
const chatContainer = document.getElementById('chat-container');
const languageSelect = document.getElementById('language');
const statusIndicator = document.getElementById('status-indicator');
const statusText = document.getElementById('status-text');
const recordingIndicator = document.getElementById('recording-indicator');
const offlineNotice = document.getElementById('offline-notice');
const audioPlayer = document.getElementById('audio-player');

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log('SaarthiAI initialized');
    checkServerStatus();
    loadCachedResponses();
    
    // Set up mic button
    micButton.addEventListener('click', toggleRecording);
});

// Check server health status
async function checkServerStatus() {
    try {
        const response = await fetch('/health');
        const data = await response.json();
        
        if (data.status === 'healthy') {
            setOnlineStatus(true);
        } else {
            setOnlineStatus(false);
        }
    } catch (error) {
        console.error('Server offline:', error);
        setOnlineStatus(false);
    }
}

// Set online/offline status
function setOnlineStatus(online) {
    isOnline = online;
    
    if (online) {
        statusIndicator.className = 'status-online';
        statusText.textContent = 'Online';
        offlineNotice.style.display = 'none';
    } else {
        statusIndicator.className = 'status-offline';
        statusText.textContent = 'Offline';
        offlineNotice.style.display = 'block';
    }
}

// Toggle recording
async function toggleRecording() {
    if (isRecording) {
        stopRecording();
    } else {
        await startRecording();
    }
}

// Start recording
async function startRecording() {
    try {
        // Request microphone access
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        
        // Create media recorder
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];
        
        // Collect audio chunks
        mediaRecorder.ondataavailable = (event) => {
            audioChunks.push(event.data);
        };
        
        // Handle recording stop
        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            await processAudio(audioBlob);
            
            // Stop all tracks
            stream.getTracks().forEach(track => track.stop());
        };
        
        // Start recording
        mediaRecorder.start();
        isRecording = true;
        
        // Update UI
        micButton.classList.add('recording');
        micButton.querySelector('.button-text').textContent = 'Stop Recording';
        recordingIndicator.style.display = 'flex';
        
        console.log('Recording started');
        
    } catch (error) {
        console.error('Error accessing microphone:', error);
        alert('Could not access microphone. Please grant permission and try again.');
    }
}

// Stop recording
function stopRecording() {
    if (mediaRecorder && isRecording) {
        mediaRecorder.stop();
        isRecording = false;
        
        // Update UI
        micButton.classList.remove('recording');
        micButton.querySelector('.button-text').textContent = 'Press to Speak';
        recordingIndicator.style.display = 'none';
        
        console.log('Recording stopped');
    }
}

// Process recorded audio
async function processAudio(audioBlob) {
    const language = languageSelect.value;
    
    // Add user message placeholder
    addMessage('user', 'Processing your voice...');
    
    try {
        // Step 1: Transcribe audio to text
        const transcribedText = await transcribeAudio(audioBlob, language);
        
        // Update user message with transcribed text
        updateLastUserMessage(transcribedText);
        
        // Step 2: Get response with audio
        await getResponse(transcribedText, language);
        
    } catch (error) {
        console.error('Error processing audio:', error);
        
        // If offline, show cached responses
        if (!isOnline) {
            showCachedResponses();
        } else {
            addMessage('bot', 'Sorry, there was an error processing your request. Please try again.', 'general');
        }
    }
}

// Transcribe audio to text
async function transcribeAudio(audioBlob, language) {
    const formData = new FormData();
    formData.append('audio', audioBlob, 'recording.wav');
    formData.append('language', language);
    
    const response = await fetch('/transcribe', {
        method: 'POST',
        body: formData
    });
    
    if (!response.ok) {
        throw new Error('Transcription failed');
    }
    
    const data = await response.json();
    return data.text;
}

// Get response from server
async function getResponse(text, language) {
    const formData = new FormData();
    formData.append('text', text);
    formData.append('language', language);
    
    try {
        // First get the guidance text
        const guidanceResponse = await fetch('/get-guidance', {
            method: 'POST',
            body: formData
        });
        
        const guidanceData = await guidanceResponse.json();
        
        // Add bot message with guidance
        addMessage('bot', guidanceData.guidance, guidanceData.intent);
        
        // Cache the response for offline use
        cacheResponse({
            text: text,
            guidance: guidanceData.guidance,
            intent: guidanceData.intent,
            language: language,
            timestamp: new Date().toISOString()
        });
        
        // Get and play audio
        const audioResponse = await fetch('/respond', {
            method: 'POST',
            body: formData
        });
        
        if (audioResponse.ok) {
            const audioBlob = await audioResponse.blob();
            playAudio(audioBlob);
        }
        
    } catch (error) {
        console.error('Error getting response:', error);
        setOnlineStatus(false);
        throw error;
    }
}

// Play audio response
function playAudio(audioBlob) {
    const audioUrl = URL.createObjectURL(audioBlob);
    audioPlayer.src = audioUrl;
    audioPlayer.play();
    
    // Clean up URL after playing
    audioPlayer.onended = () => {
        URL.revokeObjectURL(audioUrl);
    };
}

// Add message to chat
function addMessage(type, text, intent = null) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${type}-message`;
    
    const label = document.createElement('div');
    label.className = 'message-label';
    label.textContent = type === 'user' ? 'You' : 'Saarthi AI';
    
    const bubble = document.createElement('div');
    bubble.className = 'message-bubble';
    
    // Add intent badge for bot messages
    if (type === 'bot' && intent) {
        const badge = document.createElement('div');
        badge.className = `intent-badge intent-${intent}`;
        badge.textContent = intent.charAt(0).toUpperCase() + intent.slice(1);
        bubble.appendChild(badge);
        bubble.appendChild(document.createElement('br'));
    }
    
    const textNode = document.createTextNode(text);
    bubble.appendChild(textNode);
    
    messageDiv.appendChild(label);
    messageDiv.appendChild(bubble);
    
    chatContainer.appendChild(messageDiv);
    
    // Scroll to bottom
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Update the last user message (used after transcription)
function updateLastUserMessage(text) {
    const messages = chatContainer.querySelectorAll('.user-message');
    if (messages.length > 0) {
        const lastMessage = messages[messages.length - 1];
        const bubble = lastMessage.querySelector('.message-bubble');
        bubble.textContent = text;
    }
}

// Cache response to localStorage
function cacheResponse(response) {
    try {
        let cached = JSON.parse(localStorage.getItem('saarthiCache')) || [];
        
        // Add new response to beginning
        cached.unshift(response);
        
        // Keep only last MAX_CACHED_RESPONSES
        if (cached.length > MAX_CACHED_RESPONSES) {
            cached = cached.slice(0, MAX_CACHED_RESPONSES);
        }
        
        localStorage.setItem('saarthiCache', JSON.stringify(cached));
        console.log('Response cached');
        
    } catch (error) {
        console.error('Error caching response:', error);
    }
}

// Load cached responses
function loadCachedResponses() {
    try {
        const cached = JSON.parse(localStorage.getItem('saarthiCache')) || [];
        console.log(`Loaded ${cached.length} cached responses`);
        return cached;
    } catch (error) {
        console.error('Error loading cache:', error);
        return [];
    }
}

// Show cached responses when offline
function showCachedResponses() {
    const cached = loadCachedResponses();
    
    if (cached.length === 0) {
        addMessage('bot', 'No cached responses available. Please try again when online.', 'general');
        return;
    }
    
    addMessage('bot', 
        `Offline mode: Here are your last ${cached.length} cached responses:\n\n` +
        cached.map((item, index) => 
            `${index + 1}. ${item.text}\n→ ${item.guidance.substring(0, 100)}...`
        ).join('\n\n'),
        'general'
    );
}

// Periodically check server status
setInterval(checkServerStatus, 30000); // Check every 30 seconds
