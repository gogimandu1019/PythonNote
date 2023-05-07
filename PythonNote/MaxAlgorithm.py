import sys	

#주어진 데이터 중 최댓값 구하기
def main():
	#[0] initialize
	max = -sys.maxsize - 1;	#숫자형식 데이터 중 가장 작은값으로 초기화

	#[1] input
	numbers = [-2, -5, -3, -7, -1]; #max = -1
	n = len(numbers)

	#[2] process	
	for i in range(0, n): #주어진 범위
		if numbers[i] > max: #더 큰 데이터가 있다면
			max = numbers[i] #max에 더 큰 데이터를 할당
	
	#[3] output
	print(f'최댓값: {max}')

main()