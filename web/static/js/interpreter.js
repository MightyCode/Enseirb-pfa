let state = null;
let lightsArray = null;
let lightMapping = null;
let running = false;

let liveMode = true;

const interpreter = {
    setLightsArray: (array) => lightsArray = array,
    setLightMapping: (mapping) => lightMapping = mapping,
    setState: (newState) => state = newState,
    isStateSet: () => state !== null,
    run() {
        liveMode = false;
        running = true;

        while (!state.isEnded() && running) {
            this.step();
        }
    },
    step() {
        if (!state.isEnded()) {
            this.applyFrame(state.nextFrame())
        }
    },
    previousStep() {
        if (!state.isAtStart()) {
            this.applyFrame(state.previousFrame())
        }
    },
    resetAnimation() {
        running = false;
        liveMode = false;

        state.resetFrame();
        this.applyFrame(state.getCurrentFrame());
    },
    applyFrame: (frame) => {
        // Set CSS --light-color property for each light
        lightsArray.forEach((light, index) => {
            light.style.setProperty('--light-color', frame[lightMapping[index]]);
        });
    },
    pushFrame: (frame) => {
        if (interpreter.isStateSet()) {
            state.pushFrame(frame);
        } else {
            throw new Error('State is not set');
        }
    },
    isRunning: () => running,
    isLiveMode: () => liveMode,
}

export default interpreter;