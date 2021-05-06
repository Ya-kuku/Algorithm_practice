function solution(array, commands) {
    var answer = [];
    for (var i = 0; i < commands.length; i++) {
        var array2 = [];
        array2 = array.slice(commands[i][0]-1,commands[i][1]);
        array2.sort(function(a,b) {
            return a- b;
        })
        answer.push(array2[commands[i][2]-1]);
    }
    return answer;
}

const array = [1, 5, 2, 6, 3, 7, 4]	
const commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
console.log(solution(array,commands));
