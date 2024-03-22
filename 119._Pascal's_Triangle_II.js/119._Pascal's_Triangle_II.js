/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    const rowCoefficients = Array(rowIndex + 1).fill(1);
 
     for (let i = 2; i < rowIndex + 1; ++i) {
         
         for (let j = i - 1; j > 0; --j) {
             rowCoefficients[j] += rowCoefficients[j - 1];
         }
     }
     return rowCoefficients;
 };