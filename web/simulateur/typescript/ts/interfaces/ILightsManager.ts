import ILight from "./ILight.js";

export default interface ILightsManager {
    mapping: Array<number>;
    numberOfLights: number;
    getLight(id: number): ILight;
    applyFrame(frame: Array<Uint8Array>): void;
};