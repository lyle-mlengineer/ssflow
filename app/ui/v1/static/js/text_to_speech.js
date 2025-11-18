const languageSelect = document.getElementById('language');
const genderSelect = document.getElementById('gender');
let voiceSelect = document.getElementById('voice');
let form = document.getElementById('text-to-speech-form');
const loader = document.querySelector('.orbit-loading-ring');
const audioOutput = document.querySelector('.audio-output');
const audioElement = audioOutput.querySelector('audio');


const textInput = document.getElementById('text-input');
const convertButton = document.getElementById('convert-button');


languageSelect.addEventListener('change', (e) => {
    e.preventDefault();
    const selectedLanguage = languageSelect.value;
    const selectedGender = genderSelect.value;
    // Fetch voices for the selected language
    fetch(`/api/v1/audio/voices?gender=${selectedGender}&language=${selectedLanguage}`)
        .then(response => response.json())
        .then(data => {
            const voices = data.voices;
            voiceSelect.innerHTML = voices.map(voice => `<option value="${voice}">${voice}</option>`).join('');
        })
        .catch(error => {
            console.error('Error fetching voices:', error);
        });
});

genderSelect.addEventListener('change', (e) => {
    e.preventDefault();
    const selectedLanguage = languageSelect.value;
    const selectedGender = genderSelect.value;
    // Fetch voices for the selected language
    fetch(`/api/v1/audio/voices?gender=${selectedGender}&language=${selectedLanguage}`)
        .then(response => response.json())
        .then(data => {
            const voices = data.voices;
            voiceSelect.innerHTML = voices.map(voice => `<option value="${voice}">${voice}</option>`).join('');
        })
        .catch(error => {
            console.error('Error fetching voices:', error);
        })
});

form.addEventListener('submit', (e) => {
    e.preventDefault();
    // Show the loader
    loader.classList.toggle('hidden');
    audioOutput.classList.remove('visible');
    const formData = new FormData(form);
    fetch('/api/v1/audio/generate_speech', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            console.log('Speech generated successfully:', data);
            loader.classList.toggle('hidden');
            audioOutput.classList.add('visible');
            audioElement.src = data.audio_url;
            // audioElement.play();
        })
        .catch(error => {
            console.error('Error generating speech:', error);
        });
});