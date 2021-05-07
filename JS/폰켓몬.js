function solution(nums) {

    var answer = 0;
    let set = new Set();

    for(const number of nums){
        set.add(number);
    }

    console.log(`set = ${set.size}, num = ${nums.length/2}`)

    if( set.size < nums.length/2){
        answer = set.size;
    } else { 
        answer = nums.length/2;
    }

    return answer;
}