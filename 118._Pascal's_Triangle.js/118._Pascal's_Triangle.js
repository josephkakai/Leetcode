/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    if (numRows === 0) return [];
    if (numRows === 1) return [[1]];

    let result = []
    for (let row = 0; row < numRows; row++) {
        let currentRow = [];
        for (let col = 0; col <= row; col++) {
            if (col === 0  || col === row) {
                currentRow.push(1);
            } else {
                currentRow.push(result[row - 1][col -1] + result[row - 1][col]);
            }
        }
        result.push(currentRow)
    }
    return result;
};