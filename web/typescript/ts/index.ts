import LightsManager from "./lightsManager.js";
import AnimationManager from "./animationManager.js";

// Connect to localhost:5000 server
// @ts-ignore - SocketIO is imported in the HTML file
const socket = io.connect('http://localhost:5000');

// Find buttons in page
const playButton = document.querySelector('#play-button');
const stopButton = document.querySelector('#stop-button');
const nextButton = document.querySelector('#next-button');
const previousButton = document.querySelector('#previous-button');

const lightInformations = document.querySelector('#light-informations');

const lightMapping = [
    0, 1, 2,
    27, 28, 29,
    3, 4, 5,
    30, 31, 32,
    6, 7, 8,
    33, 34, 35,
    9, 10, 11,
    36, 37, 38,
    12, 13, 14,
    39, 40, 41,
    15, 16, 17,
    42, 43, 44,
    18, 19, 20,
    45, 46, 47,
    21, 22, 23,
    48, 49, 50,
    24, 25, 26,
    51, 52, 53
];

const lightManager = new LightsManager(document);
lightManager.mapping = lightMapping;

const animationManager = new AnimationManager(lightManager);

socket.on('connect', () => {
    console.log('[*] Connected to server');
});

socket.on('lights_state_reset', () => {
});

socket.on('light_frame', (data) => {
    console.log('[*] Update light status');

    const uint8Array = new Uint8Array(data);

    // Split the data into packs of 4 bytes
    const packets = [];
    for (let i = 0; i < uint8Array.length; i += 4) {
        packets.push(uint8Array.slice(i, i + 4));
    }

    animationManager.addFrame(packets);
});

// Add event listeners to buttons
playButton.addEventListener('click', () => {
    animationManager.runAnimation();
});