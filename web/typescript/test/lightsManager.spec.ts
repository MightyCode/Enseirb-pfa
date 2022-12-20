/**
 * Mocha test for the LightsManager class.
 */

import { expect } from 'chai';
import LightsManager from '../ts/lightsManager';
import { generateMockDocument, generateRandomFrame } from './utils';

// Mock DOM document
const document = generateMockDocument();

describe('LightsManager', () => {


    describe('constructor', () => {

        it('should initialize without errors', () => {
            expect(() => {
                // Create a new instance of the LightsManager class, passing the document object to it.
                const lightManager = new LightsManager(document);

                // Check the _lightsElements property of the instance.
                expect(lightManager._lightsElements).to.be.an('array');

                // Check the _lightsArray property of the instance.
                expect(lightManager._lightsArray).to.be.an('object');

                // Check the _mapping property of the instance.
                expect(lightManager._mapping).to.be.an('array').that.has.lengthOf(53);

            }).to.not.throw();
        });

        it('should throw a TypeError if the document is not an object', () => {
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
                expect(() => new LightsManager(element)).to.throw(TypeError);
            });
        });

    });

    describe('mapping', () => {

        it("should set the mapping", () => {
            // Create a new LightsManager instance
            const lightManager = new LightsManager(document);

            // Set the mapping to an array with 5 elements
            expect(() => lightManager.mapping = [1, 2, 3, 4, 5]).not.to.throw();

            // Check that the mapping is an array with 5 elements
            expect(lightManager._mapping).to.be.an('array').that.has.lengthOf(5);
        });

        it("should throw a TypeError if the mapping is not an array", () => {
            const lightManager = new LightsManager(document);

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
                expect(() => lightManager.mapping = element).to.throw(TypeError);
            });
        });

    });

    describe('getLight', () => {

        it("should return a light", () => {
            // Create a LightsManager object
            const lightManager = new LightsManager(document);

            // Get a light object
            const light1 = lightManager.getLight(1);

            // Check that the returned value is an object
            expect(light1).to.be.an('object');
        });

        it("should throw a TypeError if the ID is not a number", () => {
            const lightManager = new LightsManager(document);

            // Array of random elements to test
            const notNumbers = [
                'string',
                true,
                false,
                () => { },
                Symbol('test')
            ];

            // Test each element
            notNumbers.forEach((element) => {
                expect(() => lightManager.getLight(element)).to.throw(TypeError);
            });
        });

    });

    describe('numberOfLights', () => {

        it("should return the number of lights", () => {
            // create a new instance of the LightsManager class
            // pass in the document object to the constructor
            const lightManager = new LightsManager(document);

            // get the number of lights
            const numberOfLights = lightManager.numberOfLights;

            // verify that the number of lights is a number
            expect(numberOfLights).to.be.a('number');

            // verify that the number of lights is 54
            expect(numberOfLights).to.equal(54);
        });

    });

    describe('applyFrame', () => {

        it("should apply a frame", () => {
            const lightManager = new LightsManager(document);

            // Create an array with 10 items, each of which is a new array with 54 items, each of which is a new Uint8Array with 4 items, each of which is a random number between 0 and 255
            const frames = Array.from({ length: 10 }, () => generateRandomFrame());

            // Test each frame
            frames.forEach((frame) => {
                expect(() => lightManager.applyFrame(frame)).not.to.throw();

                frame.forEach((value, i) => {
                    const light = lightManager.getLight(i + 1);

                    // light.rgbwString should be a string of the form '#RRGGBBWW'
                    expect(light.rgbwString).to.be.a('string').that.is.equal(`#${value[0].toString(16).padStart(2, '0')}${value[1].toString(16).padStart(2, '0')}${value[2].toString(16).padStart(2, '0')}${value[3].toString(16).padStart(2, '0')}`);
                });

            });
        });

        it("should throw a TypeError if the frame is not an array", () => {
            const lightManager = new LightsManager(document);

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
                expect(() => lightManager.applyFrame(element)).to.throw(TypeError);
            });
        });

    });

});