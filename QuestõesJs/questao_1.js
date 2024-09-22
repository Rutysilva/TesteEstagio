function q1_remover_duplicados(nums) {
    nums = [...new Set(nums)];
    return nums;
}

const nums = [1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 9, 10, 10, 10];
console.log(q1_remover_duplicados(nums));

