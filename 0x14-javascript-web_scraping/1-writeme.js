#!/usr/bin/node
// Writes a string to some file
const argv = process.argv;
const fs = require('fs');
fs.writeFile(argv[2], argv[3], 'utf8', function (err, data) {
  if (err) {
    console.error(err);
  }
});
