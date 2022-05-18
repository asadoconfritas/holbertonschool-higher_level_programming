#!/usr/bin/node
// Writes a string to a file
const argv = process.argv;
const axios = require('axios').default;
axios.get(argv[2])
    .then((response) => {
        console.log('code: ' + response.status);
    })
    .catch((error) => {
        console.log('code: ' + error.response.status);
    })
    .then(() => {
});
