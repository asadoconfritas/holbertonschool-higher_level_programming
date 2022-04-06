#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const list2 = list.map((list, id) => list * id);
console.log(list2);
