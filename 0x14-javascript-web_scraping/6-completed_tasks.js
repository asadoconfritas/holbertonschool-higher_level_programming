#!/usr/bin/node
// computes the number of tasks completed by user id
const axios = require('axios').default;
const argv = process.argv;
const apidata = argv[2];

axios.get(apidata)
  .then(function (response) {
    const dict = {};
    for (const x in response.data) {
      const user = response.data[x].userId;
      const ended = response.data[x].completed;
      if (isNaN(dict[user]) && ended) {
        dict[user] = 1;
      } else if (ended) {
        dict[user] += 1;
      }
    }
    console.log(dict);
  });
