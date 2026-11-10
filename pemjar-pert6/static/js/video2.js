document.addEventListener("DOMContentLoaded", function () {
    // VIDEO DOKUMENTASI
    const video = document.getElementById("videoPlayer2");
    const playBtn = document.getElementById("playBtn2");
    const pauseBtn = document.getElementById("pauseBtn2");
    const fullScreenBtn = document.getElementById("fullScreenBtn2");

    if (!video || !playBtn || !pauseBtn || !fullScreenBtn) return;

    // Play
    playBtn.addEventListener("click", function () {
        video.play();
    });

    // Pause
    pauseBtn.addEventListener("click", function () {
        video.pause();
    });

    // Fullscreen
    fullScreenBtn.addEventListener("click", function () {
        if (video.requestFullscreen) {
            video.requestFullscreen();
        } else if (video.mozRequestFullScreen) {
            video.mozRequestFullScreen();
        } else if (video.webkitRequestFullscreen) {
            video.webkitRequestFullscreen();
        }
    });
});

