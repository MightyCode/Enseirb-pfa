/**
 * Mocha test for the Light class.
 */

import { expect } from 'chai';
import Light from '../ts/light';

// Mock HTML element
const mockHTMLElement = {
    style: {
        setProperty: () => { }
    },
    classList: ['light', 'l-00']
};

describe('Light', () => {

    describe('constructor', () => {

        it('should throw a TypeError if the ID is not a number', () => {
            // Array of random elements to test
            const randomElements = [
                'string',
                true,
                false,
                null,
                undefined,
                {},
                [],
                () => { },
                Symbol('test')
            ];

            // Test each element
            randomElements.forEach((element) => {
                expect(() => new Light(element, mockHTMLElement)).to.throw(TypeError);
            });
        });


        it('should throw a TypeError if the element is not an object', () => {
            // Array of random elements to test
            const randomElements = [
                'string',
                true,
                false,
                undefined,
                0,
                () => { },
                Symbol('test')
            ];

            // Test each element
            randomElements.forEach((element) => {
                expect(() => new Light(0, element)).to.throw(TypeError);
            });
        });

        it('should not throw a TypeError if the ID is a number and the element is an object', () => {
            // Array of random number IDs to test
            const randomIDs = new Array(10).fill(0).map(() => Math.floor(Math.random() * 100));

            // Test each element
            randomIDs.forEach((id) => {
                expect(() => new Light(id, mockHTMLElement)).to.not.throw(TypeError);
            });
        });

    });

    describe('rgbw', () => {

        it('should set the light\'s color from a Uint8Array containing RGBW values', () => {
            const light = new Light(0, mockHTMLElement);

            // Array of random Uint8Arrays to test
            const randomArrays = new Array(10).fill(0).map(() => new Uint8Array(4).map(() => Math.floor(Math.random() * 256)));

            // Test each element
            randomArrays.forEach((array) => {
                light.rgbw = array;
                expect(light._rgbw).to.deep.equal(array);
            });
        });

        it('should throw a TypeError if the color is not a Uint8Array', () => {
            const light = new Light(0, mockHTMLElement);

            // Array of random elements to test
            const randomElements = [
                'string',
                true,
                false,
                null,
                undefined,
                {},
                [],
                () => { },
                Symbol('test')
            ];

            // Test each element
            randomElements.forEach((element) => {
                expect(() => light.rgbw = element).to.throw(TypeError);
            });
        });

    });

    describe('classId', () => {

        it('should return the class ID of the light', () => {
            const light = new Light(0, mockHTMLElement);

            // Expect type to be a string
            expect(light.classId).to.be.a('string');
            expect(light.classId).to.equal('l-00');
        });

    });

    describe('id', () => {
            
        it('should return the ID of the light', () => {
            // Array of random number IDs to test
            const randomIDs = new Array(10).fill(0).map(() => Math.floor(Math.random() * 100));

            // Test each element
            randomIDs.forEach((id) => {
                const light = new Light(id, mockHTMLElement);

                // Expect type to be a number
                expect(light.id).to.be.a('number');
                expect(light.id).to.equal(id);
            });
        });

    });

    describe('rgbwString', () => {

        it('should return the light\'s color as a string', () => {
            
            const light = new Light(0, mockHTMLElement);

            // Array of random Uint8Arrays to test
            const randomArrays = new Array(10).fill(0).map(() => new Uint8Array(4).map(() => Math.floor(Math.random() * 256)));

            // Test each element and expect the string to be in the format of #RRGGBBWW
            randomArrays.forEach((array) => {
                light.rgbw = array;
                expect(light.rgbwString).to.be.a('string');
                expect(light.rgbwString).to.equal(`#${array[0].toString(16).padStart(2, '0')}${array[1].toString(16).padStart(2, '0')}${array[2].toString(16).padStart(2, '0')}${array[3].toString(16).padStart(2, '0')}`);
            });
        
        });

    });

});
