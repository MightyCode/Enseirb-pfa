import ILight from "./interfaces/ILight.js";
import ILightsManager from "./interfaces/ILightsManager.js";
import Light from "./light.js";

export default class LightsManager implements ILightsManager {

    _lightsElements: HTMLElement[];
    _lightsArray: { [id: number]: ILight };
    _mapping: number[];

    constructor(_document: Document) {
        // Check type
        if (typeof _document !== 'object') throw new TypeError('Document must be an object');

        this._lightsElements = Array.from(_document.querySelectorAll('.light')); // Get all the lights elements
        this._lightsArray = {};

        // Mapping is an array from 1 to 54
        this._mapping = [...Array(53).keys()].map(i => i + 1);

        this._lightsElements.forEach(light => {
            const lightID = light.classList[1].split('-')[1]; // Get the light ID from the class name            
            this._lightsArray[parseInt(lightID)] = new Light(parseInt(lightID), light); // Add the light to the array
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
     * @returns {Light} The light object
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

        frame.forEach((light, index) => {
            this.getLight(index + 1).rgbw = light;
        });
    }
}