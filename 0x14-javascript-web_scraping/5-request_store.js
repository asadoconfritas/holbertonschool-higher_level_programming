#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file
const argv = process.argv;
const axios = require('axios').default;
axios.get(argv[2])
    .then(function (response) {
        fs.writeFile(argv[3], response.data, 'utf8', function (err, data) {
            if (err) {
                console.log(err);
            }
        });
    })
    .catch(function (error) {
        console.log('code: ' + error.response.status);
});
