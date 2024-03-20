/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
    if (x < 0 || x === NaN) {
        return NaN;
    }
    let squareRoot = x / 2;
    let temp = 0;

    while (squareRoot !== temp) {
        temp = squareRoot;
        squareRoot = (squareRoot + x / squareRoot) / 2;
    }
    return Math.floor(squareRoot);

};

console.log(mySqrt(8)); // 2