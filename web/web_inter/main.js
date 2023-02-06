var audioTrack = WaveSurfer.create({
    container: ".audio",
    waveColor: "violet",
    progressColor: "yellow",
    height: 70,                      
    hideScrollbar: false,                                            
    barWidth: 2,
  });
  const fileChosen1 = document.getElementById('track-name');
  var project_name = document.getElementById('fname') ;
  document.querySelector("#actual-btn").addEventListener("change", function() {
    var file = this.files[0];
    fileChosen1.textContent = this.files[0].name
    document.getElementById('project_name').textContent=project_name.value;
    audioTrack.loadBlob(file);
    audioTrack.play();
  });
  
  const playBtn = document.querySelector(".play-btn");
  const stopBtn = document.querySelector(".stop-btn");
  const muteBtn = document.querySelector(".mute-btn");
  const volumeSlider = document.querySelector(".volume-slider");
  
  playBtn.addEventListener("click", () => {
    audioTrack.playPause();
  
    if (audioTrack.isPlaying()) {
      playBtn.classList.add("playing");
    } else {
      playBtn.classList.remove("playing");
    }
  });
  
  stopBtn.addEventListener("click", () => {
    audioTrack.stop();
    playBtn.classList.remove("playing");
  });
  
  volumeSlider.addEventListener("mouseup", () => {
    changeVolume(volumeSlider.value);
  });
  
  const changeVolume = (volume) => {
    if (volume == 0) {
      muteBtn.classList.add("muted");
    } else {
      muteBtn.classList.remove("muted");
    }
  
    audioTrack.setVolume(volume);
  };
  
  muteBtn.addEventListener("click", () => {
    if (muteBtn.classList.contains("muted")) {
      muteBtn.classList.remove("muted");
      audioTrack.setVolume(0.5);
      volumeSlider.value = 0.5;
    } else {
      audioTrack.setVolume(0);
      muteBtn.classList.add("muted");
      volumeSlider.value = 0;
    }
  });

  