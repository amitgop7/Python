def numbers(nums):
    sum=0
    for n in nums:
        sum+=n
    return sum
print(numbers([1,2,3,4,5]))


def multiply_num(nums):
    mul=1
    for n in nums:
        mul*=n
    return mul
print(multiply_num([1,2,3,4,5]))
