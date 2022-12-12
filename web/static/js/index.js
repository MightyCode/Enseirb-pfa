// Connect to localhost:5000 server
const socket = io.connect('http://localhost:5000');

const lights = document.querySelectorAll('.light');
const lightsArray = new Array(54);

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
});

socket.on('light_frame', (data) => {
    console.log('[*] Update light status');

    // data is an ArrayBuffer
    // Convert to Uint8Array
    const lightsFrame = new Uint8Array(data);

    // Split it in groups of 4 bytes
    const lightsFrameGroup = [];
    for (let i = 0; i < lightsFrame.length; i += 4) {
        lightsFrameGroup.push(lightsFrame.slice(i, i + 4));
    }

    // Convert RGBW to RGB
    const lightsFrameRGB = lightsFrameGroup.map(group => {
        const [r, g, b, w] = group;

        const newRed = ((r - w) < 0 ? 0 : (r - w)).toString(16).padStart(2, '0');
        const newGreen = ((g - w) < 0 ? 0 : (g - w)).toString(16).padStart(2, '0');
        const newBlue = ((b - w) < 0 ? 0 : (b - w)).toString(16).padStart(2, '0');

        return `#${newRed}${newGreen}${newBlue}`;
    });

    // Set CSS --light-color property for each light
    lightsArray.forEach((light, index) => {
        light.style.setProperty('--light-color', lightsFrameRGB[lightMapping[index]]);
    });
});