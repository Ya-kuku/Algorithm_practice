function solution(parti, comple) {
    var answer = '';
    parti.sort();
    comple.sort();
    console.log(parti)
    console.log(comple)
    for (var i = 0; i < parti.length; i++) {
        if (parti[i] !== comple[i]) {
            answer = parti[i]
            return answer;
        }
    }
}