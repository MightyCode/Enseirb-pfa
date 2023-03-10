import IAnimationManager from "./interfaces/IAnimationManager.js";
import ILightsManager from "./interfaces/ILightsManager.js";

export default class AnimationManager implements IAnimationManager {

    _rawFrames: Array<Array<Uint8Array>>;
    _frameIndex: number;
    _lightsManager: ILightsManager;

    _loopMode: boolean;
    _liveMode: boolean;

    _pending: boolean;

    constructor(lightsManager: ILightsManager) {
        // Check type
        if (typeof lightsManager !== 'object') throw new TypeError('Lights manager must be an object');

        this._lightsManager = lightsManager;
        this._rawFrames = [];
        this._frameIndex = 0;

        this._loopMode = false;
        this._liveMode = true;
        this._pending = true;
    }

    /**
     * Wipes the animation
     */
    wipe(): void {
        this._rawFrames = [];
        this._frameIndex = 0;

        // Generate a frame of black lights
        const blackFrame = new Array(this._lightsManager.numberOfLights)
            .fill(new Uint8Array([0, 0, 0, 0]));

        // Apply the frame
        this._lightsManager.applyFrame(blackFrame);
    }

    /**
     * Resets the animation to its first frame
     */
    resetAnimation(): void {
        this._frameIndex = 0;

        // Apply first frame
        this._lightsManager.applyFrame(this.currentFrame);
    }

    get frameIndex(): number {
        return this._frameIndex;
    }

    nextFrame(): void {
        if (this._frameIndex >= this._rawFrames.length) {
            if (this._loopMode) {
                this._frameIndex = 0;
            } else {
                return;
            }
        }

        this._lightsManager.applyFrame(this.currentFrame);
        this._frameIndex++;
    }

    get currentFrame(): Array<Uint8Array> {
        return this._rawFrames[this._frameIndex];
    }

    /**
     * Sets the animation to live mode
     */
    liveMode(): void {
        this._liveMode = true;
        this._loopMode = false;
    }

    /**
     * Sets the animation to loop mode
     */
    loopMode(): void {
        this._liveMode = false;
        this._loopMode = true;
    }

    /**
     * Checks if the animation is in loop mode
     * @returns {boolean} True if the animation is in loop mode
     */
    get isLoopMode(): boolean {
        return this._loopMode;
    }

    /**
     * Checks if the animation is in live mode
     * @returns {boolean} True if the animation is in live mode
     */
    get isLiveMode(): boolean {
        return this._liveMode;
    }

    hasAnimationEnded(): boolean {
        return this._frameIndex >= this._rawFrames.length;
    }

    addFrame(frame: Array<Uint8Array>): void {
        // Check type
        if (!Array.isArray(frame)) throw new TypeError('Frame must be an array');
        
        this._rawFrames.push(frame);

        // If the animation is in live mode, apply the frame if the animation is has not ended
        if (this._liveMode && this._pending) {
            this.nextFrame();
        }
    }

    finishedReceiving(): void {
        this._pending = false;
    }

    runAnimation(): void {
        this._liveMode = false;

        this.resetAnimation();
        while (!this.hasAnimationEnded()) {
            this.nextFrame();
        }
    }
}