const path = require('path');
require('ts-mocha');
const Mocha = require('mocha');

// Loads the Mocha test framework and creates a new Mocha test runner
const mocha = new Mocha();

mocha.addFile(path.join(__dirname, 'light.spec.ts'));
mocha.addFile(path.join(__dirname, 'lightsManager.spec.ts'));
mocha.addFile(path.join(__dirname, 'animationManager.spec.ts'));

// Runs the tests and exits with status 1 if there are any failures
mocha.run((failures) => {
    process.on('exit', () => {
        process.exit(failures);
    });
});