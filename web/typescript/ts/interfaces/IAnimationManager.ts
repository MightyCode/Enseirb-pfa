import ILightsManager from "./ILightsManager.js";

export default interface IAnimationManager {
    frameIndex: number;
    currentFrame: Array<Uint8Array>;
    isLoopMode: boolean;
    isLiveMode: boolean;

    wipe(): void;
    resetAnimation(): void;
    nextFrame(): void;
    liveMode(): void;
    loopMode(): void;
    hasAnimationEnded(): boolean;
    addFrame(frame: Array<Uint8Array>): void;
    finishedReceiving(): void;
    runAnimation(): void;
};