const changeAudioBtn = document.querySelector('.change-audio-btn');
const transcriptionForm = document.getElementById('transcription');
const promptOutput = document.getElementById('prompt-container');

changeAudioBtn.addEventListener('click', function(event) {
    event.preventDefault();
    window.location.href = '/audio_picker';
});

transcriptionForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Show loading indicator
    const loader = document.querySelector('.orbit-loading-ring');
    loader.classList.remove('hidden');
    promptOutput.classList.remove('visible');

    const audioUrl = document.getElementById('audio').value;
    const languageSelect = document.getElementById('language');
    const selectedLanguage = languageSelect.value;

    const payload = {
        audio: audioUrl,
        language: selectedLanguage
    };

    fetch('/api/v1/audio/transcribe_speech', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
        .then(response => response.json())
        .then(data => {
            // Hide loading indicator
            console.log('Transcription successful:', data);
            loader.classList.add('hidden');
            const textOutput = document.getElementById('text-output');
            textOutput.textContent = data.transcription;
            promptOutput.classList.add('visible');
        })
        .catch(error => {
            console.error('Error:', error);
        });
});