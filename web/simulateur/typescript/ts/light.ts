import ILight from "./interfaces/ILight.js";

export default class Light implements ILight {
    // Light ID (00-53): Type number
    _id: number;
    // RGBW value stored as bytes: Type Uint8Array
    _rgbw: Uint8Array;
    // HTML element
    _element: HTMLElement;

    constructor(id: number, _element: HTMLElement) {
        // Check types
        if (typeof id !== 'number') throw new TypeError('Light ID must be a number');
        if (typeof _element !== 'object') throw new TypeError('Light element must be an object');

        this._id = id;
        this._element = _element;

        // The light defaults to black
        this._rgbw = new Uint8Array([0, 0, 0, 0]);
    }

    /**
     * Gets the light's current color as a RGB string
     * @returns {string} The light's current color as a RGB string (e.g. #FF0000)
     */
    get rgbString(): string {
        // Convert RGBW to RGB
        const [r, g, b, w] = this._rgbw;

        const newRed = ((r - w) < 0 ? 0 : (r - w)).toString(16).padStart(2, '0');
        const newGreen = ((g - w) < 0 ? 0 : (g - w)).toString(16).padStart(2, '0');
        const newBlue = ((b - w) < 0 ? 0 : (b - w)).toString(16).padStart(2, '0');

        return `#${newRed}${newGreen}${newBlue}`;
    }

    /**
     * Gets the light's current color as a RGBW string
     * @returns {string} The light's current color as a RGBW string (e.g. #FF0000FF)
     */
    get rgbwString(): string {
        const [r, g, b, w] = this._rgbw;

        const newRed = r.toString(16).padStart(2, '0');
        const newGreen = g.toString(16).padStart(2, '0');
        const newBlue = b.toString(16).padStart(2, '0');
        const newWhite = w.toString(16).padStart(2, '0');

        return `#${newRed}${newGreen}${newBlue}${newWhite}`;
    }

    /**
     * Sets the light's color from a Uint8Array containing RGBW values
     * Actualizes the light's color on the HTML element by using the --light-color CSS variable
     * @param {Uint8Array} rgbw The light's new color as a Uint8Array containing RGBW values
     */
    set rgbw(rgbw: Uint8Array) {
        // Check type
        if (!(rgbw instanceof Uint8Array)) throw new TypeError('Light color must be a Uint8Array');

        this._rgbw = rgbw;
        this._element.style.setProperty('--light-color', this.rgbString);
    }

    get classId(): string {
        // Get element style like l-[00-99]
        return this._element.classList[1];
    }

    get id(): number {
        return this._id;
    }
}