export function rawFrameToRGBArray(rawFrame) {
    // Convert to Uint8Array
    const lightsFrame = new Uint8Array(rawFrame);
    // Split it in groups of 4 bytes
    const lightsFrameGroup = [];
    for (let i = 0; i < lightsFrame.length; i += 4) {
        lightsFrameGroup.push(lightsFrame.slice(i, i + 4));
    }
    // Convert RGBW to RGB
    return lightsFrameGroup.map(group => {
        if (group.length !== 4) {
            throw new Error('Invalid frame format');
        }
        const [r, g, b, w] = group;
        const newRed = ((r - w) < 0 ? 0 : (r - w)).toString(16).padStart(2, '0');
        const newGreen = ((g - w) < 0 ? 0 : (g - w)).toString(16).padStart(2, '0');
        const newBlue = ((b - w) < 0 ? 0 : (b - w)).toString(16).padStart(2, '0');
        return `#${newRed}${newGreen}${newBlue}`;
    });
}
export function rawFrameToRGBWArray(rawFrame) {
    // data is an ArrayBuffer
    // Convert to Uint8Array
    const lightsFrame = new Uint8Array(rawFrame);
    // Split it in groups of 4 bytes
    const lightsFrameGroup = [];
    for (let i = 0; i < lightsFrame.length; i += 4) {
        lightsFrameGroup.push(lightsFrame.slice(i, i + 4));
    }
    return lightsFrameGroup.map(group => {
        // Convert RGBW to RGB
        const [r, g, b, w] = group;
        const newRed = r.toString(16).padStart(2, '0');
        const newGreen = g.toString(16).padStart(2, '0');
        const newBlue = b.toString(16).padStart(2, '0');
        const newWhite = w.toString(16).padStart(2, '0');
        // Check for invalid values
        if (r < 0 || r > 255) {
            throw new Error('Invalid red value');
        }
        if (g < 0 || g > 255) {
            throw new Error('Invalid green value');
        }
        if (b < 0 || b > 255) {
            throw new Error('Invalid blue value');
        }
        if (w < 0 || w > 255) {
            throw new Error('Invalid white value');
        }
        return `#${newRed}${newGreen}${newBlue}${newWhite}`;
    });
}
