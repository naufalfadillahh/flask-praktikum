document.addEventListener("DOMContentLoaded", function () {
    // VIDEO UTAMA
    const video = document.getElementById("videoPlayer");
    const playBtn = document.getElementById("playBtn1");
    const pauseBtn = document.getElementById("pauseBtn1");
    const fullScreenBtn = document.getElementById("fullScreenBtn1");

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

