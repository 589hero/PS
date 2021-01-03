# # 10818번
# n = int(input())
# nums = list(map(int, input().split()))
#
# max_value = max(nums)
# min_value = min(nums)
#
# print(min_value, end=' ')
# print(max_value, end='')

# # 4344번
# def get_rate(scores):
#     avg_score = sum(scores) / len(scores)
#     score_over_avg = list(score for score in scores if score > avg_score)
#     # return round((len(score_over_avg) / len(scores)) * 100, 3)
#     return (len(score_over_avg) / len(scores)) * 100
#
#
# N = int(input())
# rates = list()
# for i in range(N):
#     inputs = list(map(int, input().split()))
#     student_num = inputs[0]
#     scores = inputs[1:]
#     rate = get_rate(scores)
#     rates.append(rate)
#
# for rate in rates:
#     print('%.3f%%' % rate)

# # 11720번
# N = int(input())
# num = input()
# num = list(map(int, num[:N]))
#
# print(sum(num))

# 1152번
# input_str = input().split()
# print(len(input_str))

# # 1157번
# str = input().upper()
# char_set = set(str)
# char_dict = dict.fromkeys(char_set, 0)
#
# for char in char_set:
#     char_dict[char] = str.count(char)
#
# max_count = max(char_dict.values())
# max_char_list = [char for (char, count) in char_dict.items() if count == max_count]
# max_char = '?' if len(max_char_list) > 1 else max_char_list[0]
# # max_char = None
# # for (char, count) in char_dict.items():
# #     if count == max_count:
# #         if max_char is None:
# #             max_char = char
# #         else:
# #             max_char = '?'
# #             break
#
# print(max_char)

# # 2908번
# nums = input().split()
# num1, num2 = int(nums[0][::-1]), int(nums[1][::-1])
# result = num1 if num1 > num2 else num2
# print(result)

# 1712번
# a, b, c = map(int, sys.stdin.readline().split())
# break_point = 0
#
# # n개 생산 ==> 지출 : a + b*n, 수익 : n*c
# if b >= c:
#     break_point = -1
# else:
#     break_point = a // (c - b) + 1
#
# print(break_point)

# 10872번
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#
#     return n * factorial(n-1)
#
# n = int(input())
# print(factorial(n))

# 10870번
# import sys
#
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#
#     return fibonacci(n-1) + fibonacci(n-2)
#
# n = int(sys.stdin.readline())
# print(fibonacci(n))

# 2798번
# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# cards = list(map(int, sys.stdin.readline().split()))
# min_diff = M
#
# for i in range(0, N-2):
#     for j in range(1, N-1):
#         for k in range(2, N):
#             if i == j or j == k or i == k:
#                 continue
#
#             diff = M - (cards[i] + cards[j] + cards[k])
#
#             if 0 <= diff < min_diff:
#                 min_diff = diff
#
# print(M - min_diff)

# 10817번
# import sys
#
# nums = list(map(int, sys.stdin.readline().split()))
# print(sorted(nums)[1])

# 2775번
# import sys
#
# T = int(sys.stdin.readline())
#
# for _ in range(T):
#     k = int(sys.stdin.readline()) # 층
#     n = int(sys.stdin.readline()) # 호
#
#     cur_results = [i+1 for i in range(n)] # 0층
#     for _ in range(1, k+1):
#         prev_results = cur_results.copy()
#
#         for i in range(n):
#             cur_results[i] = sum(prev_results[:i+1])
#
#     print(cur_results[n-1])

# 10250번
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    if N % H == 0:
        result = H * 100 + N//H + 1
    else:
        result = (N%H)*100 + N//H + 1

    if H == 1:
        result -= 1

    print(result)
























