import ILight from "./interfaces/ILight.js";
import ILightsManager from "./interfaces/ILightsManager.js";
import Light from "./light.js";

export default class LightsManager implements ILightsManager {

    _lightsElements: HTMLElement[];
    _lightsArray: { [id: number]: ILight };
    _mapping: number[];

    _selectedLight: ILight;
    _callback: (light: ILight) => void;

    constructor(_document: Document, _callback?: (light: ILight) => void) {
        // Check type
        if (typeof _document !== 'object') throw new TypeError('Document must be an object');

        this._lightsElements = Array.from(_document.querySelectorAll('.light')); // Get all the lights elements
        this._lightsArray = {};

        // If no callback is provided, do nothing
        if (!_callback) {
            this._callback = () => { };
        } else {
            this._callback = _callback;
        }

        // Mapping is an array from 1 to 54
        this._mapping = [...Array(53).keys()].map(i => i + 1);

        this._lightsElements.forEach(light => {
            const lightID = light.classList[1].split('-')[1]; // Get the light ID from the class name
            const lightObject = new Light(parseInt(lightID), light);
            this._lightsArray[parseInt(lightID)] = lightObject; // Add the light to the array

            // On click, return the light's RGBW value to the callback
            light.addEventListener('click', () => {
                this._selectedLight = lightObject;
                this._callback(lightObject);
            });
        });
    }

    /**
     * Set the mapping of the lights
     * @param mapping {number[]} The mapping of the lights
     */
    set mapping(mapping: number[]) {
        // If the mapping is not an array, throw an error
        if (!Array.isArray(mapping)) throw new TypeError('Mapping must be an array');

        this._mapping = mapping;
    }

    /**
     * Gets a specific light from its ID
     * @param id {number} The light ID [0-53]
     * @returns {ILight} The light object
     */
    getLight(id: number): ILight {
        // Check types
        if (typeof id !== 'number') throw new TypeError('Light ID must be a number');

        return this._lightsArray[id];
    }

    /**
     * Gets the number of lights
     * @returns {number} The number of lights
     */
    get numberOfLights(): number {
        return Object.keys(this._lightsArray).length;
    }

    /**
     * Applies a frame to the lights
     * @param frame {Array} The frame to apply
     */
    applyFrame(frame: Array<Uint8Array>) {
        // Check types
        if (!Array.isArray(frame)) throw new TypeError('Frame must be an array');

        // Call the callback with the selected light
        if (this._selectedLight) this._callback(this._selectedLight);

        // For each light in the frame, apply the RGBW value
        frame.forEach((light, index) => {
            this.getLight(index + 1).rgbw = light;
        });
    }
}