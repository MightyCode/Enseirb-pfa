// Returns a random byte in the range [0, 255]
function randomByte(): number {
    return Math.floor(Math.random() * 255);
}

// Generate a random frame of 54 Uint8Arrays, each containing four bytes.
export function generateRandomFrame(): Array<Uint8Array> {
    return Array.from({
        length: 54
    }, () => new Uint8Array([randomByte(), randomByte(), randomByte(), randomByte()]));
}

// This function generates a black frame that contains 54 black lights. 
// This is used to fill the screen when an animation is wiped.
export function generateBlackFrame(): Array<Uint8Array> {
    return Array.from({
        length: 54
    }, () => new Uint8Array([0, 0, 0, 0]));
}

/**
 * Generates a mock document object with the appropriate elements to mock the DOM for testing
 * @returns {object} Mock document object
 */
export function generateMockDocument(): object {
    return {
        querySelectorAll: (_) => {
            // Array of mock HTML elements
            // Generate random class list 'l-xx'
            const randomClassList = Array.from({length: 54}, (_, index) => `l-${(index + 1) < 10 ? '0' + (index + 1) : (index + 1)}`);
    
            // Mock elements
            const elements = Array.from({length: 54}, (_, i) => ({
                classList: ['light', randomClassList[i]],
                style: {
                    setProperty: () => { }
                }
            }));
    
            return elements;
        }
    };
}