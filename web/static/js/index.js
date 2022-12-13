import interpreter from './interpreter.js';
import state from './state.js';
import {rawFrameToRGBArray} from "./utils.js";

// Connect to localhost:5000 server
const socket = io.connect('http://localhost:5000');

const lights = document.querySelectorAll('.light');
const lightsArray = new Array(54);

// Find buttons in page
const playButton = document.querySelector('#play-button');
const stopButton = document.querySelector('#stop-button');
const nextButton = document.querySelector('#next-button');
const previousButton = document.querySelector('#previous-button');

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

// For each light, check the class like l-[00-99] and add it to the lightsObject
lights.forEach(light => {
    const lightID = light.classList[1].split('-')[1];
    lightsArray[parseInt(lightID)] = light;
});

socket.on('connect', () => {
    console.log('[*] Connected to server');

    // Make a deep copy of state
    const newState = {...state};

    // Set attributes
    interpreter.setState(newState);
    interpreter.setLightMapping(lightMapping);
    interpreter.setLightsArray(lightsArray);
});

socket.on('lights_state_reset', () => {
    // Reset the state
    interpreter.setState({...state});
});

socket.on('light_frame', (data) => {
    console.log('[*] Update light status');
    interpreter.pushFrame(rawFrameToRGBArray(data));

    if (interpreter.isLiveMode()) {
        interpreter.step();
    }
});

// Add event listeners to buttons
playButton.addEventListener('click', () => {
    interpreter.run();
});

stopButton.addEventListener('click', () => {
    interpreter.resetAnimation();
});

nextButton.addEventListener('click', () => {
    interpreter.step();
});

previousButton.addEventListener('click', () => {
    interpreter.previousStep();
});

