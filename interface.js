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
    // create a player from a URL
    var speakersPosition = [
        [-2, 5, 0],
        [0, 5, 0],
        [2, 5, 0],

        [-2, -5, 0],
        [0, -5, 0],
        [2, -5, 0],

        [-5, 2, 0],
        [-5, -2, 0],

        [5, 2, 0],
        [5, -2, 0],
    ]

    var speakers = [];
    for (var i = 0; i <= 9; ++i){
        speakers.push(
            new Tone.Panner3D({
                panningModel: "HRTF",
                positionX : speakersPosition[i][0],
                positionY : speakersPosition[i][1],
                positionZ : speakersPosition[i][2],
            }).toDestination()
        );
    }

    function createPlayerPlusPanner(url, speakerId) {
        const player = new Tone.Player({
            url,
            loop: true,
        }).connect(speakers[speakerId]);

        setTimeout(() => player.start(), 2000);

        console.log("Play " + url)
    }

    for (var i = 0; i <= 9; ++i){ 
        createPlayerPlusPanner("out/speaker" + i + ".wav", i);
    }
    
    function setRotation(angle) {
        document.getElementById("orientationLabel").innerText = angle;

        Tone.Listener.forwardX.value = Math.sin(angle);
        Tone.Listener.forwardY.value = 0;
        Tone.Listener.forwardZ.value = -Math.cos(angle);
    }
    
    Tone.Listener.positionX = 0;
    Tone.Listener.positionY = 0;
    Tone.Listener.positionZ = 0;

    document.getElementById("orientation").addEventListener("input", (e) => setRotation(parseFloat(e.target.value)));
}
