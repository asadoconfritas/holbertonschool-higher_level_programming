#!/usr/bin/node
exports.converter = function (base) {
	return function holaq (number) {
		return number.toString(base);
	};
};
