#[?]주어진 데이터에서 가장 많이 나타난 값
import sys

#[1]input
scores = [1,3,4,3,5] #0~5점까지만 허용한다고 가정
indexes = [0] * 6 #0~5점 점수 인덱스: 갯수 저장
max = -sys.maxsize - 1 #맥스알고리즘 적용
mode = 0 #최빈값이 담길 그릇
n = len(scores)
m = len(indexes)

#[2]process
for i in range(0, n):
	indexes[scores[i]] = indexes[scores[i]]+1 #count 1씩 증가

for i in range(0, m):
	if indexes[i] > max:
		max = indexes[i] #최대
		mode = i #mode

#[3]output
print(f'최빈값 {mode} => {max}번 나타남')