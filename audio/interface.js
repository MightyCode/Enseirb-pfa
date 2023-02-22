function load(){
    var head = document.getElementsByTagName('head')[0];
    var js = document.createElement("script");
    js.type = "text/javascript";
    js.src = 'tone.js';
    head.appendChild(js);

    var button = document.getElementById("lauchTests");
    button.disabled = false;
}

function tests(){
    // create a synth using an Oscillator
    const synth = new Tone.Synth().toDestination();

    // play a note with the synth
    synth.triggerAttackRelease("C4", "8n");

    // create a player from a URL
    const player = new Tone.Player("mp3/cuicui.mp3").toDestination();

    setTimeout(() => player.start(), 2000);
    // start playing the sample

    /*

    // create two Panner3D nodes for the speakers
    const speaker1 = new Tone.Panner3D().toDestination();
    console.log(speaker1);
    speaker1.setPosition(-1, 0, 0);

    const speaker2 = new Tone.Panner3D().toDestination();
    speaker2.setPosition(1, 0, 0);

    const player = new Tone.Player("mp3/beeehhhh.mp3");
    // load audio files into Tone.js AudioBuffers
    const buffer1 = new Tone.ToneAudioBuffer("mp3/beeehhhh.mp3").load();
    const buffer2 = new Tone.ToneAudioBuffer("mp3/cuicui.mp3").load();

    buffer1.connect

    // start playing the audio files from the speakers
    buffer1.connect(speaker1).start(0);
    buffer2.connect(speaker2).start(0);

    // set the initial position of the virtual listener
    const listener = Tone.Listener.setPosition(0, 0, 0);

    // move the listener to a new position
    const moveListener = (x, y, z) => {
        listener.setPosition(x, y, z);
    };

    // Example usage: move the listener to (1, 2, 3) after 2 seconds
    setTimeout(() => moveListener(1, 2, 3), 2000);*/
}
