#!/usr/bin/node
exports.esrever = function (list) {
	const newL = [];
	for (let i = list.lenght - 1; i >= 0; i--) {
		newL.push(list[i]);
	}
	return newL;
};
