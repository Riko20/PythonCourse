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

# ==========================
# TASK-2
# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones
# at both ends in the binary representation of N.
# For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
# The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
# The number 20 has binary representation 10100 and contains one binary gap of length 1.
# The number 15 has binary representation 1111 and has no binary gaps.
# The number 32 has binary representation 100000 and has no binary gaps.
#
# Write a function:
#
# def solution(N)
#
# that, given a positive integer N, returns the length of its longest binary gap.
# The function should return 0 if N doesn't contain a binary gap.
#
# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
# Assume that:
# N is an integer within the range [1..2,147,483,647].
# ============================


def solution(integ):
    count =0
    who_largest = []
    binar = "{0:b}".format(integ)
    for dig in binar:
        if dig =='0':
            count +=1
        if dig=='1':
            who_largest.append(count)
            count = 0

    max_bingap = max((who_largest), default=0)
    return max_bingap

print(solution(1041))


