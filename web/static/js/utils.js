export function rawFrameToRGBArray(rawFrame) {
    // data is an ArrayBuffer
    // Convert to Uint8Array
    const lightsFrame = new Uint8Array(rawFrame);

    // Split it in groups of 4 bytes
    const lightsFrameGroup = [];
    for (let i = 0; i < lightsFrame.length; i += 4) {
        lightsFrameGroup.push(lightsFrame.slice(i, i + 4));
    }

    // Convert RGBW to RGB
    return lightsFrameGroup.map(group => {
        const [r, g, b, w] = group;

        const newRed = ((r - w) < 0 ? 0 : (r - w)).toString(16).padStart(2, '0');
        const newGreen = ((g - w) < 0 ? 0 : (g - w)).toString(16).padStart(2, '0');
        const newBlue = ((b - w) < 0 ? 0 : (b - w)).toString(16).padStart(2, '0');

        return `#${newRed}${newGreen}${newBlue}`;
    });
}