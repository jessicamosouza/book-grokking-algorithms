# Criar uma tabela de multiplicação com todos os elementos do array.
# [2, 3, 7, 8, 10] -> 2 * 3, 2 * 7, .... , 3 * 7, 3 * 8, ..., 8 * 10

def multiply(nums):
    if len(nums) == 1:
        return [nums[0] * nums[0]]

    return [nums[0] * i for i in nums[0:]] + multiply(nums[1:])


print(multiply([2, 3, 7, 8, 10]))
