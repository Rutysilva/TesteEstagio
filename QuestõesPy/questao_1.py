def q1_remover_duplicados(nums):
    nums = list(set(nums))
    return nums

nums = [1,2,2,3,3,4,5,5,5,6,6,6,6,7,8,9,10,10,10]
print (q1_remover_duplicados(nums))