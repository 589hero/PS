# 1339번
import sys

N = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(N)]

word2coef = {}
for word in words:
    for i, ch in enumerate(word):
        if ch not in word2coef:
            word2coef[ch] = 10 ** (len(word) - i - 1)
        else:
            word2coef[ch] += 10 ** (len(word) - i - 1)

word_coefs = sorted(word2coef.items(), key=lambda x: -x[1]) # (alphabet, coefficient)

word2num = {}
for word_coef in word_coefs:
    word = word_coef[0]
    word2num[word] = 9 - len(word2num)

sum = 0
for word in words:
    for i, ch in enumerate(word):
        sum += word2num[ch] * 10 ** (len(word) - i - 1)

print(sum)

