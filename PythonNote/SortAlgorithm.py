#[?] 무작위데이터를 순서대로 오름차순(asc) / 내림차순(desc) 정렬

#정렬알고리즘(sort algorithm) : 가장 작은/큰 데이터를 왼쪽으로 순서대로 이동
def main():
	
	#[1] input	: 자료구조 (array / list / stack / queue / tree / db / ...)
	data = [3, 2, 1, 5, 4] #정렬되지 않은 데이터
	n = len(data)
	temp = 0
	#[2] process : selection sort (선택정렬)
	for i in range(0, n-1): #i = 0 ~ n-1
		for j in range(i+1, n): #j = i+1 ~ n
			if data[i] > data[j]:	#부등호방향 오름차순정렬 > / 내림차순정렬 <
				temp = data[i]
				data[i] = data[j]
				data[j] = temp #swap
		print(data)

	#[3] output
	for i in range(n):
		print(data[i])
main()