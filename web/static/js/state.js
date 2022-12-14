const frames = [];
let frameIndex = 0;

const state = {
    pushFrame: (frame) => frames.push(frame),
    getCurrentFrame: () => frames[frameIndex],
    nextFrame: () => frames[frameIndex++],
    resetFrame: () => frameIndex = 0,
    previousFrame: () => frames[frameIndex--],
    isEnded: () => frameIndex >= frames.length,
    isAtStart: () => frameIndex === 0,
};

export default state;
