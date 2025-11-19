const changeAudioBtn = document.querySelector('.change-audio-btn');

changeAudioBtn.addEventListener('click', function(event) {
    event.preventDefault();
    window.location.href = '/audio_picker';
});