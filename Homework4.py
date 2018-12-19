# TASK-1
# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Assume that:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

def solution(array):
    set_array = set(array)
    smallest_int = 1
    for nums in set_array:
        if nums < 0:
            return 1
        else:
            while smallest_int in set_array:
                smallest_int +=1
    return smallest_int

array = [1,3,6,4,1,2]
print(solution(array))