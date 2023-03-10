/**
 * Mocha test for the AnimationManager class.
 */

import { expect } from 'chai';
import AnimationManager from '../ts/animationManager';
import LightsManager from '../ts/lightsManager';
import { generateRandomFrame, generateBlackFrame, generateMockDocument } from './utils';

// Mock DOM document
const document = generateMockDocument();

describe('AnimationManager', () => {

    describe('constructor', () => {

        it('should initialize without errors', () => {
            expect(() => {
                const lightsManager = new LightsManager(document);

                // Create a new instance of the AnimationManager class, passing the document object to it.
                const animationManager = new AnimationManager(lightsManager);

                // Check the _lightsManager property of the instance.
                expect(animationManager._lightsManager).to.be.an('object');

                // Check the _lightsElements property of the instance.
                expect(animationManager._rawFrames).to.be.an('array');

                // Check the _lightsArray property of the instance.
                expect(animationManager._frameIndex).to.be.a('number');

                // Check the _mapping property of the instance.
                expect(animationManager._loopMode).to.be.a('boolean');

                // Check the _mapping property of the instance.
                expect(animationManager._liveMode).to.be.a('boolean');

                // Check the _mapping property of the instance.
                expect(animationManager._pending).to.be.a('boolean');

                // Check default values
                expect(animationManager.isLiveMode).to.be.true;
                expect(animationManager.isLoopMode).to.be.false;

            }).to.not.throw();
        });

        it('should throw a TypeError if the lightsManager is not an object', () => {
            // Array of random elements to test
            const notObjects = [
                'string',
                true,
                false,
                0,
                () => { },
                Symbol('test')
            ];

            // Test each element
            notObjects.forEach((element) => {
                expect(() => {
                    // Create a new instance of the AnimationManager class, passing the document object to it.
                    new AnimationManager(element);
                }).to.throw(TypeError);
            });
        });

    });

    describe('addFrame', () => {

        it('should add a frame to the _rawFrames property', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);
            const frame = generateRandomFrame();

            // Add a frame
            animationManager.addFrame(frame);

            // Check the _rawFrames property
            expect(animationManager._rawFrames).to.be.an('array').that.has.lengthOf(1);
        });

        it('should go to the next frame if the animation is live', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            expect(animationManager.isLiveMode).to.be.true;
            expect(animationManager.frameIndex).to.be.equal(0);

            const frame = generateRandomFrame();

            // Add a frame
            animationManager.addFrame(frame);

            expect(animationManager.frameIndex).to.be.equal(1);
        });

        it('should not go to the next frame if the animation is not live', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            animationManager.loopMode();

            expect(animationManager.isLiveMode).to.be.false;
            expect(animationManager.frameIndex).to.be.equal(0);

            const frame = generateRandomFrame();

            // Add a frame
            animationManager.addFrame(frame);

            expect(animationManager.frameIndex).to.be.equal(0);
        });

        it('should throw a TypeError if the frame is not an array', () => {
            // Array of random elements to test
            const notArrays = [
                'string',
                true,
                false,
                0,
                () => { },
                Symbol('test')
            ];

            // Test each element
            notArrays.forEach((element) => {
                expect(() => {
                    const lightsManager = new LightsManager(document);
                    const animationManager = new AnimationManager(lightsManager);

                    // Add a frame
                    animationManager.addFrame(element);
                }).to.throw(TypeError);
            });
        });

    });

    describe('runAnimation', () => {

        it('should run the animation', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            const frame = generateRandomFrame();

            // Add a frame
            animationManager.addFrame(frame);

            // Run the animation
            animationManager.runAnimation();

            expect(animationManager.frameIndex).to.be.equal(1);
        });

    });

    describe('hasAnimationEnded', () => {

        it('should return true if the animation has ended', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            const frame = generateRandomFrame();

            // Add a frame
            animationManager.addFrame(frame);

            // Run the animation
            animationManager.runAnimation();

            expect(animationManager.hasAnimationEnded()).to.be.true;
        });

        it('should return false if the animation has not ended', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            const frame = generateRandomFrame();

            animationManager.loopMode();

            // Add a frame
            animationManager.addFrame(frame);

            expect(animationManager.hasAnimationEnded()).to.be.false;
        });

    });

    describe('isLoopMode', () => {

        it('should return true if the animation is in loop mode', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            animationManager.loopMode();

            expect(animationManager.isLoopMode).to.be.true;
        });

        it('should return false if the animation is not in loop mode', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            expect(animationManager.isLoopMode).to.be.false;
        });

    });

    describe('isLiveMode', () => {

        it('should return true if the animation is in live mode', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            expect(animationManager.isLiveMode).to.be.true;
        });

        it('should return false if the animation is not in live mode', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            animationManager.loopMode();

            expect(animationManager.isLiveMode).to.be.false;
        });

    });

    describe('loopMode', () => {

        it('should set the animation to loop mode', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            animationManager.loopMode();

            expect(animationManager.isLoopMode).to.be.true;
            expect(animationManager.isLiveMode).to.be.false;
        });

    });

    describe('liveMode', () => {

        it('should set the animation to live mode', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            animationManager.loopMode();
            animationManager.liveMode();

            expect(animationManager.isLoopMode).to.be.false;
            expect(animationManager.isLiveMode).to.be.true;
        });

    });

    describe('nextFrame', () => {

        it('should go to the next frame', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            const frame = generateRandomFrame();

            animationManager.loopMode();

            // Add a frame
            animationManager.addFrame(frame);

            expect(animationManager.frameIndex).to.be.equal(0);
            expect(animationManager.currentFrame).to.be.deep.equal(frame);

            // Go to the next frame
            animationManager.nextFrame();

            expect(animationManager.frameIndex).to.be.equal(1);
            expect(animationManager.currentFrame).not.to.be.deep.equal(frame);
        });

    });

    describe('currentFrame', () => {

        it('should return the current frame', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            const frame = generateRandomFrame();

            animationManager.loopMode();

            // Add a frame
            animationManager.addFrame(frame);

            expect(animationManager.currentFrame).to.be.deep.equal(frame);
        });

    });

    describe('frameIndex', () => {

        it('should return the current frame index', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            const frame = generateRandomFrame();

            animationManager.loopMode();

            // Add a frame
            animationManager.addFrame(frame);

            expect(animationManager.frameIndex).to.be.equal(0);
        });

        it('should increase on nextFrame()', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            const frame = generateRandomFrame();

            animationManager.loopMode();

            // Add a frame
            animationManager.addFrame(frame);

            expect(animationManager.frameIndex).to.be.equal(0);

            // Go to the next frame
            animationManager.nextFrame();

            expect(animationManager.frameIndex).to.be.equal(1);
        });

    });

    describe('resetAnimation', () => {

        it('should reset the animation', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            const frame = generateRandomFrame();

            animationManager.loopMode();

            // Add a frame
            animationManager.addFrame(frame);

            expect(animationManager.frameIndex).to.be.equal(0);
            expect(animationManager.currentFrame).to.be.deep.equal(frame);

            // Go to the next frame
            animationManager.nextFrame();

            expect(animationManager.frameIndex).to.be.equal(1);
            expect(animationManager.currentFrame).not.to.be.deep.equal(frame);

            // Reset the animation
            animationManager.resetAnimation();

            expect(animationManager.frameIndex).to.be.equal(0);
            expect(animationManager.currentFrame).to.be.deep.equal(frame);
        });

    });

    describe('wipe', () => {

        it('should wipe the animation', () => {
            const lightsManager = new LightsManager(document);
            const animationManager = new AnimationManager(lightsManager);

            const frame = generateRandomFrame();

            animationManager.loopMode();

            // Add a frame
            animationManager.addFrame(frame);

            expect(animationManager.frameIndex).to.be.equal(0);
            expect(animationManager.currentFrame).to.be.deep.equal(frame);

            // Wipe the animation
            animationManager.wipe();

            expect(animationManager.frameIndex).to.be.equal(0);
            console.log(animationManager.currentFrame);
        });

    });

});