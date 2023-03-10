export default class AnimationManager {
    constructor(lightsManager) {
        // Check type
        if (typeof lightsManager !== 'object')
            throw new TypeError('Lights manager must be an object');
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
    wipe() {
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
    resetAnimation() {
        this._frameIndex = 0;
        // Apply first frame
        this._lightsManager.applyFrame(this.currentFrame);
    }
    get frameIndex() {
        return this._frameIndex;
    }
    nextFrame() {
        if (this._frameIndex >= this._rawFrames.length) {
            if (this._loopMode) {
                this._frameIndex = 0;
            }
            else {
                return;
            }
        }
        this._lightsManager.applyFrame(this.currentFrame);
        this._frameIndex++;
    }
    get currentFrame() {
        return this._rawFrames[this._frameIndex];
    }
    /**
     * Sets the animation to live mode
     */
    liveMode() {
        this._liveMode = true;
        this._loopMode = false;
    }
    /**
     * Sets the animation to loop mode
     */
    loopMode() {
        this._liveMode = false;
        this._loopMode = true;
    }
    /**
     * Checks if the animation is in loop mode
     * @returns {boolean} True if the animation is in loop mode
     */
    get isLoopMode() {
        return this._loopMode;
    }
    /**
     * Checks if the animation is in live mode
     * @returns {boolean} True if the animation is in live mode
     */
    get isLiveMode() {
        return this._liveMode;
    }
    hasAnimationEnded() {
        return this._frameIndex >= this._rawFrames.length;
    }
    addFrame(frame) {
        // Check type
        if (!Array.isArray(frame))
            throw new TypeError('Frame must be an array');
        this._rawFrames.push(frame);
        // If the animation is in live mode, apply the frame if the animation is has not ended
        if (this._liveMode && this._pending) {
            this.nextFrame();
        }
    }
    finishedReceiving() {
        this._pending = false;
    }
    runAnimation() {
        this._liveMode = false;
        this.resetAnimation();
        while (!this.hasAnimationEnded()) {
            this.nextFrame();
        }
    }
}
