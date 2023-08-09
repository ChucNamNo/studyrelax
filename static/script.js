const audio = document.getElementById('music'); // Đổi id thành 'music'
const playButton = document.querySelector('.play-button');
const timeElement = document.getElementById('time');

const playButtonImg = "{{ url_for('static', filename='play_button.png') }}";
const pauseButtonImg = "{{ url_for('static', filename='pause_button.png') }}";
const audioSource = "/static/music.wav";

let isPlaying = false;

playButton.addEventListener('click', () => {
    if (isPlaying) {
        audio.pause();
        playButton.src = playButtonImg;
    } else {
        if (audio.currentTime === 0) { // Kiểm tra nếu âm thanh đang ở vị trí ban đầu
            audio.src = audioSource;
        }
        audio.play();
        playButton.src = pauseButtonImg;
    }
    isPlaying = !isPlaying;
});

// Hàm để tự động phát lại âm thanh khi kết thúc
function playAudioAgain() {
    audio.currentTime = 0; // Đặt thời gian của âm thanh về 0
    audio.play();
}

// Sự kiện lắng nghe khi âm thanh kết thúc
audio.addEventListener('ended', playAudioAgain);

// Sự kiện lắng nghe khi thời gian của âm thanh thay đổi (để cập nhật thời gian hiển thị)
audio.addEventListener('timeupdate', () => {
    const totalSeconds = Math.floor(audio.currentTime);
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    
    const formattedTime = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    timeElement.textContent = formattedTime;
});
